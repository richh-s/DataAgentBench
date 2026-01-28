code = """import json

# Load the result from the first query
with open(var_functions.query_db:0, 'r') as f:
    nyse_arca_etfs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'count': len(nyse_arca_etfs),
    'sample': nyse_arca_etfs[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
