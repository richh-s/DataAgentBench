code = """import json
import os

# Get all temp files to find our data
files = []
for root, dirs, filenames in os.walk('/tmp'):
    for filename in filenames:
        if filename.endswith('.json'):
            files.append(os.path.join(root, filename))

print('JSON files found:')
for f in files:
    print('  ' + f)

# Try to read civic docs
for f in files:
    if 'civic' in f.lower() or 'doc' in f.lower():
        try:
            with open(f, 'r') as file:
                data = json.load(file)
                print('\nSuccessfully loaded civic data from ' + f)
                print('  Records: ' + str(len(data)))
                # Show first record keys
                if data:
                    print('  Keys: ' + str(list(data[0].keys())))
                break
        except:
            continue

# Try to read funding data
for f in files:
    if 'funding' in f.lower() or f.endswith('.json'):
        try:
            with open(f, 'r') as file:
                data = json.load(file)
                if len(data) > 0 and 'Funding_ID' in data[0]:
                    print('\nSuccessfully loaded funding data from ' + f)
                    print('  Records: ' + str(len(data)))
                    if data:
                        print('  Keys: ' + str(list(data[0].keys())))
                    break
        except:
            continue"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
