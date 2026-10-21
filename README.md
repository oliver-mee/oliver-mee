<h1 align="center">Oliver Mee</h1>

<p align="center">
  Always experimenting with new tools, ideas and ways of working.
</p>

<p align="center">
  Interested in my interests? <a href="https://github.com/oliver-mee/stars">Here are my stars.</a>
</p>

<p align="center">
  <a href="https://preface.ai">Preface</a> &middot; Hong Kong
</p>

---

### What I'm into

Most of what I build is private or still in progress, so only some of it ends up here. I spend a lot of time around AI coding agents: the skills, tools, infrastructure and integrations that make them genuinely useful day to day. I self-host a lot of the underlying stack, and when I run into problems in tools I use, I usually end up digging into them and contributing fixes upstream.

### Current stack

| Layer | What I use |
| --- | --- |
| Models / inference | Codex · Claude · Kimi · MiniMax · [Alibaba Cloud Token Plan](https://www.alibabacloud.com/help/en/model-studio/token-plan-overview) |
| Agent runtime | [Hermes](https://github.com/NousResearch/hermes-agent) |
| Coding agents | [OpenCode](https://github.com/anomalyco/opencode) · [Claude Code](https://github.com/anthropics/claude-code) · [Codex](https://github.com/openai/codex) |
| Agent workspace | [Orca](https://github.com/stablyai/orca) |
| Agent orchestration | [Paperclip](https://github.com/paperclipai/paperclip) |
| Session memory & knowledge | [OpenViking](https://github.com/volcengine/OpenViking) · [Basic Memory](https://github.com/basicmachines-co/basic-memory) |
| Browser automation | [Agent Browser](https://github.com/vercel-labs/agent-browser) |
| VPS | [Oracle Cloud](https://www.oracle.com/cloud/) |
| Sync & config | [Syncthing](https://github.com/syncthing/syncthing) · [chezmoi](https://github.com/twpayne/chezmoi) |

### Projects

- **[Hermes Alibaba Token Plan](https://github.com/oliver-mee/hermes-alibaba-token-plan)** — Hermes provider plugin for Alibaba Cloud Token Plan across Global/China and Personal/Team tiers, with native image, speech, transcription and video tools.
- **[iconify-cli](https://github.com/oliver-mee/iconify-cli)** — local-first Go CLI, SQLite index, agent skill and MCP server for searching, auditing and migrating roughly 294k Iconify icons.
- **[Alibaba Token Plan Wiki](https://github.com/oliver-mee/alibaba-token-plan-wiki)** — live-verified reference for Token Plan models, pricing, limits and gateway behaviour.
- **[shortcuttr](https://github.com/oliver-mee/shortcuttr)** — tiny web redirector for launching named Apple Shortcuts from URL query parameters.

### Open-source contributions

- **[models.dev](https://github.com/anomalyco/models.dev)** — [Alibaba Token Plan Global/China providers; qwen3.7-plus, glm-5.2 and kimi-k2.7-code coverage; live-gateway limit and capability corrections; multimodal metadata; deepseek-v4.1-flash provider overrides](https://github.com/anomalyco/models.dev/pull/3695).
- **[OpenClaw](https://github.com/openclaw/openclaw)** — [first-class Alibaba Token Plan provider; Global/China onboarding; model catalogue, thinking and streaming behaviour; live-gateway catalogue corrections](https://github.com/openclaw/openclaw/pull/94419).
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** — [plugin-doctor provider validation](https://github.com/NousResearch/hermes-agent/pull/117451) and [vendor-cased model display names](https://github.com/NousResearch/hermes-agent/pull/121996); open PRs for [Token Plan picker grouping](https://github.com/NousResearch/hermes-agent/pull/101222) and the [v2 provider/media catalogue](https://github.com/NousResearch/hermes-agent/pull/142141).
- **[Basic Memory](https://github.com/basicmachines-co/basic-memory)** — [CLI project reconciliation](https://github.com/basicmachines-co/basic-memory/pull/1354) and [custom OpenAI-compatible embedding endpoint support](https://github.com/basicmachines-co/basic-memory/pull/1370).
- **[cmux](https://github.com/manaflow-ai/cmux)** — [remote relay lifecycle](https://github.com/manaflow-ai/cmux/pull/9760) and [SSH-agent-hook diagnoses](https://github.com/manaflow-ai/cmux/issues/9793) that led to upstream fixes.
- **[Orca](https://github.com/stablyai/orca)** — [shell prompt composition](https://github.com/stablyai/orca/pull/14619), [browser keypress safety](https://github.com/stablyai/orca/pull/28221), [cookie-import diagnostics](https://github.com/stablyai/orca/pull/28269), [staged profile switching](https://github.com/stablyai/orca/pull/30452) and [updater guidance](https://github.com/stablyai/orca/pull/27464); open work on [browser controls](https://github.com/stablyai/orca/pull/30353), [cookie imports](https://github.com/stablyai/orca/pull/29054), [headless rendering](https://github.com/stablyai/orca/pull/26139) and [webhooks](https://github.com/stablyai/orca/pull/31121).
- **[Hindsight](https://github.com/vectorize-io/hindsight)** — [OpenCode 2 stable-package migration for the coding-agent integration](https://github.com/vectorize-io/hindsight/pull/4351).
- **[OpenCodex](https://github.com/lidge-jun/opencodex)** — [Alibaba Token Plan catalogue and endpoint updates](https://github.com/lidge-jun/opencodex/pull/7439); open work on [opt-in tier routing](https://github.com/lidge-jun/opencodex/pull/7435) and [shell-integration test deadlines](https://github.com/lidge-jun/opencodex/pull/7449).
- **[Lark CLI](https://github.com/larksuite/cli)** — open PRs for [Base field-group creation](https://github.com/larksuite/cli/pull/2656) and [superseded CI-run handling](https://github.com/larksuite/cli/pull/2814), with validation and regression tests.
- **[Honcho](https://github.com/plastic-labs/honcho)** — [OpenAI-compatible embedding batch-size diagnosis for providers such as DashScope, followed by upstream configurable batch sizing](https://github.com/plastic-labs/honcho/pull/983).
- **[Get Shit Done](https://github.com/gsd-build/get-shit-done)** — [custom-file backup false positives](https://github.com/gsd-build/get-shit-done/pull/2511), [future-phase health warnings](https://github.com/gsd-build/get-shit-done/pull/2027), [parallel worktree planning-file conflicts](https://github.com/gsd-build/get-shit-done/pull/1599) and [MCP-tool fallback diagnosis](https://github.com/gsd-build/get-shit-done/pull/2074).
- **[notcrawl](https://github.com/openclaw/notcrawl)** — [unsupported Notion block-child recovery and retention of previously valid blocks during partial sync](https://github.com/openclaw/notcrawl/pull/60).
- **[HarnessKit](https://github.com/RealZST/HarnessKit)** — [Linux ARM64/aarch64 release builds and installer support for machines such as Oracle Cloud Ampere instances](https://github.com/RealZST/HarnessKit/pull/93).
- **[Notion MCP Server](https://github.com/awkoy/notion-mcp-server)** — [page creation from Notion templates and data-source template discovery](https://github.com/awkoy/notion-mcp-server/pull/24).
- **[ccgram](https://github.com/alexei-led/ccgram)** — [transient tmux-poll false-dead-session diagnosis; maintainer-confirmed fix landed through the lower-level reconciliation path](https://github.com/alexei-led/ccgram/pull/131#issuecomment-5202100025).
- **[claude-remember](https://github.com/Digital-Process-Tools/claude-remember)** — [malformed-summary validation bug diagnosis that fed into the merged save-pipeline fix](https://github.com/Digital-Process-Tools/claude-remember/pull/160).
- **[AgentMemory](https://github.com/rohitg00/agentmemory)** — [iii-engine version/PATH mismatch and aarch64 install traps; upstream fix isolated the pinned engine in a private install path](https://github.com/rohitg00/agentmemory/pull/774).
- **[NanoClaw](https://github.com/nanocoai/nanoclaw)** — [missing sqlite3 CLI dependency across migration and skill workflows; upstream replacement with the in-tree better-sqlite3 path](https://github.com/nanocoai/nanoclaw/pull/2309).
- **[Fancy](https://github.com/danielpetho/fancy)** — [open PR for shadcn registry descriptions and schema wiring across 45 components for registry search](https://github.com/danielpetho/fancy/pull/71).
- **[Amicro](https://github.com/Subhan-code/Amicro--Micro-transitions-)** — [registry-build diagnosis](https://github.com/Subhan-code/Amicro--Micro-transitions-/issues/8); maintainer confirmed the serving issue was resolved.
- **[OpenViking](https://github.com/volcengine/OpenViking)** — open PRs for [OpenCode recall latency](https://github.com/volcengine/OpenViking/pull/5496), [session-cleanup commit watermarks](https://github.com/volcengine/OpenViking/pull/5497) and [Codex hooks surviving plugin upgrades](https://github.com/volcengine/OpenViking/pull/5986).
- **[Paperclip](https://github.com/paperclipai/paperclip)** — open PRs for [git-ref installation](https://github.com/paperclipai/paperclip/pull/13928), [intentional non-Git workspaces](https://github.com/paperclipai/paperclip/pull/13929), [dashboard regression coverage](https://github.com/paperclipai/paperclip/pull/13925) and [colour-scheme-safe favicons](https://github.com/paperclipai/paperclip/pull/14374).
- **[OpenLogi](https://github.com/AprilNEA/OpenLogi)** — open PRs for [thumb-wheel zoom](https://github.com/AprilNEA/OpenLogi/pull/1743) and [responsive, action-paced chained gestures](https://github.com/AprilNEA/OpenLogi/pull/1761).
- **[XiaomiGateway3](https://github.com/AlexxIT/XiaomiGateway3)** — [Hub 2 gateway-key recovery](https://github.com/AlexxIT/XiaomiGateway3/pull/1781) implementation and investigation, incorporated into the released integration.
- **[coding_agent_session_search](https://github.com/Dicklesworthstone/coding_agent_session_search)** — [OpenCode 2 session-indexing diagnosis and reproduction](https://github.com/Dicklesworthstone/coding_agent_session_search/issues/504), fixed upstream and shipped in v0.10.0.
