code = """import json, os

# Check what variables we have
vars_list = [k for k in locals().keys() if k.startswith('var_')]
print('Variables starting with var_:', vars_list)

# Check if files exist
tmp_files = os.listdir('/tmp')
json_files = [f for f in tmp_files if f.endswith('.json')]
print('JSON files in /tmp:', json_files)

# Try to load one of the files if it exists
if json_files:
    test_file = os.path.join('/tmp', json_files[0])
    try:
        with open(test_file, 'r') as f:
            data = json.load(f)
        print('Loaded test file with', len(data), 'records')
    except Exception as e:
        print('Error loading file:', e)

result = {'status': 'checked'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
