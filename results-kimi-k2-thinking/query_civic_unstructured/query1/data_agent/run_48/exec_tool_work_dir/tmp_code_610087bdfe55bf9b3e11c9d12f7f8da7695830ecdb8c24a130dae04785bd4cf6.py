code = """import json
f1 = open(var_functions.query_db:0)
funding = json.load(f1)
f1.close()

f2 = open(var_functions.query_db:2)
docs = json.load(f2)
f2.close()

high_funding = []
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding.append(r['Project_Name'])

projects = []
for doc in docs:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    section = text[start+37:]
    end = len(section)
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        pos = section.find(marker)
        if pos > 0 and pos < end:
            end = pos
    section = section[:end]
    blocks = section.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 10:
            first_line = block.split('\n')[0].strip()
            if len(first_line) > 10 and not first_line.isupper():
                projects.append(first_line)

import re
matched = 0
for p in projects:
    p_lower = p.lower()
    for f in high_funding:
        f_lower = f.lower()
        if p_lower == f_lower or p in f or f in p:
            matched += 1
            break
        p_words = set(p_lower.split())
        f_words = set(f_lower.split())
        if len(p_words) >= 2 and len(f_words) >= 2 and len(p_words & f_words) >= 2:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}]}

exec(code, env_args)
