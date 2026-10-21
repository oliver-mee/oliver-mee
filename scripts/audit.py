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


def search(query, resource='issues'):
    from urllib.parse import urlencode
    items = []
    page = 1
    while True:
        result = gh(f'search/{resource}?' + urlencode({'q': query, 'per_page': 100, 'page': page}))
        if result.get('incomplete_results'):
            raise RuntimeError('GitHub returned incomplete search results; retry before advancing audit state')
        items.extend(result['items'])
        if len(items) >= result['total_count']:
            return items
        if page >= 10:
            raise RuntimeError('Search exceeds GitHub 1000-result cap; split the date range')
        page += 1


def secret_patterns_present(text):
    """Credential-shape guard; deliberately returns no matching credential values."""
    import re
    patterns = [r'gh[opusr]_[A-Za-z0-9]{20,}', r'github_pat_[A-Za-z0-9_]{30,}',
                r'sk-ant-[A-Za-z0-9_-]{20,}', r'xox[baprs]-[A-Za-z0-9-]{20,}',
                r'AKIA[A-Z0-9]{16}', r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----']
    return any(re.search(pattern, text) for pattern in patterns)


def check_public():
    """Scan tracked and outgoing non-ignored files, never read local credential stores."""
    names = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '--cached', '--others', '--exclude-standard', '-z']).decode().split('\0')
    flagged = []
    scanned = 0
    for name in dict.fromkeys(names):
        if not name:
            continue
        path = ROOT / name
        if not path.is_file() or path.is_symlink():
            continue
        text = path.read_text(errors='replace')
        scanned += 1
        if secret_patterns_present(text):
            flagged.append(name)
    if flagged:
        raise RuntimeError('Credential-shaped content found; inspect locally before publication: ' + ', '.join(flagged))
    print(f'Public-file credential-pattern scan clean: {scanned} files. This is a heuristic check, not proof that arbitrary secrets cannot exist.')


def refresh_stars():
    """Validate all ranking metadata before writing; preserve reviewed claims and audit state."""
    from concurrent.futures import ThreadPoolExecutor
    path = ROOT / '.profile/profile.json'
    source = json.loads(path.read_text())
    repositories = sorted({item['repo'] for section in source['sections'] for item in section['items']})

    def collect(repo):
        metadata = gh(f'repos/{repo}')
        count = metadata.get('stargazers_count')
        if metadata.get('private') is not False or metadata.get('visibility') != 'public':
            raise ValueError(f'Repository is not verified public: {repo}')
        if type(count) is not int or count < 0:
            raise ValueError(f'Invalid star count: {repo}')
        return repo, count

    with ThreadPoolExecutor(max_workers=4) as pool:
        counts = dict(pool.map(collect, repositories))
    for section in source['sections']:
        for item in section['items']:
            item['stars'] = counts[item['repo']]
    source['stars_checked_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    path.write_text(json.dumps(source, indent=2) + '\n')
    print(f'Refreshed public GitHub star counts for {len(counts)} repositories')


def contribution_sort_key(item):
    count = item.get('stars')
    if type(count) is not int or count < 0:
        raise ValueError(f"Missing or invalid stars for {item['repo']}; run --refresh-stars first")
    return (-count, item['name'].casefold(), item['repo'].casefold())


def render_profile():
    """Render plain-language descriptions with short references, never blue paragraph links."""
    import re
    source = json.loads((ROOT / '.profile/profile.json').read_text())
    readme = ROOT / 'README.md'
    current = readme.read_text()
    if current.count('### Open-source contributions\n') != 1:
        raise ValueError('README contribution marker must occur exactly once')
    prefix = current.split('### Open-source contributions\n', 1)[0]
    rows = []
    for section in source['sections']:
        rows.extend([f"### {section['title']}", ''])
        for item in sorted(section['items'], key=contribution_sort_key):
            description = []
            for part in item['parts']:
                description.append(part['text'])
                if 'url' in part:
                    match = re.fullmatch(r'https://github.com/[^/]+/[^/]+/(pull|issues|commit)/([A-Za-z0-9]+)(?:#[^\s]+)?', part['url'])
                    if not match:
                        raise ValueError(f"Invalid evidence target: {part['url']}")
                    kind, identifier = match.groups()
                    label = {'pull': 'PR\u00a0#', 'issues': 'Issue\u00a0#', 'commit': 'Commit\u00a0'}[kind]
                    label += identifier[:7] if kind == 'commit' else identifier
                    description.append(f" [`{label}`]({part['url']})")
            badge = f"[![Stars](https://img.shields.io/github/stars/{item['repo']}?style=social)](https://github.com/{item['repo']}/stargazers)"
            rows.append(f"- **[{item['name']}](https://github.com/{item['repo']})** {badge} — {''.join(description)}")
        rows.append('')
    rows.extend(['[Full public contribution record](CONTRIBUTIONS.md)', ''])
    readme.write_text(prefix + '\n'.join(rows))
    print('Rendered plain descriptions and compact evidence references into README.md')


def render_coverage():
    """Render the reviewed ledger, keeping technical credit separate from routine discussion."""
    report = json.loads((ROOT / '.profile/coverage.json').read_text())
    records = report['records']
    rows = ['# Public contribution record', '',
            'An evidence-linked record of implementations, active proposals, issue-led fixes, testing and technical review. A closed original PR can still represent landed work; the evidence column records the adopted route. Routine discussion is recorded separately, not presented as code authorship.', '',
            '## Scope', '', report['scope'], '',
            f"Reviewed sources: **{report['counts']['authored']} authored items**, **{report['counts']['participated']} other-authored discussions**, across **{report['counts']['repositories']} repositories**. These are activity counts, not merged-PR or implementation counts.", '']
    def table(items):
        out = ['| Source | Work | Outcome / role | Evidence |', '| --- | --- | --- | --- |']
        for r in items:
            title = r['title'].replace('|', r'\|').replace('\n', ' ')
            outcome = r['disposition'] + (f". {r['note']}" if r['note'] else '')
            evidence = ', '.join(f'[adoption / fix]({url})' for url in r['evidence']) or '—'
            out.append(f"| [{r['kind']} #{r['number']}]({r['source']}) | {title} | {outcome} | {evidence} |")
        return out
    routine = []
    for repo in sorted({r['repo'] for r in records}, key=str.lower):
        selected = [r for r in records if r['repo'] == repo and not r['disposition'].startswith('discussion/triage/support')]
        routine.extend(r for r in records if r['repo'] == repo and r['disposition'].startswith('discussion/triage/support'))
        if selected:
            rows.extend([f'## [{repo}](https://github.com/{repo})', ''] + table(selected) + [''])
    rows.extend(['## Other discussion and triage', '',
                 'These items were checked but are not additional implementation claims. They include support, duplicate triage and comments that do not establish shipped changes.', '',
                 '<details><summary>Activity appendix</summary>', ''])
    for repo in sorted({r['repo'] for r in routine}, key=str.lower):
        rows.extend([f'### {repo}', ''] + table([r for r in routine if r['repo'] == repo]) + [''])
    rows.extend(['</details>', ''])
    (ROOT / 'CONTRIBUTIONS.md').write_text('\n'.join(rows))
    print(f'Rendered {len(records)} reviewed source records into CONTRIBUTIONS.md')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--since', help='Override stored audit timestamp')
    parser.add_argument('--full', action='store_true', help='Audit since account creation, not the incremental checkpoint')
    parser.add_argument('--commits', action='store_true', help='Collect authored/co-authored commit candidates instead of PRs/issues')
    parser.add_argument('--participated', action='store_true', help='Collect other authors’ public items commented on by Oliver')
    parser.add_argument('--output', default='.profile/activity.json')
    parser.add_argument('--timelines', action='store_true', help='Enrich an existing --output report with paginated issue/PR timelines')
    parser.add_argument('--render', action='store_true', help='Render reviewed coverage/profile JSON into CONTRIBUTIONS.md and README.md without network access')
    parser.add_argument('--refresh-stars', action='store_true', help='Refresh public repository star counts for contribution ordering; combine with --render to regenerate the profile')
    parser.add_argument('--check', action='store_true', help='Scan tracked/non-ignored publication files for credential-shaped content')
    args = parser.parse_args()
    if args.check:
        check_public()
        return
    if args.refresh_stars:
        refresh_stars()
        if not args.render:
            return
    if args.render:
        render_profile()
        render_coverage()
        return
    if args.timelines:
        target = ROOT / args.output
        report = json.loads(target.read_text())
        from concurrent.futures import ThreadPoolExecutor

        def enrich(record):
            endpoint = f'repos/{record["repo"]}/issues/{record["number"]}/timeline?per_page=100'
            pages = json.loads(subprocess.check_output(['gh', 'api', '--paginate', '--slurp', endpoint], text=True))
            record['timeline'] = [event for page in pages for event in page
                                  if event.get('event') in ('closed', 'referenced', 'cross-referenced', 'merged')]
            return record

        report['records'] = list(ThreadPoolExecutor(max_workers=4).map(enrich, report['records']))
        target.write_text(json.dumps(report, indent=2) + '\n')
        print(f'Enriched {len(report["records"])} timelines in {target}')
        return
    state = json.loads((ROOT / '.profile/state.json').read_text())
    since = '2022-03-30T00:00:00Z' if args.full else args.since or state['last_audited_through']
    collected = datetime.datetime.now(datetime.timezone.utc).isoformat()
    records = []
    if args.commits:
        seen = set()
        queries = [f'author:oliver-mee is:public committer-date:>={since}',
                   f'"Co-authored-by" "oliver-mee" is:public committer-date:>={since}']
        for query in queries:
            for item in search(query, 'commits'):
                repo = item['repository']['full_name']
                if repo.split('/')[0].lower() in ('oliver-mee', 'preface-ai', 'prefacecontent', 'magven-org'):
                    continue
                key = (repo, item['sha'])
                if key in seen:
                    continue
                seen.add(key)
                records.append({'repo': repo, 'sha': item['sha'], 'html_url': item['html_url'],
                                'message': item['commit']['message'], 'author': item['commit']['author'],
                                'matched_query': query})
        target = ROOT / args.output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps({'since': since, 'collected_at': collected, 'queries': queries,
                                    'records': records, 'note': 'Commit candidates; verify default-branch reachability and exclude fork mirrors before claiming new upstream work.'}, indent=2) + '\n')
        print(f'Collected {len(records)} commit candidates into {target}')
        return
    actor_query = 'commenter:oliver-mee -author:oliver-mee' if args.participated else 'author:oliver-mee'
    for kind in ('pr', 'issue'):
        for item in search(f'{actor_query} is:{kind} is:public updated:>={since}'):
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
