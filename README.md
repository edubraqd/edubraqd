## Eduardo Alcantara

Software engineer in São Paulo, Brazil. I build systems that run in production — logistics tooling, point-of-sale, APIs — and I spend my open-source time on two things: **the infrastructure around LLM agents** (context, retrieval, cost) and **numerical correctness in Rust**, most recently inside **Qiskit**.

Open to roles in LLM/agent engineering and quantum software. Remote or hybrid (SP). English and Portuguese; working Spanish.

---

### LLM agents: measure first, then build

- [`claude-context-forensics`](https://github.com/edubraqd/claude-context-forensics) — where the tokens go in an agentic coding session, measured on **641 real sessions / 134k API calls**. Cache reads are ~62% of the bill; 80% of cache *writes* come from a handful of full re-writes (an idle gap past the 1-hour TTL breaks the cache 93–97% of the time). Ships the measurement tools and four hooks that act on the findings. Filed upstream as [anthropics/claude-code#94177](https://github.com/anthropics/claude-code/issues/94177).
- [`arquimedesbr`](https://github.com/edubraqd/arquimedesbr) — turns a personal library (178 books and papers) into per-chapter markdown with BM25 + embedding search + cross-encoder rerank and Rocchio relevance feedback, so an agent gets the *right 400 words* with title, chapter and page. No LLM in the pipeline, no network. Evaluated on a 140-question benchmark: choosing the category by hand lifts hit@1 from 73 to 95 — the agent's judgment beats every automatic classifier I tried.
- [`caveman`](https://github.com/JuliusBrussee/caveman) (contributor) — eval harness isolation, per-language prompts and a pt-BR snapshot for a token-saving Claude Code skill; measured the effect at −8% output tokens in Portuguese ([#1044](https://github.com/JuliusBrussee/caveman/pull/1044)).

### Quantum computing

Starting where I can be useful now — correctness of the classical layer under the circuits:

- [Qiskit/qiskit#16980](https://github.com/Qiskit/qiskit/pull/16980) — `ParameterExpression` integer arithmetic overflowed its internal `i64`: panic in debug, silently wrong global phase in release. Reproduced from the public Python API, fixed with checked arithmetic in the Rust core.

### Rust, correctness and open source

Pattern across projects: find the panic, write the reproduction, fix it, keep the test.

| Project | What |
|---|---|
| [apache/datafusion](https://github.com/apache/datafusion/issues?q=author%3Aedubraqd) | 14 correctness bugs reported in the SQL engine — decimal overflow with negative scale, `RANGE` frames over `Interval`/`Duration`, panics in `COPY ... PARTITIONED BY`, `approx_percentile_cont`, `Date64` display. Fixes submitted; 1 PR open. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant/pull/10448) | Merged: test coverage for `Bits1_5` in the TurboQuant quantization matrices. |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch/pulls?q=author%3Aedubraqd) | 3 bugs + 3 PRs in `common_utils`: masking underflow, `MaskedEmail` panic on short local parts, decimal overflow in major-unit conversion. |
| [apache/arrow-rs](https://github.com/apache/arrow-rs/issues?q=author%3Aedubraqd) | Decimal arithmetic overflows `i8` precision/scale math for negative scales. |
| [kobotoolbox/kpi](https://github.com/kobotoolbox/kpi/pull/7586) · [meyfa/CobolCraft](https://github.com/meyfa/CobolCraft/pulls?q=author%3Aedubraqd) | Asset save in one transaction (Django); JSON integer/float encoding bugs — in COBOL. |

### Systems in production

Day job in **logistics**, where I have built several internal systems for the operation on **Microsoft Power Apps**. The users are the people on the floor, so the constraint is always the same: it has to work on a phone and need zero training.

Freelance and own products (client code is closed by agreement):

| System | Problem | Stack |
|---|---|---|
| [RenderShot](https://rendershot.dev) | URL/HTML → PNG/JPEG/WebP/PDF as an API; GitHub Action and SDK examples. Paid product with users. | TypeScript · Chromium |
| Order-taking POS for a bakery in New York | Sell and close the till with no internet; thermal printing, PIN per sale, sync to a web admin | Rust · Tauri · SQLite |
| POS for a grocery in the Dominican Republic | Cash, inventory, store credit, delivery and local tax compliance (NCF, 606/607 reports) | TypeScript · PHP · Next.js |
| ERP migration | Delphi 7 + Paradox management system replaced by a current stack | .NET · PostgreSQL |
| Android app on the Play Store | — | Kotlin · Flutter |

### Stack

`Rust` `Python` `TypeScript` `SQL` · `Qiskit` · `Power Apps` · `Tauri` `Next.js` `PostgreSQL` `SQLite` · `Claude Code` `MCP` `embeddings / BM25 / rerankers`

### Contact

eduardoalcantara.sp@gmail.com · [rendershot.dev](https://rendershot.dev)
