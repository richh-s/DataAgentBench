code = """import json

# Get the file path from the storage
result_file_path = locals()['var_functions.query_db:5']

# Read the query result from file
with open(result_file_path, 'r') as f:
    order_items = json.load(f)

# Calculate total sales per agent
agent_sales = {}
for item in order_items:
    try:
        quantity = float(item['Quantity'])
        unit_price = float(item['UnitPrice'])
        sales_amount = quantity * unit_price
        
        owner_id = item['OwnerId']
        
        # Clean up OwnerId (handle leading #)
        if owner_id.startswith('#'):
            owner_id = owner_id[1:]
            
        agent_sales[owner_id] = agent_sales.get(owner_id, 0) + sales_amount
    except (ValueError, TypeError):
        # Skip items with invalid numeric data
        continue

# Find agent with highest sales
if agent_sales:
    top_agent = max(agent_sales.items(), key=lambda x: x[1])
    result = top_agent[0]
else:
    result = "No sales data found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
