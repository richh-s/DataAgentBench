code = """import json

# Load funding data and check its structure
funding_path = locals()['var_functions.query_db:64']
with open(funding_path) as f:
    funding_data = json.load(f)

print('Type:', type(funding_data))
print('Length:', len(funding_data))

# Check first few records to see structure
if funding_data:
    print('First record:', funding_data[0])
    print('Second record:', funding_data[1])

# Check all keys
if funding_data:
    all_keys = set()
    for record in funding_data[:10]:
        all_keys.update(record.keys())
    print('All keys found:', list(all_keys))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
