code = """import json, os
print('Starting')

# Check all variables in global scope
all_vars = list(globals().keys())
print('Variables starting with var:')
for key in all_vars:
    if str(key).startswith('var_'):
        print(key)

# Let's look for files that might contain our data
for fname in os.listdir('.'):
    if 'functions' in fname and fname.endswith('.json'):
        print('Found file:', fname)

print('Done')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
