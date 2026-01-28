code = """import json, re

# Load data
c_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
f_records = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Docs:', len(c_docs), 'Records:', len(f_records))

# Process the data
projects_2022 = []
park_projects = []

for doc in c_docs:
    text = doc.get('text', '')
    
    # Simple parsing approach
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        # Look for completed projects in 2022
        if '2022' in line and 'completed' in line.lower():
            if 'park' in line.lower():
                projects_2022.append(line.strip())
        
        # Look for park-related completed projects
        if 'completed' in line.lower() and 'park' in line.lower():
            if '2022' in line or '2022' in text:
                park_projects.append(line.strip())

print('Found 2022 projects:', len(projects_2022))
print('Found park projects:', len(park_projects))

__RESULT__:
print(json.dumps({'status': 'loaded', 'civic_docs': len(c_docs), 'funding': len(f_records)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
