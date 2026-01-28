code = """import json
c_docs = json.load(open(var_functions.query_db:60))
print('Loaded', len(c_docs), 'documents')

# Extract park projects completed in 2022
park_projects = []

for doc in c_docs:
    t = doc.get('text','')
    lines = t.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for project names with Park
        if 'Park' in line and len(line) > 10:
            # Skip headers
            if 'Subject' in line or 'Page' in line or 'Item' in line:
                continue
            if line.startswith('('):
                continue
                
            # Check next lines for completion in 2022
            next_part = '\n'.join(lines[i:i+15])
            if 'completed' in next_part.lower() and '2022' in next_part:
                park_projects.append(line)

unique = list(set(park_projects))
print('Found', len(unique), 'unique park projects')
print('Sample:', unique[:5])

# Now load funding data
funding = json.load(open(var_functions.query_db:48))

# Match projects to funding
total = 0
matches = []

for proj in unique:
    for rec in funding:
        name = rec.get('Project_Name','')
        if proj.lower() in name.lower():
            total += int(rec.get('Amount',0))
            matches.append([proj, name, int(rec.get('Amount',0))])

result = {'project_count': len(unique), 'total_funding': total, 'projects': unique, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
