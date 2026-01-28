code = """import json
import re
import os

# Load data files
files = os.listdir('/root/shared_data')
funding_file = None
civic_file = None
for f in files:
    if ':5.' in f:
        funding_file = f
    if ':2.' in f:
        civic_file = f

with open('/root/shared_data/' + funding_file, 'r') as f:
    funding = json.load(f)
with open('/root/shared_data/' + civic_file, 'r') as f:
    civic = json.load(f)

# Extract projects starting Spring 2022
spring_names = []
for doc in civic:
    txt = doc['text']
    if 'Spring 2022' in txt or '2022-Spring' in txt:
        lines = txt.split('\n')
        for i in range(len(lines)):
            if 'Spring 2022' in lines[i] or '2022-Spring' in lines[i]:
                for j in range(max(0, i-5), i):
                    prev = lines[j].strip()
                    if prev and len(prev) > 15 and not prev.startswith('('):
                        spring_names.append(prev)
                        break

# Match funding
total = 0
seen = set()
for fund in funding:
    fname = fund['Project_Name']
    for proj in spring_names:
        if fname in proj or proj in fname:
            if fname not in seen:
                seen.add(fname)
                total += int(fund['Amount'])
                break

count = len(seen)
print('__RESULT__:')
print(json.dumps({'count': count, 'total': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
