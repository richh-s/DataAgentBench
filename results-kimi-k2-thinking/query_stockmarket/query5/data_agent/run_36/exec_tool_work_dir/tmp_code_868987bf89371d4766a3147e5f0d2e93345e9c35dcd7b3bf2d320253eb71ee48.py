code = """# Check what variables are available
available_vars = list(locals().keys())
print("Available variables:", available_vars[:50])

# Look for our specific variables
nasdaq_vars = [var for var in available_vars if 'query_db' in var]
list_vars = [var for var in available_vars if 'list_db' in str(var)]

print("Variables with query_db:", nasdaq_vars)
print("Variables with list_db:", list_vars)

# Check the actual variables
if nasdaq_vars:
    nasdaq_data = locals()[nasdaq_vars[0]]
    print("Type of nasdaq_data:", type(nasdaq_data))
    print("Length of nasdaq_data:", len(nasdaq_data))
    print("First item:", nasdaq_data[0] if nasdaq_data else "Empty")

if list_vars:
    list_data = locals()[list_vars[0]]
    print("Type of list_data:", type(list_data))
    print("Length of list_data:", len(list_data))
    print("First 10 items:", list_data[:10] if list_data else "Empty")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
