import ast
import json

lines = []
with open('app.txt') as f:
    lines = f.readlines()

key = ''
value = ''
pairs = []
for line in lines:
    if ':' in line:
        key = line.split(':')[-1].strip()

    elif line.strip().startswith('[') and line.strip().endswith(']'):
        value = line.strip()[1:-1]
        pairs.append((key, ast.literal_eval('[' + value + ']')))
        key, value = '', ''

    elif line.startswith('  '):
        value += line

    elif line.strip() == ']':
        pairs.append((key, ast.literal_eval('[' + value + ']')))
        key, value = '', ''

metadata = {}
for token, scope in pairs:
    if token == '': continue
    if 'punctuation.definition.comment.java' in scope or 'comment.block.javadoc.java' in scope or 'comment.line.double-slash.java' in scope: continue

with open('metadata.json', 'w') as f:
    json.dump(metadata, f, indent=4)
