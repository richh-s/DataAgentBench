code = """import json

funding_file = var_functions.query_db:0
civic_file = var_functions.query_db:2

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
    docs = json.load(f)

print('Funding rows:', len(funding))
print('Civic docs:', len(docs))

# Extract project names from civic docs
project_names = []
for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) > 10 and 'road' in line.lower():
            project_names.append(line)

project_names = list(set(project_names))
print('Project name candidates:', len(project_names))

# Count matches
matches = 0
for proj in project_names:
    proj_l = proj.lower()
    for f in funding:
        if int(f['Amount']) > 50000:
            if proj_l in f['Project_Name'].lower():
                matches += 1
                break

print('Matches:', matches)
print('__RESULT__:')
print(json.dumps({'count': matches}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
