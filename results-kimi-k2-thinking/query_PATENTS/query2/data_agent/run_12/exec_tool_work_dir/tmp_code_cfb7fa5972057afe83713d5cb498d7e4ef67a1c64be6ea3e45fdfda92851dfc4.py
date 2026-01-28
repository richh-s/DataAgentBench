code = """# Let's continue processing - check what country codes and patents_info look like
import json

patents_data = locals()['var_functions.execute_db:2']
if isinstance(patents_data, str) and patents_data.endswith('.json'):
    with open(patents_data, 'r') as f:
        patents_data = json.load(f)

# Check the structure of Patents_info field to find country codes
samples = []
for i in range(min(5, len(patents_data))):
    rec = patents_data[i]
    patents_info = rec.get('Patents_info', '')
    samples.append(patents_info[:300])
    print('Sample ' + str(i) + ': ' + patents_info[:200])
    print('---')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 1433}

exec(code, env_args)
