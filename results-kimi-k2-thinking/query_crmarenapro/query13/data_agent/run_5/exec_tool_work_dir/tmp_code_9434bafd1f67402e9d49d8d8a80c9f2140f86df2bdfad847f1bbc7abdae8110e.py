code = """import json
import os

# Read the order data from the variable
orders = locals()['var_functions.query_db:2']

# Let's write it to a file to inspect
with open('orders_debug.json', 'w') as f:
    json.dump(orders, f, indent=2)

print(f"Number of orders: {len(orders)}")
print(orders[:5])

# Check unique dates
unique_dates = set()
for order in orders:
    unique_dates.add(order['EffectiveDate'])

print(f"Unique dates in data: {sorted(unique_dates)[:20]}")
print("...")
print(f"Total unique dates: {len(unique_dates)}")"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
