code = """# Let's check what variables we have access to
available_vars = [name for name in locals().keys() if 'query' in name]
print("Available query-related variables:", available_vars)

# Let's also check for order-related data
order_vars = [name for name in locals().keys() if 'order' in name]
print("Available order-related variables:", order_vars)

# Let's also print all variable names that contain colon
colon_vars = [name for name in locals().keys() if ':' in name]
print("Variables with colons:", colon_vars)"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
