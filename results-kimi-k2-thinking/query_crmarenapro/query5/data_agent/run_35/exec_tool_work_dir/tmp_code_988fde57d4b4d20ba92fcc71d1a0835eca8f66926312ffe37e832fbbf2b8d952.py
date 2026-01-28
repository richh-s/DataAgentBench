code = """import json

# Read the order items from the file
order_items_path = var_functions.query_db:0
with open(order_items_path, 'r') as f:
    order_items = json.load(f)

# Extract OrderItem Ids
order_item_ids = [item['Id'] for item in order_items]
print(f"Found {len(order_item_ids)} order items")

# Show first few order item IDs
print("Sample OrderItem IDs:", order_item_ids[:5])

# Prepare data for next query
print("__RESULT__:")
print(json.dumps(order_item_ids))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
