# LLM Benchmarks 系列

逐篇拆解大模型评测基准：它到底考什么、怎么跑、分数怎么读、哪里最容易误读。
面向工程师而非刷榜读者——每篇都尽量给出可复现的评测链路、原始数据口径与已知缺陷，
而不是只复述榜首分数。

收录范围：模型能力评测（agent / 编码 / 推理 / 工具调用）与评测方法论。
同一基准的大版本更新（如 v4.0 → v5.0）单独成篇；小版本修订并入原篇。

仓库级 Agent 约定（仓库边界、校验命令、提交规范）见 [../AGENTS.md](../AGENTS.md)。

## 文章列表

| 序号 | 文章 | 基准版本 | 排版版本 | 源稿 |
|---|---|---|---|---|
| 01 | [Humanity's Last Exam (HLE)](hle/hle_排版_橄榄手记(olive-journal).html) | 2,500 题（2026-11 核验） | 橄榄手记 | `benchmarks/hle.md` |
| 02 | [Agents' Last Exam (ALE)](agents-last-exam/agents-last-exam_排版_石墨极简风(graphite-minimal).html) | v1.1（122 tasks，2026-11-05） | 石墨极简风 | `benchmarks/agents-last-exam.md` |
| 03 | Science's Last Exam (SLE) | Release v1（113 tasks，2026-11-06） | 待排 | `benchmarks/sciences-last-exam.md` |
| 04 | [Terminal-Bench 4.0](terminal-bench-v4-0/terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html) | v4.0.0 | 摸鱼绿 / 留白禅意 / 橄榄手记 | `benchmarks/terminal-bench-v4-0.md` |

HLE 为系列第一篇，按用户指定使用**橄榄手记**；ALE 为第二篇，主推**石墨极简风**；SLE 规划为第三篇，建议等 ALE 发布且 SLE v1 相对稳定后再排；Terminal-Bench 4.0 原为 02，现顺延为 04，主推版本为**摸鱼绿**，另两版为同一内容的主题对照存档。

## 系列内文件

```
llm-benchmarks/
├── README.md                                  # 本文件：系列说明与索引
├── gzh/                                       # 新构建架构：内容层 / 主题层 / CLI
│   ├── render.py                              # leaf / token / 转义等通用工具
│   ├── registry.py                            # 文章注册表：slug / 目录 / 系列号 / 源稿
│   ├── cli.py                                 # 构建入口
│   ├── themes/                                # 主题组件层（base.py + 各主题）
│   └── articles/                              # 文章内容层（只调用主题接口）
├── hle/                                       # 01 · HLE（一篇文章一个子目录）
│   ├── hle_排版_橄榄手记(olive-journal).html
│   └── hle_排版_橄榄手记(olive-journal)_预览.html
├── agents-last-exam/                          # 02 · ALE（同一篇的多主题排版都放这里）
│   ├── agents-last-exam_排版_石墨极简风(graphite-minimal).html
│   └── agents-last-exam_排版_石墨极简风(graphite-minimal)_预览.html
├── terminal-bench-v4-0/                       # 04 · Terminal-Bench 4.0（同一篇的多主题排版都放这里）
│   ├── <slug>_排版_<主题名>(<theme>).html       # 公众号正文（内联样式，可直接粘贴）
│   └── <slug>_排版_<主题名>(<theme>)_预览.html  # 预览页，带「复制」按钮
├── gzh_<theme>_<slug>_gen.py                  # 旧脚本：迁移完成后只作兼容入口
├── patches/                                   # 一次性补丁，仅作历史留档
└── check_completeness.py                      # 核对 HTML 相对源 Markdown 有无遗漏
```

- `<slug>` 采用 `<benchmark>-v<major>-<minor>`，如 `terminal-bench-v4-0`；同名的子目录存放该篇的全部产物。
- 同一篇文章的多主题版本共享内容装配层，只替换组件层，保证内容零差异。
- 封面眉标统一标注系列与序号：HLE 为 `01`，ALE 为 `02`，SLE 预留 `03`，Terminal-Bench 4.0 顺延为 `04`（禅意版写作 `—— LLM Benchmarks 系列 · 04`）。
- 正文 HTML 由脚本生成，不手改；改内容改脚本后重跑。
- 一次性补丁脚本重复运行会触发断言失败，仅作留档。

## 构建架构

新文章走 `gzh/` 包，把「文章内容」「主题组件」「渲染工具」分开：

- `gzh/articles/<slug>.py`：正文内容，暴露 `build(t, meta)`，只调用主题接口，不直接拼主题样式。
- `gzh/themes/<theme>.py`：主题组件；`base.py` 定义组件契约。
- `gzh/render.py`：leaf / token / 转义等通用工具。
- `gzh/registry.py`：slug、输出目录、系列号、源稿路径、可用主题。
- `gzh/cli.py`：构建入口。

```bash
# 在 llm-benchmarks/ 下执行
python3 -m gzh.cli build agents-last-exam --theme graphite --preview --check
python3 -m gzh.cli build --all
```

当前迁移状态：ALE、Terminal-Bench、HLE 均已迁到 `gzh/`。TB 提供 `moyu` / `olive` / `zen` 三套主题；`zen` 由 `gzh/articles/terminal_bench_zen.py` 冻结现有定稿（导语、TOC 与表格是单独改写的，不走组件层），`patches/` 中的 zen 补丁已停止使用。HLE 使用 `olive-hle` 变体（与 `olive` 共用组件，保留 HLE 旧稿的换行与行内代码样式）；HLE 公众号版为节选，`--check` 只跑 HTML 合规，不核对源稿逐项完整性。

## 排版与校验

排版使用仓库根目录的 `.claude/skills/gzh-layout-pro`（6 套主题组件库）。
交付前两道校验须全部通过：

```bash
# 产物合规（禁用标签 / leaf 包裹 / 全角标点），须 0 ERROR
python3 ../.claude/skills/gzh-layout-pro/scripts/validate_gzh_html.py \
  "terminal-bench-v4-0/terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html"

# 内容零遗漏（对比源 Markdown）
python3 check_completeness.py \
  "terminal-bench-v4-0/terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html"

# 非 Terminal-Bench 源稿：第二个参数传源 Markdown 路径
python3 check_completeness.py \
  "agents-last-exam/agents-last-exam_排版_石墨极简风(graphite-minimal).html" \
  /Users/admin/work/llm-benchmarks/benchmarks/agents-last-exam.md
```

## 新增一篇的流程

1. 源稿 Markdown 落在 `~/work/llm-benchmarks/benchmarks/<slug>.md`（本仓库只存排版产物）。
2. 新建同名子目录 `<slug>/`，该篇的全部 HTML（各主题正文 + 预览页）都放进去。
3. 写内容层 `gzh/articles/<slug>.py`（暴露 `build(t, meta)`）与主题层 `gzh/themes/<theme>.py`；在 `gzh/registry.py` 登记 slug、输出目录、系列号、源稿路径与可用主题。
4. 在 `llm-benchmarks/` 下执行 `python3 -m gzh.cli build <slug> --theme <theme> --preview --check`，两关校验清零。
5. 在本文「文章列表」登记一行。
