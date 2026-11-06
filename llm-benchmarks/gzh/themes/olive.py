# -*- coding: utf-8 -*-
"""橄榄手记主题（Olive Journal）。

实现 gzh-layout-pro `references/theme-olive-journal.md` 的组件层。
"""
import re

from ..render import tokens, leaf
from .base import Theme


def blank():
    """橄榄手记的装饰性空元素用 &nbsp;，与摸鱼绿/石墨的 <br> 不同。"""
    return '<span leaf="">&nbsp;</span>'


COVER_ROBOT_SVG = r'''<svg width="96" height="96" viewBox="0 0 96 96" aria-hidden="true" style="display:block;">
  <line x1="23" y1="24" x2="23" y2="17" stroke="#1e1f23" stroke-width="2" stroke-linecap="round"></line>
  <circle cx="23" cy="14" r="2.6" fill="#ed7b2f"></circle>
  <rect x="8" y="24" width="30" height="26" rx="7" fill="#fdfdf8" stroke="#1e1f23" stroke-width="2"></rect>
  <circle cx="17" cy="36" r="2.3" fill="#1e1f23"></circle>
  <circle cx="29" cy="36" r="2.3" fill="#1e1f23"></circle>
  <path d="M19 43 Q23 46 27 43" fill="none" stroke="#4d4f46" stroke-width="1.6" stroke-linecap="round"></path>
  <rect x="20" y="49" width="6" height="4" fill="#fdfdf8" stroke="#1e1f23" stroke-width="1.6"></rect>
  <rect x="11" y="52" width="24" height="14" rx="5" fill="#fdfdf8" stroke="#1e1f23" stroke-width="2"></rect>
  <path d="M52 22 L84 22 L92 30 L92 70 L52 70 Z" fill="#fdfdf8" stroke="#1e1f23" stroke-width="2"></path>
  <path d="M84 22 L92 30 L84 30 Z" fill="#eeefe9" stroke="#1e1f23" stroke-width="1.6"></path>
  <line x1="58" y1="34" x2="83" y2="34" stroke="#bfc1b7" stroke-width="2" stroke-linecap="round"></line>
  <line x1="58" y1="41" x2="78" y2="41" stroke="#bfc1b7" stroke-width="2" stroke-linecap="round"></line>
  <line x1="58" y1="48" x2="81" y2="48" stroke="#bfc1b7" stroke-width="2" stroke-linecap="round"></line>
  <circle cx="60" cy="58" r="3.2" fill="none" stroke="#4d4f46" stroke-width="2"></circle>
  <circle cx="71" cy="58" r="3.2" fill="none" stroke="#4d4f46" stroke-width="2"></circle>
  <circle cx="82" cy="58" r="3.2" fill="none" stroke="#4d4f46" stroke-width="2"></circle>
  <ellipse cx="60" cy="58" rx="7" ry="6" fill="none" stroke="#ed7b2f" stroke-width="2.6"></ellipse>
  <path d="M56 64 C67 62 77 63 86 65" fill="none" stroke="#bfc1b7" stroke-width="1.6" stroke-linecap="round"></path>
  <rect x="2" y="66" width="90" height="4" rx="2" fill="#fdfdf8" stroke="#1e1f23" stroke-width="1.8"></rect>
  <line x1="10" y1="70" x2="10" y2="88" stroke="#1e1f23" stroke-width="2" stroke-linecap="round"></line>
  <line x1="86" y1="70" x2="86" y2="88" stroke="#1e1f23" stroke-width="2" stroke-linecap="round"></line>
  <path d="M12 57 Q7 62 8 65" fill="none" stroke="#1e1f23" stroke-width="2" stroke-linecap="round"></path>
  <circle cx="8" cy="66" r="3" fill="#fdfdf8" stroke="#1e1f23" stroke-width="2"></circle>
  <path d="M35 57 Q42 55 48 54" fill="none" stroke="#1e1f23" stroke-width="2" stroke-linecap="round"></path>
  <circle cx="49" cy="54" r="3" fill="#fdfdf8" stroke="#1e1f23" stroke-width="2"></circle>
  <path d="M75 7 C75 2 84 2 84 8 C84 12 79 11 79 15" fill="none" stroke="#ed7b2f" stroke-width="2.8" stroke-linecap="round"></path>
  <circle cx="79" cy="20" r="2.2" fill="#ed7b2f"></circle>
</svg>'''


FLOW_OLIVE = r'''<section style="margin:0 0 24px;">
  <p style="margin:0 0 12px;font-size:10px;font-weight:800;letter-spacing:3px;color:#ed7b2f;"><span leaf="">TRIAL FLOW · 一次 trial 的链路</span></p>

  <section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;"><span leaf="">01 · 数据集 4.0.0 · 66 题</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">instruction.md + 独立环境</span></p>
      <p style="margin:0;font-size:12px;color:#65675e;line-height:1.7;"><span leaf="">人工解 + 全量测试</span></p>
    </section>
  </section>

  <p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#ed7b2f;letter-spacing:0.5px;"><span leaf="">↓　T → AG</span></p>

  <section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;"><span leaf="">02 · Agent 容器</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">模型 + harness</span></p>
      <p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;"><span leaf="">Claude Code / Codex / Grok Build / mini-SWE-agent / Muse Code</span></p>
    </section>
    <section style="background:#fdfdf8;border:1px dashed #bfc1b7;border-radius:6px;padding:7px 12px;margin-top:8px;">
      <p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;"><span leaf="">↳ AG → AT　8 小时 flat timeout</span></p>
    </section>
  </section>

  <p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#ed7b2f;letter-spacing:0.5px;"><span leaf="">↓　AG → AR</span></p>

  <section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;"><span leaf="">03 · Verifier 容器（separate）</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">下载 Agent 产物并转入</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#ed7b2f;"><span leaf="">↓　AR → TS</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">运行该任务的全部测试</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#ed7b2f;"><span leaf="">↓　TS → P</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">全部通过 = 1 次 trial 成功</span></p>
    </section>
  </section>

  <p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#ed7b2f;letter-spacing:0.5px;"><span leaf="">↓　P → K</span></p>

  <section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">
    <p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;"><span leaf="">04 · 计分</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">每题 5 次 trial　66 × 5 = 330</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#ed7b2f;"><span leaf="">↓　K → CI</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">resolution rate + 95% CI</span></p>
    </section>
    <p style="margin:6px 0;text-align:center;font-size:11px;color:#ed7b2f;"><span leaf="">↓　CI → LB</span></p>
    <section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 12px;">
      <p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;"><span leaf="">官方榜 35 行</span></p>
    </section>
  </section>

</section>'''


class OliveTheme(Theme):
    name = '橄榄手记'
    label = '橄榄手记'
    slug = 'olive-journal'
    tight_global = True

    def global_open(self):
        return ('<section style="max-width:677px;margin:0 auto;padding:8px;box-sizing:border-box;'
                'background:#fdfdf8;color:#4d4f46;font-family:\'IBM Plex Sans\',-apple-system,system-ui,'
                '\'PingFang SC\',\'Hiragino Sans GB\',\'Microsoft YaHei\',sans-serif;line-height:1.75;">\n')

    def rich(self, text):
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
                out.append('<span style="background:#eeefe9;color:#23251d;padding:2px 6px;border-radius:4px;font-family:ui-monospace,Menlo,Monaco,Consolas,monospace;font-size:13px;border:1px solid #b6b7af;">' + leaf(seg[2:-2]) + '</span>')
            elif seg.startswith('!!') and seg.endswith('!!'):
                out.append('<span style="color:#9ea096;text-decoration:line-through;">' + leaf(seg[2:-2]) + '</span>')
            else:
                out.append(leaf(seg))
        return ''.join(out)

    def cover(self, series, date, kicker, title, accent, subtitle, benchmark, meta, tags, compact_meta=None):
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
        self.w('<section style="padding:28px 24px 22px;">')
        self.w('<section style="display:flex;align-items:center;gap:8px;margin-bottom:22px;">')
        self.w('<span style="width:8px;height:8px;background:#1e1f23;border-radius:50%;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="font-size:10px;font-weight:700;letter-spacing:3px;color:#65675e;">' + leaf('LLM BENCHMARKS · ' + series) + '</span>')
        self.w('<span style="flex:1;height:1px;background:#bfc1b7;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="font-size:10px;color:#9ea096;font-weight:500;">' + leaf(date) + '</span>')
        self.w('</section>')
        self.w('<section style="display:flex;align-items:stretch;gap:18px;">')
        self.w('<section style="flex:1;min-width:0;">')
        self.w('<p style="font-size:14px;color:#9ea096;margin:0 0 8px;letter-spacing:0.3px;text-decoration:line-through;">' + leaf(kicker) + '</p>')
        self.w('<p style="font-size:24px;font-weight:800;color:#23251d;margin:0 0 10px;line-height:1.15;letter-spacing:-0.75px;">'
               + leaf(title) + '<span style="color:#4d4f46;">' + leaf(' · ') + '</span>'
               + '<span style="border-bottom:3px solid #ed7b2f;">' + leaf(accent) + '</span></p>')
        self.w('<section style="display:flex;align-items:center;gap:4px;margin-bottom:12px;">')
        self.w('<span style="width:22px;height:3px;background:#1e1f23;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="width:8px;height:3px;background:#bfc1b7;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('</section>')
        self.w('<p style="font-size:12px;font-weight:800;letter-spacing:2px;color:#4d4f46;margin:0 0 8px;">' + leaf(benchmark) + '</p>')
        self.w('<p style="font-size:13px;color:#65675e;margin:0;line-height:1.7;">' + leaf(compact_meta or (subtitle + ' · ' + meta)) + '</p>')
        self.w('</section>')
        self.w('<section style="flex-shrink:0;width:112px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#eeefe9;border:1px dashed #bfc1b7;border-radius:6px;padding:8px;">')
        self.w(COVER_ROBOT_SVG)
        self.w('<span style="font-size:8px;font-weight:700;color:#9ea096;letter-spacing:1px;margin-top:4px;">' + leaf('FIELD NOTE') + '</span>')
        self.w('</section></section></section>')
        self.w('<section style="background:#1e1f23;padding:11px 24px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
        self.w('<p style="font-size:12px;color:rgba(255,255,255,0.92);margin:0;font-weight:600;">' + leaf('智能漫游 ｜ Neuro Nomad') + '</p>')
        self.w('<section style="display:flex;gap:6px;flex-wrap:wrap;">')
        for tag in tags:
            self.w('<span style="background:#e5e7e0;color:#23251d;padding:3px 8px;border-radius:4px;font-size:8px;font-weight:700;border:1px solid #bfc1b7;">' + leaf(tag) + '</span>')
        self.w('</section></section></section>')

    def toc(self, items):
        self.w('<section style="margin:24px 0 28px;padding:18px;border-radius:6px;background:#fdfdf8;border:1px solid #bfc1b7;">')
        self.w('<p style="margin:0 0 12px;font-size:11px;font-weight:800;letter-spacing:2px;color:#65675e;">' + leaf('CONTENTS · 本期目录') + '</p>')
        self.w('<section style="display:flex;flex-wrap:wrap;gap:8px;">')
        for i, (name, sub) in enumerate(items):
            if i < 9:
                label = str(i + 1).zfill(2) + ' ' + name + ' · ' + sub
                self.w('<span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#e5e7e0;border:1px solid #bfc1b7;font-size:12px;font-weight:700;color:#23251d;">' + leaf(label) + '</span>')
            else:
                self.w('<span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#1e1f23;border:1px solid #23251d;font-size:12px;font-weight:700;color:#ffffff;">' + leaf('/// ' + name + ' · ' + sub) + '</span>')
        self.w('</section></section>')

    def oneliner(self, guide, text):
        self.w('<section style="margin:0 0 24px;background:#eeefe9;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
        self.w('<section style="padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;">')
        self.w('<section>')
        self.w('<p style="margin:0 0 4px;font-size:10px;color:#9ea096;letter-spacing:2px;">' + leaf(guide) + '</p>')
        self.w('<p style="margin:0;font-size:13px;line-height:1.7;color:#23251d;font-weight:700;">' + leaf(text) + '</p>')
        self.w('</section>')
        self.w('<span style="font-size:10px;color:#65675e;font-weight:800;letter-spacing:2px;">' + leaf('SUMMARY') + '</span>')
        self.w('</section></section>')

    def cards3(self, items):
        self.w('<section style="margin:0 0 24px;background:#eeefe9;padding:16px;border-radius:6px;border:1px solid #bfc1b7;">')
        self.w('<section style="display:flex;align-items:stretch;justify-content:center;gap:8px;">')
        for i, (t1, t2) in enumerate(items):
            if i == 0:
                box, c1, c2 = 'background:#1e1f23;border:1px solid #23251d;', '#ffffff', 'rgba(255,255,255,0.75)'
            else:
                box, c1, c2 = 'background:#fdfdf8;border:1px solid #bfc1b7;', '#23251d', '#65675e'
            self.w('<section style="flex:1;text-align:center;padding:10px 8px;border-radius:6px;' + box + '">')
            self.w('<p style="font-size:13px;font-weight:800;color:' + c1 + ';margin:0 0 3px;">' + leaf(t1) + '</p>')
            self.w('<p style="font-size:10px;color:' + c2 + ';margin:0;line-height:1.5;">' + leaf(t2) + '</p>')
            self.w('</section>')
        self.w('</section></section>')

    def chapter(self, num, cn, en, first=False):
        self.w('<section style="margin-top:36px;">')
        if num in (4, 8):
            self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
            self.w('<section style="display:flex;align-items:center;gap:10px;">')
            self.w('<span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:#1e1f23;color:#fff;font-size:11px;font-weight:800;">' + leaf(str(num).zfill(2)) + '</span>')
            self.w('<section>')
            self.w('<p style="margin:0 0 3px;font-size:14px;font-weight:800;color:#23251d;letter-spacing:0.2px;">' + leaf(cn) + '</p>')
            self.w('<p style="margin:0;font-size:11px;color:#65675e;letter-spacing:1.2px;">' + leaf(en) + '</p>')
            self.w('</section></section>')
            self.w('<span style="font-size:10px;color:#9ea096;letter-spacing:1px;">' + leaf('ISSUE ' + str(num).zfill(2)) + '</span>')
            self.w('</section>')
        else:
            self.w('<section style="display:flex;align-items:center;gap:14px;margin-bottom:18px;">')
            self.w('<section style="text-align:center;flex-shrink:0;">')
            self.w('<p style="margin:0;font-size:24px;font-weight:800;color:#23251d;line-height:1;letter-spacing:-2px;">' + leaf(str(num).zfill(2)) + '</p>')
            self.w('<p style="margin:0;font-size:8px;font-weight:700;color:#9ea096;letter-spacing:2px;">' + leaf('PART') + '</p>')
            self.w('</section>')
            self.w('<span style="width:1px;height:36px;background:#bfc1b7;flex-shrink:0;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
            self.w('<section>')
            self.w('<p style="margin:0 0 1px;font-size:17px;font-weight:800;color:#23251d;letter-spacing:0.2px;">' + leaf(cn) + '</p>')
            self.w('<p style="margin:0;font-size:11px;font-weight:600;color:#65675e;letter-spacing:1.2px;">' + leaf(en) + '</p>')
            self.w('</section></section>')

    def para(self, t, mb=16):
        self.w('<p style="margin:0 0 ' + str(mb) + 'px;font-size:14px;line-height:1.9;text-align:justify;color:#4d4f46;">' + self.rich(t) + '</p>')

    def h3(self, t, mt=32):
        m = re.match(r'^(\d+\.\d+)', t)
        prog = m.group(1) if m else '§'
        self.w('<section style="margin:' + str(mt) + 'px 0 16px;display:flex;align-items:flex-end;gap:12px;flex-wrap:wrap;border-bottom:1px solid #bfc1b7;padding-bottom:10px;">')
        self.w('<span style="font-size:10px;font-weight:800;letter-spacing:3px;color:#ed7b2f;">' + leaf('SECTION') + '</span>')
        self.w('<span style="font-size:18px;font-weight:800;color:#23251d;line-height:1.2;">' + leaf(t) + '</span>')
        self.w('<span style="margin-left:auto;font-size:10px;color:#9ea096;">' + leaf(prog) + '</span>')
        self.w('</section>')

    def quote(self, t, label='EDITOR NOTE', sub='核验与口径'):
        self.w('<section style="margin:0 0 24px;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
        self.w('<section style="padding:10px 16px;background:#1e1f23;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
        self.w('<p style="margin:0;font-size:10px;font-weight:800;letter-spacing:2px;color:#ffffff;">' + leaf(label) + '</p>')
        self.w('<span style="font-size:10px;color:rgba(255,255,255,0.65);">' + leaf(sub) + '</span>')
        self.w('</section>')
        self.w('<section style="padding:16px 18px 18px;background:#eeefe9;">')
        self.w('<p style="margin:0;font-size:14px;line-height:1.9;color:#4d4f46;text-align:justify;">' + self.rich(t) + '</p>')
        self.w('</section></section>')

    def warn(self, t, label=None):
        self.w('<section style="margin:0 0 24px;background:#fdfdf8;border:1px solid #bfc1b7;border-left:3px solid #ed7b2f;border-radius:6px;padding:14px 18px;">')
        self.w('<p style="margin:0 0 8px;font-size:10px;font-weight:800;letter-spacing:2px;color:#ed7b2f;">' + leaf('CAVEAT · 口径提示') + '</p>')
        self.w('<p style="margin:0;font-size:13px;line-height:1.8;color:#4d4f46;text-align:justify;">' + self.rich(t) + '</p>')
        self.w('</section>')

    def cap(self, t):
        self.w('<p style="margin:0 0 10px;font-size:12px;font-weight:800;color:#ed7b2f;letter-spacing:1px;">' + leaf('▍ ' + t) + '</p>')

    def table(self, caption, headers, rows, widths=None, tight=False, real=False):
        self.cap(caption)
        n = len(headers)
        if n <= 3:
            widths = {2: [42, 58], 3: [24, 32, 44]}.get(n, [100 // n] * n)
            self.w('<section style="margin:0 0 24px;border-radius:6px;overflow:hidden;border:1px solid #bfc1b7;background:#fdfdf8;">')
            self.w('<section style="display:flex;background:#eeefe9;border-bottom:1px solid #bfc1b7;">')
            for i, hcell in enumerate(headers):
                bd = 'border-left:1px solid #bfc1b7;' if i else ''
                self.w('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:12px;font-weight:800;color:#23251d;' + bd + '">' + self.rich(hcell) + '</section>')
            self.w('</section>')
            for ri, row in enumerate(rows):
                last = (ri == len(rows) - 1)
                self.w('<section style="display:flex;' + ('' if last else 'border-bottom:1px solid #bfc1b7;') + '">')
                for i, cell in enumerate(row):
                    bd = 'border-left:1px solid #bfc1b7;' if i else ''
                    self.w('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:13px;color:#4d4f46;' + bd + '">' + self.rich(cell) + '</section>')
                self.w('</section>')
            self.w('</section>')
        else:
            mw = {8: 720, 7: 700, 6: 660, 5: 600, 4: 520}.get(n, 520)
            tstyle = 'width:100%;border-collapse:collapse;font-size:' + ('12px' if tight else '13px') + ';min-width:' + str(mw) + 'px;'
            pad = '6px 8px' if tight else '8px 10px'
            s = '<section style="margin:0 0 24px;overflow-x:auto;-webkit-overflow-scrolling:touch;"><table style="' + tstyle + '"><thead><tr>'
            for hcell in headers:
                s += '<th style="background:#1e1f23;color:#fdfdf8;font-weight:800;padding:' + pad + ';text-align:left;border:1px solid #23251d;">' + leaf(hcell) + '</th>'
            s += '</tr></thead><tbody>'
            for i, row in enumerate(rows):
                bg = 'background:#eeefe9;' if i % 2 == 1 else 'background:#fdfdf8;'
                s += '<tr>'
                for cell in row:
                    s += '<td style="padding:' + pad + ';border:1px solid #bfc1b7;color:#4d4f46;' + bg + '">' + self.rich(cell) + '</td>'
                s += '</tr>'
            s += '</tbody></table></section>'
            self.w(s)

    def code(self, lang, lines):
        s = '<section style="margin:0 0 20px;border-radius:6px;overflow:hidden;background:#23251d;border:1px solid #1e1f23;">'
        s += '<section style="display:flex;align-items:center;padding:9px 14px;background:#1e1f23;">'
        for c in ('#9ea096', '#d4c9b8', '#ed7b2f'):
            s += '<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:' + c + ';margin-right:7px;">' + blank() + '</span>'
        s += '<span style="margin-left:12px;font-size:12px;color:#9ea096;font-family:Consolas,Monaco,monospace;letter-spacing:1px;">' + leaf(lang) + '</span>'
        s += '</section><section style="padding:11px 14px;">'
        for line in lines:
            s += '<p style="margin:0;font-family:\'SF Mono\',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#f5f5f0;">' + leaf(line) + '</p>'
        s += '</section></section>'
        self.w(s)

    def ol(self, items, small=False):
        fs = '12px' if small else '14px'
        self.w('<section style="margin:0 0 24px;">')
        self.w('<ul style="margin:0;padding-left:0;line-height:1.8;list-style-position:outside;">')
        for i, it in enumerate(items, 1):
            self.w('<li style="margin-bottom:10px;font-size:' + fs + ';color:#4d4f46;list-style-type:none;">')
            self.w('<section style="text-align:justify;">'
                   '<span style="display:inline-block;background:#e5e7e0;border:1px solid #bfc1b7;color:#23251d;border-radius:4px;padding:1px 6px;font-size:11px;font-weight:800;margin-right:8px;">'
                   + leaf(str(i).zfill(2)) + '</span>' + self.rich(it) + '</section>')
            self.w('</li>')
        self.w('</ul></section>')

    def ul(self, items):
        for i, (label, desc) in enumerate(items):
            dot = '#ed7b2f' if i % 2 == 0 else '#4d4f46'
            self.w('<section style="margin-bottom:14px;">')
            self.w('<p style="margin:0 0 6px;">'
                   '<span style="display:inline-block;font-size:13px;font-weight:700;color:#23251d;background:#e5e7e0;padding:3px 10px;border-radius:999px;border:1px solid #bfc1b7;">'
                   '<span style="display:inline-block;width:6px;height:6px;background:' + dot + ';border-radius:50%;margin-right:5px;vertical-align:middle;overflow:hidden;font-size:0;line-height:0;">'
                   + blank() + '</span>' + leaf(label) + '</span></p>')
            self.w('<p style="font-size:13px;color:#4d4f46;margin:0;line-height:1.7;text-align:justify;">' + self.rich(desc) + '</p>')
            self.w('</section>')

    def flow_terminal_bench(self):
        self.w(FLOW_OLIVE)

    # ---------- HLE 专用组件 ----------
    def cover_hle(self, series, date, title, subtitle, benchmark, meta, tags):
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
        self.w('<section style="padding:28px 24px 22px;">')
        self.w('<section style="display:flex;align-items:center;gap:8px;margin-bottom:22px;">')
        self.w('<span style="width:8px;height:8px;background:#1e1f23;border-radius:50%;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="font-size:10px;font-weight:700;letter-spacing:3px;color:#65675e;">' + leaf('LLM BENCHMARKS · ' + series) + '</span>')
        self.w('<span style="flex:1;height:1px;background:#bfc1b7;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="font-size:10px;color:#9ea096;font-weight:500;font-variant-numeric:tabular-nums;">' + leaf(date) + '</span>')
        self.w('</section>')
        self.w('<section style="display:flex;align-items:stretch;gap:18px;">')
        self.w('<section style="flex:1;min-width:0;">')
        self.w('<p style="font-size:24px;font-weight:800;color:#23251d;margin:0 0 10px;line-height:1.35;letter-spacing:-0.75px;">'
               + leaf(title) + '<br>'
               + '<span style="font-size:19px;border-bottom:3px solid #ed7b2f;">' + leaf(subtitle) + '</span></p>')
        self.w('<section style="display:flex;align-items:center;gap:4px;margin-bottom:12px;">')
        self.w('<span style="width:22px;height:3px;background:#1e1f23;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('<span style="width:8px;height:3px;background:#bfc1b7;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        self.w('</section>')
        self.w('<p style="font-size:12px;font-weight:800;letter-spacing:2px;color:#4d4f46;margin:0 0 8px;">' + leaf(benchmark) + '</p>')
        self.w('<p style="font-size:13px;color:#65675e;margin:0;line-height:1.7;">' + leaf(meta) + '</p>')
        self.w('</section>')
        self.w('<section style="flex-shrink:0;width:112px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#eeefe9;border:1px dashed #bfc1b7;border-radius:6px;padding:8px;">')
        self.w(COVER_ROBOT_SVG)
        self.w('<span style="font-size:8px;font-weight:700;color:#9ea096;letter-spacing:1px;margin-top:4px;">' + leaf('LLM × HLE') + '</span>')
        self.w('</section></section></section>')
        self.w('<section style="background:#1e1f23;padding:11px 24px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
        self.w('<p style="font-size:12px;color:rgba(255,255,255,0.92);margin:0;font-weight:600;">' + leaf('智能漫游 ｜ Neuro Nomad') + '</p>')
        self.w('<section style="display:flex;gap:6px;flex-wrap:wrap;">')
        for tag in tags:
            self.w('<span style="background:#e5e7e0;color:#23251d;padding:3px 8px;border-radius:4px;font-size:8px;font-weight:700;border:1px solid #bfc1b7;">' + leaf(tag) + '</span>')
        self.w('</section></section></section>')

    def toc_hle(self, items):
        self.w('<section style="margin:24px 0 28px;padding:18px;border-radius:6px;background:#fdfdf8;border:1px solid #bfc1b7;">')
        self.w('<p style="margin:0 0 12px;font-size:11px;font-weight:800;letter-spacing:2px;color:#65675e;">' + leaf('CONTENTS · 本期目录') + '</p>')
        self.w('<section style="display:flex;flex-wrap:wrap;gap:8px;">')
        for i, (name, sub) in enumerate(items):
            if i == len(items) - 1:
                label = '/// ' + name + ' · ' + sub
                style = 'background:#1e1f23;border:1px solid #23251d;color:#ffffff;'
            else:
                label = str(i + 1).zfill(2) + ' ' + name + ' · ' + sub
                style = 'background:#e5e7e0;border:1px solid #bfc1b7;color:#23251d;'
            self.w('<span style="display:inline-block;padding:6px 10px;border-radius:999px;' + style
                   + 'font-size:12px;font-weight:700;">' + leaf(label) + '</span>')
        self.w('</section></section>')

    def small_note(self, t):
        self.w('<p style="margin:0 0 16px;font-size:13px;line-height:1.8;text-align:justify;color:#65675e;">' + self.rich(t) + '</p>')

    def bullet(self, items):
        self.w('<section style="margin:0 0 24px;">')
        self.w('<ul style="margin:0;padding-left:22px;line-height:1.8;list-style-position:outside;">')
        for it in items:
            self.w('<li style="margin-bottom:10px;font-size:14px;color:#4d4f46;list-style-type:disc;text-align:justify;">'
                   + '<section>' + self.rich(it) + '</section></li>')
        self.w('</ul></section>')

    def ul_hle(self, items):
        for i, (label, desc) in enumerate(items):
            dot = '#ed7b2f' if i % 2 == 0 else '#4d4f46'
            self.w('<section style="margin-bottom:16px;">')
            self.w('<p style="margin:0 0 6px;">'
                   '<span style="display:inline-block;font-size:13px;font-weight:700;color:#23251d;background:#e5e7e0;padding:3px 10px;border-radius:999px;border:1px solid #bfc1b7;">'
                   '<span style="display:inline-block;width:6px;height:6px;background:' + dot + ';border-radius:50%;margin-right:5px;vertical-align:middle;overflow:hidden;font-size:0;line-height:0;">'
                   + blank() + '</span>' + leaf(label) + '</span></p>')
            self.w('<p style="font-size:13px;color:#4d4f46;margin:0;line-height:1.7;text-align:justify;">' + self.rich(desc) + '</p>')
            self.w('</section>')

    def ol_hle(self, items, small=False):
        fs = '12px' if small else '14px'
        self.w('<section style="margin:0 0 24px;">')
        self.w('<ul style="margin:0;padding-left:0;line-height:1.8;list-style-position:outside;">')
        for i, it in enumerate(items, 1):
            self.w('<li style="margin-bottom:10px;font-size:' + fs + ';color:#4d4f46;list-style-type:none;">')
            self.w('<section style="text-align:justify;word-break:break-word;">'
                   '<span style="display:inline-block;background:#e5e7e0;border:1px solid #bfc1b7;color:#23251d;border-radius:4px;padding:1px 6px;font-size:11px;font-weight:800;margin-right:8px;">'
                   + leaf(str(i).zfill(2)) + '</span>' + self.rich(it) + '</section>')
            self.w('</li>')
        self.w('</ul></section>')

    def table_hle(self, caption, headers, rows, widths=None, tight=False, real=False):
        self.cap(caption)
        n = len(headers)
        if n <= 3 and not real:
            if widths is None:
                widths = {2: [42, 58], 3: [24, 32, 44]}[n]
            self.w('<section style="margin:0 0 24px;border-radius:6px;overflow:hidden;border:1px solid #bfc1b7;background:#fdfdf8;">')
            self.w('<section style="display:flex;background:#eeefe9;border-bottom:1px solid #bfc1b7;">')
            for i, hcell in enumerate(headers):
                bd = 'border-left:1px solid #bfc1b7;' if i else ''
                self.w('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:12px;font-weight:800;color:#23251d;' + bd + '">' + leaf(hcell) + '</section>')
            self.w('</section>')
            for ri, row in enumerate(rows):
                last = (ri == len(rows) - 1)
                self.w('<section style="display:flex;' + ('' if last else 'border-bottom:1px solid #bfc1b7;') + '">')
                for i, cell in enumerate(row):
                    bd = 'border-left:1px solid #bfc1b7;' if i else ''
                    self.w('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:13px;color:#4d4f46;' + bd + '">' + self.rich(cell) + '</section>')
                self.w('</section>')
            self.w('</section>')
        else:
            mw = {3: 640, 4: 560, 5: 700, 6: 780, 7: 840, 8: 900}.get(n, 640)
            tstyle = 'width:100%;border-collapse:collapse;font-size:' + ('12px' if tight else '13px') + ';min-width:' + str(mw) + 'px;'
            pad = '6px 8px' if tight else '8px 10px'
            s = '<section style="margin:0 0 24px;overflow-x:auto;-webkit-overflow-scrolling:touch;"><table style="' + tstyle + '"><thead><tr>'
            for hcell in headers:
                s += '<th style="background:#1e1f23;color:#fdfdf8;font-weight:800;padding:' + pad + ';text-align:left;border:1px solid #23251d;">' + leaf(hcell) + '</th>'
            s += '</tr></thead><tbody>'
            for i, row in enumerate(rows):
                bg = 'background:#eeefe9;' if i % 2 == 1 else 'background:#fdfdf8;'
                s += '<tr>'
                for cell in row:
                    s += '<td style="padding:' + pad + ';border:1px solid #bfc1b7;color:#4d4f46;' + bg + '">' + self.rich(cell) + '</td>'
                s += '</tr>'
            s += '</tbody></table></section>'
            self.w(s)

    def label_bar(self, label, version, note):
        self.w('<section style="margin-top:36px;">')
        self.w('<section style="background:#eeefe9;border:1px solid #bfc1b7;border-radius:6px;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
        self.w('<p style="margin:0;font-size:10px;font-weight:800;letter-spacing:4px;color:#23251d;">' + leaf(label) + '</p>')
        self.w('<section style="display:flex;gap:8px;flex-wrap:wrap;">')
        self.w('<span style="font-size:10px;color:#65675e;font-weight:700;">' + leaf(version) + '</span>')
        self.w('<span style="font-size:10px;color:#9ea096;">' + leaf(note) + '</span>')
        self.w('</section></section></section>')

    def summary_split(self, left, right_label, right):
        self.w('<section style="margin:0 0 24px;">')
        self.w('<section style="border-radius:6px;overflow:hidden;border:1px solid #23251d;background:#1e1f23;display:flex;align-items:stretch;">')
        self.w('<section style="flex:1;padding:18px 18px 20px;border-right:1px solid rgba(255,255,255,0.08);">')
        self.w('<p style="margin:0 0 8px;font-size:11px;letter-spacing:2px;color:rgba(255,255,255,0.55);font-weight:700;">' + leaf('SUMMARY') + '</p>')
        self.w('<p style="margin:0;font-size:15px;line-height:1.9;color:rgba(255,255,255,0.92);">' + leaf(left) + '</p>')
        self.w('</section>')
        self.w('<section style="width:34%;min-width:120px;padding:18px;background:#23251d;display:flex;flex-direction:column;justify-content:center;gap:10px;">')
        self.w('<span style="display:inline-block;padding:4px 8px;background:#eeefe9;color:#23251d;border-radius:4px;font-size:10px;font-weight:800;align-self:flex-start;">' + leaf(right_label) + '</span>')
        self.w('<p style="margin:0;font-size:13px;line-height:1.8;color:rgba(255,255,255,0.76);">' + leaf(right) + '</p>')
        self.w('</section></section></section>')

    def flow_hle(self):
        self.w('<section style="margin:0 0 24px;">')
        self.w('<p style="margin:0 0 12px;font-size:10px;font-weight:800;letter-spacing:3px;color:#ed7b2f;">' + leaf('FLOW · 从 70,000 次投稿到 2,500 题') + '</p>')
        self.w('<section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">')
        self.w('<p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;">' + leaf('01 · 命题层 · 全球专家众包') + '</p>')
        self.w('<section style="display:flex;gap:8px;">')
        self.w('<section style="flex:1;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('70,000+ 次投稿') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('近 1,000 名专家 · 500+ 机构 · 50 国') + '</p></section>')
        self.w('<section style="flex:1;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('50 万美元奖金池') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('前 50 题各 5,000 美元') + '</p></section>')
        self.w('</section></section>')
        self.w('<p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#ed7b2f;letter-spacing:0.5px;">' + leaf('↓　A / B → C') + '</p>')
        self.w('<section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">')
        self.w('<p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;">' + leaf('02 · 难度门槛 · 前沿模型预筛') + '</p>')
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('GPT-4o / Gemini 1.5 Pro / Claude 3.5 Sonnet / o1') + '</p></section>')
        self.w('<p style="margin:6px 0;text-align:center;font-size:11px;color:#ed7b2f;">' + leaf('↓　C → D') + '</p>')
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('约 13,000 题过门槛') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('精确答案须全部答错 · 多选最多允许 1 个蒙对') + '</p></section>')
        self.w('</section>')
        self.w('<p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#ed7b2f;letter-spacing:0.5px;">' + leaf('↓　D → E') + '</p>')
        self.w('<section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">')
        self.w('<p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;">' + leaf('03 · 人工评审与清洗') + '</p>')
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('两轮研究生学历专家评审') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('约 2,700 公开题 + 私有题') + '</p></section>')
        self.w('<p style="margin:6px 0;text-align:center;font-size:11px;color:#ed7b2f;">' + leaf('↓　E → F') + '</p>')
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('Bug Bounty 勘误 + 可检索题审计') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('2025-04-03 定稿 2,500 题') + '</p></section>')
        self.w('</section>')
        self.w('<p style="margin:8px 0;text-align:center;font-size:11px;font-weight:700;color:#ed7b2f;letter-spacing:0.5px;">' + leaf('↓　F → G') + '</p>')
        self.w('<section style="background:#eeefe9;border:1px solid #bfc1b7;border-left:3px solid #1e1f23;border-radius:6px;padding:12px 14px;">')
        self.w('<p style="margin:0 0 8px;font-size:11px;font-weight:800;color:#23251d;letter-spacing:1px;">' + leaf('04 · 发布与衍生题集') + '</p>')
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('G · 公开 2,500 题') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('Hugging Face cais/hle') + '</p></section>')
        self.w('<p style="margin:6px 0;text-align:center;font-size:11px;color:#ed7b2f;">' + leaf('↓　G → H / I / J') + '</p>')
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;margin-bottom:6px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('H · HLE-Rolling') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('动态换题 fork') + '</p></section>')
        self.w('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:8px 10px;margin-bottom:6px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('I · HLE-Diamond') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('1,000 题精炼子集') + '</p></section>')
        self.w('<section style="background:#fdfdf8;border:1px dashed #bfc1b7;border-radius:6px;padding:8px 10px;">'
               '<p style="margin:0;font-size:13px;color:#23251d;line-height:1.7;">' + leaf('J · HLE-Verified') + '</p>'
               '<p style="margin:0;font-size:11px;color:#65675e;line-height:1.7;">' + leaf('第三方 1,811 题修订 · G 虚线指向') + '</p></section>')
        self.w('</section></section>')

    def signature(self):
        self.w('<section style="margin:24px 0 0;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
        self.w('<section style="padding:10px 16px;background:#1e1f23;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
        self.w('<p style="margin:0;font-size:10px;font-weight:800;letter-spacing:3px;color:#ffffff;">' + leaf('ABOUT') + '</p>')
        self.w('<span style="font-size:10px;color:rgba(255,255,255,0.65);">' + leaf('智能漫游 ｜ Neuro Nomad') + '</span>')
        self.w('</section>')
        self.w('<section style="padding:16px 18px 18px;background:#eeefe9;">')
        self.w('<p style="font-size:18px;font-weight:800;color:#23251d;margin:0 0 4px;">' + leaf('智能漫游') + '</p>')
        self.w('<p style="font-size:11px;color:#9ea096;letter-spacing:2px;margin:0 0 12px;">' + leaf('Neuro Nomad') + '</p>')
        self.w('<p style="font-size:13px;color:#ed7b2f;margin:0 0 8px;line-height:1.8;">' + leaf('大模型 · AI智能体 · 多模态 · 具身智能') + '</p>')
        self.w('<p style="font-size:14px;color:#4d4f46;margin:0;line-height:1.9;text-align:justify;">'
               + self.rich('聚焦[[模型原理、AI工程与推理优化实践]]。') + '</p>')
        self.w('</section></section>')

    def footer_cta(self):
        self.w('''<section style="margin:24px 0 8px;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:22px 16px;text-align:center;">
  <p style="font-size:13px;font-weight:700;color:#23251d;line-height:1.6;margin:0 0 14px;">
    <span leaf="">如果觉得今天这篇有收获，欢迎点赞、在看、收藏三连，我们下篇见。</span>
  </p>
  <section style="display:flex;justify-content:center;gap:18px;margin-bottom:14px;flex-wrap:wrap;">
    <section style="text-align:center;color:#4d4f46;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#eeefe9;border-radius:6px;border:1px solid #bfc1b7;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path></svg>
      </section>
      <span style="font-size:11px;font-weight:600;"><span leaf="">赞</span></span>
    </section>
    <section style="text-align:center;color:#4d4f46;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#eeefe9;border-radius:6px;border:1px solid #bfc1b7;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="3"></circle><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path></svg>
      </section>
      <span style="font-size:11px;font-weight:600;"><span leaf="">在看</span></span>
    </section>
    <section style="text-align:center;color:#23251d;">
      <section style="width:40px;height:40px;display:flex;align-items:center;justify-content:center;margin:0 auto 6px;background:#d4c9b8;border-radius:6px;border:1px solid #b17816;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#23251d" stroke-width="1.8"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
      </section>
      <span style="font-size:11px;font-weight:700;"><span leaf="">收藏</span></span>
    </section>
  </section>
  <p style="line-height:1.6;font-size:10px;color:#9ea096;letter-spacing:2px;margin:0;font-weight:500;">
    <span leaf="">THANKS FOR READING</span>
  </p>
</section>''')
