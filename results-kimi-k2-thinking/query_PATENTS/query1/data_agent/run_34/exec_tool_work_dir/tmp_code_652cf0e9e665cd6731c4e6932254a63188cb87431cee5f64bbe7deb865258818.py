code = """# Let's see what's in locals()
print("Variables in locals():")
for key, value in locals().items():
    if not key.startswith('__'):
        print(f"{key}: {type(value)} = {str(value)[:100]}")

# Let's also check if there's any storage key
print("\nStorage key check:")
if 'storage' in locals():
    print("Storage exists")
    print(list(storage.keys()))
else:
    print("No storage found")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}]}

exec(code, env_args)
