# Profile maintenance

This file is the handoff for any agent maintaining this GitHub profile. It replaces the old scheduled GitHub Actions updater.

The instructions are runner-agnostic. Hermes is currently the intended cron runner, but Claude Code, Codex, OpenCode or another agent should be able to use the same file without changing the maintenance model.

## Goal

Keep `README.md` current without repeatedly re-auditing Oliver's entire GitHub history.

Read `.profile/state.json` first. Treat the current README and the state's known contribution repositories as the established baseline. Inspect activity newer than `last_audited_through`. Do not rescan older history unless a newer event changes how an older contribution should be described.

If nothing meaningful changed, make no commit and open no PR.

## What to check

1. External pull requests authored by `oliver-mee` that were created or updated after the last audit point.
2. External issues authored by `oliver-mee` that were created or updated after the last audit point.
3. For relevant issues or closed PRs, inspect maintainer comments, linked PRs, closing PRs, replacement PRs and merged commits when needed to understand the outcome.
4. Public repositories owned by `oliver-mee` that were created or materially changed after the last audit point.
5. Do not infer changes to the Current stack from GitHub activity alone. Change that section only when Oliver has explicitly changed what he uses or there is direct evidence in the repo instructions.

## What counts as a contribution

Use a practical standard: would a reasonable reader of the public activity regard Oliver as having meaningfully contributed to the project?

That can include:

- merged code;
- a substantive open PR;
- a bug report, diagnosis, reproduction or technical investigation that materially led to an upstream fix;
- testing or live-system evidence that materially changed an upstream implementation;
- a closed or superseded PR whose work was adopted through another upstream route.

Code authorship is not required. Do not add trivial questions, drive-by comments, duplicate reports, routine refresh requests, or interactions with no meaningful effect on the project.

Open PRs can appear while active, but their wording must not imply that the change has shipped. If an open PR later closes without merge or adoption, remove the associated claim unless other meaningful contribution evidence remains for that repository.

## Writing the contribution ledger

- Keep exactly one bullet per repository and aggregate related work into that bullet.
- Describe concrete changes, bugs, integrations or technical areas. Avoid generic résumé language such as "contributed to" or "worked on".
- Prefer compact noun phrases separated by commas or semicolons.
- Link descriptive contribution phrases to the relevant PR, adopted replacement or issue-led fix. Keep repository-name links pointing at the project. Avoid bare PR numbers and replacement-process commentary; describe landed work directly, and label genuinely open proposals.
- Do not explain the tracking methodology in the README.
- Preserve existing contributions unless new evidence changes them.
- Add a new repository only when the activity meets the meaningful-contribution standard above.

## Projects

The Projects section is broader than "currently building".

- User-owned public non-fork repositories can be included even when they are older or inactive.
- `stars` does not belong in Projects; it is linked near the top of the profile.
- A fork can appear only when Oliver has made substantial original changes to it, and the wording must make the derivative relationship clear rather than presenting the upstream project as his own.
- Do not pad the section with untouched or near-identical forks.

## Profile voice

Keep the profile concise and human. Do not turn it into a résumé, a changelog or an audit report.

The opening line is intentionally:

> Always experimenting with new tools, ideas and ways of working.

Do not rewrite it during routine maintenance.

## Reusable audit command

Run `python3 scripts/audit.py` from any directory. It uses the saved audit timestamp, paginates public external PRs and issues through authenticated `gh`, reads actual PR merge status (closed is not merged), and collects human discussion for review in `.profile/activity.json`. `--since TIMESTAMP` replays a window; `--output PATH` writes a different repo-relative report. It does not edit the README or advance the checkpoint automatically. The report is public-source evidence, not an automatically approved contribution list.

Run `python3 -m unittest discover -s tests` for the collector tests.

For each closed original PR, inspect the discussion and linked replacement PR. Verify that the replacement merged, then inspect its commits for Oliver's original author identity or `Co-authored-by: ... <102673257+oliver-mee@users.noreply.github.com>`. Record original URL, replacement URL, credited commit and attribution kind in `special_cases`. A maintainer's explicit adoption statement can support a contribution even without a co-author footer, but do not label that verified commit authorship. Never discard adopted work merely because the original PR is closed. Conversely, remove implementation claims for declined work with no adoption evidence.

Retain historical contributions even when Oliver no longer uses the product. Keep current-stack membership separate from contribution history. Review the saved special cases on every refresh; an author-only search cannot discover all maintainer-authored replacement PRs.

## Update procedure

1. Read `README.md`, this file and `.profile/state.json`.
2. Inspect only the relevant GitHub activity since `last_audited_through`.
3. Update README only for meaningful changes.
4. Update `.profile/state.json` with the new audit point, any newly established contribution repositories and any special evidence needed by future agents.
5. Put automated changes on a branch and open a draft pull request. Never merge the profile PR automatically.
