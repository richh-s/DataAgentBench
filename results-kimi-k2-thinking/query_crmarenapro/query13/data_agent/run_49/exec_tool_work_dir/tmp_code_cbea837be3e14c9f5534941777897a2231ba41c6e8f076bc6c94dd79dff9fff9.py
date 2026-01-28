code = """import json

# Load the result from storage
result_file_path = var_functions.query_db:2
with open(result_file_path, 'r') as f:
    order_sales_data = json.load(f)

print("__RESULT__:")
print(json.dumps(order_sales_data[:5]))  # Print first 5 records as preview"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
