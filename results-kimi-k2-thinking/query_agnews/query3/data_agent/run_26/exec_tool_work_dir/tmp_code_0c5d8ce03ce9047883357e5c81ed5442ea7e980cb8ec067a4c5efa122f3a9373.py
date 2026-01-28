code = """import json

# Access the stored result
metadata_path = locals()['var_functions.query_db:2']

# Load the JSON file
with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

# Show basic info
print('__RESULT__:')
print(json.dumps({
    'total_records': len(metadata_records)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
