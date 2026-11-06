# -*- coding: utf-8 -*-
"""公众号图文构建 CLI。

用法（在 llm-benchmarks 目录执行）：
    python3 -m gzh.cli build agents-last-exam --theme graphite
    python3 -m gzh.cli build agents-last-exam --theme graphite --preview --check
    python3 -m gzh.cli build --all
"""
import argparse
import importlib
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # llm-benchmarks
REPO = os.path.dirname(BASE)                                        # neuro-nomad
SKILL = os.path.join(REPO, '.claude', 'skills', 'gzh-layout-pro')
CHECKER = os.path.join(BASE, 'check_completeness.py')


def _build_one(article_key, theme_key, preview=False, check=False):
    from .registry import ARTICLES
    from .themes import get_theme

    meta = ARTICLES[article_key]
    module_name = meta.get('theme_modules', {}).get(theme_key, meta['module'])
    module = importlib.import_module(module_name)
    theme = get_theme(theme_key)
    if hasattr(module, 'build_raw'):
        html = module.build_raw(meta)
    else:
        html = module.build(theme, meta)

    out_dir = os.path.join(BASE, meta['output_dir'])
    os.makedirs(out_dir, exist_ok=True)
    filename = '%s_排版_%s(%s).html' % (article_key, theme.label, theme.slug)
    out_path = os.path.join(out_dir, filename)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print('已生成:', out_path)
    print('字节数:', len(html.encode('utf-8')))
    print('span leaf 数:', html.count('<span leaf="">'))

    if preview:
        subprocess.run(
            [sys.executable, os.path.join(SKILL, 'scripts', 'wrap_preview.py'), out_path],
            check=False,
        )
    if check:
        completeness = meta.get('theme_completeness', {}).get(
            theme_key, meta.get('completeness', True)
        )
        _check_one(out_path, meta['source'], completeness)
    return out_path


def _check_one(out_path, source, check_completeness=True):
    validate = os.path.join(SKILL, 'scripts', 'validate_gzh_html.py')
    print('\n--- validate ---')
    r1 = subprocess.run([sys.executable, validate, out_path], check=False)
    r2 = None
    print('\n--- completeness ---')
    if check_completeness:
        r2 = subprocess.run([sys.executable, CHECKER, out_path, source], check=False)
    else:
        print('该篇为节选版，跳过源稿逐项核对')
    if r1.returncode != 0 or (r2 is not None and r2.returncode != 0):
        raise SystemExit('校验未通过')


def main(argv=None):
    ap = argparse.ArgumentParser(description='公众号图文构建')
    sub = ap.add_subparsers(dest='cmd', required=True)

    b = sub.add_parser('build', help='构建正文 HTML')
    b.add_argument('article', nargs='?', help='文章 slug')
    b.add_argument('--theme', action='append', dest='themes', help='主题 key，可重复')
    b.add_argument('--all', action='store_true', help='构建全部已注册文章/主题')
    b.add_argument('--preview', action='store_true', help='同时生成预览页')
    b.add_argument('--check', action='store_true', help='构建后跑合规与内容校验')
    args = ap.parse_args(argv)

    from .registry import ARTICLES

    if args.all:
        for key, meta in ARTICLES.items():
            for theme_key in meta['themes']:
                _build_one(key, theme_key, args.preview, args.check)
        return

    if not args.article:
        ap.error('需要指定文章 slug，或使用 --all')
    meta = ARTICLES[args.article]
    theme_keys = args.themes or meta['themes']
    for theme_key in theme_keys:
        _build_one(args.article, theme_key, args.preview, args.check)


if __name__ == '__main__':
    main()
