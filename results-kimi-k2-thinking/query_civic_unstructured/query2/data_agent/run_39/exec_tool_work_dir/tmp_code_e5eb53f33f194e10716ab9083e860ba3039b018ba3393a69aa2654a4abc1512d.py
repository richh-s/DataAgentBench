code = """import json
import re

mongo_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Find park projects completed in 2022 from MongoDB
park_projects_2022 = []

for doc in mongo_docs:
    text = doc.get('text', '')
    # Simple search for park projects completed in 2022
    if 'park' in text.lower() and 'completed' in text.lower() and '2022' in text:
        # Extract lines that mention completion in 2022
        for line in text.split('\n'):
            line_lower = line.lower()
            if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
                # Extract the project name (usually previous line)
                park_projects_2022.append(line.strip())

# Get funding for these projects
total_funding = 0
for record in funding_records:
    proj_name = record.get('Project_Name', '')
    for park_proj in park_projects_2022:
        if proj_name.lower() in park_proj.lower() or park_proj.lower() in proj_name.lower():
            total_funding += int(record.get('Amount', 0))

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'projects_found': len(park_projects_2022)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
