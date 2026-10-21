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
| Models / inference | Codex · Claude · Kimi · MiniMax |
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
- **[Alibaba Token Plan Wiki](https://github.com/oliver-mee/alibaba-token-plan-wiki)** — live-verified reference for Token Plan models, pricing, limits and gateway behaviour.
- **[iconify-cli](https://github.com/oliver-mee/iconify-cli)** — local-first Go CLI, SQLite index, agent skill and MCP server for searching, auditing and migrating roughly 294k Iconify icons.

### Open-source contributions

- **[models.dev](https://github.com/anomalyco/models.dev)** — China Token Plan provider [`PR #2145`](https://github.com/anomalyco/models.dev/pull/2145), Qwen 3.7 Plus [`PR #2146`](https://github.com/anomalyco/models.dev/pull/2146), GLM 5.2 and Kimi K2.7 Code [`PR #2684`](https://github.com/anomalyco/models.dev/pull/2684), gateway limits and capabilities [`PR #3695`](https://github.com/anomalyco/models.dev/pull/3695), multimodal metadata [`PR #3705`](https://github.com/anomalyco/models.dev/pull/3705), DeepSeek availability [`PR #7147`](https://github.com/anomalyco/models.dev/pull/7147) and provider overrides [`PR #7203`](https://github.com/anomalyco/models.dev/pull/7203); issue-led fixes for retired Qwen rows [`PR #6663`](https://github.com/anomalyco/models.dev/pull/6663) and DeepSeek catalogue changes [`PR #10544`](https://github.com/anomalyco/models.dev/pull/10544); open endpoint migration [`PR #7977`](https://github.com/anomalyco/models.dev/pull/7977).
- **[OpenClaw](https://github.com/openclaw/openclaw)** — Token Plan Team Edition provider and reasoning integration [`PR #94419`](https://github.com/openclaw/openclaw/pull/94419), Qwen 3.8 model support [`PR #131294`](https://github.com/openclaw/openclaw/pull/131294), and technical reports on catalogue limits and video input [`Issue #113577`](https://github.com/openclaw/openclaw/issues/113577) and hosted-catalogue video validation [`Issue #119587`](https://github.com/openclaw/openclaw/issues/119587).
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** — plugin-doctor validation [`PR #117451`](https://github.com/NousResearch/hermes-agent/pull/117451), model-name casing [`PR #121996`](https://github.com/NousResearch/hermes-agent/pull/121996), remote SSH session resume [`PR #99672`](https://github.com/NousResearch/hermes-agent/pull/99672), dynamic provider prefixes [`Commit 19e51d2`](https://github.com/NousResearch/hermes-agent/commit/19e51d2ccabf6c7f5d2f230777e9a9faedf84aa9), system-browser sign-in design [`PR #46554`](https://github.com/NousResearch/hermes-agent/pull/46554), and issue-led fixes for setup-app versioning [`PR #107186`](https://github.com/NousResearch/hermes-agent/pull/107186) and broken plugin discovery [`Issue #86154`](https://github.com/NousResearch/hermes-agent/issues/86154); open PRs for plugin-defined picker groups [`PR #86138`](https://github.com/NousResearch/hermes-agent/pull/86138), Team picker grouping [`PR #101222`](https://github.com/NousResearch/hermes-agent/pull/101222), provider-driven model identity [`PR #66135`](https://github.com/NousResearch/hermes-agent/pull/66135) and the v2 media catalogue [`PR #142141`](https://github.com/NousResearch/hermes-agent/pull/142141); production evidence for native OAuth refresh races [`Issue #55712`](https://github.com/NousResearch/hermes-agent/issues/55712).
- **[Basic Memory](https://github.com/basicmachines-co/basic-memory)** — CLI project reconciliation [`PR #1354`](https://github.com/basicmachines-co/basic-memory/pull/1354) and custom OpenAI-compatible embedding endpoint support [`PR #1370`](https://github.com/basicmachines-co/basic-memory/pull/1370).
- **[cmux](https://github.com/manaflow-ai/cmux)** — issue-led fixes for relay-drop SIGHUP [`Issue #8315`](https://github.com/manaflow-ai/cmux/issues/8315), live PTY preservation [`PR #9760`](https://github.com/manaflow-ai/cmux/pull/9760) and SSH agent hooks [`Issue #9793`](https://github.com/manaflow-ai/cmux/issues/9793).
- **[Orca](https://github.com/stablyai/orca)** — shell prompt composition [`PR #14619`](https://github.com/stablyai/orca/pull/14619), keypress safety [`PR #28221`](https://github.com/stablyai/orca/pull/28221), cookie-import diagnostics [`PR #28269`](https://github.com/stablyai/orca/pull/28269), staged profile switching [`PR #30452`](https://github.com/stablyai/orca/pull/30452), updater guidance [`PR #27464`](https://github.com/stablyai/orca/pull/27464) and Linux session-bus diagnosis [`Issue #21119`](https://github.com/stablyai/orca/issues/21119); open PRs for profile selection [`PR #31116`](https://github.com/stablyai/orca/pull/31116), browser controls [`PR #30353`](https://github.com/stablyai/orca/pull/30353), cookie imports [`PR #29054`](https://github.com/stablyai/orca/pull/29054), headless rendering [`PR #26139`](https://github.com/stablyai/orca/pull/26139), webhooks [`PR #31121`](https://github.com/stablyai/orca/pull/31121) and manual-update reporting [`PR #31124`](https://github.com/stablyai/orca/pull/31124); independent testing of element annotations [`PR #22813`](https://github.com/stablyai/orca/pull/22813) and OpenCode 2 status hooks [`PR #21322`](https://github.com/stablyai/orca/pull/21322).
- **[Hindsight](https://github.com/vectorize-io/hindsight)** — stable OpenCode 2 packages [`PR #4351`](https://github.com/vectorize-io/hindsight/pull/4351), plus issue-led fixes for Docker diagnostics ownership [`PR #4430`](https://github.com/vectorize-io/hindsight/pull/4430) and native companion-skill installation [`PR #4439`](https://github.com/vectorize-io/hindsight/pull/4439).
- **[OpenCodex](https://github.com/lidge-jun/opencodex)** — native pnpm self-updates [`PR #4235`](https://github.com/lidge-jun/opencodex/pull/4235), gateway-verified Token Plan catalogues [`PR #4888`](https://github.com/lidge-jun/opencodex/pull/4888) and GLM 5.3 restoration [`PR #5010`](https://github.com/lidge-jun/opencodex/pull/5010); open PRs for dated models and endpoints [`PR #7439`](https://github.com/lidge-jun/opencodex/pull/7439), tier routing [`PR #7435`](https://github.com/lidge-jun/opencodex/pull/7435) and test deadlines [`PR #7449`](https://github.com/lidge-jun/opencodex/pull/7449); independent runtime-fixture validation [`PR #7447`](https://github.com/lidge-jun/opencodex/pull/7447).
- **[Lark CLI](https://github.com/larksuite/cli)** — open PRs for Base field-group creation [`PR #2656`](https://github.com/larksuite/cli/pull/2656) and superseded CI-run handling [`PR #2814`](https://github.com/larksuite/cli/pull/2814), with validation and regression tests.
- **[Honcho](https://github.com/plastic-labs/honcho)** — embedding batch-size diagnosis [`PR #983`](https://github.com/plastic-labs/honcho/pull/983) and Qwen JSON-mode analysis [`Issue #663`](https://github.com/plastic-labs/honcho/issues/663).
- **[Get Shit Done](https://github.com/gsd-build/get-shit-done)** — custom-file backup false positives [`PR #2511`](https://github.com/gsd-build/get-shit-done/pull/2511), future-phase health warnings [`PR #2027`](https://github.com/gsd-build/get-shit-done/pull/2027), parallel worktree planning-file conflicts [`PR #1599`](https://github.com/gsd-build/get-shit-done/pull/1599) and MCP-tool fallback diagnosis [`PR #2074`](https://github.com/gsd-build/get-shit-done/pull/2074).
- **[notcrawl](https://github.com/openclaw/notcrawl)** — unsupported Notion block-child recovery [`PR #60`](https://github.com/openclaw/notcrawl/pull/60), preserving valid content during partial sync.
- **[HarnessKit](https://github.com/RealZST/HarnessKit)** — Linux ARM64 builds and installation [`PR #93`](https://github.com/RealZST/HarnessKit/pull/93).
- **[Notion MCP Server](https://github.com/awkoy/notion-mcp-server)** — Notion template creation and discovery [`PR #24`](https://github.com/awkoy/notion-mcp-server/pull/24).
- **[ccgram](https://github.com/alexei-led/ccgram)** — false-dead-session diagnosis [`PR #131`](https://github.com/alexei-led/ccgram/pull/131#issuecomment-5202100025), fixed upstream.
- **[claude-remember](https://github.com/Digital-Process-Tools/claude-remember)** — malformed-summary validation diagnosis [`PR #160`](https://github.com/Digital-Process-Tools/claude-remember/pull/160).
- **[AgentMemory](https://github.com/rohitg00/agentmemory)** — pinned-engine version, PATH and ARM64 install diagnosis [`PR #774`](https://github.com/rohitg00/agentmemory/pull/774).
- **[NanoClaw](https://github.com/nanocoai/nanoclaw)** — missing sqlite3 CLI dependency diagnosis [`PR #2309`](https://github.com/nanocoai/nanoclaw/pull/2309), followed by the in-tree wrapper fix.
- **[Fancy](https://github.com/danielpetho/fancy)** — open PR for searchable shadcn registry descriptions [`PR #71`](https://github.com/danielpetho/fancy/pull/71).
- **[Amicro](https://github.com/Subhan-code/Amicro--Micro-transitions-)** — registry-build diagnosis [`Issue #8`](https://github.com/Subhan-code/Amicro--Micro-transitions-/issues/8); maintainer confirmed the serving issue was resolved.
- **[OpenViking](https://github.com/volcengine/OpenViking)** — open PRs for OpenCode recall latency [`PR #5496`](https://github.com/volcengine/OpenViking/pull/5496), session-cleanup commit watermarks [`PR #5497`](https://github.com/volcengine/OpenViking/pull/5497) and Codex hooks surviving plugin upgrades [`PR #5986`](https://github.com/volcengine/OpenViking/pull/5986).
- **[Paperclip](https://github.com/paperclipai/paperclip)** — issue templates adopted upstream [`PR #4189`](https://github.com/paperclipai/paperclip/pull/4189); open PRs for git-ref installation [`PR #13928`](https://github.com/paperclipai/paperclip/pull/13928), non-Git workspaces [`PR #13929`](https://github.com/paperclipai/paperclip/pull/13929), dashboard regression tests [`PR #13925`](https://github.com/paperclipai/paperclip/pull/13925) and colour-scheme-safe favicons [`PR #14374`](https://github.com/paperclipai/paperclip/pull/14374); technical investigations of agent permission grants [`Issue #1323`](https://github.com/paperclipai/paperclip/issues/1323) and run-context write restrictions [`Issue #12637`](https://github.com/paperclipai/paperclip/issues/12637).
- **[OpenLogi](https://github.com/AprilNEA/OpenLogi)** — open PRs for thumb-wheel zoom [`PR #1743`](https://github.com/AprilNEA/OpenLogi/pull/1743), action-paced chained gestures [`PR #1761`](https://github.com/AprilNEA/OpenLogi/pull/1761) and continuous volume gestures [`PR #1909`](https://github.com/AprilNEA/OpenLogi/pull/1909).
- **[XiaomiGateway3](https://github.com/AlexxIT/XiaomiGateway3)** — Hub 2 gateway-key recovery [`PR #1781`](https://github.com/AlexxIT/XiaomiGateway3/pull/1781), incorporated into the released integration.
- **[coding_agent_session_search](https://github.com/Dicklesworthstone/coding_agent_session_search)** — OpenCode 2 session-indexing diagnosis [`Issue #504`](https://github.com/Dicklesworthstone/coding_agent_session_search/issues/504), shipped in v0.10.0.
- **[GBrain](https://github.com/garrytan/gbrain)** — native-provider configuration diagnosis [`Issue #3350`](https://github.com/garrytan/gbrain/issues/3350), addressed in the upstream gateway fix.
- **[acpx](https://github.com/openclaw/acpx)** — session-resume metadata diagnosis [`Issue #747`](https://github.com/openclaw/acpx/issues/747), fixed upstream.
- **[FunASR](https://github.com/modelscope/FunASR)** — missing CTC checkpoint investigation [`Issue #3496`](https://github.com/modelscope/FunASR/issues/3496), independently confirmed upstream; capability boundaries documented while the native artifact publication remains unresolved.

### Testing & technical review

- **[Google Workspace MCP](https://github.com/taylorwilsdon/google_workspace_mcp)** — production Slides-schema testing [`PR #777`](https://github.com/taylorwilsdon/google_workspace_mcp/pull/777) and Drive-scope compatibility evidence [`PR #761`](https://github.com/taylorwilsdon/google_workspace_mcp/pull/761).
- **[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)** — OAuth Basic-auth reproduction and token-handler analysis [`Issue #1315`](https://github.com/modelcontextprotocol/python-sdk/issues/1315).
- **[Printing Press](https://github.com/mvanhorn/cli-printing-press)** — binary-response diagnosis [`Issue #4066`](https://github.com/mvanhorn/cli-printing-press/issues/4066), live-test coverage investigation [`Issue #4046`](https://github.com/mvanhorn/cli-printing-press/issues/4046) and an npm-statistics failure report [`Issue #4244`](https://github.com/mvanhorn/cli-printing-press/issues/4244).
- **[Claude Honcho](https://github.com/plastic-labs/claude-honcho)** — per-directory peer-isolation review [`PR #64`](https://github.com/plastic-labs/claude-honcho/pull/64).
- **[OpenCode](https://github.com/anomalyco/opencode)** — plugin-cache update investigation [`Issue #54127`](https://github.com/anomalyco/opencode/issues/54127).
- **[Codex](https://github.com/openai/codex)** — non-interactive session naming [`Issue #46804`](https://github.com/openai/codex/issues/46804), plugin-upgrade hook failures [`Issue #31383`](https://github.com/openai/codex/issues/31383) and remote app-server lifecycle evidence [`Issue #24542`](https://github.com/openai/codex/issues/24542).
- **[VoiceMode](https://github.com/mbailey/voicemode)** — OAuth redirect CSP diagnosis [`Issue #329`](https://github.com/mbailey/voicemode/issues/329).

[Full public contribution record](CONTRIBUTIONS.md)
