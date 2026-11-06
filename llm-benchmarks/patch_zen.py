# -*- coding: utf-8 -*-
"""禅意版：移除「09 附：快照与入库边界」整节，参考来源编号 10 -> 09。

一次性补丁：正文已处理过，重复运行会触发断言失败；仅作历史留档。
"""
import os

p = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 'terminal-bench-v4-0_排版_留白禅意风(zen-whitespace).html')
h = open(p, encoding='utf-8').read()

SEP = '<section style="padding:0 16px;"><section style="height:1px;background:#E8E8E8;margin:64px 0 0;">'
HEAD = '<section style="margin-top:64px;margin-bottom:32px;padding:0 16px;">'

a = h.find('09 · APPENDIX')
b = h.find('10 · SOURCES')
assert a > 0 and b > a, '标题定位失败'
start = h.rfind(SEP, 0, a)          # 附节前的细线分隔符
end = h.rfind(SEP, 0, b)            # 参考来源前的细线分隔符，保留
assert start > 0 and end > start
seg = h[start:end]
assert '附：快照与入库边界' in seg
assert seg.count(HEAD) == 1, '删除区间应只含一个章节标题块'
assert '10 · SOURCES' not in seg, '不能切到参考来源章节'

h2 = h[:start] + h[end:]
assert h2.count('10 · SOURCES') == 1
h2 = h2.replace('10 · SOURCES', '09 · SOURCES')
assert '09 · APPENDIX' not in h2 and '附：快照与入库边界' not in h2
assert '09 · SOURCES' in h2

open(p, 'w', encoding='utf-8').write(h2)
print('禅意版：已删除附节 %d 字符；参考来源编号 10 -> 09' % len(seg))
print('剩余字符:', len(h2))
