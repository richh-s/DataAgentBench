code = """import json

# The result is stored as a string path to JSON file
result_file = '/home/user/vb_share/temp_result_53.json'
print('__RESULT__:')
print(result_file)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
