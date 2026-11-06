# -*- coding: utf-8 -*-
"""主题基类：渲染缓冲区、全局容器、行内 token 接口与组件契约。

约定：
- 文章内容层只调用 Theme 的组件方法，不直接拼 HTML。
- 主题层实现组件；共用逻辑放这里，主题只覆写差异部分。
"""

GLOBAL_CLOSE = '\n</section>\n'


class Theme:
    name = ''
    label = ''
    slug = ''
    # 旧脚本的全局容器换行方式不同：moyu / olive 不留额外空行
    tight_global = False

    def __init__(self):
        self.out = []

    # ---------- 渲染缓冲区 ----------
    def w(self, s):
        self.out.append(s)

    def start(self):
        s = self.global_open()
        self.w(s.rstrip('\n') if self.tight_global else s)

    def finish(self):
        self.w('</section>\n' if self.tight_global else GLOBAL_CLOSE)
        return self.html()

    def html(self):
        return '\n'.join(self.out)

    # ---------- 主题必须实现 ----------
    def global_open(self):
        raise NotImplementedError

    def rich(self, text):
        raise NotImplementedError

    # ---------- 组件契约 ----------
    def cover(self, **kwargs):
        raise NotImplementedError

    def toc(self, items):
        raise NotImplementedError

    def chapter(self, num, cn, en, first=False):
        raise NotImplementedError

    def endchapter(self):
        self.w('</section>')

    def h3(self, text, mt=32):
        raise NotImplementedError

    def para(self, text, mb=16):
        raise NotImplementedError

    def quote(self, text):
        raise NotImplementedError

    def note(self, text):
        raise NotImplementedError

    def warn(self, text, label=None):
        raise NotImplementedError

    def oneliner(self, guide, text):
        raise NotImplementedError

    def cards3(self, items):
        raise NotImplementedError

    def cap(self, text):
        raise NotImplementedError

    def table(self, caption, headers, rows, widths=None, tight=False, real=False):
        raise NotImplementedError

    def data_cards(self, items):
        raise NotImplementedError

    def ul(self, items):
        raise NotImplementedError

    def ol(self, items, small=False):
        raise NotImplementedError

    def code(self, lang, lines):
        raise NotImplementedError

    def flow_stages(self, title, stages):
        raise NotImplementedError

    def flow_terminal_bench(self):
        raise NotImplementedError

    def divider(self):
        raise NotImplementedError

    def end_line(self):
        raise NotImplementedError

    def signature(self):
        raise NotImplementedError

    def footer_cta(self):
        raise NotImplementedError
