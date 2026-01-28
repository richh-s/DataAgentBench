code = """import json, os

# Check what's in locals
print('Variables available:')
for key in locals().keys():
    if key.startswith('var_'):
        print(' ', key, '=', locals()[key])

# Check tmp directory
print('\nFiles in /tmp:')
for f in sorted(os.listdir('/tmp')):
    if f.endswith('.json'):
        print(' ', f)

result = {'status': 'checked'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
