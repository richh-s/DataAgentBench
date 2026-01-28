code = """import json
import os

# Read the full result from the file
with open('/tmp/tmp6l9qnyjg.json', 'r') as f:
    full_data = json.load(f)

print('__RESULT__:')
print(f'Loaded {len(full_data)} records')
print('First record structure:', list(full_data[0].keys()))
print('Sample CPC data:', full_data[0]['cpc'][:200])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
