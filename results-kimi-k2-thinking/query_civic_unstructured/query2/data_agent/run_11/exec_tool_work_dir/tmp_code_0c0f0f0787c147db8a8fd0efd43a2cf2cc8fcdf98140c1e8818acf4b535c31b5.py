code = """import json

# Load civic documents
civic_path = var_functions.query_db:60
with open(civic_path) as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = var_functions.query_db:48
with open(funding_path) as f:
    funding = json.load(f)

park_projects = []

# Find park projects
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.split('\n')
    for i,line in enumerate(lines):
        line = line.strip()
        if 'Park' in line and len(line)>10:
            if 'Subject' not in line and 'Page' not in line and 'Item' not in line:
                if not line.startswith('('):
                    next_section = '\n'.join(lines[i:i+15])
                    if 'completed' in next_section.lower() and '2022' in next_section:
                        park_projects.append(line)

unique_parks = list(set(park_projects))

# Calculate funding
total = 0
matches = []

for proj in unique_parks:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() in name.lower():
            amt = int(rec.get('Amount',0))
            total += amt
            matches.append([proj, name, amt])

print('__RESULT__:')
print(json.dumps({'count':len(unique_parks),'funding':total,'projects':unique_parks,'matches':matches}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
