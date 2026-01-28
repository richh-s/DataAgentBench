code = """import json

# Check what variables are available
available_vars = [k for k in locals().keys() if k.startswith('var_')]
print('Available vars:', available_vars)

# Try different approaches to access data
if 'var_functions.query_db:2' in locals():
    citations_file = locals()['var_functions.query_db:2']
    print('Found citations file:', citations_file)
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
    print('Citations loaded, count:', len(citations_data))
else:
    print('var_functions.query_db:2 not found in locals')

# Try accessing via globals
if 'var_functions.query_db:2' in globals():
    print('Found in globals')

# List all local variables
for k, v in locals().items():
    if 'query_db' in k:
        print(k, type(v), str(v)[:100])"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
