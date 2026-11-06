# -*- coding: utf-8 -*-
"""兼容入口：Terminal-Bench 橄榄手记版已迁到 gzh/ 包。

等价命令：
    python3 -m gzh.cli build terminal-bench-v4-0 --theme olive
"""
from gzh.cli import main

if __name__ == '__main__':
    main(['build', 'terminal-bench-v4-0', '--theme', 'olive'])
