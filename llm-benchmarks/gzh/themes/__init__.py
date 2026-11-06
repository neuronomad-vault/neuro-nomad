# -*- coding: utf-8 -*-
"""主题注册表。新增主题时在这里登记。"""
from .graphite import GraphiteTheme
from .moyu import MoyuTheme
from .olive import OliveTheme
from .olive_hle import OliveHleTheme
from .zen import ZenTheme

THEMES = {
    'graphite': GraphiteTheme,
    'moyu': MoyuTheme,
    'olive': OliveTheme,
    'olive-hle': OliveHleTheme,
    'zen': ZenTheme,
}


def get_theme(key):
    if key not in THEMES:
        raise KeyError('未知主题: %s（可选: %s）' % (key, ', '.join(sorted(THEMES))))
    return THEMES[key]()
