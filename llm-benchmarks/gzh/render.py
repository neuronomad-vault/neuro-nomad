# -*- coding: utf-8 -*-
"""公众号 HTML 渲染的通用工具：转义、leaf 包裹、行内 token 切分。

主题只负责把 token 映射成自己的配色与样式，不重复实现切分逻辑。
token 约定：
  [[文字]]  关键词下划线
  **文字**  加粗
  ~~文字~~  浅底标签
  {{文字}}  行内代码
  %%文字%%  可断行行内代码
  !!文字!!  删除线
  ^^文字^^  橙色锚点下划线（石墨极简用）
"""
import html
import re

TOKEN = re.compile(
    r'(\[\[.+?\]\]|\*\*.+?\*\*|~~.+?~~|\{\{.+?\}\}|%%.+?%%|!!.+?!!|\^\^.+?\^\^)',
    re.S,
)


def esc(t):
    return html.escape(t, quote=False)


def leaf(t):
    return '<span leaf="">' + esc(t) + '</span>'


def blank():
    return '<span leaf=""><br></span>'


def tokens(text):
    return TOKEN.split(text)
