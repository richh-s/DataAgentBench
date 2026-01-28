code = """import json
funding_data = json.load(open(locals()['var_functions.query_db:2']))
docs_data = json.load(open(locals()['var_functions.query_db:0']))

results = []
for rec in funding_data:
    pn = rec['Project_Name'].lower()
    if 'emergency' in pn or 'fema' in pn:
        results.append({
            'Project_Name': rec['Project_Name'],
            'Funding_Source': rec['Funding_Source'],
            'Amount': int(rec['Amount']),
            'Status': 'not started',
            'Type': 'disaster' if 'fema' in pn else 'capital'
        })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'docs_type': "<class 'str'>"}, 'var_functions.execute_python:34': {'funding_count': 500, 'docs_count': 5}}

exec(code, env_args)
