code = """# Debug: Check what variables are available
print("Available variables:")
for key in list(locals().keys()):
    if key.startswith('var_'):
        print(f"  {key}: {type(locals()[key])}")
        
# Try to access the query result
if 'var_functions.query_db:4' in locals():
    data = locals()['var_functions.query_db:4']
    print(f"\nRaw data type: {type(data)}")
    print(f"Raw data (first 200 chars): {str(data)[:200]}")
else:
    print("var_functions.query_db:4 not found in locals()")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
