code = """import json
import re

# Access the funding data - it should be stored as a variable
funding_data = var_functions_query_db_5

# Filter for FEMA or emergency related projects
fema_projects = []
for row in funding_data:
    project_name = row.get('Project_Name', '').lower()
    if 'fema' in project_name or 'emergency' in project_name or 'warning' in project_name:
        fema_projects.append(row)

print('__RESULT__:')
print(json.dumps(fema_projects[:20]))  # Return first 20 to check"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_storage_key': 'var_functions.query_db:5', 'civic_docs_storage_key': 'var_functions.query_db:8'}}

exec(code, env_args)
