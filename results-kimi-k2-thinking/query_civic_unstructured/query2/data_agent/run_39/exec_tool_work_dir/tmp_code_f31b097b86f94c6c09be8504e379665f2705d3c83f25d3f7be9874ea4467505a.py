code = """import json
import re

mongo_file_path = locals()['var_functions.query_db:2']
funding_file_path = locals()['var_functions.query_db:5']

with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

park_projects = []

for doc in mongo_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Skip headers - check each pattern separately
        if line.startswith('Page') or line.startswith('Agenda Item'):
            continue
        if line.startswith('To:') or line.startswith('Prepared by:') or line.startswith('Approved by:'):
            continue
        if line.startswith('Subject:') or line.startswith('RECOMMENDED ACTION:') or line.startswith('DISCUSSION:'):
            continue
        if line.startswith('Date prepared:') or line.startswith('Meeting date:'):
            continue
        if line.startswith('Public Works') or line.startswith('Commission'):
            continue
        if line.startswith('Capital Improvement Projects') or '(cid:' in line:
            continue
            
        # Look for project names
        if 5 < len(line) < 200 and not line.endswith(':'):
            # Check ahead for completion info
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip().lower()
                if 'completed' in next_line and '2022' in next_line:
                    # Check if this is a park project
                    if 'park' in line.lower():
                        park_projects.append(line)
                    break

park_projects = list(set(park_projects))

result = {'projects': park_projects, 'count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
