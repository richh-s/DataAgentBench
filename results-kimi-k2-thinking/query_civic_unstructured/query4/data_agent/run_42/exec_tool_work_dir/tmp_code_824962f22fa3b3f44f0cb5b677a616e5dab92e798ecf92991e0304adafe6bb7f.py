code = """import json
import os

# Get file paths from the variables dictionary
all_vars = locals()
mongo_path = all_vars['var_functions.query_db:42']
funding_path = all_vars['var_functions.query_db:4']

# Load the data
with open(mongo_path) as f:
    mongo_docs = json.load(f)

with open(funding_path) as f:
    funding_recs = json.load(f)

# Build funding lookup
d = {}
for rec in funding_recs:
    d[rec['Project_Name']] = int(rec['Amount'])

# Find Spring 2022 projects
spring = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if 'Begin Construction' in line and '2022' in line:
            for j in range(i-1, max(i-8, -1), -1):
                cand = lines[j].strip()
                if cand and cand[0] != '(' and 'Schedule' not in cand:
                    if len(cand) > 5:
                        spring.add(cand)
                        break

# Match with funding
matched = [{'name': p, 'funding': d[p]} for p in spring if p in d]

count = len(matched)
total_funding = sum(m['funding'] for m in matched)

result = {'project_count': count, 'total_funding': total_funding}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
