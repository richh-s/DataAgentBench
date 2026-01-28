code = """import json, re

# Load data from stored results
civic_docs = json.loads(var_functions_query_db_5)
funding = json.loads(var_functions_query_db_6)

# Find FEMA/emergency projects
projects = []
for f in funding:
    name = f['Project_Name']
    if 'FEMA' in name.upper() or 'EMERGENCY' in name.upper():
        projects.append({
            'Project_Name': name,
            'Funding_Source': f['Funding_Source'],
            'Amount': int(f['Amount'])
        })

print('Projects found:', len(projects))
for p in projects[:10]:
    print('-', p['Project_Name'])

# Output as JSON
result = json.dumps(projects, indent=2)
print(result[:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
