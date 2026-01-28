code = """import json

# The variable should contain the file path
file_path = var_functions.query_db:0
print('__RESULT__:')
print(json.dumps(str(file_path)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
