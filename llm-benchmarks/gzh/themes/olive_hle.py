# -*- coding: utf-8 -*-
"""橄榄手记 · HLE 变体。

与 Terminal-Bench 的橄榄手记版共用组件；HLE 旧脚本的全局容器换行方式不同，
因此单独保留 tight_global=False。
"""
from ..render import tokens, leaf
from .olive import OliveTheme


class OliveHleTheme(OliveTheme):
    name = '橄榄手记'
    label = '橄榄手记'
    slug = 'olive-journal'
    tight_global = False

    def rich(self, text):
        """HLE 旧脚本的行内代码带 word-break:break-all，且支持 %%...%% 长串。"""
        out = []
        for seg in tokens(text):
            if not seg:
                continue
            if seg.startswith('[[') and seg.endswith(']]'):
                out.append('<span style="border-bottom:2px solid #ed7b2f;font-weight:600;color:#23251d;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('**') and seg.endswith('**'):
                out.append('<strong style="color:#23251d;">' + leaf(seg[2:-2]) + '</strong>')
            elif seg.startswith('~~') and seg.endswith('~~'):
                out.append('<span style="background:#eeefe9;padding:1px 5px;border-radius:4px;font-weight:600;color:#23251d;border:1px solid #bfc1b7;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('{{') and seg.endswith('}}'):
                out.append('<span style="background:#eeefe9;color:#23251d;padding:2px 6px;border-radius:4px;font-family:ui-monospace,Menlo,Monaco,Consolas,monospace;font-size:13px;border:1px solid #b6b7af;word-break:break-all;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('%%') and seg.endswith('%%'):
                out.append('<span style="background:#eeefe9;color:#23251d;padding:2px 6px;border-radius:4px;font-family:ui-monospace,Menlo,Monaco,Consolas,monospace;font-size:12px;border:1px solid #b6b7af;word-break:break-all;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('!!') and seg.endswith('!!'):
                out.append('<span style="color:#9ea096;text-decoration:line-through;">' + leaf(seg[2:-2]) + '</span>')
            else:
                out.append(leaf(seg))
        return ''.join(out)
