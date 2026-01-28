code = """import json

# Let's check what variables are available
available_vars = [name for name in dir() if not name.startswith('__')]
print("Available variables:", available_vars[:10])

# Check if we can access the query result variable directly
if 'var_functions.query_db:2' in dir():
    sample_data = locals()['var_functions.query_db:2']
    print("Sample data type:", type(sample_data))
    if isinstance(sample_data, list):
        print("Sample records:", len(sample_data))
        if sample_data:
            print("First record keys:", list(sample_data[0].keys()))
            print("First record Patents_info:", sample_data[0].get('Patents_info', 'Not found'))
    else:
        print("Sample data is not a list, it's:", type(sample_data))
else:
    print("var_functions.query_db:2 not found in local variables")
    # Try to access via globals
    if 'var_functions.query_db:2' in globals():
        sample_data = globals()['var_functions.query_db:2']
        print("Found in globals, type:", type(sample_data))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition']}

exec(code, env_args)
