code = """import json, re

# Get data from storage
civic = locals()['var_functions.query_db:8']
funding = locals()['var_functions.query_db:10']

# Show first few items
print('Civic docs first 2 items:', json.dumps(civic[:2])[:200])
print('Funding first 2 items:', json.dumps(funding[:2])[:200])

# Build lookup
lookup = {}
for item in funding:
    key = item['Project_Name'].lower().replace(' ', '')
    lookup[key] = int(item['Amount'])

# Check for park projects in 2022
total = 0
projects = []

# Look for Bluffs Park
if 'bluffsparkshadestructure' in lookup:
    total += lookup['bluffsparkshadestructure']
    projects.append({'project': 'Bluffs Park Shade Structure', 'amount': lookup['bluffsparkshadestructure']})

print('__RESULT__:')
print(json.dumps({'total': total, 'projects': projects}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs'], 'var_functions.execute_python:52': {'debug': 'done'}, 'var_functions.execute_python:54': {'status': 'debug'}, 'var_functions.execute_python:58': {'status': 'debug_info_recorded'}}

exec(code, env_args)
