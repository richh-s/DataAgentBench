code = """import json

# Read the data from the files (the variables contain file paths)
with open(var_functions.query_db:12, 'r') as f:
    order_items = json.load(f)
    
with open(var_functions.query_db:10, 'r') as f:
    orders = json.load(f)

# Calculate sales amount for each order item and aggregate by owner
owner_sales = {}

# Create a map from order ID to owner ID
order_to_owner = {order['Id']: order['OwnerId'] for order in orders}

# Process order items and calculate sales
for item in order_items:
    order_id = item['OrderId']
    
    # Only process if we have the order
    if order_id in order_to_owner:
        owner_id = order_to_owner[order_id]
        
        # Extract quantity and unit price
        try:
            quantity = float(item['Quantity'])
            unit_price = float(item['UnitPrice'])
            sales_amount = quantity * unit_price
            
            # Add to owner's total
            if owner_id in owner_sales:
                owner_sales[owner_id] += sales_amount
            else:
                owner_sales[owner_id] = sales_amount
        except (ValueError, TypeError):
            # Skip invalid data
            pass

# Find the agent with highest sales
if owner_sales:
    top_agent = max(owner_sales, key=owner_sales.get)
    result = {'top_agent_id': top_agent, 'total_sales': owner_sales[top_agent]}
else:
    result = {'top_agent_id': None, 'total_sales': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'name': 'ProductCategory'}, {'name': 'Product2'}, {'name': 'ProductCategoryProduct'}, {'name': 'Pricebook2'}, {'name': 'PricebookEntry'}, {'name': 'Order'}, {'name': 'OrderItem'}], 'var_functions.query_db:3': [{'name': 'Contract'}, {'name': 'Lead'}, {'name': 'Opportunity'}, {'name': 'OpportunityLineItem'}, {'name': 'Quote'}, {'name': 'QuoteLineItem'}], 'var_functions.query_db:6': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_functions.query_db:7': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'order_items_count': 39, 'orders_count': 39}, 'var_functions.execute_python:18': {'order_items_type': "<class 'str'>", 'orders_type': "<class 'str'>", 'order_items_preview': 'file_storage/functions.query_db:12.json', 'orders_preview': 'file_storage/functions.query_db:10.json'}}

exec(code, env_args)
