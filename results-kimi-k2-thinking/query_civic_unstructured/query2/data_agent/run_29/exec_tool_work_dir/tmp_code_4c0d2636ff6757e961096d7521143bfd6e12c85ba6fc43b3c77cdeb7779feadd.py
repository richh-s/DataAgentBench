code = """import os, glob, json

# Find all JSON files in /tmp/
files = glob.glob('/tmp/*.json')
print('JSON files in /tmp/:')
for f in files:
    print(f)

# Determine which file is which
for f in files:
    try:
        data = json.load(open(f))
        print(f'\nFile: {f}')
        print(f'Type: {type(data)}')
        if isinstance(data, list) and len(data) > 0:
            print(f'First item type: {type(data[0])}')
            print(f'First item keys: {data[0].keys() if isinstance(data[0], dict) else "N/A"}')
    except:
        pass"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
