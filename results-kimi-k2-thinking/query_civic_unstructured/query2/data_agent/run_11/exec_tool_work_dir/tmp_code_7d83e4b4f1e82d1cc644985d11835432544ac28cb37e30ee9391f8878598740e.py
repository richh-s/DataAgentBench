code = """import json, re

# Load data files
civic_docs = json.load(open(var_functions.query_db:5))
funding = json.load(open(var_functions.query_db:6))

park_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    if all(x in text for x in ['Park','2022']) and 'completed' in text.lower():
        for line in text.split('\n'):
            line = line.strip()
            if 'Park' in line and len(line)>5 and not line.startswith('('):
                if 'Subject' not in line and 'Page' not in line and 'Item' not in line:
                    park_projects.append(line)

unique_parks = list(set(park_projects))

# Find funding
total = 0
matches = []

for proj in unique_parks:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() == name.lower() or proj.lower() in name.lower():
            total += int(rec.get('Amount',0))
            matches.append({'project':proj,'match':name,'amount':int(rec.get('Amount',0))})

print('__RESULT__:')
print(json.dumps({'projects':unique_parks,'count':len(unique_parks),'total_funding':total,'matches':matches}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
