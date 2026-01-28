code = """# Let's check what variables are available in the storage
import json

# Check the actual variable content
var_16 = var_functions.query_db:16
var_8 = var_functions.query_db:8

# Determine types
print(f"var_functions.query_db:16 type: {type(var_16)}")
print(f"var_functions.query_db:8 type: {type(var_8)}")

# If they're strings, they might be file paths
if isinstance(var_16, str):
    print(f"var_16 is a string (likely file path): {var_16[:100]}...")
elif isinstance(var_16, list):
    print(f"var_16 is a list with {len(var_16)} items")
    if len(var_16) > 0:
        print(f"First item keys: {list(var_16[0].keys())}")

if isinstance(var_8, str):
    print(f"var_8 is a string (likely file path): {var_8[:100]}...")
elif isinstance(var_8, list):
    print(f"var_8 is a list with {len(var_8)} items")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
