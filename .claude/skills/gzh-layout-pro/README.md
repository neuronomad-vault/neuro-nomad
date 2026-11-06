# 公众号排版设计专家（WeChat Article Layout Expert）

> **Claude Code skill 适配版（2026-11-06）**
> 本目录是 WorkBuddy 专家包 `gzh-layout-pro` v1.0.0（作者：开心一点）的一份副本，按 `.claude/skills/` 约定改造入口后归档于此：
> - 源包入口 `agents/gzh-layout-pro.md` → 本目录 `SKILL.md`。仅补 `name` frontmatter、把资源路径说明从「专家包根目录」改为「skill 目录」，工作流正文同源；**SKILL.md 是唯一主文档**，源包 `agents/` 未复制，避免两处主文档分叉。
> - `references/`、`scripts/`、`assets/`、`avatars/`、`.codebuddy-plugin/plugin.json` 原样复制；`.downloaded_at`（下载时间戳）未复制。下方「目录结构」段描述的是**源包结构**，本副本差异以本段为准。
> - 脚本用 `__file__` 相对定位模板与组件库，无需改代码。调用时给脚本的绝对路径，产物路径另给：`python3 /path/to/neuro-nomad/.claude/skills/gzh-layout-pro/scripts/validate_gzh_html.py <产物.html>`。
> - 在 Claude Code 里直接描述任务即可触发，例如「用摸鱼绿主题把 `benchmarks/xxx.md` 排成可直接粘贴的公众号图文」。
> - 源包 README 声明 AGPL-3.0，但包内未附 `LICENSE` 文件；若对外分发，请先补齐授权文本。

把一篇 Markdown / Word / PDF / 纯文本文章，转成**可直接复制粘贴进微信公众号编辑器、且粘贴后样式不丢失**的精致 HTML。按文章题材推荐主题并排版，自动章节编号、关键词下划线、引言卡与目录、代码块与图片适配、作者签名合并；用双关卡脚本确定性兜底平台限制，并生成带「复制」按钮的预览页。

> 本专家不负责写文章——它只做排版。先有稿件，再交给它排。

## ✨ 核心特性

- **6 套精选主题**：摸鱼绿（默认）· 红白 · 石墨极简 · 留白禅意 · 摸鱼票据 · 橄榄手记——每套都是自成体系的厚组件库（设计变量 + 数十个精细组件 + 视觉层级 + 文章类型配方表）。
- **主题生成器**：现成主题不够？用一句话描述或一张参考图，生成一套全新组件库并保存本地复用。
- **内容全兼容**：代码块（深/浅色，等宽不折行）、图片、GIF（带动图角标）、行内代码、引用、列表、产品徽章。
- **智能排版**：章节自动编号（末章可 ∞）、每段主动标 1–3 个关键词下划线、从正文提炼引言卡与目录、作者签名去重合并。
- **中文全角标点**：正文自动规范全角，代码块内原样保留。
- **不掉格式**：所有样式内联、文字 `<span leaf="">` 包裹，规避 `<style>/<div>/class/grid/position` 等公众号会过滤的写法。
- **双关卡质量校验**：`component_lint.py`（组件库源头）+ `validate_gzh_html.py`（最终产物），构成可复现的「改→验→修」闭环。
- **一键复制**：生成带「复制」按钮的预览页，点一下把富文本复制到剪贴板，直接粘进公众号，免手动全选。

## 🗂 常见使用场景

| 你的内容 | 推荐怎么排 |
|---|---|
| 观点 / 深度长文 | 红白 或 石墨极简；关键词下划线 + 金句引用 + 居中金句 |
| 产品测评 / 工具盘点 | 摸鱼绿 或 摸鱼票据；step/tool-label + 卡片，按配方表走 |
| 教程 / 操作指南 | 摸鱼绿；step-label + 代码块 + 编号列表 |
| 数据复盘 / 年度报告 | 摸鱼绿 或 橄榄手记；数据卡 + 表格 |
| 禅意 / 极简随笔 | 留白禅意；大留白 + 居中衬线引用 |
| 内刊 / 深度评测 / 案例复盘 | 橄榄手记；编者按 + 分节 + 暗色摘要框 |
| Word / PDF 稿转公众号 | 先自动格式归一化 → 再按题材选主题 |
| 想要现成之外的风格 | 主题生成器：一句话或参考图现造一套 |

## 🚀 怎么用

直接在 WorkBuddy 里对这位专家说：

> 用禅意留白主题把 `article.md` 排成可直接粘贴的公众号图文
>
> 把这篇深度长文排成公众号样式，按内容调性挑个最抓眼球的主题
>
> 按「治愈系旅行手账风」给我定制一套公众号主题

专家会按 `agents/gzh-layout-pro.md` 的工作流执行：选主题 → 读组件库 → 解析结构 → 装配 HTML → 跑 `validate_gzh_html.py` 校验（ERROR 清零才交付）→ 生成干净正文 + 带「复制」按钮的预览页。

### 全自动模式

说「直接排 / 一键 / 不用问」时，专家跳过结构确认与选主题提问，自动推断结构、按题材自选主题、排版校验，交付时附决策说明（章节结构、自拟标题、选题理由）。

## 🧩 公众号平台限制（已内置兜底）

生成的 HTML 严格遵守：禁 `<style>/<script>/<div>`、`class/id`、`position:fixed/absolute/sticky`、`float`、`@media/@keyframes`、`display:grid`、CSS 变量、外部字体；样式全部内联；所有文字用 `<span leaf="">` 包裹。这些由校验脚本确定性检查，而非靠模型自觉。

## 🔁 可验证循环

```bash
python3 scripts/component_lint.py .            # 源头关：扫组件库反模式
python3 scripts/validate_gzh_html.py out.html  # 产物关：扫最终 HTML 合规
```

- **源头关** 查 `white-space:pre`（大空白）、正文四周虚线框、平台禁用项——须 0 ERROR。
- **产物关** 查禁用标签、`<span leaf>` 包裹、半角标点——须 0 ERROR / 半角 0 WARN。

## 📁 目录结构

```
公众号排版设计专家/
├── .codebuddy-plugin/plugin.json   # WorkBuddy 专家元数据
├── agents/gzh-layout-pro.md        # 排版工作流主文档（专家入口）
├── references/
│   ├── theme-index.md              # 6 套主题索引（主色/适用/下划线，单一来源）
│   ├── theme-*.md                  # 6 套主题组件库
│   ├── theme-generator.md          # 主题生成器（按描述/参考图生成新主题）
│   ├── common-components.md        # 跨主题通用增量组件（代码块/图片/小标签）
│   ├── format-normalize.md         # 格式归一化（docx/pdf/纯文本 → Markdown）
│   └── eval-cases.md               # 触发用例 + 可验证循环
├── scripts/
│   ├── validate_gzh_html.py        # 产物合规校验
│   ├── component_lint.py           # 组件库源头检查
│   ├── extract_docx.py             # Word(.docx) → Markdown
│   └── wrap_preview.py             # 生成带「复制」按钮的预览页
├── assets/
│   ├── preview-template.html       # 预览页外壳模板
│   ├── sample-article.md           # 演示输入
│   └── theme-previews/             # 主题生成器产出的区块库预览
└── LICENSE                         # AGPL-3.0
```

## 🎯 设计原则

- **约束而非自由**——用预设主题色板和固定组件保证输出下限，不让模型现场发挥。
- **确定性下沉脚本**——平台限制这类死规则交给校验脚本，模型只做内容判断。
- **小标签，不用虚线框**——强调用左竖条/药丸标签，笨重的四周虚线框只留给「待补素材」居中占位。
- **每处经验都可复现**——踩过的坑写进 gotchas 和校验脚本，用可验证循环防回归。
- **配方优于自由**——先按文章类型查主题库的「配方表」定组件组合，再装配，同类文章排版气质稳定。
- **克制用色**——主色只在锚点出现（全文 ≤5 处），大面积白底 + 灰阶，彩色只做点缀。
