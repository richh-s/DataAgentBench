code = """import json
civics = var_functions.query_db:2
funds = var_functions.query_db:5
result = {'civic_type': str(type(civics)), 'funding_type': str(type(funds))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
