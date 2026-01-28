code = """import json

# Load the data
var_funding = locals()['var_functions.query_db:6']
if isinstance(var_funding, str):
    with open(var_funding) as f:
        funding_data = json.load(f)
else:
    funding_data = var_funding

# Check which projects have funding > 50000
high_funding = []
for f in funding_data:
    if int(f['Amount']) > 50000:
        high_funding.append(f['Project_Name'])

print('__RESULT__:')
print(json.dumps(high_funding[:50]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:22': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
