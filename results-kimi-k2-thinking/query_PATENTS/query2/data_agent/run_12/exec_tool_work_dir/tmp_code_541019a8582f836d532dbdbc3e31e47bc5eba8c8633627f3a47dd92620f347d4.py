code = """import json
import os

# Load the data from the result
result_file = str(locals()['var_functions.query_db:2'])
print('File path: ' + result_file)

if result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        patents_data = json.load(f)
else:
    patents_data = locals()['var_functions.query_db:2']

print('Total patent records: ' + str(len(patents_data)))

# Show first record structure
first = patents_data[0]
print('Grant date: ' + first['grant_date'])
print('CPC type: ' + str(type(first['cpc'])))
print('CPC sample: ' + str(first['cpc'])[:150])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
