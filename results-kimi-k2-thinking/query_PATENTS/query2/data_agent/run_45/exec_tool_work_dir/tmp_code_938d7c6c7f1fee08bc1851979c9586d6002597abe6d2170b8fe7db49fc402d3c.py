code = """import json

result_file = 'var_functions.query_db:2'
print('Result file path:', result_file)

with open(result_file, 'r') as f:
    data = json.load(f)

print('Total records:', len(data))

for i in range(min(3, len(data))):
    record = data[i]
    print('\nRecord', i+1)
    print('Grant date:', record['grant_date'])
    print('Patents_info preview:', record['Patents_info'][:150])
    cpc_length = len(record['cpc']) if record['cpc'] else 0
    print('CPC length:', cpc_length)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
