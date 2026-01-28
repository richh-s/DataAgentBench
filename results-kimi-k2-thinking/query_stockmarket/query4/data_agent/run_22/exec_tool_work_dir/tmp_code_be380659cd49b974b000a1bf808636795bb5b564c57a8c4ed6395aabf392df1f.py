code = """import json

# Debug - see what type of data we have
query_result = var_functions.query_db:10
print('__RESULT__:')
print(json.dumps({"type": str(type(query_result)), "value": str(query_result)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
