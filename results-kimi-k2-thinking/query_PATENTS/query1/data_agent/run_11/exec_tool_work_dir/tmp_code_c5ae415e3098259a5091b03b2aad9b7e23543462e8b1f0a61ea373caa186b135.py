code = """import json
from datetime import datetime
import os

# Load data from the result file
with open(locals()['var_functions.query_db:22'], 'r') as f:
    raw_data = f.read()

print('Data size:', len(raw_data))
print('Data type:', type(raw_data))

# If it's a plain string, parse it as JSON
try:
    data = json.loads(raw_data)
    print('Parsed as JSON - records:', len(data))
except:
    # Try to read as Python list (might be a string representation)
    try:
        data = eval(raw_data)
        print('Parsed as eval - records:', len(data))
    except:
        print('Failed to parse data')
        print(raw_data[:500])

print('\n__RESULT__:')
print(json.dumps('success'))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
