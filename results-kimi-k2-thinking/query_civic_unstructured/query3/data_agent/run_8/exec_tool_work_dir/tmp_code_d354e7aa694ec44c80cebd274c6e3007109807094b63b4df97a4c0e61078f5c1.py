code = """import json
import re

# Access the stored data using the correct variable names
funding_data = locals()['var_functions.query_db:5']
civic_docs = locals()['var_functions.query_db:8']

# Filter funding data for FEMA/emergency projects
fema_funding = []
for row in funding_data:
    project_name = row.get('Project_Name', '').lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_funding.append(row)

print('__RESULT__:')
print(json.dumps({
    'fema_funding_count': len(fema_funding),
    'sample_funding': fema_funding[:15]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_storage_key': 'var_functions.query_db:5', 'civic_docs_storage_key': 'var_functions.query_db:8'}, 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', '__builtins__', 'json', 're'], 'var_functions.execute_python:26': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.query_db:8', 'var_functions.execute_python:12', 'var_functions.execute_python:20']}

exec(code, env_args)
