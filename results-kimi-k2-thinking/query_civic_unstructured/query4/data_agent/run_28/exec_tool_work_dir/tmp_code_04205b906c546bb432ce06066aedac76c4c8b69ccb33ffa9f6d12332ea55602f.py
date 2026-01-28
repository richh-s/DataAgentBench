code = """# Check what variables are available
available_keys = [k for k in locals().keys() if 'query_db' in k]
print("Available keys:", available_keys)

# Try to access the result
try:
    file_info = locals()['var_functions.query_db:2']
    print("File info type:", type(file_info))
    print("File info content:", file_info)
except KeyError:
    print("var_functions.query_db:2 not found")
    
# Also check other possible variable names
for k in locals().keys():
    if 'query_db' in str(k):
        print(f"Found key: {k}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
