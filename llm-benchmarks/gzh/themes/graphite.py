# -*- coding: utf-8 -*-
"""石墨极简风主题（Graphite Minimal）。

实现 gzh-layout-pro `references/theme-graphite-minimal.md` 的组件层。
"""
from ..render import tokens, leaf, blank
from .base import Theme


class GraphiteTheme(Theme):
    name = '石墨极简风'
    label = '石墨极简风'
    slug = 'graphite-minimal'

    # ---------- 全局容器 ----------
    def global_open(self):
        return ('<section style="max-width:677px;margin:0 auto;background:#FFFFFF;'
                'font-family:-apple-system,BlinkMacSystemFont,\'PingFang SC\',\'Hiragino Sans GB\','
                '\'Microsoft YaHei\',sans-serif;color:#52525B;line-height:1.8;letter-spacing:0.3px;'
                'overflow-x:hidden;">\n')

    # ---------- 行内 token ----------
    def rich(self, text):
        out = []
        for seg in tokens(text):
            if not seg:
                continue
            if seg.startswith('[[') and seg.endswith(']]'):
                out.append('<span style="border-bottom:2px solid #52525B;font-weight:600;color:#27272A;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('**') and seg.endswith('**'):
                out.append('<strong style="color:#27272A;">' + leaf(seg[2:-2]) + '</strong>')
            elif seg.startswith('~~') and seg.endswith('~~'):
                out.append('<span style="background:#F4F4F5;color:#27272A;padding:1px 6px;border-radius:3px;font-weight:700;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('{{') and seg.endswith('}}'):
                out.append('<span style="background:#F4F4F5;color:#27272A;padding:2px 6px;border-radius:4px;font-family:\'SF Mono\',Consolas,Monaco,monospace;font-size:13px;word-break:break-all;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('%%') and seg.endswith('%%'):
                out.append('<span style="background:#F4F4F5;color:#27272A;padding:2px 6px;border-radius:4px;font-family:\'SF Mono\',Consolas,Monaco,monospace;font-size:12px;word-break:break-all;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('!!') and seg.endswith('!!'):
                out.append('<span style="color:#A1A1AA;text-decoration:line-through;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('^^') and seg.endswith('^^'):
                out.append('<span style="border-bottom:2px solid #F97316;font-weight:700;color:#27272A;">' + leaf(seg[2:-2]) + '</span>')
            else:
                out.append(leaf(seg))
        return ''.join(out)

    # ---------- 封面 ----------
    def cover(self, series, date, title, subtitle, benchmark, meta):
        self.w('<section style="margin:10px 10px 40px;padding:32px 24px 24px;border-top:1px solid #E4E4E7;border-bottom:1px solid #E4E4E7;background:#FFFFFF;">')
        self.w('<section style="display:flex;align-items:center;gap:8px;margin-bottom:26px;">')
        self.w('<span style="width:6px;height:6px;background:#27272A;border-radius:50%;display:inline-block;overflow:hidden;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="font-size:10px;font-weight:700;letter-spacing:3px;color:#52525B;">' + leaf('LLM BENCHMARKS · ' + series) + '</span>')
        self.w('<span style="flex:1;height:1px;background:#E4E4E7;display:inline-block;overflow:hidden;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="font-size:10px;color:#A1A1AA;font-weight:500;">' + leaf(date) + '</span>')
        self.w('</section>')
        self.w('<p style="font-size:11px;color:#A1A1AA;letter-spacing:2px;margin:0 0 18px;font-weight:400;">' + leaf('QUOTE') + '</p>')
        self.w('<p style="font-size:24px;font-weight:900;color:#27272A;margin:0 0 10px;line-height:1.35;letter-spacing:-0.75px;">' + leaf(title) + '</p>')
        self.w('<p style="font-size:19px;font-weight:700;color:#27272A;margin:0 0 18px;line-height:1.5;letter-spacing:0.3px;">' + '<span style="border-bottom:2px solid #F97316;">' + leaf(subtitle) + '</span></p>')
        self.w('<section style="width:48px;height:3px;background:#27272A;margin-bottom:16px;">' + blank() + '</section>')
        self.w('<p style="font-size:11px;font-weight:800;letter-spacing:2.5px;color:#52525B;margin:0 0 8px;">' + leaf(benchmark) + '</p>')
        for i, line in enumerate(meta):
            if i == 0:
                self.w('<p style="font-size:13px;color:#71717A;margin:0 0 6px;line-height:1.7;">' + leaf(line) + '</p>')
            else:
                self.w('<p style="font-size:11px;color:#A1A1AA;margin:0;line-height:1.7;">' + leaf(line) + '</p>')
        self.w('</section>')

    # ---------- 导读 ----------
    def toc(self, items):
        self.w('<section style="padding:0 10px 40px;">')
        self.w('<p style="font-size:11px;color:#A1A1AA;margin:0 0 16px;letter-spacing:2px;">' + leaf('本文看点') + '</p>')
        self.w('<section style="display:flex;justify-content:space-between;">')
        for i, (title, sub) in enumerate(items):
            margin = 'margin-right:8px;' if i < len(items) - 1 else ''
            self.w('<section style="flex:1;background:#FAFAFA;border-top:1px solid #E4E4E7;padding:18px 12px 16px;' + margin + '">')
            self.w('<p style="font-size:11px;color:#A1A1AA;font-weight:500;margin:0 0 8px;letter-spacing:1px;">' + leaf(str(i + 1).zfill(2)) + '</p>')
            self.w('<p style="font-size:13px;font-weight:700;color:#27272A;margin:0 0 6px;line-height:1.5;">' + leaf(title) + '</p>')
            self.w('<p style="font-size:11px;color:#71717A;margin:0;line-height:1.6;">' + leaf(sub) + '</p>')
            self.w('</section>')
        self.w('</section></section>')

    # ---------- 章节 ----------
    def divider(self):
        self.w('<section style="padding:0 10px;">')
        self.w('<section style="height:1px;background:#E4E4E7;margin:0;">' + blank() + '</section>')
        self.w('</section>')

    def chapter(self, num, cn, en, first=False):
        mt = '16px' if first else '56px'
        self.w('<section style="margin-top:' + mt + ';margin-bottom:32px;padding:0 10px;">')
        self.w('<section style="position:relative;padding-bottom:20px;border-bottom:1px solid #E4E4E7;">')
        self.w('<p style="font-size:48px;font-weight:900;color:#E4E4E7;margin:0;line-height:1;letter-spacing:-2px;">' + leaf(str(num).zfill(2)) + '</p>')
        self.w('<section style="margin-top:-8px;">')
        self.w('<p style="font-size:10px;color:#A1A1AA;font-weight:500;letter-spacing:3px;margin:0 0 6px;text-transform:uppercase;">' + leaf(en) + '</p>')
        self.w('<h3 style="font-size:20px;font-weight:800;color:#27272A;margin:0;letter-spacing:0.5px;line-height:1.4;">' + leaf(cn) + '</h3>')
        self.w('</section></section>')

    # ---------- 正文 ----------
    def para(self, text, mb=22):
        self.w('<p style="margin:0 0 ' + str(mb) + 'px;font-size:15px;line-height:1.8;text-align:justify;color:#52525B;letter-spacing:0.3px;">' + self.rich(text) + '</p>')

    def h3(self, text, mt=28):
        self.w('<p style="font-size:15px;font-weight:800;color:#27272A;margin:' + str(mt) + 'px 0 14px;padding-left:12px;border-left:3px solid #52525B;line-height:1.4;">' + leaf(text) + '</p>')

    def quote(self, text):
        self.w('<section style="border-left:3px solid #52525B;padding:16px 0 16px 24px;margin:0 0 28px;">')
        self.w('<p style="font-size:16px;font-weight:700;color:#27272A;margin:0;line-height:1.7;letter-spacing:0.5px;">' + self.rich('「' + text + '」') + '</p>')
        self.w('</section>')

    def note(self, text):
        self.w('<section style="border-left:2px solid #E4E4E7;padding:12px 0 12px 20px;margin:0 0 24px;">')
        self.w('<p style="font-size:13px;color:#A1A1AA;margin:0;line-height:1.8;text-align:justify;">' + self.rich(text) + '</p>')
        self.w('</section>')

    def warn(self, text, label='CAVEAT · 口径提示'):
        self.w('<section style="background:#FAFAFA;border-top:2px solid #27272A;padding:18px 22px;margin:0 0 24px;">')
        self.w('<p style="font-size:11px;color:#A1A1AA;margin:0 0 10px;letter-spacing:2px;font-weight:500;">' + leaf(label) + '</p>')
        self.w('<p style="font-size:14px;color:#52525B;margin:0;line-height:1.8;text-align:justify;">' + self.rich(text) + '</p>')
        self.w('</section>')

    def cap(self, text):
        self.w('<p style="margin:0 0 10px;font-size:12px;font-weight:800;color:#52525B;letter-spacing:1px;">' + leaf('▍ ' + text) + '</p>')

    # ---------- 表格 ----------
    def table(self, caption, headers, rows, widths=None, tight=False, real=False):
        self.cap(caption)
        n = len(headers)
        if n <= 3 and not real:
            if widths is None:
                widths = {2: [42, 58], 3: [24, 32, 44]}[n]
            self.w('<section style="margin:0 0 24px;border:1px solid #E4E4E7;background:#FFFFFF;">')
            self.w('<section style="display:flex;background:#FAFAFA;border-bottom:1px solid #E4E4E7;">')
            for i, hcell in enumerate(headers):
                bd = 'border-left:1px solid #E4E4E7;' if i else ''
                self.w('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:12px;font-weight:800;color:#27272A;' + bd + '">' + leaf(hcell) + '</section>')
            self.w('</section>')
            for ri, row in enumerate(rows):
                last = (ri == len(rows) - 1)
                self.w('<section style="display:flex;' + ('' if last else 'border-bottom:1px solid #E4E4E7;') + '">')
                for i, cell in enumerate(row):
                    bd = 'border-left:1px solid #E4E4E7;' if i else ''
                    self.w('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:13px;color:#52525B;' + bd + '">' + self.rich(cell) + '</section>')
                self.w('</section>')
            self.w('</section>')
        else:
            mw = {3: 640, 4: 560, 5: 700, 6: 780, 7: 840, 8: 900}.get(n, 640)
            tstyle = 'width:100%;border-collapse:collapse;font-size:' + ('12px' if tight else '13px') + ';min-width:' + str(mw) + 'px;'
            pad = '6px 8px' if tight else '8px 10px'
            s = '<section style="margin:0 0 24px;overflow-x:auto;-webkit-overflow-scrolling:touch;"><table style="' + tstyle + '"><thead><tr>'
            for hcell in headers:
                s += '<th style="background:#27272A;color:#FFFFFF;font-weight:800;padding:' + pad + ';text-align:left;border:1px solid #27272A;">' + leaf(hcell) + '</th>'
            s += '</tr></thead><tbody>'
            for i, row in enumerate(rows):
                bg = 'background:#FAFAFA;' if i % 2 == 1 else 'background:#FFFFFF;'
                s += '<tr>'
                for cell in row:
                    s += '<td style="padding:' + pad + ';border:1px solid #E4E4E7;color:#52525B;' + bg + '">' + self.rich(cell) + '</td>'
                s += '</tr>'
            s += '</tbody></table></section>'
            self.w(s)

    # ---------- 数据卡 ----------
    def data_cards(self, items):
        self.w('<section style="display:flex;margin:0 0 28px;">')
        for i, (num, label) in enumerate(items):
            margin = 'margin-right:8px;' if i < len(items) - 1 else ''
            self.w('<section style="flex:1;border:1px solid #E4E4E7;padding:22px 16px;text-align:center;' + margin + '">')
            self.w('<p style="font-size:32px;font-weight:900;color:#27272A;margin:0 0 6px;line-height:1;letter-spacing:-1px;">' + leaf(num) + '</p>')
            self.w('<p style="font-size:11px;color:#A1A1AA;margin:0;letter-spacing:1px;">' + leaf(label) + '</p>')
            self.w('</section>')
        self.w('</section>')

    # ---------- 列表 ----------
    def ul(self, items):
        for label, desc in items:
            self.w('<section style="margin-bottom:16px;">')
            self.w('<p style="margin:0 0 6px;">')
            self.w('<span style="display:inline-block;font-size:14px;font-weight:700;color:#27272A;background:#F4F4F5;padding:3px 10px;border-radius:999px;">')
            self.w('<span style="display:inline-block;width:6px;height:6px;background:#52525B;border-radius:50%;margin-right:5px;vertical-align:middle;">' + blank() + '</span>')
            self.w(leaf(label))
            self.w('</span></p>')
            self.w('<p style="font-size:14px;color:#71717A;margin:0;line-height:1.7;text-align:justify;">' + self.rich(desc) + '</p>')
            self.w('</section>')

    def ol(self, items, small=False):
        fs = '13px' if small else '15px'
        self.w('<section style="margin:0 0 24px;">')
        for i, it in enumerate(items, 1):
            self.w('<section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">')
            self.w('<span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;background:#27272A;color:#FFFFFF;font-size:12px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;">' + leaf(str(i)) + '</span>')
            self.w('<p style="font-size:' + fs + ';color:#52525B;margin:0;line-height:1.8;flex:1;text-align:justify;word-break:break-word;">' + self.rich(it) + '</p>')
            self.w('</section>')
        self.w('</section>')

    # ---------- 代码 ----------
    def code(self, lang, lines):
        s = '<section style="margin:0 0 20px;border-radius:4px;overflow:hidden;background:#27272A;">'
        s += '<section style="display:flex;align-items:center;padding:9px 14px;background:#18181B;">'
        for c in ('#71717A', '#A1A1AA', '#E4E4E7'):
            s += '<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:' + c + ';margin-right:7px;overflow:hidden;font-size:0;line-height:0;">' + blank() + '</span>'
        s += '<span style="margin-left:12px;font-size:12px;color:#A1A1AA;font-family:Consolas,Monaco,monospace;letter-spacing:1px;">' + leaf(lang) + '</span>'
        s += '</section><section style="padding:11px 14px;">'
        for line in lines:
            s += '<p style="margin:0;font-family:\'SF Mono\',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E4E4E7;">' + leaf(line) + '</p>'
        s += '</section></section>'
        self.w(s)

    # ---------- 流程图 ----------
    def flow_stages(self, title, stages):
        self.w('<section style="margin:0 0 24px;">')
        self.w('<p style="font-size:10px;font-weight:800;letter-spacing:3px;color:#52525B;margin:0 0 12px;">' + leaf(title) + '</p>')
        for si, (stage_title, cards) in enumerate(stages):
            self.w('<section style="background:#FAFAFA;border:1px solid #E4E4E7;border-left:3px solid #52525B;padding:14px 16px;">')
            self.w('<p style="margin:0 0 10px;font-size:12px;font-weight:800;color:#27272A;letter-spacing:1px;">' + leaf(stage_title) + '</p>')
            self.w('<section style="display:flex;">')
            for j, (head, desc) in enumerate(cards):
                margin = 'margin-right:8px;' if j < len(cards) - 1 else ''
                self.w('<section style="flex:1;background:#FFFFFF;border:1px solid #E4E4E7;padding:9px 11px;' + margin + '">')
                self.w('<p style="margin:0;font-size:13px;font-weight:700;color:#27272A;line-height:1.6;">' + leaf(head) + '</p>')
                self.w('<p style="margin:0;font-size:11px;color:#71717A;line-height:1.6;">' + leaf(desc) + '</p>')
                self.w('</section>')
            self.w('</section></section>')
            if si < len(stages) - 1:
                self.w('<p style="margin:8px 0;text-align:center;font-size:12px;font-weight:700;color:#A1A1AA;letter-spacing:1px;">' + leaf('↓') + '</p>')
        self.w('</section>')

    # ---------- 结尾 ----------
    def end_line(self):
        self.w('<section style="padding:0 10px;">')
        self.w('<section style="text-align:center;margin:0 0 36px;">')
        self.w('<section style="display:flex;align-items:center;justify-content:center;">')
        self.w('<span style="height:1px;width:48px;background:#E4E4E7;margin-right:16px;">' + blank() + '</span>')
        self.w('<span style="font-size:10px;color:#A1A1AA;letter-spacing:4px;font-weight:500;">' + leaf('END') + '</span>')
        self.w('<span style="height:1px;width:48px;background:#E4E4E7;margin-left:16px;">' + blank() + '</span>')
        self.w('</section></section></section>')

    def signature(self):
        self.w('<section style="padding:0 10px 24px;">')
        self.w('<section style="border-top:1px solid #E4E4E7;padding-top:28px;">')
        self.w('<p style="margin:0 0 8px;font-size:18px;font-weight:800;color:#27272A;letter-spacing:1px;">' + leaf('智能漫游') + '</p>')
        self.w('<p style="margin:0 0 14px;font-size:10px;color:#A1A1AA;letter-spacing:3px;">' + leaf('NEURO NOMAD') + '</p>')
        self.w('<p style="margin:0 0 10px;font-size:13px;color:#52525B;line-height:1.8;">' + leaf('大模型 · AI智能体 · 多模态 · 具身智能') + '</p>')
        self.w('<p style="margin:0 0 16px;font-size:15px;line-height:1.8;color:#52525B;text-align:justify;">' + self.rich('聚焦[[模型原理、AI工程与推理优化实践]]。') + '</p>')
        self.w('<p style="margin:0;font-size:15px;line-height:1.8;color:#52525B;text-align:justify;">' + self.rich('如果你觉得今天这篇有收获，欢迎**点赞、在看、转发**三连，我们下篇见。') + '</p>')
        self.w('</section></section>')
