code = """import json

# Try to access the variable directly
# First, let's see what variables we have
print("Available variables:")
for key in list(locals().keys()):
    if key.startswith('var_'):
        print(f"  {key}: {type(locals()[key])}")

# Now try to access our specific variable
var_name = 'var_functions.query_db:0'
if var_name in locals():
    result_data = locals()[var_name]
    print(f"\nFound data of type: {type(result_data)}")
    if isinstance(result_data, str):
        print(f"It's a string of length: {len(result_data)}")
        print("Content starts with:", result_data[:200])
    elif isinstance(result_data, list):
        print(f"It's a list with {len(result_data)} items")
        if result_data:
            print("First item:", result_data[0])
else:
    print(f"\nVariable {var_name} not found!")
    print("All variables:", list(locals().keys()))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
