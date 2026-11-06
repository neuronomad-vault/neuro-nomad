# -*- coding: utf-8 -*-
"""留白禅意风主题（Zen Whitespace）。

现有 zen 文章是独立改写的定稿，内容层用 raw HTML 冻结；本主题目前只提供
主题名与文件名标识，组件式实现留待后续需要时再补。
"""
from .base import Theme


class ZenTheme(Theme):
    name = '留白禅意风'
    label = '留白禅意风'
    slug = 'zen-whitespace'

    def global_open(self):
        return ('<section style="max-width:677px;margin:0 auto;background:#FFFFFF;'
                'font-family:-apple-system,BlinkMacSystemFont,\'PingFang SC\',\'Hiragino Sans GB\','
                '\'Microsoft YaHei\',sans-serif;color:#525252;line-height:1.9;letter-spacing:0.3px;'
                'overflow-x:hidden;">\n')

    def rich(self, text):
        raise NotImplementedError('zen 当前是 raw 内容模块，不使用组件式 rich()')
