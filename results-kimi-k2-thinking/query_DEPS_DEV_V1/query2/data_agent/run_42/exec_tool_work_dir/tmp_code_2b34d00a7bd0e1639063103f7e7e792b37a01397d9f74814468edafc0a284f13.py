code = """import json

# Read the file path from storage
file_path = var_functions.query_db:2

# Try to read the data
with open(file_path, 'r') as f:
    data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'file_path': file_path,
    'record_count': len(data),
    'sample_record': data[0] if data else None
}))"""

env_args = {'var_functions.list_db:0': ['packageinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
