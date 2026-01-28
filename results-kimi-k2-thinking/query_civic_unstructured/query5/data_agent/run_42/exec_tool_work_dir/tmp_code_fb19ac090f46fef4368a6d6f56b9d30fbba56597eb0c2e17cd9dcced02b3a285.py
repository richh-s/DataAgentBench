code = """import json, os, sys, re
# Get the filepath from the previous query result stored in variable.
# It is under key var_functions.query_db:2.
filepath = locals().get('var_functions.query_db:2')
# If it's a filepath string, read it.
if isinstance(filepath, str) and os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
else:
    data = None
# Print result in required format
print('__RESULT__:')
print(json.dumps({'success': data is not None, 'num_docs': len(data) if data else 0}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
