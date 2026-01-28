code = """import json, re

# Load data
cdocs = json.load(open('/tmp/tmp7.json'))
fdocs = json.load(open('/tmp/tmp8.json'))

# Build funding dict
funding = {}
for r in fdocs:
    funding[r['Project_Name']] = funding.get(r['Project_Name'], 0) + int(r['Amount'])

# Find 2022 projects
proj2022 = []
for doc in cdocs:
    t = doc.get('text', '')
    for ln in t.split('\n'):
        ln = ln.strip()
        if '2022' in ln and len(ln) > 10:
            proj2022.append(ln)

# Deduplicate
unique = list(dict.fromkeys(proj2022))

# Match with funding
count = 0
total = 0

for p in unique:
    if p in funding:
        count += 1
        total += funding[p]

# Add funding records 2022
for name, amt in funding.items():
    if '2022' in name and ('Morning View' in name or 'Annual' in name):
        count += 1
        total += amt

result = {'count': count, 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': 'file_storage/functions.query_db:55.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:61': 'file_storage/functions.query_db:61.json', 'var_functions.query_db:82': 'file_storage/functions.query_db:82.json', 'var_functions.query_db:83': 'file_storage/functions.query_db:83.json'}

exec(code, env_args)
