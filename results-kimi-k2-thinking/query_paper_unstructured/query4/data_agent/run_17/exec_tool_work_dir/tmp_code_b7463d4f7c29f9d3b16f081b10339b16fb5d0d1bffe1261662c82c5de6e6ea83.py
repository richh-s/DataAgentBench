code = """import os
print('Files in /tmp directory:')
for filename in os.listdir('/tmp'):
    if filename.endswith('.json'):
        print('  ' + filename)
        file_path = os.path.join('/tmp', filename)
        print('  Path: ' + file_path)
        print('  Size: ' + str(os.path.getsize(file_path)) + ' bytes')
        break
else:
    print('  No JSON files found in /tmp')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'status': 'debugging'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
