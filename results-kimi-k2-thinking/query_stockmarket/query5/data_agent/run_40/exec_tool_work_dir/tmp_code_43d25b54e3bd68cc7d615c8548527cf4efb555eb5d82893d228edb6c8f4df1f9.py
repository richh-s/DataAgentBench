code = """import json

# Load companies data from previous query
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    companies_data = json.load(f)

print('__RESULT__:')
print(json.dumps({'total_companies': len(companies_data), 'sample': companies_data[:3]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
