code = """import json

# Load the data
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

with open('var_functions.query_db:2', 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup
funded = {}
for rec in funding_data:
    funded[rec['Project_Name'].lower()] = int(rec['Amount'])

# Extract design capital projects
design_capital = []
for doc in civic_docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        section = text.split('Capital Improvement Projects (Design)')[-1].split('Capital Improvement Projects (Construction)')[0]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 5 and 'Updates:' not in line and 'Project Schedule:' not in line:
                design_capital.append(line.lower())

# Count projects with funding > $50,000
count = 0
for project in set(design_capital):
    if project in funded and funded[project] > 50000:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
