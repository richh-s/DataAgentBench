code = """import json

# Load data through direct assignment
with open('var_functions.query_db:0') as f:
    funding = json.load(f)

with open('var_functions.query_db:20') as f:
    docs = json.load(f)

# Build funded lookup
funded = {}
for rec in funding:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Extract design projects from first document
text = docs[0]['text']
section = text.split('Capital Improvement Projects (Design)')[1].split('Capital Improvement Projects (Construction)')[0]

projects = []
for line in section.split('\n'):
    line = line.strip()
    if line and len(line) > 5 and '▪' not in line:
        if 'Updates:' not in line and 'Project Schedule:' not in line:
            if 'Capital Improvement' not in line and 'Page' not in line:
                projects.append(line.lower())

# Count matches
count = 0
seen = set()
for p in projects:
    if p not in seen:
        seen.add(p)
        if p in funded and funded[p] > 50000:
            count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:54': 0}

exec(code, env_args)
