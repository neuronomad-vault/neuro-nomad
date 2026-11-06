# -*- coding: utf-8 -*-
"""摸鱼绿主题（Moyu Green）。

实现 gzh-layout-pro `references/theme-moyu-green.md` 的组件层。
"""
from ..render import tokens, leaf, blank
from .base import Theme


FLOW_MOYU = r'''<section style="margin:0 20px 24px;">
  <p style="margin:0 0 12px;font-size:10px;font-weight:700;letter-spacing:2px;color:#059669;"><span leaf="">TRIAL FLOW · 一次 trial 的链路</span></p>

  <section style="background:#ECFDF5;border-radius:12px;border-left:3px solid #059669;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#059669;letter-spacing:1px;"><span leaf="">① 数据集 4.0.0 · 66 题</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">instruction.md + 独立环境</span></p>
      <p style="margin:0;font-size:12px;color:#6B7280;line-height:1.7;"><span leaf="">人工解 + 全量测试</span></p>
    </section>
  </section>

  <p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#059669;letter-spacing:0.5px;"><span leaf="">↓　T → AG</span></p>

  <section style="background:#ECFDF5;border-radius:12px;border-left:3px solid #059669;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#059669;letter-spacing:1px;"><span leaf="">② Agent 容器</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">模型 + harness</span></p>
      <p style="margin:0;font-size:11px;color:#6B7280;line-height:1.7;"><span leaf="">Claude Code / Codex / Grok Build / mini-SWE-agent / Muse Code</span></p>
    </section>
    <section style="background:#F9FAFB;border:1px dashed #D1D5DB;border-radius:8px;padding:7px 12px;margin-top:8px;">
      <p style="margin:0;font-size:11px;color:#6B7280;line-height:1.7;"><span leaf="">↳ AG → AT　8 小时 flat timeout</span></p>
    </section>
  </section>

  <p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#059669;letter-spacing:0.5px;"><span leaf="">↓　AG → AR</span></p>

  <section style="background:#ECFDF5;border-radius:12px;border-left:3px solid #059669;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#059669;letter-spacing:1px;"><span leaf="">③ Verifier 容器（separate）</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">下载 Agent 产物并转入</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#059669;"><span leaf="">↓　AR → TS</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">运行该任务的全部测试</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#059669;"><span leaf="">↓　TS → P</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">全部通过 = 1 次 trial 成功</span></p>
    </section>
  </section>

  <p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#059669;letter-spacing:0.5px;"><span leaf="">↓　P → K</span></p>

  <section style="background:#ECFDF5;border-radius:12px;border-left:3px solid #059669;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#059669;letter-spacing:1px;"><span leaf="">④ 计分</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">每题 5 次 trial　66 × 5 = 330</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#059669;"><span leaf="">↓　K → CI</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">resolution rate + 95% CI</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#059669;"><span leaf="">↓　CI → LB</span></p>
    <section style="background:#ffffff;border:1px solid #D1FAE5;border-radius:8px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#111827;line-height:1.7;"><span leaf="">官方榜 35 行</span></p>
    </section>
  </section>

</section>'''


class MoyuTheme(Theme):
    name = '摸鱼绿'
    label = '摸鱼绿'
    slug = 'moyu-green'
    tight_global = True

    def global_open(self):
        return ('<section style="max-width:677px;margin:0 auto;background:#ffffff;'
                'font-family:-apple-system,BlinkMacSystemFont,\'PingFang SC\',\'Hiragino Sans GB\','
                '\'Microsoft YaHei\',sans-serif;color:#374151;line-height:1.75;letter-spacing:0.5px;overflow-x:hidden;">\n')

    def rich(self, text):
        out = []
        for seg in tokens(text):
            if not seg:
                continue
            if seg.startswith('[[') and seg.endswith(']]'):
                out.append('<span style="border-bottom:2px solid #A7F3D0;font-weight:600;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('**') and seg.endswith('**'):
                out.append('<strong style="color:#059669;">' + leaf(seg[2:-2]) + '</strong>')
            elif seg.startswith('~~') and seg.endswith('~~'):
                out.append('<span style="background:linear-gradient(120deg,#FDE68A 0%,rgba(255,255,255,0) 100%);padding:0 4px;border-radius:2px;font-weight:600;color:#111827;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('{{') and seg.endswith('}}'):
                out.append('<span style="background:#F3F4F6;color:#1F2937;padding:2px 6px;border-radius:4px;font-size:13px;font-weight:600;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('!!') and seg.endswith('!!'):
                out.append('<span style="border-bottom:2px solid #FECACA;">' + leaf(seg[2:-2]) + '</span>')
            else:
                out.append(leaf(seg))
        return ''.join(out)

    def cover(self, series, date, kicker, title, accent, subtitle, benchmark, meta, tags, compact_meta=None):
        self.w('<section style="margin:0 0 32px;background:#fff;border:1.5px solid rgba(5,150,105,0.15);'
               'border-radius:20px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.06);width:100%;">')
        self.w('<section style="padding:32px 28px 28px;">')
        self.w('<section style="display:flex;align-items:center;gap:8px;margin-bottom:28px;">')
        self.w('<span style="width:6px;height:6px;background:#059669;border-radius:50%;"><span leaf=""><br></span></span>')
        self.w('<span style="font-size:11px;font-weight:700;letter-spacing:3px;color:#059669;">' + leaf('LLM BENCHMARKS · ' + series) + '</span>')
        self.w('<section style="flex:1;height:1px;overflow:hidden;background:linear-gradient(to right,rgba(5,150,105,0.12),transparent);"><span leaf=""><br></span></section>')
        self.w('<span style="font-size:10px;color:#D1D5DB;font-weight:600;">' + leaf(date) + '</span>')
        self.w('</section>')
        self.w('<section>')
        self.w('<p style="font-size:15px;color:#D1D5DB;margin:0 0 6px;text-decoration:line-through;letter-spacing:0.5px;">' + leaf(kicker) + '</p>')
        self.w('<p style="font-size:24px;font-weight:900;color:#111827;margin:0;line-height:1.05;letter-spacing:-2px;">'
               + leaf(title) + '<span style="color:#059669;">' + leaf(accent) + '</span></p>')
        self.w('<p style="font-size:24px;font-weight:900;color:#059669;margin:0 0 16px;line-height:1.05;letter-spacing:-2px;">' + leaf(subtitle) + '</p>')
        self.w('<section style="width:48px;height:3px;background:linear-gradient(to right,#059669,#34D399);border-radius:2px;margin-bottom:12px;"><span leaf=""><br></span></section>')
        self.w('<p style="font-size:12px;font-weight:800;letter-spacing:2px;color:#059669;margin:0 0 10px;">' + leaf(benchmark) + '</p>')
        self.w('<p style="font-size:13px;color:#9CA3AF;margin:0;line-height:1.7;letter-spacing:0.5px;">' + leaf(meta) + '</p>')
        self.w('</section></section>')
        self.w('<section style="background:linear-gradient(135deg,#059669,#10B981);padding:12px 28px;display:flex;align-items:center;justify-content:space-between;">')
        self.w('<p style="font-size:12px;color:rgba(255,255,255,0.9);margin:0;font-weight:600;letter-spacing:0.5px;">' + leaf('智能漫游 | Neuro Nomad') + '</p>')
        self.w('<section style="display:flex;gap:4px;">')
        for tag in tags:
            self.w('<span style="background:rgba(255,255,255,0.2);padding:1px 6px;border-radius:3px;font-size:8px;color:#fff;font-weight:600;">' + leaf(tag) + '</span>')
        self.w('</section></section></section>')

    def toc(self, items):
        self.w('<section style="margin:0 20px 32px;">')
        self.w('<section style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;">')
        self.w('<p style="font-size:10px;color:#9CA3AF;margin:0;text-transform:uppercase;letter-spacing:2px;font-weight:600;">' + leaf('📦 9 Parts + Conclusion') + '</p>')
        self.w('<p style="font-size:10px;color:#9CA3AF;margin:0;">' + leaf('👉 滑动') + '</p></section>')
        self.w('<section style="overflow-x:scroll;-webkit-overflow-scrolling:touch;white-space:nowrap;padding-bottom:8px;">')
        for i, (name, sub) in enumerate(items):
            first = (i == 0)
            if first:
                box = 'background:linear-gradient(135deg,#059669,#10B981);'
                c1, c2, c3 = 'rgba(255,255,255,0.7)', '#fff', 'rgba(255,255,255,0.7)'
            else:
                box = 'background:#fff;border:1px solid #E5E7EB;box-shadow:0 2px 6px rgba(0,0,0,0.04);'
                c1, c2, c3 = '#9CA3AF', '#111827', '#9CA3AF'
            mr = 'margin-right:8px;' if i < len(items) - 1 else ''
            part = 'PART ' + str(i + 1).zfill(2) if i < 9 else 'PART ///'
            self.w('<section style="display:inline-block;white-space:normal;vertical-align:top;width:110px;' + box
                   + 'border-radius:12px;padding:12px;' + mr + '">')
            self.w('<p style="font-size:9px;font-weight:700;color:' + c1 + ';letter-spacing:1px;margin:0 0 5px;">' + leaf(part) + '</p>')
            self.w('<p style="font-size:13px;font-weight:800;color:' + c2 + ';margin:0 0 3px;">' + leaf(name) + '</p>')
            self.w('<p style="font-size:10px;color:' + c3 + ';margin:0;">' + leaf(sub) + '</p></section>')
        self.w('</section></section>')

    def chapter(self, num, cn, en, first=False):
        mt = '16px' if first else '48px'
        self.w('<section style="margin-top:' + mt + ';margin-bottom:32px;padding:0 20px;">')
        self.w('<section style="display:flex;align-items:center;gap:16px;margin-bottom:24px;">')
        self.w('<section style="text-align:center;flex-shrink:0;">')
        self.w('<p style="margin:0;font-size:28px;font-weight:900;color:#059669;line-height:1;letter-spacing:-2px;">' + leaf(str(num).zfill(2)) + '</p>')
        self.w('<p style="margin:0;font-size:8px;font-weight:700;color:#D1D5DB;letter-spacing:2px;">' + leaf('PART') + '</p></section>')
        self.w('<span style="width:1px;height:36px;background:#E5E7EB;flex-shrink:0;"><span leaf=""><br></span></span>')
        self.w('<section>')
        self.w('<p style="margin:0 0 1px;font-size:17px;font-weight:900;color:#111827;letter-spacing:0.3px;">' + leaf(cn) + '</p>')
        self.w('<p style="margin:0;font-size:11px;font-weight:600;color:#9CA3AF;letter-spacing:1.5px;">' + leaf(en) + '</p>')
        self.w('</section></section>')

    def para(self, t, mb=16):
        self.w('<p style="margin-bottom:' + str(mb) + 'px;font-size:14px;line-height:1.9;text-align:justify;">' + self.rich(t) + '</p>')

    def oneliner(self, guide, text):
        self.w('<section style="background:#FFF;border:1px dashed #BBF7D0;border-radius:8px;padding:14px 16px;margin:0 20px 24px;text-align:center;">')
        self.w('<p style="font-size:12px;color:#9CA3AF;margin:0 0 6px;line-height:1.5;">' + leaf(guide) + '</p>')
        self.w('<p style="margin:0;line-height:1.6;"><span style="font-size:15px;color:#059669;font-weight:bold;border-bottom:3px solid #FDE68A;padding-bottom:2px;">' + leaf(text) + '</span></p>')
        self.w('</section>')

    def h3(self, t, mt=32):
        self.w('<p style="font-size:15px;font-weight:900;color:#111827;margin:' + str(mt) + 'px 0 16px;">'
               '<span style="background:linear-gradient(180deg,transparent 65%,#FDE68A 65%);padding:0 4px;">' + leaf(t) + '</span></p>')

    def quote(self, t):
        self.w('<section style="background:#F9FAFB;border:1px dashed #D1D5DB;border-radius:8px;padding:12px 16px;margin-bottom:24px;text-align:justify;">'
               '<p style="font-size:13px;color:#374151;margin:0;line-height:1.7;">' + self.rich(t) + '</p></section>')

    def warn(self, t, label=None):
        self.w('<section style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:12px;padding:12px 16px;margin-bottom:20px;">'
               '<p style="font-size:13px;color:#92400E;margin:0;font-weight:700;line-height:1.8;">' + self.rich(t) + '</p></section>')

    def cards3(self, items):
        self.w('<section style="background:#F9FAFB;padding:16px;border-radius:12px;border:1px solid #F3F4F6;margin:0 0 28px;">'
               '<section style="display:flex;align-items:stretch;justify-content:center;gap:6px;">')
        for i, (t1, t2) in enumerate(items):
            if i == 0:
                box = 'background:linear-gradient(135deg,#059669,#10B981);'
                c1, c2 = '#fff', 'rgba(255,255,255,0.8)'
            else:
                box = 'background:#fff;border:1px solid #E5E7EB;'
                c1, c2 = '#111827', '#9CA3AF'
            self.w('<section style="flex:1;text-align:center;padding:10px 8px;' + box + 'border-radius:8px;">')
            self.w('<p style="font-size:13px;font-weight:800;color:' + c1 + ';margin:0 0 3px;">' + leaf(t1) + '</p>')
            self.w('<p style="font-size:10px;color:' + c2 + ';margin:0;line-height:1.5;">' + leaf(t2) + '</p></section>')
        self.w('</section></section>')

    def cap(self, t):
        self.w('<p style="margin:0 0 10px;font-size:12px;font-weight:700;color:#059669;letter-spacing:1px;">' + leaf('✦ ' + t) + '</p>')

    def table(self, caption, headers, rows, widths=None, tight=False, real=False):
        self.cap(caption)
        n = len(headers)
        mw = {8: 720, 7: 700, 6: 660, 5: 600, 4: 520, 3: 420}.get(n)
        tstyle = 'width:100%;border-collapse:collapse;font-size:' + ('12px' if tight else '13px') + ';'
        if mw:
            tstyle += 'min-width:' + str(mw) + 'px;'
        pad = '6px 8px' if tight else '8px 12px'
        s = '<section style="margin-bottom:24px;overflow-x:auto;"><table style="' + tstyle + '"><thead><tr>'
        for hcell in headers:
            s += '<th style="background:#059669;color:#fff;font-weight:700;padding:' + pad + ';text-align:left;">' + leaf(hcell) + '</th>'
        s += '</tr></thead><tbody>'
        for i, row in enumerate(rows):
            bg = 'background:#F9FAFB;' if i % 2 == 1 else ''
            s += '<tr>'
            for cell in row:
                s += '<td style="padding:' + pad + ';border-bottom:1px solid #E5E7EB;color:#374151;' + bg + '">' + self.rich(cell) + '</td>'
            s += '</tr>'
        s += '</tbody></table></section>'
        self.w(s)

    def code(self, lang, lines):
        s = '<section style="margin:0 0 20px;border-radius:8px;overflow:hidden;background:#1E293B;box-shadow:0 4px 16px -8px rgba(15,23,42,0.4);">'
        s += '<section style="display:flex;align-items:center;padding:9px 14px;background:#0F172A;">'
        for c in ('#FF5F56', '#FFBD2E', '#27C93F'):
            s += '<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:' + c + ';margin-right:7px;"><span leaf=""><br></span></span>'
        s += '<span style="margin-left:12px;font-size:12px;color:#64748B;font-family:Consolas,Monaco,monospace;letter-spacing:1px;">' + leaf(lang) + '</span>'
        s += '</section><section style="padding:11px 14px;">'
        for line in lines:
            s += '<p style="margin:0;font-family:\'SF Mono\',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#E2E8F0;">' + leaf(line) + '</p>'
        s += '</section></section>'
        self.w(s)

    def ol(self, items, small=False):
        fs = '12px' if small else '14px'
        self.w('<section style="margin-bottom:24px;">')
        for i, it in enumerate(items, 1):
            self.w('<section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">')
            self.w('<span style="display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;'
                   'background:#059669;color:#fff;font-size:11px;font-weight:700;border-radius:50%;flex-shrink:0;margin-top:2px;">' + leaf(str(i)) + '</span>')
            self.w('<p style="font-size:' + fs + ';color:#374151;margin:0;line-height:1.9;flex:1;text-align:justify;">' + self.rich(it) + '</p></section>')
        self.w('</section>')

    def ul(self, items):
        for label, desc in items:
            self.w('<section style="margin-bottom:14px;"><p style="margin:0 0 6px;">'
                   '<span style="display:inline-block;font-size:13px;font-weight:700;color:#059669;background:rgba(5,150,105,0.08);'
                   'padding:3px 10px;border-radius:999px;">'
                   '<span style="display:inline-block;width:6px;height:6px;background:#059669;border-radius:50%;margin-right:5px;'
                   'vertical-align:middle;"><span leaf=""><br></span></span>' + leaf(label) + '</span></p>')
            self.w('<p style="font-size:13px;color:#4B5563;margin:0;line-height:1.7;text-align:justify;">' + self.rich(desc) + '</p></section>')

    def flow_terminal_bench(self):
        self.w(FLOW_MOYU)

    def signature(self):
        self.w('<section style="margin:0 20px 24px;">')
        self.w('<section style="background:#F0FDF4;padding:16px 20px;border-radius:8px;border:1px solid #BBF7D0;">')
        self.w('<p style="font-size:10px;color:#059669;font-weight:700;letter-spacing:3px;margin:0 0 12px;">' + leaf('✦ ABOUT') + '</p>')
        self.w('<p style="font-size:18px;font-weight:800;color:#059669;margin:0 0 4px;line-height:1.6;">' + leaf('智能漫游') + '</p>')
        self.w('<p style="font-size:11px;color:#9CA3AF;margin:0 0 14px;letter-spacing:2px;">' + leaf('Neuro Nomad') + '</p>')
        self.w('<p style="font-size:13px;color:#059669;margin:0 0 10px;line-height:1.8;">' + leaf('大模型 · AI智能体 · 多模态 · 具身智能') + '</p>')
        self.w('<p style="font-size:14px;color:#374151;margin:0;line-height:1.9;text-align:justify;">'
               + self.rich('聚焦[[模型原理、AI工程与推理优化实践]]。') + '</p>')
        self.w('</section></section>')

    def footer_cta(self):
        self.w('''<section style="background:radial-gradient(circle at center,#F9FAFB 0%,#FFFFFF 100%);border:1px solid #E5E7EB;border-radius:16px;padding:32px 20px;text-align:center;box-shadow:0 4px 12px rgba(0,0,0,0.03);margin:0 20px 24px;">
  <p style="font-size:13px;font-weight:bold;color:#111827;margin-bottom:20px;line-height:1.6;">
    <span leaf="">既然看到这里了，如果觉得有用，随手点个赞、在看、转发三连吧。</span>
  </p>
  <section style="display:flex;justify-content:center;gap:24px;margin-bottom:16px;">
    <section style="text-align:center;cursor:pointer;color:#4B5563;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#fff;border-radius:12px;box-shadow:0 2px 4px rgba(0,0,0,0.05);border:1px solid #F3F4F6;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg>
      </section>
      <span style="font-size:10px;font-weight:600;"><span leaf="">点赞</span></span>
    </section>
    <section style="text-align:center;cursor:pointer;color:#4B5563;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#fff;border-radius:12px;box-shadow:0 2px 4px rgba(0,0,0,0.05);border:1px solid #F3F4F6;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"></circle><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path></svg>
      </section>
      <span style="font-size:10px;font-weight:600;"><span leaf="">在看</span></span>
    </section>
    <section style="text-align:center;cursor:pointer;color:#059669;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#ECFDF5;border-radius:12px;box-shadow:0 2px 4px rgba(5,150,105,0.15);border:1px solid #A7F3D0;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 18v-4a8 8 0 0 1 8-8h8"></path><polyline points="16 2 20 6 16 10"></polyline></svg>
      </section>
      <span style="font-size:10px;font-weight:600;"><span leaf="">转发</span></span>
    </section>
  </section>
  <p style="font-size:10px;color:#9CA3AF;letter-spacing:1px;margin:0;">
    <span leaf="">THANKS FOR READING</span>
  </p>
</section>''')
