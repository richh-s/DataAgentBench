code = """import json

with open('civic_docs.json', 'w') as f:
    json.dump({'message': 'test'}, f)

print('__RESULT__:')
print('test complete')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
