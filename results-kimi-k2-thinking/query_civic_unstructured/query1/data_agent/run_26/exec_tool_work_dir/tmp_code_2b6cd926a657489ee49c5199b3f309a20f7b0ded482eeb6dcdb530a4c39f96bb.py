code = """import json

# Load data
with open('var_functions.query_db:0', 'r') as f:
    funding = json.load(f)

with open('var_functions.query_db:2', 'r') as f:
    docs = json.load(f)

# Create funding lookup
funded = {}
for rec in funding:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Find design projects
design = []
for doc in docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[1]
        section = section.split('Capital Improvement Projects (Construction)')[0]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 5:
                if '▪' not in line and 'Updates:' not in line:
                    if 'Project Schedule:' not in line and 'Page' not in line:
                        if 'Capital Improvement' not in line:
                            design.append(line.lower())

count = 0
for p in design:
    if p in funded and funded[p] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
