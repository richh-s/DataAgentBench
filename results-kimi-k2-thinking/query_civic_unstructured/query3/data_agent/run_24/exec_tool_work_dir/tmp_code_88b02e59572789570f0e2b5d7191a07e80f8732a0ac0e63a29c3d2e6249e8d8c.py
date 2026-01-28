code = """import json

funding_file = var_functions.query_db:18
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Records:', len(funding_data))
print('First record:', funding_data[0] if funding_data else 'None')

fema_projects = []
for rec in funding_data:
    name_lower = rec['Project_Name'].lower()
    if 'fema' in name_lower or 'emergency' in name_lower:
        fema_projects.append(rec)

print('FEMA/Emergency count:', len(fema_projects))
result = fema_projects
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
