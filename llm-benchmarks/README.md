# LLM Benchmarks 系列

逐篇拆解大模型评测基准：它到底考什么、怎么跑、分数怎么读、哪里最容易误读。
面向工程师而非刷榜读者——每篇都尽量给出可复现的评测链路、原始数据口径与已知缺陷，
而不是只复述榜首分数。

收录范围：模型能力评测（agent / 编码 / 推理 / 工具调用）与评测方法论。
同一基准的大版本更新（如 v4.0 → v5.0）单独成篇；小版本修订并入原篇。

## 文章列表

| 文章 | 基准版本 | 排版版本 | 源稿 |
|---|---|---|---|
| [Terminal-Bench 4.0](terminal-bench-v4-0/terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html) | v4.0.0 | 摸鱼绿 / 留白禅意 / 橄榄手记 | `benchmarks/terminal-bench-v4-0.md` |

已发布文章的主推版本为**摸鱼绿**；另两版为同一内容的主题对照存档。

## 系列内文件

```
llm-benchmarks/
├── README.md                                  # 本文件：系列说明与索引
├── terminal-bench-v4-0/                       # 一篇文章一个子目录（同一篇的多主题排版都放这里）
│   ├── <slug>_排版_<主题名>(<theme>).html       # 公众号正文（内联样式，可直接粘贴）
│   └── <slug>_排版_<主题名>(<theme>)_预览.html  # 预览页，带「复制」按钮
├── gzh_<theme>_gen.py                         # 该主题的装配脚本
├── patch_<theme>*.py                          # 一次性补丁，仅作历史留档
└── check_completeness.py                      # 核对 HTML 相对源 Markdown 有无遗漏
```

- `<slug>` 采用 `<benchmark>-v<major>-<minor>`，如 `terminal-bench-v4-0`；同名的子目录存放该篇的全部产物。
- 同一篇文章的多主题版本共享内容装配层，只替换组件层，保证内容零差异。
- 封面眉标统一标注系列与序号：`LLM BENCHMARKS · 01`（禅意版写作 `—— LLM Benchmarks 系列 · 01`），新文章顺延编号。
- 正文 HTML 由脚本生成，不手改；改内容改脚本后重跑。
- 一次性补丁脚本重复运行会触发断言失败，仅作留档。

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
```

## 新增一篇的流程

1. 源稿 Markdown 落在 `~/work/llm-benchmarks/benchmarks/<slug>.md`（本仓库只存排版产物）。
2. 新建同名子目录 `<slug>/`，该篇的全部 HTML（各主题正文 + 预览页）都放进去。
3. 用 `gzh-layout-pro` 按题材选主题，写 `gzh_<theme>_gen.py`，输出目录指向 `<slug>/`。
4. 跑上面两条校验，ERROR 清零。
5. 在本文「文章列表」登记一行。
