code = """import json, os

# Get all JSON files from query results
files = [f for f in os.listdir('.') if f.endswith('.json') and 'query_db' in f]
print('Found files:', files)

for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
    print('File:', file, 'Records:', len(data))
    if data:
        print('Sample keys:', list(data[0].keys()))
        print('First record:', data[0])
        print('---')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
