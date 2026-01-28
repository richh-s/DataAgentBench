code = """import json
import os

print('=== DEBUG: All available variables ===')

# Check what variables are actually available
available_vars = sorted([name for name in dir() if not name.startswith('__')])
print('Available variables:', available_vars)

# Look for query_db related variables
query_vars = [v for v in available_vars if 'query_db' in v]
print('Query DB variables:', query_vars)

# Try to find the correct variable names
for var_name in query_vars:
    var_value = locals()[var_name]
    print(f'{var_name} = {var_value}')

# Also check if there are JSON files in current directory
json_files = [f for f in os.listdir('.') if f.endswith('.json')]
print('JSON files in current directory:', json_files)

# Check storage directory
if os.path.exists('storage'):
    storage_files = [f for f in os.listdir('storage') if f.endswith('.json')]
    print('JSON files in storage:', storage_files)
else:
    print('No storage directory found')

result = {'debug': 'complete'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:96': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:100': {'status': 'debug_complete'}, 'var_functions.query_db:102': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}], 'var_functions.query_db:104': 'file_storage/functions.query_db:104.json', 'var_functions.query_db:110': 'file_storage/functions.query_db:110.json'}

exec(code, env_args)
