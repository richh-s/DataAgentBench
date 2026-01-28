code = """import json

# Get the stored results from storage (they're file paths due to large size)
stockinfo_result = locals()['var_functions.query_db:0']
tables_result = locals()['var_functions.query_db:4']

# Load the actual data from the JSON files
with open(stockinfo_result, 'r') as f:
    stockinfo_data = json.load(f)

with open(tables_result, 'r') as f:
    tables_data = json.load(f)

# Debug info
print('First few stockinfo entries:')
for i, item in enumerate(stockinfo_data[:3]):
    print(f"  {item}")

print('\nFirst few tables entries:')
for i, item in enumerate(tables_data[:3]):
    print(f"  {item}")

print(f"\nTotal stockinfo entries: {len(stockinfo_data)}")
print(f"Total tables: {len(tables_data)}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
