code = """import json, re

# Load the civic documents file
civic_docs_file = var_functions.query_db:5
if isinstance(civic_docs_file, str):
    with open(civic_docs_file) as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_file

# Load the funding file
funding_file = var_functions.query_db:6
if isinstance(funding_file, str):
    with open(funding_file) as f2:
        funding = json.load(f2)
else:
    funding = funding_file

park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if 'Park' in line and len(line) > 5 and not line.startswith('('):
            # Skip headers
            if 'Subject' in line or 'Page' in line or 'Item' in line:
                continue
            
            # Check following lines for 2022 completion
            next_part = ' '.join(lines[i:i+10])
            if 'completed' in next_part.lower() and '2022' in next_part:
                park_projects.append(line)

unique_parks = list(set(park_projects))

# Calculate funding
funding_total = 0
matches = []

for proj in unique_parks:
    for rec in funding:
        name = rec.get('Project_Name', '')
        if proj.lower() == name.lower() or proj.lower() in name.lower():
            funding_total += int(rec.get('Amount', 0))
            matches.append({'project': proj, 'match': name, 'amount': int(rec.get('Amount', 0))})

result = {
    'projects': unique_parks,
    'count': len(unique_parks),
    'total_funding': funding_total,
    'funding_matches': matches
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
