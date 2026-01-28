code = """import json

# Access the file path from storage
storage_key = 'var_functions.query_db:2'
file_path = locals()[storage_key]
print('File path:', file_path)

# Read and analyze the data
with open(file_path, 'r') as f:
    records = json.load(f)

print('Total records:', len(records))

# Examine structure of first record
if records:
    first_record = records[0]
    print('Keys in record:', list(first_record.keys()))
    
    for key in ['Patents_info', 'citation', 'cpc']:
        print('\n=== ' + key + ' ===')
        if first_record.get(key):
            content = first_record[key]
            print('Type:', type(content))
            print('Preview:', str(content)[:300])
        else:
            print('No data or empty')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
