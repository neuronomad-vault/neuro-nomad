# -*- coding: utf-8 -*-
"""按 gzh-layout-pro 橄榄手记组件库装配 terminal-bench-v4-0.md 公众号正文。

内容装配段直接复用同目录的 gzh_moyu_gen.py（保证三版内容零差异），只重写组件层。
产物写到脚本所在目录；源 Markdown 仍在 /Users/admin/work/llm-benchmarks/benchmarks/。
"""
import html
import os
import re

OUT = []


def W(s):
    OUT.append(s)


def esc(t):
    return html.escape(t, quote=False)


def leaf(t):
    return '<span leaf="">' + esc(t) + '</span>'


def blank():
    """装饰性空元素占位（组件库用 &nbsp; 而非 <br>）"""
    return '<span leaf="">&nbsp;</span>'


TOKEN = re.compile(r'(\[\[.+?\]\]|\*\*.+?\*\*|~~.+?~~|\{\{.+?\}\}|!!.+?!!)', re.S)


def rich(t):
    out = []
    for seg in TOKEN.split(t):
        if not seg:
            continue
        if seg.startswith('[[') and seg.endswith(']]'):
            # 文字强调 c：橙色下划线（theme-index 权威值）
            out.append('<span style="border-bottom:2px solid #ed7b2f;font-weight:600;color:#23251d;">' + leaf(seg[2:-2]) + '</span>')
        elif seg.startswith('**') and seg.endswith('**'):
            # 文字强调 a：强调加粗
            out.append('<strong style="color:#23251d;">' + leaf(seg[2:-2]) + '</strong>')
        elif seg.startswith('~~') and seg.endswith('~~'):
            # 文字强调 b：浅底高亮框
            out.append('<span style="background:#eeefe9;padding:1px 5px;border-radius:4px;font-weight:600;color:#23251d;border:1px solid #bfc1b7;">' + leaf(seg[2:-2]) + '</span>')
        elif seg.startswith('{{') and seg.endswith('}}'):
            # 文字强调 d：行内代码标签（monospace 使其进入 code 区，豁免半角符号）
            out.append('<span style="background:#eeefe9;color:#23251d;padding:2px 6px;border-radius:4px;font-family:ui-monospace,Menlo,Monaco,Consolas,monospace;font-size:13px;border:1px solid #b6b7af;">' + leaf(seg[2:-2]) + '</span>')
        elif seg.startswith('!!') and seg.endswith('!!'):
            # 文字强调 e：删除线旧词
            out.append('<span style="color:#9ea096;text-decoration:line-through;">' + leaf(seg[2:-2]) + '</span>')
        else:
            out.append(leaf(seg))
    return ''.join(out)


# ---------- 组件 1 全局容器 ----------
GLOBAL_OPEN = ('<section style="max-width:677px;margin:0 auto;padding:8px;box-sizing:border-box;'
               'background:#fdfdf8;color:#4d4f46;font-family:\'IBM Plex Sans\',-apple-system,system-ui,'
               '\'PingFang SC\',\'Hiragino Sans GB\',\'Microsoft YaHei\',sans-serif;line-height:1.75;">\n')
GLOBAL_CLOSE = '\n</section>\n'


# ---------- 4.1 内联流程图（公众号不渲染 Mermaid，用纯内联 HTML 等价重画） ----------
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


# ---------- 组件 2 头图卡 hero-card（全文唯一，不设 margin-top） ----------
def cover():
    W('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
    W('<section style="padding:28px 24px 22px;">')
    W('<section style="display:flex;align-items:center;gap:8px;margin-bottom:22px;">')
    W('<span style="width:8px;height:8px;background:#1e1f23;border-radius:50%;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
    W('<span style="font-size:10px;font-weight:700;letter-spacing:3px;color:#65675e;">' + leaf('LLM BENCHMARKS · 02') + '</span>')
    W('<span style="flex:1;height:1px;background:#bfc1b7;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
    W('<span style="font-size:10px;color:#9ea096;font-weight:500;">' + leaf('2026.11') + '</span>')
    W('</section>')
    W('<section style="display:flex;align-items:stretch;gap:18px;">')
    W('<section style="flex:1;min-width:0;">')
    W('<p style="font-size:14px;color:#9ea096;margin:0 0 8px;letter-spacing:0.3px;text-decoration:line-through;">' + leaf('跑个榜就能看出谁更强？') + '</p>')
    W('<p style="font-size:24px;font-weight:800;color:#23251d;margin:0 0 10px;line-height:1.15;letter-spacing:-0.75px;">'
      + leaf('64.85% 的榜首，') + '<span style="color:#4d4f46;">' + leaf(' · ') + '</span>'
      + '<span style="border-bottom:3px solid #ed7b2f;">' + leaf('并不稳') + '</span></p>')
    W('<section style="display:flex;align-items:center;gap:4px;margin-bottom:12px;">')
    W('<span style="width:22px;height:3px;background:#1e1f23;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
    W('<span style="width:8px;height:3px;background:#bfc1b7;border-radius:2px;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
    W('</section>')
    W('<p style="font-size:12px;font-weight:800;letter-spacing:2px;color:#4d4f46;margin:0 0 8px;">' + leaf('TERMINAL-BENCH 4.0') + '</p>')
    W('<p style="font-size:13px;color:#65675e;margin:0;line-height:1.7;">' + leaf('30 道题的评分缺陷 · 66 题 · 330 trials · 独立 verifier') + '</p>')
    W('</section>')
    W('<section style="flex-shrink:0;width:112px;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#eeefe9;border:1px dashed #bfc1b7;border-radius:6px;padding:8px;">')
    W('<svg width="72" height="72" viewBox="0 0 64 64" style="display:block;">'
      '<ellipse cx="32" cy="36" rx="22" ry="18" fill="none" stroke="#4d4f46" stroke-width="2"></ellipse>'
      '<circle cx="26" cy="30" r="3" fill="#4d4f46"></circle>'
      '<circle cx="38" cy="30" r="3" fill="#4d4f46"></circle>'
      '<path d="M28 40 Q32 44 36 40" fill="none" stroke="#4d4f46" stroke-width="1.5"></path>'
      '<path d="M12 34 L8 28 M52 34 L56 28" stroke="#bfc1b7" stroke-width="2" stroke-linecap="round"></path></svg>')
    W('<span style="font-size:8px;font-weight:700;color:#9ea096;letter-spacing:1px;margin-top:4px;">' + leaf('FIELD NOTE') + '</span>')
    W('</section></section></section>')
    W('<section style="background:#1e1f23;padding:11px 24px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
    W('<p style="font-size:12px;color:rgba(255,255,255,0.92);margin:0;font-weight:600;">' + leaf('智能漫游 ｜ Neuro Nomad') + '</p>')
    W('<section style="display:flex;gap:6px;flex-wrap:wrap;">')
    for tag in ('TERMINAL-BENCH 4.0', 'v4.0.0'):
        W('<span style="background:#e5e7e0;color:#23251d;padding:3px 8px;border-radius:4px;font-size:8px;font-weight:700;border:1px solid #bfc1b7;">' + leaf(tag) + '</span>')
    W('</section></section></section>')


# ---------- 组件 29 路线胶囊组（本期目录变体） ----------
def toc(items):
    W('<section style="margin:24px 0 28px;padding:18px;border-radius:6px;background:#fdfdf8;border:1px solid #bfc1b7;">')
    W('<p style="margin:0 0 12px;font-size:11px;font-weight:800;letter-spacing:2px;color:#65675e;">' + leaf('CONTENTS · 本期目录') + '</p>')
    W('<section style="display:flex;flex-wrap:wrap;gap:8px;">')
    for i, (name, sub) in enumerate(items):
        if i < 9:
            label = str(i + 1).zfill(2) + ' ' + name + ' · ' + sub
            W('<span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#e5e7e0;border:1px solid #bfc1b7;font-size:12px;font-weight:700;color:#23251d;">' + leaf(label) + '</span>')
        else:
            W('<span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#1e1f23;border:1px solid #23251d;font-size:12px;font-weight:700;color:#ffffff;">' + leaf('/// ' + name + ' · ' + sub) + '</span>')
    W('</section></section>')


# ---------- 组件 32 摘要横幅条 ----------
def oneliner(guide, text):
    W('<section style="margin:0 0 24px;background:#eeefe9;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
    W('<section style="padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;">')
    W('<section>')
    W('<p style="margin:0 0 4px;font-size:10px;color:#9ea096;letter-spacing:2px;">' + leaf(guide) + '</p>')
    W('<p style="margin:0;font-size:13px;line-height:1.7;color:#23251d;font-weight:700;">' + leaf(text) + '</p>')
    W('</section>')
    W('<span style="font-size:10px;color:#65675e;font-weight:800;letter-spacing:2px;">' + leaf('SUMMARY') + '</span>')
    W('</section></section>')


# ---------- 组件 21 对比摘要卡（三列扩展变体） ----------
def cards3(items):
    W('<section style="margin:0 0 24px;background:#eeefe9;padding:16px;border-radius:6px;border:1px solid #bfc1b7;">')
    W('<section style="display:flex;align-items:stretch;justify-content:center;gap:8px;">')
    for i, (t1, t2) in enumerate(items):
        if i == 0:
            box, c1, c2 = 'background:#1e1f23;border:1px solid #23251d;', '#ffffff', 'rgba(255,255,255,0.75)'
        else:
            box, c1, c2 = 'background:#fdfdf8;border:1px solid #bfc1b7;', '#23251d', '#65675e'
        W('<section style="flex:1;text-align:center;padding:10px 8px;border-radius:6px;' + box + '">')
        W('<p style="font-size:13px;font-weight:800;color:' + c1 + ';margin:0 0 3px;">' + leaf(t1) + '</p>')
        W('<p style="font-size:10px;color:' + c2 + ';margin:0;line-height:1.5;">' + leaf(t2) + '</p>')
        W('</section>')
    W('</section></section>')


# ---------- 组件 3 章节标题 / 组件 6 期号徽章条（交替） ----------
def chapter(num, cn, en, first=False):
    W('<section style="margin-top:36px;">')
    if num in (4, 8):
        # 组件 6 期号徽章条：专题章节用，制造内刊分节节奏
        W('<section style="background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
        W('<section style="display:flex;align-items:center;gap:10px;">')
        W('<span style="display:inline-flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:50%;background:#1e1f23;color:#fff;font-size:11px;font-weight:800;">' + leaf(str(num).zfill(2)) + '</span>')
        W('<section>')
        W('<p style="margin:0 0 3px;font-size:14px;font-weight:800;color:#23251d;letter-spacing:0.2px;">' + leaf(cn) + '</p>')
        W('<p style="margin:0;font-size:11px;color:#65675e;letter-spacing:1.2px;">' + leaf(en) + '</p>')
        W('</section></section>')
        W('<span style="font-size:10px;color:#9ea096;letter-spacing:1px;">' + leaf('ISSUE ' + str(num).zfill(2)) + '</span>')
        W('</section>')
    else:
        # 组件 3 section-title：默认主力
        W('<section style="display:flex;align-items:center;gap:14px;margin-bottom:18px;">')
        W('<section style="text-align:center;flex-shrink:0;">')
        W('<p style="margin:0;font-size:24px;font-weight:800;color:#23251d;line-height:1;letter-spacing:-2px;">' + leaf(str(num).zfill(2)) + '</p>')
        W('<p style="margin:0;font-size:8px;font-weight:700;color:#9ea096;letter-spacing:2px;">' + leaf('PART') + '</p>')
        W('</section>')
        W('<span style="width:1px;height:36px;background:#bfc1b7;flex-shrink:0;display:inline-block;overflow:hidden;vertical-align:middle;font-size:0;line-height:0;">' + blank() + '</span>')
        W('<section>')
        W('<p style="margin:0 0 1px;font-size:17px;font-weight:800;color:#23251d;letter-spacing:0.2px;">' + leaf(cn) + '</p>')
        W('<p style="margin:0;font-size:11px;font-weight:600;color:#65675e;letter-spacing:1.2px;">' + leaf(en) + '</p>')
        W('</section></section>')


def endchapter():
    W('</section>')


# ---------- 组件 10 正文段落 ----------
def para(t, mb=16):
    W('<p style="margin:0 0 ' + str(mb) + 'px;font-size:14px;line-height:1.9;text-align:justify;color:#4d4f46;">' + rich(t) + '</p>')


# ---------- 组件 9 前导词标题（小节） ----------
def h3(t, mt=32):
    m = re.match(r'^(\d+\.\d+)', t)
    prog = m.group(1) if m else '§'
    W('<section style="margin:' + str(mt) + 'px 0 16px;display:flex;align-items:flex-end;gap:12px;flex-wrap:wrap;border-bottom:1px solid #bfc1b7;padding-bottom:10px;">')
    W('<span style="font-size:10px;font-weight:800;letter-spacing:3px;color:#ed7b2f;">' + leaf('SECTION') + '</span>')
    W('<span style="font-size:18px;font-weight:800;color:#23251d;line-height:1.2;">' + leaf(t) + '</span>')
    W('<span style="margin-left:auto;font-size:10px;color:#9ea096;">' + leaf(prog) + '</span>')
    W('</section>')


# ---------- 组件 14 编者按（引用 / 核验说明） ----------
def quote(t):
    W('<section style="margin:0 0 24px;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
    W('<section style="padding:10px 16px;background:#1e1f23;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
    W('<p style="margin:0;font-size:10px;font-weight:800;letter-spacing:2px;color:#ffffff;">' + leaf('EDITOR NOTE') + '</p>')
    W('<span style="font-size:10px;color:rgba(255,255,255,0.65);">' + leaf('核验与口径') + '</span>')
    W('</section>')
    W('<section style="padding:16px 18px 18px;background:#eeefe9;">')
    W('<p style="margin:0;font-size:14px;line-height:1.9;color:#4d4f46;text-align:justify;">' + rich(t) + '</p>')
    W('</section></section>')


# ---------- 组件 15 重点观点卡（口径警示变体） ----------
def warn(t):
    W('<section style="margin:0 0 24px;background:#fdfdf8;border:1px solid #bfc1b7;border-left:3px solid #ed7b2f;border-radius:6px;padding:14px 18px;">')
    W('<p style="margin:0 0 8px;font-size:10px;font-weight:800;letter-spacing:2px;color:#ed7b2f;">' + leaf('CAVEAT · 口径提示') + '</p>')
    W('<p style="margin:0;font-size:13px;line-height:1.8;color:#4d4f46;text-align:justify;">' + rich(t) + '</p>')
    W('</section>')


# ---------- 表序小标签 ----------
def cap(t):
    W('<p style="margin:0 0 10px;font-size:12px;font-weight:800;color:#ed7b2f;letter-spacing:1px;">' + leaf('▍ ' + t) + '</p>')


# ---------- 组件 22 精简对照表（2-3 列，flex 仿表格） / 真 table（4 列以上横滑） ----------
def table(caption, headers, rows, tight=False):
    cap(caption)
    n = len(headers)
    if n <= 3:
        # 组件 22：flex 仿表格，不用 table / grid
        widths = {2: [42, 58], 3: [24, 32, 44]}.get(n, [100 // n] * n)
        W('<section style="margin:0 0 24px;border-radius:6px;overflow:hidden;border:1px solid #bfc1b7;background:#fdfdf8;">')
        W('<section style="display:flex;background:#eeefe9;border-bottom:1px solid #bfc1b7;">')
        for i, hcell in enumerate(headers):
            bd = 'border-left:1px solid #bfc1b7;' if i else ''
            W('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:12px;font-weight:800;color:#23251d;' + bd + '">' + rich(hcell) + '</section>')
        W('</section>')
        for ri, row in enumerate(rows):
            last = (ri == len(rows) - 1)
            W('<section style="display:flex;' + ('' if last else 'border-bottom:1px solid #bfc1b7;') + '">')
            for i, cell in enumerate(row):
                bd = 'border-left:1px solid #bfc1b7;' if i else ''
                W('<section style="width:' + str(widths[i]) + '%;padding:10px 12px;font-size:13px;color:#4d4f46;' + bd + '">' + rich(cell) + '</section>')
            W('</section>')
        W('</section>')
    else:
        # 宽表：真 table + 横滑（8 列 15 行用 flex 会在手机端挤成乱码）
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
                s += '<td style="padding:' + pad + ';border:1px solid #bfc1b7;color:#4d4f46;' + bg + '">' + rich(cell) + '</td>'
            s += '</tr>'
        s += '</tbody></table></section>'
        W(s)


# ---------- 通用库 1a 深色代码块（强调色换主题墨色） ----------
def code(lang, lines):
    s = '<section style="margin:0 0 20px;border-radius:6px;overflow:hidden;background:#23251d;border:1px solid #1e1f23;">'
    s += '<section style="display:flex;align-items:center;padding:9px 14px;background:#1e1f23;">'
    for c in ('#9ea096', '#d4c9b8', '#ed7b2f'):
        s += '<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:' + c + ';margin-right:7px;">' + blank() + '</span>'
    s += '<span style="margin-left:12px;font-size:12px;color:#9ea096;font-family:Consolas,Monaco,monospace;letter-spacing:1px;">' + leaf(lang) + '</span>'
    s += '</section><section style="padding:11px 14px;">'
    for line in lines:
        s += '<p style="margin:0;font-family:\'SF Mono\',Consolas,Monaco,monospace;font-size:13px;line-height:1.6;color:#f5f5f0;">' + leaf(line) + '</p>'
    s += '</section></section>'
    W(s)


# ---------- 组件 13 无序列表（编号变体，用于有序列表） ----------
def ol(items, small=False):
    fs = '12px' if small else '14px'
    W('<section style="margin:0 0 24px;">')
    W('<ul style="margin:0;padding-left:0;line-height:1.8;list-style-position:outside;">')
    for i, it in enumerate(items, 1):
        W('<li style="margin-bottom:10px;font-size:' + fs + ';color:#4d4f46;list-style-type:none;">')
        W('<section style="text-align:justify;">'
          '<span style="display:inline-block;background:#e5e7e0;border:1px solid #bfc1b7;color:#23251d;border-radius:4px;padding:1px 6px;font-size:11px;font-weight:800;margin-right:8px;">'
          + leaf(str(i).zfill(2)) + '</span>' + rich(it) + '</section>')
        W('</li>')
    W('</ul></section>')


# ---------- 组件 24 条目列表卡 ----------
def ul(items):
    for i, (label, desc) in enumerate(items):
        dot = '#ed7b2f' if i % 2 == 0 else '#4d4f46'
        W('<section style="margin-bottom:14px;">')
        W('<p style="margin:0 0 6px;">'
          '<span style="display:inline-block;font-size:13px;font-weight:700;color:#23251d;background:#e5e7e0;padding:3px 10px;border-radius:999px;border:1px solid #bfc1b7;">'
          '<span style="display:inline-block;width:6px;height:6px;background:' + dot + ';border-radius:50%;margin-right:5px;vertical-align:middle;overflow:hidden;font-size:0;line-height:0;">'
          + blank() + '</span>' + leaf(label) + '</span></p>')
        W('<p style="font-size:13px;color:#4d4f46;margin:0;line-height:1.7;text-align:justify;">' + rich(desc) + '</p>')
        W('</section>')


# ---------- 组件 14 编者按变体：品牌介绍卡 ----------
def signature():
    W('<section style="margin:24px 0 0;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;overflow:hidden;">')
    W('<section style="padding:10px 16px;background:#1e1f23;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;">')
    W('<p style="margin:0;font-size:10px;font-weight:800;letter-spacing:3px;color:#ffffff;">' + leaf('ABOUT') + '</p>')
    W('<span style="font-size:10px;color:rgba(255,255,255,0.65);">' + leaf('智能漫游 ｜ Neuro Nomad') + '</span>')
    W('</section>')
    W('<section style="padding:16px 18px 18px;background:#eeefe9;">')
    W('<p style="font-size:18px;font-weight:800;color:#23251d;margin:0 0 4px;">' + leaf('智能漫游') + '</p>')
    W('<p style="font-size:11px;color:#9ea096;letter-spacing:2px;margin:0 0 12px;">' + leaf('Neuro Nomad') + '</p>')
    W('<p style="font-size:13px;color:#ed7b2f;margin:0 0 8px;line-height:1.8;">' + leaf('大模型 · AI智能体 · 多模态 · 具身智能') + '</p>')
    W('<p style="font-size:14px;color:#4d4f46;margin:0;line-height:1.9;text-align:justify;">'
      + rich('聚焦[[模型原理、AI工程与推理优化实践]]。') + '</p>')
    W('</section></section>')


# ---------- 组件 28 结尾行动区 ----------
def footer_cta():
    W('''<section style="margin:24px 0 8px;background:#fdfdf8;border:1px solid #bfc1b7;border-radius:6px;padding:22px 16px;text-align:center;">
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


# ============ 复用内容装配段（与摸鱼绿版逐字相同，保证零删减） ============
_moyu = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gzh_moyu_gen.py'), encoding='utf-8').read()
body = _moyu[_moyu.index('# ================= 装配开始 ================='):]
body = body.replace('terminal-bench-v4-0_排版_摸鱼绿(moyu-green).html',
                    'terminal-bench-v4-0_排版_橄榄手记(olive-journal).html')
body = body.replace('W(FLOW_MOYU)', 'W(FLOW_OLIVE)')
_a = body.index('# ---- 签名区')
_b = body.index("''')", body.index('# ---- 组件 13a footer-cta')) + len("''')")
body = body[:_a] + 'signature()\nfooter_cta()\n' + body[_b:]
exec(compile(body, 'assembly', 'exec'), globals())
