# Eduardo Alcantara

**I build and measure infrastructure for LLM agents, and fix bugs in quantum software.** Python and Rust. São Paulo, open to remote.

- **LLM agents:** measured where the tokens go in 641 real Claude Code sessions (134k API calls) and shipped the hooks that act on it. Three prompt-cache reports filed upstream in [anthropics/claude-code](https://github.com/anthropics/claude-code/issues?q=author%3Aedubraqd).
- **Quantum:** 4 PRs in review across [Qiskit](https://github.com/Qiskit/qiskit), [Qiskit Aer](https://github.com/Qiskit/qiskit-aer) and [Qiskit Nature](https://github.com/qiskit-community/qiskit-nature): overflow in the Rust core, a transpiler pass, simulator gate semantics, Hamiltonian sign conventions.
- **Upstream record:** fixes merged in [DataFusion](https://github.com/apache/datafusion/pull/24916), [Qdrant](https://github.com/qdrant/qdrant/pull/10448) and [CHT Core](https://github.com/medic/cht-core/pull/11439). 22 bugs filed, each with a reproduction; every fix ships with its test.

**Looking for:** remote roles in LLM/agent infrastructure, evals and retrieval, or quantum software tooling. UTC−3: full overlap with US Eastern, 4–5 h with Pacific. English and Portuguese, working Spanish.
**Contact:** [eduardoalcantara.sp@gmail.com](mailto:eduardoalcantara.sp@gmail.com)

---

## LLM agents

### [Lastro](https://github.com/edubraqd/lastro) — where the tokens go in a coding-agent session
Forensics on **641 Claude Code sessions / 134k API calls**. Cache reads are ~62% of the bill. 80% of cache *writes* come from a handful of full re-writes; an idle gap past the 1-hour TTL breaks the cache 93–97% of the time. Ships the measurement tools and four hooks built on the findings (context guard, batch eviction, handoff, canary). CI on Linux and Windows, Python 3.8 and 3.12.
Upstream: [#94177](https://github.com/anthropics/claude-code/issues/94177) cache forensics with mitigations from the literature · [#94417](https://github.com/anthropics/claude-code/issues/94417) memory block never shared across sessions · [#95694](https://github.com/anthropics/claude-code/issues/95694) unreachable cold-compact path.

`Python` `prompt caching` `agent hooks` `measurement`

### [arquimedesbr](https://github.com/edubraqd/arquimedesbr) — a library an agent can actually cite
234 books and papers turned into per-chapter markdown. Retrieval is BM25 + local embeddings fused, a cross-encoder rerank, and Rocchio feedback for a second round, so the agent gets the right ~400 words with title, chapter and page. No LLM in the pipeline, no network. Evaluated on 140 questions: the right passage is in the top 6 for 132 of them, 133 after one feedback round. Docs in EN and PT-BR.

`Python` `BM25` `embeddings` `rerankers` `evals` `MCP`

### Evals
[caveman#1044](https://github.com/JuliusBrussee/caveman/pull/1044) (106k ⭐): isolated eval runs from local config, per-language prompts, pt-BR snapshot. Measured −8% output tokens in Portuguese.

## Quantum software

| PR | What was wrong |
| --- | --- |
| [Qiskit#16980](https://github.com/Qiskit/qiskit/pull/16980) | `ParameterExpression` integer arithmetic overflowed its `i64`: panic in debug, silently wrong global phase in release. Checked arithmetic in the Rust core. |
| [Qiskit#17012](https://github.com/Qiskit/qiskit/pull/17012) | `OptimizeSwapBeforeMeasure` recursed into control-flow blocks and could drop SWAPs whose effect is observable there. |
| [qiskit-aer#2463](https://github.com/Qiskit/qiskit-aer/pull/2463) | Controlled gates with more than one target and a non-default `ctrl_state` (e.g. an open-control CSWAP) applied the control's X gates to a target qubit too. |
| [qiskit-nature#1410](https://github.com/qiskit-community/qiskit-nature/pull/1410) | `HeisenbergModel` and `IsingModel` docstrings gave the Hamiltonian with the wrong sign relative to the code. |

All four are in review. Each one started as a failing reproduction.

## Other upstream work

| Project | Merged | In review / filed |
| --- | --- | --- |
| [apache/datafusion](https://github.com/apache/datafusion) | [#24916](https://github.com/apache/datafusion/pull/24916) `RANGE` window frames over `Duration`/`Interval` | [13 issues](https://github.com/apache/datafusion/issues?q=author%3Aedubraqd): decimal overflow with negative scale, panics in `COPY … PARTITIONED BY`, `approx_percentile_cont` |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | [#10448](https://github.com/qdrant/qdrant/pull/10448) `Bits1_5` in the TurboQuant test matrices | |
| [medic/cht-core](https://github.com/medic/cht-core) | [#11439](https://github.com/medic/cht-core/pull/11439) task filter broke under Nepali digits | |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | | [#14069](https://github.com/juspay/hyperswitch/pull/14069) [#14070](https://github.com/juspay/hyperswitch/pull/14070) [#14071](https://github.com/juspay/hyperswitch/pull/14071) panics and overflow in `common_utils` |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | | [2 issues](https://github.com/apache/arrow-rs/issues?q=author%3Aedubraqd): decimal precision/scale overflow |
| [sepinf-inc/IPED](https://github.com/sepinf-inc/IPED) | | [#2975](https://github.com/sepinf-inc/IPED/pull/2975) [#2976](https://github.com/sepinf-inc/IPED/pull/2976) OCR parser, approved |

<details>
<summary><b>Products and day job</b></summary>

- **[RenderShot](https://rendershot.dev):** screenshot and PDF API with paying users. [GitHub Action](https://github.com/edubraqd/rendershot-action), [examples](https://github.com/edubraqd/rendershot-examples). `TypeScript` `Chromium`
- **Point of sale, twice:** an offline-first POS for a New York bakery (`Rust` `Tauri` `SQLite`) and a POS with inventory and Dominican tax compliance for a grocery (`Next.js` `PHP`). Client code is closed.
- **Logistics (day job):** internal systems on Power Apps for the operations floor, a Delphi 7 + Paradox ERP migrated to .NET + PostgreSQL, an Android app on the Play Store, and [restore-check](https://github.com/edubraqd/restore-check) for backup verification.

</details>

**Stack:** Python · Rust · TypeScript · SQL — Qiskit · Claude Code / MCP · BM25, embeddings, rerankers · PostgreSQL · Docker · GitHub Actions
