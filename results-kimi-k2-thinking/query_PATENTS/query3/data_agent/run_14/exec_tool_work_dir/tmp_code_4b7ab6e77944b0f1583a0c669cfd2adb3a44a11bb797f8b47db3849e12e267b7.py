code = """import json

# Get the file path from storage
file_path = var_functions.query_db:2
print('File path:', file_path)

# Read the file
with open(file_path, 'r') as f:
    records = json.load(f)

print('Total records:', len(records))
print('First record keys:', list(records[0].keys()))

# Show sample data
sample = records[0]
for key in ['Patents_info', 'citation', 'cpc']:
    print('\n' + key + ':')
    value = sample.get(key)
    if value:
        print(str(value)[:500])
    else:
        print('None')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
