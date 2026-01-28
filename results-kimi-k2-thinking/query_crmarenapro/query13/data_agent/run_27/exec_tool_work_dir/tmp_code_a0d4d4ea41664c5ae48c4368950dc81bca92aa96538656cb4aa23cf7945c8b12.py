code = """import json

# Get the file path from storage
result_file = locals()['var_functions.query_db:10']

# Read the query results
with open(result_file, 'r') as f:
    order_items = json.load(f)

# Calculate total sales per agent
agent_sales = {}
for item in order_items:
    try:
        quantity = float(item['Quantity'])
        unit_price = float(item['UnitPrice'])
        sales_amount = quantity * unit_price
        
        owner_id = item['OwnerId']
        
        # Clean up OwnerId (handle leading # and trailing whitespace)
        owner_id = owner_id.lstrip('#').strip()
            
        agent_sales[owner_id] = agent_sales.get(owner_id, 0) + sales_amount
    except (ValueError, TypeError, KeyError):
        # Skip items with invalid data
        continue

# Find agent with highest sales
if agent_sales:
    top_agent_id = max(agent_sales.items(), key=lambda x: x[1])[0]
else:
    top_agent_id = "No sales data found"

print('__RESULT__:')
print(json.dumps(top_agent_id))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': '005Wt000003NJg9IAG', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
