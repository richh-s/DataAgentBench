code = """import json

# Load the previous query result
orders_result = locals()['var_functions.query_db:4']

# Debug: print what we got
print("__RESULT__:")
print(json.dumps(orders_result))"""

env_args = {'var_functions.query_db:0': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_functions.query_db:4': [], 'var_functions.list_db:6': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem']}

exec(code, env_args)
