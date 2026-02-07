# -*- coding: utf-8 -*-
"""Add UTF-8 BOM to all .md files (so VS etc. detect UTF-8). Skips Library, .git."""
import os

BOM = b'\xef\xbb\xbf'
root = os.path.dirname(os.path.abspath(__file__))
SKIP_DIRS = {'Library', '.git', 'node_modules'}
count = 0
for dirpath, dirnames, filenames in os.walk(root):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for name in filenames:
        if not name.lower().endswith('.md'):
            continue
        path = os.path.join(dirpath, name)
        with open(path, 'rb') as f:
            raw = f.read()
        if raw.startswith(BOM):
            continue
        with open(path, 'wb') as f:
            f.write(BOM + raw)
        count += 1
        print('BOM added:', path)
print('Done. %d file(s) updated.' % count)
