code = """import json

data_file = 'var_functions.query_db:2'

# Since the data is stored in a file path, read it
with open(data_file, 'r') as f:
    data = json.load(f)

print('Number of UNIV CALIFORNIA patents:', len(data))

# First record structure
if len(data) > 0:
    rec = data[0]
    print('\nFirst record keys:', list(rec.keys()))
    print('\nFirst record Patents_info:', rec['Patents_info'])
    print('\nFirst record citation preview:', str(rec['citation'])[:200])
    print('\nFirst record cpc preview:', str(rec['cpc'])[:200])

# __RESULT__
print('\n__RESULT__:')
print(json.dumps({'count': len(data), 'first_record_keys': list(data[0].keys()) if data else None}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
