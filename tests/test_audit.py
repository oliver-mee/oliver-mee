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


if __name__ == '__main__':
    unittest.main()
