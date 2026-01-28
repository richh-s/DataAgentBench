code = """# Check what variables are available
available_vars = list(locals().keys())
print("Total variables available:", len(available_vars))

# Display first 20 variables
print("First 20 variables:", available_vars[:20])

# Look for specific variables containing our data
nasdaq_data = None
list_data = None

for var in available_vars:
    if 'query_db' in var:
        nasdaq_data = locals()[var]
        print("Found nasdaq data:", var)
    if 'list_db' in var:
        list_data = locals()[var]
        print("Found list data:", var)

if nasdaq_data:
    print("Type of nasdaq_data:", type(nasdaq_data))
    print("Length of nasdaq_data:", len(nasdaq_data))
    print("First item:", nasdaq_data[0] if nasdaq_data else "Empty")

if list_data:
    print("Type of list_data:", type(list_data))
    print("Length of list_data:", len(list_data))
    print("First 10 items:", list_data[:10] if list_data else "Empty")

# Combine the data
if nasdaq_data and list_data:
    nasdaq_symbols = [item['Symbol'] for item in nasdaq_data]
    available_symbols = list(set(nasdaq_symbols) & set(list_data))
    
    print("Total NASDAQ Capital symbols:", len(nasdaq_symbols))
    print("Available in trade database:", len(available_symbols))
    print("Sample available:", available_symbols[:5])

print('__RESULT__:')
print("Test completed")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
