code = """import json
import os

# Try to access the stored result directly
result_var = locals().get('var_functions.query_db:2')
print("Result variable:", result_var)
print("Type:", type(result_var))

if isinstance(result_var, str) and result_var.endswith('.json'):
    # It's a file path
    with open(result_var, 'r') as f:
        docs = json.load(f)
    print("Loaded docs count:", len(docs))
else:
    # It might be the data itself
    docs = result_var
    print("Direct data, count:", len(docs) if hasattr(docs, '__len__') else "Not a list")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
