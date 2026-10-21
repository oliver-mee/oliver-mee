import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('audit', Path(__file__).resolve().parents[1] / 'scripts/audit.py')
assert spec is not None and spec.loader is not None
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class SearchTests(unittest.TestCase):
    def test_paginates_to_declared_total(self):
        with patch.object(audit, 'gh', side_effect=[
            {'items': [{'number': 1}], 'total_count': 2, 'incomplete_results': False},
            {'items': [{'number': 2}], 'total_count': 2, 'incomplete_results': False},
        ]) as api:
            self.assertEqual(len(audit.search('is:public')), 2)
            self.assertIn('page=2', api.call_args.args[0])

    def test_incomplete_is_not_silent_success(self):
        with patch.object(audit, 'gh', return_value={'incomplete_results': True}):
            with self.assertRaises(RuntimeError):
                audit.search('is:public')

    def test_empty_result(self):
        with patch.object(audit, 'gh', return_value={'items': [], 'total_count': 0}):
            self.assertEqual(audit.search('is:public'), [])

    def test_search_limit_is_not_silent_truncation(self):
        with patch.object(audit, 'gh', return_value={'items': [{}] * 100, 'total_count': 1001}):
            with self.assertRaises(RuntimeError):
                audit.search('is:public')


import json
import re
from collections import Counter


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]
        self.coverage = json.loads((self.root / '.profile/coverage.json').read_text())
        self.readme = (self.root / 'README.md').read_text()

    def test_no_duplicate_or_silently_dropped_source_rows(self):
        rows = self.coverage['records']
        keys = [(r['repo'], r['kind'], r['number']) for r in rows]
        self.assertEqual(len(keys), len(set(keys)))
        counts = Counter(r['role'] for r in rows)
        self.assertEqual(counts['authored'], self.coverage['counts']['authored'])
        self.assertEqual(counts['participated'], self.coverage['counts']['participated'])
        self.assertEqual(len({r['repo'] for r in rows}), self.coverage['counts']['repositories'])

    def test_every_directly_merged_pr_is_linked_on_profile(self):
        for r in self.coverage['records']:
            if r['role'] == 'authored' and r['merged_at']:
                self.assertIn(r['source'], self.readme, r['title'])

    def test_models_dev_has_all_six_direct_merges_and_open_endpoint_work(self):
        rows = [r for r in self.coverage['records'] if r['repo'] == 'anomalyco/models.dev' and r['merged_at']]
        self.assertEqual(len(rows), 6)
        for number in [2145, 2146, 2684, 3695, 3705, 7203, 7977, 6663, 7147, 10544]:
            self.assertIn(f'https://github.com/anomalyco/models.dev/pull/{number}', self.readme)

    def test_no_multi_change_paragraph_links(self):
        section = self.readme.split('### Open-source contributions', 1)[1]
        for label, url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', section):
            if '/pull/' in url or '/issues/' in url or '/commit/' in url:
                self.assertNotIn(';', label)
                self.assertLessEqual(len(label.split()), 14, label)

    def test_profile_evidence_is_reconciled_to_reviewed_ledger(self):
        evidence = {u.split('#')[0] for r in self.coverage['records'] for u in [r['source'], *r['evidence']]}
        for url in re.findall(r'https://github.com/[^)\s]+/(?:pull|issues|commit)/[^)\s]+', self.readme):
            self.assertIn(url.split('#')[0], evidence, url)

    def test_render_is_idempotent_and_contains_all_sources(self):
        audit.render_coverage()
        path = self.root / 'CONTRIBUTIONS.md'
        before = path.read_bytes()
        audit.render_coverage()
        self.assertEqual(before, path.read_bytes())
        text = path.read_text()
        for r in self.coverage['records']:
            self.assertIn(r['source'], text)

    def test_rejected_work_is_not_claimed_as_landed(self):
        r = next(r for r in self.coverage['records'] if r['repo'] == 'basicmachines-co/basic-memory' and r['kind'] == 'pr' and r['number'] == 1580)
        self.assertFalse(r['merged_at'])
        self.assertIn('no verified landed outcome', r['disposition'])
        self.assertNotIn('basic-memory/pull/1580', self.readme)

    def test_commit_search_uses_commit_resource(self):
        with patch.object(audit, 'gh', return_value={'items': [], 'total_count': 0}) as api:
            audit.search('author:oliver-mee', 'commits')
            self.assertTrue(api.call_args.args[0].startswith('search/commits?'))


if __name__ == '__main__':
    unittest.main()
