# AGENTS.md

本仓库是公众号「Neuro Nomad」的图文内容仓库：归档源稿对应的公众号排版产物（HTML）、预览页、装配脚本与图片素材。所有 Agent 在本仓库工作时遵循以下约定。

## 1. 仓库边界（最重要）

- 本仓库**只放公众号内容**：排版 HTML、预览页、装配脚本、图片素材。
- 基准源 Markdown 在另一个仓库：`/Users/admin/work/llm-benchmarks/benchmarks/<slug>.md`，**不在本仓库**。
- 两个仓库不要混：
  - `/Users/admin/work/llm-benchmarks`：基准文档库，含 `benchmarks/`、`sources/` 快照与自己的 `AGENTS.md`。
  - `/Users/admin/work/neuro-nomad`：公众号内容仓库，含 `llm-benchmarks/` 系列排版产物。
- 不要把基准文档、调研笔记、`sources/` 快照提交到本仓库；也不要把公众号 HTML / 图片提交到 `llm-benchmarks` 仓库。
- 图片素材落 `llm-benchmarks/<slug>/` 或 `llm-benchmarks/assets/<slug>/`，按现有文章约定，不要散落在仓库根目录。
- 本仓库**没有 `.gitignore`**；提交前用 `git status` 明确列出要加的文件，**不要 `git add -A`**。

## 2. 目录与命名

```
README.md
AGENTS.md
.claude/skills/gzh-layout-pro/          # 公众号排版技能：6 套主题组件库 + 校验脚本
llm-benchmarks/
├── README.md                           # 系列说明、文章索引、新增流程
├── <slug>/                             # 一篇文章一个子目录
│   ├── <slug>_排版_<主题中文名>(<theme>).html
│   └── <slug>_排版_<主题中文名>(<theme>)_预览.html
├── gzh_<theme>_gen.py                  # 该主题的装配脚本
├── gzh_<theme>_<slug>_gen.py           # 同主题多篇时用 slug 区分
├── patch_<theme>*.py                   # 一次性补丁，仅作历史留档
└── check_completeness.py               # 核对 HTML 相对源 Markdown 的内容零遗漏
```

- `<slug>` 取基准文档的 slug，如 `agents-last-exam`、`terminal-bench-v4-0`。
- 正文文件名：`{slug}_排版_{主题中文名}({theme}).html`；预览页在同名基础上加 `_预览`。
- 同一篇文章的多主题版本**都放同一个子目录**，共享内容装配层，只替换组件层。
- 生成脚本按主题命名；同主题多篇时用 `gzh_<theme>_<slug>_gen.py` 区分（如 `gzh_olive_hle_gen.py`、`gzh_graphite_ale_gen.py`）。

## 3. 系列与编号

当前文章索引以 `llm-benchmarks/README.md` 为单一来源：

| 序号 | 文章 | 主题 |
|---|---|---|
| 01 | Humanity's Last Exam (HLE) | 橄榄手记 |
| 02 | Agents' Last Exam (ALE) | 石墨极简风 |
| 03 | Science's Last Exam (SLE) | 待排 |
| 04 | Terminal-Bench 4.0 | 摸鱼绿（另留白禅意 / 橄榄手记为对照存档） |

- 新文章按顺序顺延编号；封面眉标统一写 `LLM BENCHMARKS · NN`，禅意版写 `—— LLM Benchmarks 系列 · NN`。
- 同一基准的大版本更新单独成篇；小版本修订并入原篇。
- 改序号必须同步四处：根 `README.md`、`llm-benchmarks/README.md`、该篇所有主题 HTML 的眉标、装配脚本里的眉标字符串。
- 新文章发布前先确认编号，避免已发布文章改号导致读者对不上。

## 4. 新增一篇的流程

1. **源稿**：确认 `/Users/admin/work/llm-benchmarks/benchmarks/<slug>.md` 已按该仓库 `AGENTS.md` 完成核验。
2. **选主题**：读 `.claude/skills/gzh-layout-pro/references/theme-index.md`，按题材推荐最契合的主题，并让用户确认；用户未指定时不要擅自定死。
3. **建目录与脚本**：新建 `llm-benchmarks/<slug>/`，写 `gzh_<theme>_<slug>_gen.py`，输出目录指向该子目录。
4. **生成正文**：脚本只输出 `<section>…</section>` 正文片段，不包 `<!DOCTYPE>` / `<html>` / `<head>` / `<body>`；所有文字节点用 `<span leaf="">` 包裹。
5. **生成预览**：`wrap_preview.py` 产出带「复制到公众号」按钮的预览页。
6. **双关校验**：
   - `validate_gzh_html.py`：必须 0 ERROR、0 WARNING。
   - `check_completeness.py`：表格单元格、URL、代码行、`##` / `###` 标题均 0 缺失。
7. **登记**：更新 `llm-benchmarks/README.md` 的文章列表与目录树，更新根 `README.md` 的系列最新文章；如改序号，按 §3 同步。

## 5. 排版契约

- 只用 `gzh-layout-pro` 提供的组件库，**不跨主题混用**；正文 HTML 由脚本生成，**不手改**，改内容改脚本后重跑。
- 平台红线：禁 `<style>` / `<script>` / `<div>`、`class` / `id`、`position:fixed/absolute/sticky`、`float`、`@media` / `@keyframes`、`display:grid`、CSS 变量；样式全部内联。
- 中文正文一律用全角标点；代码块、行内代码、URL、英文专名内部保持原样。
- 正文每段主动标 1–3 个关键词下划线；橙色锚点全篇 ≤3 处（石墨极简主题）。
- 代码块每行一个 `<p style="margin:0">`，**不用 `white-space:pre`**；缩进用全角空格。
- 图片用 `max-width:100%;height:auto;display:block;margin:0 auto`，不强制 `width:100%`。
- 一篇文章只有一个 END 分割线和一个签名区；不要在多处重复 CTA。

## 6. 校验命令

从本仓库根目录执行：

```bash
# 产物合规：禁用标签 / leaf 包裹 / 全角标点，须 0 ERROR
python3 .claude/skills/gzh-layout-pro/scripts/validate_gzh_html.py \
  "llm-benchmarks/agents-last-exam/agents-last-exam_排版_石墨极简风(graphite-minimal).html"

# 内容零遗漏：第二个参数传源 Markdown
python3 llm-benchmarks/check_completeness.py \
  "llm-benchmarks/agents-last-exam/agents-last-exam_排版_石墨极简风(graphite-minimal).html" \
  /Users/admin/work/llm-benchmarks/benchmarks/agents-last-exam.md

# 生成 / 刷新预览页
python3 .claude/skills/gzh-layout-pro/scripts/wrap_preview.py \
  "llm-benchmarks/agents-last-exam/agents-last-exam_排版_石墨极简风(graphite-minimal).html"
```

- `check_completeness.py` 不传第二个参数时默认核对 Terminal-Bench；其它基准必须传源稿路径。
- 两关都过再交付；WARNING 也要修到 0。

## 7. 提交与推送

- 提交信息格式：`<type>(<scope>): <subject>`，中文，50 字以内，如 `feat(gzh): 新增 ALE 第 2 篇图文`。
- 默认走 `feature/<slug>` 分支，**不直接推 `main`**，除非用户明确要求；推送后给出 PR 链接。
- 提交前先 `git status` 与 `git diff --stat`；只 `git add` 明确文件，不用 `git add -A`。
- 不提交 `.workbuddy/`、`*.miora`、`*_assets/`、临时文件，除非用户明确要求。
- 不 force push、不 `git reset --hard`；涉及 reset 一律用**绝对提交号**，不用 `HEAD~N`（沙箱重跑曾导致相对引用多退两格）。
- 文件删除一律用 `mv` 移到 `~/claude-temp/`，**不使用 `rm`**。

## 8. 已知坑

- `check_completeness.py` 会自动剔除 Mermaid fence；正文用内联 HTML 流程图等价呈现，不要把 Mermaid 源码直接放进公众号 HTML。
- 源稿表格单元格、URL、代码行、`##` / `###` 标题都会被逐项核对；删节必须同步改检查基线或检查器，不能静默漏内容。
- 源稿里的 `O*NET` 单星号、URL 外层反引号曾导致检查器误报，已在 `check_completeness.py` 处理；新增源稿出现类似标记时先看检查器输出再改正文。
- 同一篇文章多主题版本共享内容层，改内容后所有主题都要重跑，避免版本间内容漂移。
- 预览页的「复制」按钮只在预览外壳里，不在被复制的 `<section>` 内；不要把预览页当成正文提交给公众号。
- 图片素材与正文分离：`llm-benchmarks/hle/` 下的 PNG 目前只是归档，尚未接入排版；接入前先确认用户要求。

## 9. 当前状态

- 系列：LLM Benchmarks
- 已排：HLE（01 / 橄榄手记）、ALE（02 / 石墨极简风）、Terminal-Bench 4.0（04 / 摸鱼绿、留白禅意、橄榄手记）
- 待排：SLE（03，源稿 `benchmarks/sciences-last-exam.md`，建议等 v1 相对稳定后再排）
- 截至 2026-11-06，最近关键提交：`9684e2d chore(gzh): 合入 ALE 第 2 篇图文与序号调整`
