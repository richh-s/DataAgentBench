code = """import json

funding = locals()['var_functions.query_db:2']
docs = locals()['var_functions.query_db:0']

results = []

for record in funding:
    name = record['Project_Name'].lower()
    if 'emergency' in name or 'fema' in name:
        results.append({
            'Project_Name': record['Project_Name'],
            'Funding_Source': record['Funding_Source'],
            'Amount': record['Amount']
        })

print('Total emergency projects:', len(results))
for r in results:
    print(json.dumps(r))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
