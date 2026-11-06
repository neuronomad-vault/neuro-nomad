# -*- coding: utf-8 -*-
"""禅意版：删掉 4.1 的 Mermaid 源码块，去掉两处已悬空的源码指引。

一次性补丁：正文已处理过，重复运行会触发断言失败；仅作历史留档。
"""
import os
import re

p = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 'terminal-bench-v4-0',
                 'terminal-bench-v4-0_排版_留白禅意风(zen-whitespace).html')
h = open(p, encoding='utf-8').read()

# 1. 引导句：去掉「Mermaid 源码定义附在图后」
old_lead = '一次 trial 的链路如下图，Mermaid 源码定义附在图后：'
assert h.count(old_lead) == 1
h = h.replace(old_lead, '一次 trial 的链路如下图：')

# 2. 图注整行：删掉「图示与下方 Mermaid 源码定义一一对应」
cap = ('  <p style="margin:22px 0 0;font-size:12px;color:#A3A3A3;line-height:1.8;'
       'text-align:center;"><span leaf="">图示与下方 Mermaid 源码定义一一对应</span></p>\n')
assert h.count(cap) == 1
h = h.replace(cap, '')

# 3. Mermaid 源码块：从 flowchart TB 反推最近的 code section 起点，再做 section 配对
BLOCK = ('<section style="margin:0 16px 20px;border-radius:2px;overflow:hidden;'
         'background:#FAFBFA;border:1px solid #E8E8E8;border-left:2px solid #4A5D52;">')
i = h.find('flowchart TB')
assert i > 0, '未找到 Mermaid 源码'
start = h.rfind(BLOCK, 0, i)
assert start > 0
depth = 0
end = None
for m in re.finditer(r'</?section\b', h[start:]):
    depth += -1 if m.group().startswith('</') else 1
    if depth == 0:
        end = start + m.end()
        end = h.find('>', end - 1) + 1
        break
assert end and end > start
seg = h[start:end]
assert 'mermaid' in seg and 'flowchart TB' in seg and seg.count('subgraph') == 4
assert 'Agent 容器与 verifier' not in seg, '不能切到后文'

removed = len(seg) + len(cap)
h = h[:start] + h[end:]

assert 'flowchart TB' not in h and 'subgraph' not in h
assert 'Mermaid 源码定义' not in h and '一一对应' not in h
assert '一次 trial 的链路如下图：' in h
assert 'TRIAL FLOW' in h and '官方榜 35 行' in h  # 内联流程图仍在

open(p, 'w', encoding='utf-8').write(h)
print('禅意版：已删除 Mermaid 源码块 %d 字符 + 图注 %d 字符' % (len(seg), len(cap)))
print('剩余字符:', len(h), '| 合计移除:', removed)
