code = """import json

# Load the result from the previous query
with open('var_functions.query_db:0', 'r') as f:
    companies_data = json.load(f)

print('__RESULT__:')
print(json.dumps({'count': len(companies_data), 'sample': companies_data[:3]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
