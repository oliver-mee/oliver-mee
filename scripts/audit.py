#!/usr/bin/env python3
"""Collect public contribution candidates; never infer adoption or edit the README."""
import argparse
import datetime
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def gh(endpoint):
    return json.loads(subprocess.check_output(['gh', 'api', endpoint], text=True))


def search(query):
    from urllib.parse import urlencode
    items = []
    page = 1
    while True:
        result = gh('search/issues?' + urlencode({'q': query, 'per_page': 100, 'page': page}))
        if result.get('incomplete_results'):
            raise RuntimeError('GitHub returned incomplete search results; retry before advancing audit state')
        items.extend(result['items'])
        if len(items) >= result['total_count']:
            return items
        if page >= 10:
            raise RuntimeError('Search exceeds GitHub 1000-result cap; split the date range')
        page += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--since', help='Override stored audit timestamp')
    parser.add_argument('--output', default='.profile/activity.json')
    args = parser.parse_args()
    state = json.loads((ROOT / '.profile/state.json').read_text())
    since = args.since or state['last_audited_through']
    collected = datetime.datetime.now(datetime.timezone.utc).isoformat()
    records = []
    for kind in ('pr', 'issue'):
        for item in search(f'author:oliver-mee is:{kind} is:public updated:>={since}'):
            repo = item['repository_url'].split('/repos/', 1)[1]
            if repo.split('/')[0].lower() in ('oliver-mee', 'preface-ai', 'prefacecontent', 'magven-org'):
                continue
            record = {key: item[key] for key in ('number', 'title', 'html_url', 'state', 'updated_at')}
            record.update(repo=repo, kind=kind)
            if kind == 'pr':
                pr = gh(f'repos/{repo}/pulls/{item["number"]}')
                record['merged_at'] = pr['merged_at']
                record['draft'] = pr['draft']
            # Closed originals need human inspection of references and co-authored commits.
            comments = json.loads(subprocess.check_output(['gh', 'api', '--paginate', '--slurp', f'repos/{repo}/issues/{item["number"]}/comments?per_page=100'], text=True))
            record['discussion'] = [
                {'url': c['html_url'], 'author': c['user']['login'], 'body': c['body']}
                for page in comments for c in page
                if c['user']['type'] != 'Bot' and c['user']['login'] not in ('coderabbitai',)
            ]
            records.append(record)
    output = {'since': since, 'collected_at': collected, 'records': records,
              'note': 'Candidates, not verified claims. Review replacement PRs and commit co-authorship before editing profile or advancing state.'}
    target = ROOT / args.output
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(output, indent=2) + '\n')
    print(f'Collected {len(records)} public external PR/issue candidates into {target}')


if __name__ == '__main__':
    main()
