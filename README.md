# Neuro Nomad · 内容仓库

> 智能漫游 | Neuro Nomad
> 大模型 · AI智能体 · 多模态 · 具身智能
> 聚焦模型原理、AI工程与推理优化实践。

本仓库归档公众号「Neuro Nomad」的图文内容：源稿、公众号排版产物（HTML）与装配/校验脚本。
内容按**系列**组织：一个系列一个目录，目录内 `README.md` 负责系列定位、文章索引与文件约定；
正文 HTML 由脚本生成，便于复现与改版。

## 目录结构

```
neuro-nomad/
├── README.md
├── .claude/
│   └── skills/gzh-layout-pro/     # 公众号排版技能：6 套主题组件库 + 校验脚本
└── llm-benchmarks/                # 系列：LLM 评测基准（见该目录 README）
    ├── README.md                  # 系列说明与文章索引
    ├── terminal-bench-v4-0/       # 一篇文章一个子目录，存放该篇全部排版产物
    │   ├── terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html
    │   ├── terminal-bench-v4-0_排版_摸鱼绿(moyu-green)_预览.html
    │   ├── terminal-bench-v4-0_排版_留白禅意风(zen-whitespace).html
    │   ├── terminal-bench-v4-0_排版_留白禅意风(zen-whitespace)_预览.html
    │   ├── terminal-bench-v4-0_排版_橄榄手记(olive-journal).html
    │   └── terminal-bench-v4-0_排版_橄榄手记(olive-journal)_预览.html
    ├── gzh_moyu_gen.py            # 摸鱼绿版装配脚本
    ├── gzh_olive_gen.py           # 橄榄手记版装配脚本（复用摸鱼绿的内容层）
    ├── patch_zen.py               # 留白禅意版：删节 + 参考来源重编号（一次性补丁）
    ├── patch_zen_mermaid.py       # 留白禅意版：移除 Mermaid 源码块（一次性补丁）
    └── check_completeness.py      # 核对 HTML 相对源 Markdown 的内容零遗漏
```

## 系列

| 系列 | 目录 | 定位 | 最新文章 |
|---|---|---|---|
| LLM Benchmarks | `llm-benchmarks/` | 逐篇拆解大模型评测基准：考什么、怎么跑、分数怎么读 | Terminal-Bench 4.0 |

各系列的文章索引、文件命名与选题约定见系列目录下的 `README.md`。
源 Markdown 存放在 `/Users/admin/work/llm-benchmarks/benchmarks/`，不在本仓库。

## 排版工作流

排版统一使用 `.claude/skills/gzh-layout-pro`：先有稿件，再按题材选主题，
装配成可直接粘贴进公众号编辑器、粘贴后样式不丢失的内联 HTML。

- **主题**：摸鱼绿 · 红白 · 石墨极简 · 留白禅意 · 摸鱼票据 · 橄榄手记
- **双关卡校验**：`component_lint.py` 查组件库源头，`validate_gzh_html.py` 查最终产物
- **预览页**：`*_预览.html` 带「复制」按钮，一键把富文本粘进公众号编辑器

```bash
# 校验排版产物（须 0 ERROR 才交付）
python3 .claude/skills/gzh-layout-pro/scripts/validate_gzh_html.py \
  "llm-benchmarks/terminal-bench-v4-0/terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html"

# 核对内容零遗漏
python3 llm-benchmarks/check_completeness.py \
  "llm-benchmarks/terminal-bench-v4-0/terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html"
```

## 约定

- 正文 HTML 一律由脚本生成；直接手改会与生成脚本脱节，改内容请改脚本后重跑。
- 一次性补丁脚本（`patch_*.py`）仅作历史留档，重复运行会触发断言失败。
- 提交信息遵循 `<type>(<scope>): <subject>`，如 `docs(gzh): 归档 xxx 三版公众号图文`。
