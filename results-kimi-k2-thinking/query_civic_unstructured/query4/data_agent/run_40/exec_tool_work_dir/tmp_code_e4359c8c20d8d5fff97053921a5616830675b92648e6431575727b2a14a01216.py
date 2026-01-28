code = """import json
import re
import os

funding_file = '/root/shared_data/var_functions.query_db:5.json'
civic_file = '/root/shared_data/var_functions.query_db:2.json'

with open(funding_file, 'r') as f:
    funding = json.load(f)
with open(civic_file, 'r') as f:
    civic = json.load(f)

spring_projects = []
for doc in civic:
    txt = doc['text']
    if 'Spring 2022' in txt or '2022-Spring' in txt:
        lines = txt.split('\n')
        for i in range(len(lines)):
            curr = lines[i]
            if 'Spring 2022' in curr or '2022-Spring' in curr:
                for j in range(max(0,i-5), i):
                    line = lines[j].strip()
                    if line and len(line) > 15 and not line.startswith('('):
                        spring_projects.append(line)
                        break

matched = set()
total = 0
for fund in funding:
    name = fund['Project_Name']
    amt = int(fund['Amount'])
    for proj in spring_projects:
        if name in proj or proj in name:
            if name not in matched:
                matched.add(name)
                total += amt
                break

count = len(matched)
output = {"project_count": count, "total_funding": total}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
