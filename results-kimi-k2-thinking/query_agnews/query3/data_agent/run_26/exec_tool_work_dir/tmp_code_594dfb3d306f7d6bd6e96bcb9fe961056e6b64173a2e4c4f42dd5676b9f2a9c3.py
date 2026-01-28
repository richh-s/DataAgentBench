code = """import json

# Open the file - the result should be a file path
result = var_functions.query_db:2
metadata_path = result

with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

# Show basic info
print('__RESULT__:')
print(json.dumps('Loaded {} records'.format(len(metadata_records))))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
