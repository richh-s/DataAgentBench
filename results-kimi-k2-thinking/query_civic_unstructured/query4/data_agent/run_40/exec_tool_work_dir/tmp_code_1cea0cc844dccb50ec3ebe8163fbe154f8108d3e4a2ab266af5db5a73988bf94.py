code = """import json
import re
import os

with open('/root/shared_data/var_functions.query_db:5.json', 'r') as f:
    funding = json.load(f)
with open('/root/shared_data/var_functions.query_db:2.json', 'r') as f:
    civic = json.load(f)

print('Loaded', len(funding), 'funding records and', len(civic), 'documents')

spring_2022_ids = set()
project_candidates = []

for doc in civic:
    txt = doc['text']
    if 'Spring 2022' in txt or '2022-Spring' in txt:
        # Extract project name from text structure
        lines = txt.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look backwards up to 5 lines
                start_idx = max(0, i-5)
                for j in range(start_idx, i):
                    candidate = lines[j].strip()
                    if candidate and len(candidate) > 10 and not candidate.startswith('('):
                        project_candidates.append(candidate)
                        break
                break

print('Found', len(project_candidates), 'candidate projects')

# Match with funding
total_amt = 0
matched_projects = set()

for fund in funding:
    fund_name = fund['Project_Name']
    for proj in project_candidates:
        # If either name contains the other
        if (fund_name in proj or proj in fund_name):
            if fund_name not in matched_projects:
                matched_projects.add(fund_name)
                total_amt += int(fund['Amount'])
                break

result = {'project_count': len(matched_projects), 'total_funding': total_amt}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
