code = """import json, re

# Load funding data
f1 = var_functions.query_db:0
f2 = var_functions.query_db:2

with open(f1, 'r') as f:
    funding = json.load(f)

with open(f2, 'r') as f:
    docs = json.load(f)

# Build funding lookup
funded = {}
for rec in funding:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Extract design capital projects
design = []
for doc in docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        design_part = parts[1].split('Capital Improvement Projects (Construction)')[0]
        for line in design_part.split('\n'):
            line = line.strip()
            if line and len(line) > 5 and '▪' not in line and 'Updates:' not in line and 'Page' not in line and 'Capital Improvement' not in line:
                design.append(line.lower())

# Count matches
count = 0
for proj in design:
    if proj in funded and funded[proj] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
