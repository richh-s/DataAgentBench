code = """import json

# Load the Order data from the file
with open('/var/folders/k2/slz9n1r13g95g399mclj4qzc0000gp/T/tmp7k7w9g8b.json', 'r') as f:
    order_data = json.load(f)

# Load the OrderItem data from the file
with open('/var/folders/k2/slz9n1r13g95g399mclj4qzc0000gp/T/tmpa4x1c3i5.json', 'r') as f:
    order_item_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    "orders_count": len(order_data),
    "order_items_count": len(order_item_data),
    "sample_orders": order_data[:3],
    "sample_order_items": order_item_data[:3]
}))"""

env_args = {}

exec(code, env_args)
