code = """import json, re, os

# Try to find the data files from the query results
files = os.listdir('.')
print('Files in current directory:', files)

# Look for JSON files that contain our data
for f in files:
    if f.endswith('.json'):
        print('Checking file:', f)
        with open(f, 'r') as file:
            try:
                data = json.load(file)
                print('Record count for', f, ':', len(data))
                if len(data) > 0:
                    print('Sample:', data[0])
            except:
                pass

print('Done checking files')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
