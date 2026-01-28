code = """# Check what variables are available
available_vars = list(locals().keys())
print("All available variables:")
for var in available_vars[:50]:
    print(var)

# Count how many variables we have
print(f"\nTotal variables available: {len(available_vars)}")

# Look for our specific variables
nasdaq_vars = [var for var in available_vars if 'query_db' in var]
list_vars = [var for var in available_vars if 'list_db' in var]

print(f"\nVariables with 'query_db': {nasdaq_vars}")
print(f"Variables with 'list_db': {list_vars}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
