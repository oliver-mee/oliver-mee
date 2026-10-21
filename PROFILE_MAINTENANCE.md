# Profile maintenance

This file is the handoff for any agent maintaining this GitHub profile. It replaces the old scheduled GitHub Actions updater.

The instructions are runner-agnostic. Hermes is currently the intended cron runner, but Claude Code, Codex, OpenCode or another agent should be able to use the same file without changing the maintenance model.

## Goal

Keep `README.md` current without repeatedly re-auditing Oliver's entire GitHub history.

Read `.profile/state.json` and the reviewed `.profile/coverage.json` first. Incremental collection is appropriate only after the full-history baseline has been reconciled. A saved checkpoint is not proof of complete coverage. When Oliver challenges omissions, use `--full`, inspect authored activity, commented-on items, commit attribution and closed-item timelines, and reconcile every candidate before updating the baseline. Keep historical implementation, diagnosis and independent testing credit separate from current stack usage.

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
- Use plain-text contribution descriptions followed by compact, code-styled evidence links: ``China Token Plan provider [`PR #2145`](https://github.com/anomalyco/models.dev/pull/2145)``. Label issue and commit references distinctly. Keep repository-name links pointing at the project. GitHub's native shortened/rich issue references are conversation features, not README-file features; do not promise native PR pills or unfurls. Never link whole prose descriptions or use one reference for unrelated changes. Keep landed work direct and genuinely open proposals labelled.
- `.profile/profile.json` is the reviewed contribution-display source. Edit its text/reference parts, then run `python3 scripts/audit.py --render`; do not hand-edit the generated contribution sections. The introduction, stack and Projects sections are preserved by the renderer. Reference labels use a non-breaking space so the kind and number stay together on mobile. Explicit PR links retain GitHub-native hovercards; verify the rendered GitHub page at the tested commit rather than assuming Markdown appearance from source.
- Do not explain the tracking methodology in the README.
- Preserve existing contributions unless new evidence changes them.
- Add a new repository only when the activity meets the meaningful-contribution standard above.

## Projects

The Projects section is broader than "currently building".

- User-owned public non-fork repositories can be included even when they are older or inactive.
- `stars` does not belong in Projects; it is linked near the top of the profile.
- Keep Hermes Alibaba Token Plan and Alibaba Token Plan Wiki adjacent at the top of Projects, followed by iconify-cli. Do not re-add shortcuttr or a Token Plan vendor/referral link in Models / inference during routine maintenance.
- A fork can appear only when Oliver has made substantial original changes to it, and the wording must make the derivative relationship clear rather than presenting the upstream project as his own.
- Do not pad the section with untouched or near-identical forks.

## Profile voice

Keep the profile concise and human. Do not turn it into a résumé, a changelog or an audit report.

The opening line is intentionally:

> Always experimenting with new tools, ideas and ways of working.

Do not rewrite it during routine maintenance.

## Reusable audit command

Run `python3 scripts/audit.py` from any directory for incremental collection. For a challenged or missing baseline, use:

```sh
python3 scripts/audit.py --full --output .profile/full-history.json
python3 scripts/audit.py --timelines --output .profile/full-history.json
python3 scripts/audit.py --full --participated --output .profile/participation-history.json
python3 scripts/audit.py --full --commits --output .profile/commit-history.json
# Review evidence and update .profile/coverage.json and .profile/profile.json.
python3 scripts/audit.py --render
python3 scripts/audit.py --check
```

The collector paginates public-source `gh` searches, checks real merge status and reads discussion/timeline evidence. Commit search results must be deduplicated by SHA: copies in downstream forks are not separate contributions. Verify original authorship and default-branch ancestry in the canonical upstream when search returns a fork instead. Search cannot prove the absence of unindexed, review-only or deleted activity; retain known evidence beyond the search results.

New full-history raw collection reports are local working evidence and are ignored by Git. Commit the reviewed coverage ledger and rendered `CONTRIBUTIONS.md`, not large third-party discussion dumps. The older committed `.profile/activity.json` is a historical incremental snapshot, not the coverage baseline. The full record distinguishes directly merged work, adopted implementations, issue-led fixes, independent testing/review and activity not claimed as implementation. An update to the main profile must be reconciled against that record, not selected from a truncated search result.

Run `python3 -m unittest discover -s tests` for the collector tests.

For each closed original PR, inspect the discussion and linked replacement PR. Verify that the replacement merged, then inspect its commits for Oliver's original author identity or `Co-authored-by: ... <102673257+oliver-mee@users.noreply.github.com>`. Record original URL, replacement URL, credited commit and attribution kind in `special_cases`. A maintainer's explicit adoption statement can support a contribution even without a co-author footer, but do not label that verified commit authorship. Never discard adopted work merely because the original PR is closed. Conversely, remove implementation claims for declined work with no adoption evidence.

Retain historical contributions even when Oliver no longer uses the product. Keep current-stack membership separate from contribution history. Review the saved special cases on every refresh; an author-only search cannot discover all maintainer-authored replacement PRs.

## Update procedure

1. Read `README.md`, this file and `.profile/state.json`.
2. Inspect only the relevant GitHub activity since `last_audited_through`.
3. Update README only for meaningful changes.
4. Update `.profile/state.json` with the new audit point, any newly established contribution repositories and any special evidence needed by future agents.
5. Put automated changes on a branch and open a draft pull request. Never merge the profile PR automatically.
