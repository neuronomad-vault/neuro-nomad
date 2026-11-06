# -*- coding: utf-8 -*-
"""兼容入口：Humanity's Last Exam 橄榄手记版已迁到 gzh/ 包。

等价命令：
    python3 -m gzh.cli build hle --theme olive-hle
"""
from gzh.cli import main

if __name__ == '__main__':
    main(['build', 'hle', '--theme', 'olive-hle'])
