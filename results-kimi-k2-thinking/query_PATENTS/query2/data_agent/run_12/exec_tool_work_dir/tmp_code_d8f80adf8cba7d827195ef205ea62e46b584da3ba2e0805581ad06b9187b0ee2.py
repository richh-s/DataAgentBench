code = """import json
import os

# Get the result data
result_key = 'var_functions.query_db:2'
result_raw = locals()[result_key]
print('Type of result: ' + str(type(result_raw)))

if isinstance(result_raw, str) and result_raw.endswith('.json'):
    with open(result_raw, 'r') as f:
        patents_data = json.load(f)
    print('Loaded from file: ' + result_raw)
else:
    patents_data = result_raw
    print('Using result directly')

print('Total patent records: ' + str(len(patents_data)))

# Show first record
if len(patents_data) > 0:
    first = patents_data[0]
    print('Sample grant date: ' + first['grant_date'])
    print('Sample CPC data: ' + str(first['cpc'])[:200])

print('__RESULT__:')
print(str(len(patents_data)))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
