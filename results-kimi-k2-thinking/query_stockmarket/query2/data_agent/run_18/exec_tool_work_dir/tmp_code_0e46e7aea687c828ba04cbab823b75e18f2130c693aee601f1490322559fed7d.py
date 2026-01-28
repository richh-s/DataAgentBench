code = """import json

# Check the type and value of the stored result
stored_result = var_functions.query_db:0
print('Type:', type(stored_result))
print('Value:', str(stored_result)[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
