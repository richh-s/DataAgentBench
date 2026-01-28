code = """import json

# Read the full result from the file
result_file = var_functions.query_db:5
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        order_items_data = json.load(f)
else:
    order_items_data = result_file

# Debug: print first few records
print("First 3 records:", order_items_data[:3])
print(f"Total records: {len(order_items_data)}")

# Calculate sales amount per agent
agent_sales = {}
for record in order_items_data:
    try:
        # Extract values
        owner_id = record['OwnerId']
        quantity = float(record['Quantity'])
        unit_price = float(record['UnitPrice'])
        
        # Calculate sales amount for this line item
        line_amount = quantity * unit_price
        
        # Accumulate by agent
        if owner_id not in agent_sales:
            agent_sales[owner_id] = 0
        agent_sales[owner_id] += line_amount
    except (KeyError, ValueError, TypeError) as e:
        # Skip records with missing or invalid data
        continue

# Find top agent
top_agent = max(agent_sales.items(), key=lambda x: x[1]) if agent_sales else None

result = {
    'top_agent_id': top_agent[0] if top_agent else None,
    'total_sales': top_agent[1] if top_agent else 0,
    'total_agents': len(agent_sales)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
