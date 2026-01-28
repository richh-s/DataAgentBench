code = """import json

# Load civic documents
civic_docs_file = var_functions.query_db:60
with open(civic_docs_file) as f:
    civic_docs = json.load(f)

# Load funding data
funding_file = var_functions.query_db:48
with open(funding_file) as f:
    funding = json.load(f)

park_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Park' in line and len(line) > 10:
            if 'Subject' not in line and 'Page' not in line and 'Item' not in line:
                if not line.startswith('('):
                    next_part = '\n'.join(lines[i:i+15])
                    if 'completed' in next_part.lower() and '2022' in next_part:
                        park_projects.append(line)

unique = list(set(park_projects))

total_funding = 0
matches = []

for proj in unique:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() in name.lower():
            amount = int(rec.get('Amount',0))
            total_funding += amount
            matches.append([proj, name, amount])

result = {'count': len(unique), 'total_funding': total_funding, 'projects': unique, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
