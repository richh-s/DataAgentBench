code = """import json

# Check what type of data we have
repo_data = var_functions.query_db:0
print('Type:', type(repo_data))
print('Value:', str(repo_data)[:500])

# Try to parse as JSON if it's a string
if isinstance(repo_data, str):
    try:
        repo_list = json.loads(repo_data)
        print('Parsed JSON list with', len(repo_list), 'items')
    except:
        # It might be a file path
        with open(repo_data, 'r') as f:
            repo_list = json.load(f)
        print('Loaded from file,', len(repo_list), 'items')
else:
    repo_list = repo_data

print('First few repos:', [r['repo_name'] for r in repo_list][:5])
print('__RESULT__:')
print(json.dumps([r['repo_name'] for r in repo_list][:5]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
