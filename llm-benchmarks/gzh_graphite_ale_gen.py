# -*- coding: utf-8 -*-
"""兼容入口：ALE 石墨极简版的构建逻辑已迁到 gzh/ 包。

等价命令：
    python3 -m gzh.cli build agents-last-exam --theme graphite
"""
from gzh.cli import main

if __name__ == '__main__':
    main(['build', 'agents-last-exam', '--theme', 'graphite'])
