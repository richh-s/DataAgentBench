code = """import os, glob, json

print('Files in /tmp:')
files = glob.glob('/tmp/tmp*.json')
for f in files:
    print('  ', f, os.path.getsize(f), 'bytes')

print('\nAll files in /tmp:')
all_files = [f for f in os.listdir('/tmp') if not f.startswith('.')]
all_files.sort()
for f in all_files[:20]:
    print('  ', f)

print('__RESULT__:')
print(json.dumps({'count': len(files)}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.list_db:2': ['commits', 'contents', 'files'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'count': 0, 'first_five': []}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
