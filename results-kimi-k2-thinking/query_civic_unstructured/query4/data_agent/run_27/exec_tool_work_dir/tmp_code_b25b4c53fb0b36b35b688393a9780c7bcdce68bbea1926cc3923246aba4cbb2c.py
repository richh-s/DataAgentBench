code = """import json
import re

# Use string key to access storage variable
mongo_var_key = 'var_functions.query_db:5'
mongo_data = globals()[mongo_var_key]

print('Type of mongo_data:', type(mongo_data))
print('Value (first 200 chars):', str(mongo_data)[:200])

# The data might be a file path string if too large
if isinstance(mongo_data, str) and '.json' in mongo_data:
    print('Loading from file path...')
    with open(mongo_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = mongo_data

print('Documents loaded:', len(civic_docs))
print('First doc keys:', list(civic_docs[0].keys()) if civic_docs else 'Empty')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding']}

exec(code, env_args)
