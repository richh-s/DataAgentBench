code = """# Load the data and look for German patents
import json
import re

# Get the data from previous query
result_value = locals()['var_functions.query_db:22']
if isinstance(result_value, str) and result_value.endswith('.json'):
    with open(result_value, 'r') as f:
        patents_data = json.load(f)
else:
    patents_data = result_value

print('Sample records to check for German patents:')
for i in range(min(10, len(patents_data))):
    rec = patents_data[i]
    patents_info = rec.get('Patents_info', '')
    print('Record ' + str(i) + ': ' + patents_info[:200])
    print('---')

# Now let's search for German patents more systematically
print('Looking for DE country code...')

# Let's query for patents with DE in Patents_info
print('Need to query for German patents specifically')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433, 'var_functions.execute_python:20': 0, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
