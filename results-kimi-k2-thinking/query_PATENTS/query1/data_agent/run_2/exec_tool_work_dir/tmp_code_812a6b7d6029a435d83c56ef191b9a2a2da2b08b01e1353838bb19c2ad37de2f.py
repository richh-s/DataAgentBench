code = """# Access the variable properly
import json
filepath = locals()['var_functions.query_db:2']
print('Filepath:', filepath)

# Load the data
import os
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        print('Loaded JSON, number of records:', len(data))
        print('First record keys:', data[0].keys() if data else 'No data')
else:
    print('File not found')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
