code = """import json
local_vars = locals()
mongo_file_path = local_vars['var_functions.query_db:2']

# Read the file
with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

print('__RESULT__:')
print(json.dumps(f"Loaded {len(mongo_data)} documents from MongoDB"))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']"}

exec(code, env_args)
