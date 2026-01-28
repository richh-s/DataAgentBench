code = """import json

# Check what variables are available in locals
print("Local variables with 'var' in name:")
for key in locals():
    if 'var' in str(key):
        print(f"  {key}: {type(locals()[key])}")

# Try to access the stockinfo result
stockinfo_key = 'var_functions.query_db:2'
if stockinfo_key in locals():
    result = locals()[stockinfo_key]
    print(f"\nFound stockinfo result: {type(result)}")
    if isinstance(result, list):
        print(f"Number of records: {len(result)}")
        print(f"First record: {result[0]}")
else:
    print(f"\nKey {stockinfo_key} not found in locals")
    
# Check for list_db result
listdb_key = 'var_functions.list_db:0'
if listdb_key in locals():
    result = locals()[listdb_key]
    print(f"\nFound list_db result: {type(result)}")
    print(f"Result: {result}")
else:
    print(f"\nKey {listdb_key} not found in locals")"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
