code = """import os
import glob

# Check what files exist in the environment
print('Current directory:', os.getcwd())
print('Files in current directory:')
for f in glob.glob('*'):
    print(f'  - {f}')

print('\nData directory:')
if os.path.exists('data'):
    for f in glob.glob('data/*'):
        print(f'  - {f}')
else:
    print('  No data directory found')

print('\n/tmp directory:')
for f in glob.glob('/tmp/*'):
    print(f'  - {f}')

print('__RESULT__:')
print(json.dumps({'status': 'checked'}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs']}

exec(code, env_args)
