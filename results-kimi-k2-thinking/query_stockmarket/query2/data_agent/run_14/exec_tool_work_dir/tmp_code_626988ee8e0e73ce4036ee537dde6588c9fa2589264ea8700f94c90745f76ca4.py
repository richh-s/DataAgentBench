code = """import json

# The result is stored as a file path, let's check what it is
result_file = var_functions.query_db:0
print('__RESULT__:')
print(json.dumps(str(result_file)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
