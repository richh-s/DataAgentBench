code = """# The result is stored in storage under key var_functions.query_db:0
# Let's see if we can access it directly
print("Trying to access storage variable...")

# Try different ways to access the variable
if 'var_functions.query_db:0' in locals():
    data = locals()['var_functions.query_db:0']
    print("Found data in locals()")
    print("Type:", type(data))
    if isinstance(data, str) and data.endswith('.json'):
        print("It's a file path:", data)
        import json
        with open(data, 'r') as f:
            actual_data = json.load(f)
        print("Loaded from file, length:", len(actual_data))
    else:
        print("Direct data, length:", len(data))
elif 'var_functions.query_db:0' in globals():
    data = globals()['var_functions.query_db:0']
    print("Found data in globals()")
else:
    print("Could not find the variable")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
