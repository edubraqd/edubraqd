<div align="center">

# Eduardo Alcantara

### I find the integer overflow before it ships.

**20 correctness bugs filed in DataFusion, Arrow, Hyperswitch and Claude Code · fixes merged in DataFusion and Qdrant · 8 PRs in review** — since September 2026, each bug with a reproduction, each fix with a test.

Software engineer in São Paulo. Day job: the systems a logistics floor runs on. Open-source time: **panics and overflows in Rust codebases**, and **measuring what LLM agents cost** (641 sessions, 134k API calls).

[![Merged upstream PRs](https://img.shields.io/badge/merged_upstream_PRs-2-2EA44F?style=flat-square&logo=github)](https://github.com/pulls?q=is%3Apr+author%3Aedubraqd+is%3Amerged+-user%3Aedubraqd)
[![Open upstream PRs](https://img.shields.io/badge/in_review-8-0EA5E9?style=flat-square&logo=github)](https://github.com/pulls?q=is%3Apr+author%3Aedubraqd+is%3Aopen+-user%3Aedubraqd)
[![Bugs reported](https://img.shields.io/badge/bugs_filed-20-7C3AED?style=flat-square&logo=github)](https://github.com/issues?q=is%3Aissue+author%3Aedubraqd+-user%3Aedubraqd)

**Open to remote roles — Rust, backend, LLM-agent infrastructure.** UTC−3: full overlap with US Eastern, 4–5 h with Pacific. English, Portuguese, working Spanish.

[![Email](https://img.shields.io/badge/eduardoalcantara.sp%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:eduardoalcantara.sp@gmail.com)
[![RenderShot](https://img.shields.io/badge/RenderShot-screenshot%20API-0F766E?style=flat-square)](https://rendershot.dev)
[![Lastro](https://img.shields.io/badge/Lastro-token%20forensics-6366F1?style=flat-square)](https://github.com/edubraqd/lastro)
[![arquimedesbr](https://img.shields.io/badge/arquimedesbr-library%20for%20agents-8B5CF6?style=flat-square)](https://github.com/edubraqd/arquimedesbr)

</div>

## 🛰️ Upstream open-source

Same pattern every time: find the panic, write the reproduction, fix it, keep the test. Combined stars of the projects below: **352k**.

| Project | Stars | Merged | Open |
| --- | ---: | --- | --- |
| [apache/datafusion](https://github.com/apache/datafusion) | 9.3k ⭐ | [#24916](https://github.com/apache/datafusion/pull/24916) — free `RANGE` window frames over `Duration`/`Interval` | [13 issues](https://github.com/apache/datafusion/issues?q=author%3Aedubraqd): decimal overflow with negative scale, panics in `COPY ... PARTITIONED BY`, `approx_percentile_cont`, `Date64` display |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 34.7k ⭐ | [#10448](https://github.com/qdrant/qdrant/pull/10448) — `Bits1_5` in the TurboQuant test matrices | |
| [Qiskit/qiskit](https://github.com/Qiskit/qiskit) | 7.8k ⭐ | | [#16980](https://github.com/Qiskit/qiskit/pull/16980) — `ParameterExpression` integer arithmetic overflowed its `i64`: panic in debug, silently wrong global phase in release. Checked arithmetic in the Rust core |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | 43.6k ⭐ | | [#14069](https://github.com/juspay/hyperswitch/pull/14069) [#14070](https://github.com/juspay/hyperswitch/pull/14070) [#14071](https://github.com/juspay/hyperswitch/pull/14071) — `common_utils`: masking underflow, `MaskedEmail` panic on short local parts, `Decimal` overflow in major-unit conversion |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 106.6k ⭐ | | [#1044](https://github.com/JuliusBrussee/caveman/pull/1044) — eval isolation, per-language prompts, pt-BR snapshot; measured −8% output tokens in Portuguese |
| [apache/arrow-rs](https://github.com/apache/arrow-rs) | 3.6k ⭐ | | [2 issues](https://github.com/apache/arrow-rs/issues?q=author%3Aedubraqd) — decimal arithmetic overflows `i8` precision/scale math for negative scales |
| [meyfa/CobolCraft](https://github.com/meyfa/CobolCraft) | 702 ⭐ | | [#416](https://github.com/meyfa/CobolCraft/pull/416) [#417](https://github.com/meyfa/CobolCraft/pull/417) — JSON integer/float encoding bugs, in COBOL |
| [kobotoolbox/kpi](https://github.com/kobotoolbox/kpi) | 181 ⭐ | | [#7586](https://github.com/kobotoolbox/kpi/pull/7586) — save asset and its new version in one transaction (Django) |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | 146.3k ⭐ | | [2 issues](https://github.com/anthropics/claude-code/issues?q=author%3Aedubraqd) — [#94177](https://github.com/anthropics/claude-code/issues/94177) prompt-cache forensics from real sessions, with paper-backed mitigations |

## 🧬 Things I build

<table>
<tr>
<td width="50%" valign="top">

### 📏 [Lastro](https://github.com/edubraqd/lastro)
Where the tokens go in a Claude Code session, measured on **641 real sessions / 134k API calls**. Cache reads are ~62% of the bill; 80% of cache *writes* come from a handful of full re-writes (an idle gap past the 1-hour TTL breaks the cache 93–97% of the time). Ships the measurement tools and four hooks that act on the findings. Filed upstream as [anthropics/claude-code#94177](https://github.com/anthropics/claude-code/issues/94177).

`Python` `prompt caching` `Claude Code hooks` `measurement`

</td>
<td width="50%" valign="top">

### 📚 [arquimedesbr](https://github.com/edubraqd/arquimedesbr)
Turns a personal library (**234 books and papers**) into per-chapter markdown with BM25 + local embeddings + cross-encoder rerank and Rocchio feedback, so an agent gets the *right 400 words* with title, chapter and page. No LLM in the pipeline, no network. Evaluated on 140 questions: the agent choosing the category by hand beats every automatic classifier tried. Docs in EN and PT-BR.

`Python` `BM25` `embeddings` `rerankers` `MCP`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📸 [RenderShot](https://rendershot.dev)
URL or HTML in, PNG/JPEG/WebP/PDF out, as an API. Paid product with users. [GitHub Action](https://github.com/edubraqd/rendershot-action) and [runnable examples](https://github.com/edubraqd/rendershot-examples) in cURL, Node, Python and PHP.

`TypeScript` `Chromium` `GitHub Actions`

</td>
<td width="50%" valign="top">

### 🧾 Point of sale, twice
A bakery in New York: sell and close the till with no internet, thermal printing, PIN per sale, sync to a web admin (`Rust · Tauri · SQLite`). A grocery in the Dominican Republic: cash, inventory, store credit, delivery and local tax compliance — NCF, 606/607 reports (`TypeScript · PHP · Next.js`). Client code is closed by agreement.

`Rust` `Tauri` `Next.js` `PHP` `MySQL`

</td>
</tr>
</table>

## 🏭 Systems in production

Day job in **logistics**: several internal systems for the operation on **Microsoft Power Apps**. The users are the people on the floor, so the constraint is always the same: it has to work on a phone and need zero training.

| System | Problem | Stack |
|---|---|---|
| ERP migration | Delphi 7 + Paradox management system replaced by a current stack | .NET · PostgreSQL |
| Android app on the Play Store | — | Kotlin · Flutter |
| [restore-check](https://github.com/edubraqd/restore-check) | Restore a database backup into a throwaway container, validate it, report | Bash · Docker |

## 🧰 Stack

### 🧩 Languages

<div align="center">

![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)
![.NET](https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white)
![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)

</div>

### 🧠 Agents · retrieval · quantum

<div align="center">

![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=claude&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-111827?style=for-the-badge)
![Prompt caching](https://img.shields.io/badge/Prompt_caching-6366F1?style=for-the-badge)
![BM25](https://img.shields.io/badge/BM25-4F46E5?style=for-the-badge)
![Embeddings](https://img.shields.io/badge/Embeddings-7C3AED?style=for-the-badge)
![Cross-encoder rerank](https://img.shields.io/badge/Cross--encoder_rerank-9333EA?style=for-the-badge)
![Rocchio](https://img.shields.io/badge/Rocchio_feedback-7E22CE?style=for-the-badge)
![Qiskit](https://img.shields.io/badge/Qiskit-6929C4?style=for-the-badge&logo=qiskit&logoColor=white)

</div>

### 🧱 Apps · data · ops

<div align="center">

![Tauri](https://img.shields.io/badge/Tauri-24C8D8?style=for-the-badge&logo=tauri&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Power Apps](https://img.shields.io/badge/Power_Apps-742774?style=for-the-badge)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

## 🌀 Contribution streak

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=edubraqd&theme=dark&hide_border=true" />
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=edubraqd&theme=default&hide_border=true" />
  <img alt="GitHub streak" src="https://streak-stats.demolab.com?user=edubraqd&hide_border=true" />
</picture>
</div>

## 🐍 Contributions in motion

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/edubraqd/edubraqd/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/edubraqd/edubraqd/output/github-contribution-grid-snake.svg" />
  <img alt="GitHub contribution snake" src="https://raw.githubusercontent.com/edubraqd/edubraqd/output/github-contribution-grid-snake.svg" />
</picture>
</div>

---

<div align="center">
<sub>Find the panic → write the reproduction → fix it → keep the test.</sub>
</div>
