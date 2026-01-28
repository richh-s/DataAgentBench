code = """import json, re

# Load civic documents
civic_path = var_functions.query_db:60
with open(civic_path) as f:
    civic_docs = json.load(f)

# Look for park projects completed in 2022
park_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for project names with Park
        if 'Park' in line and len(line) > 10:
            # Skip headers
            if 'Subject' in line or 'Page' in line or 'Item' in line:
                continue
            if line.startswith('('):
                continue
            
            # Check following context for completion in 2022
            context = ' '.join(lines[i:i+15])
            if 'completed' in context.lower() and '2022' in context:
                park_projects.add(line)

# Convert to list
unique_projects = list(park_projects)

# Load funding data
funding_path = var_functions.query_db:48
with open(funding_path) as f:
    funding = json.load(f)

# Match with funding
total_funding = 0
matches = []

for proj in unique_projects:
    for rec in funding:
        name = rec.get('Project_Name', '')
        if proj.lower() in name.lower():
            amt = int(rec.get('Amount', 0))
            total_funding += amt
            matches.append([proj, name, amt])

result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
