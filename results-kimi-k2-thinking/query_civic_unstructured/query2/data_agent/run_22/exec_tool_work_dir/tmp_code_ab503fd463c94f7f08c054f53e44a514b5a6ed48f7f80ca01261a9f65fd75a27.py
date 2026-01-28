code = """import json

civic_path = var_functions.query_db_6
funding_path = var_functions.query_db_8

with open(civic_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

# Find park-related projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Park' in text and 'completed' in text.lower() and '2022' in text:
        # Extract likely project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if 'Park' in line and len(line) < 80 and 'update' not in line.lower():
                if line not in park_projects:
                    park_projects.append(line)

# Match with funding and calculate total
matched_amounts = []
for project in park_projects:
    proj = project.lower()
    for f in funding_data:
        name = f['Project_Name'].lower()
        if proj in name or name in proj:
            matched_amounts.append(int(f['Amount']))

total = sum(matched_amounts)
result = {'total': total, 'projects': len(park_projects), 'matches': len(matched_amounts)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
