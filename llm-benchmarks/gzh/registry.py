# -*- coding: utf-8 -*-
"""文章注册表：slug、内容模块、输出目录、系列号、源稿路径、可用主题。"""

ARTICLES = {
    'agents-last-exam': {
        'label': "Agents' Last Exam (ALE)",
        'module': 'gzh.articles.agents_last_exam',
        'output_dir': 'agents-last-exam',
        'series': '02',
        'date': '2026.11',
        'source': '/Users/admin/work/llm-benchmarks/benchmarks/agents-last-exam.md',
        'themes': ['graphite'],
    },
    'terminal-bench-v4-0': {
        'label': 'Terminal-Bench 4.0',
        'module': 'gzh.articles.terminal_bench',
        'output_dir': 'terminal-bench-v4-0',
        'series': '04',
        'date': '2026.11',
        'source': '/Users/admin/work/llm-benchmarks/benchmarks/terminal-bench-v4-0.md',
        'themes': ['moyu', 'olive', 'zen'],
        # zen 是独立改写的定稿，内容层用 raw HTML 冻结；源稿逐项完整性不适用
        'theme_modules': {'zen': 'gzh.articles.terminal_bench_zen'},
        'theme_completeness': {'zen': False},
    },
    'hle': {
        'label': "Humanity's Last Exam (HLE)",
        'module': 'gzh.articles.hle',
        'output_dir': 'hle',
        'series': '01',
        'date': '2026.11',
        'source': '/Users/admin/work/llm-benchmarks/benchmarks/hle.md',
        'themes': ['olive-hle'],
        # 公众号版为节选，源稿逐项完整性检查不适用；只跑 HTML 合规校验
        'completeness': False,
    },
}
