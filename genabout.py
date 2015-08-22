#!/usr/bin/python

import sys, markdown

save = False
replace = None
for arg in sys.argv:
    if arg == '--save':
        save = True
    elif arg == '--replace':
        replace = sys.argv[sys.argv.index(arg)+1]

with open('Contributors', 'r') as f:
    converted = markdown.markdown(f.read())

if save:
    with open('Contributors.html', 'w') as f:
        f.write(converted)
elif replace:
    with open(replace, 'r') as f:
        content = f.read()
    with open(replace.replace('.in', ''), 'w') as f:
        f.write(content.replace('@CONTRIBUTORS@', converted))
else:
    print(converted)
