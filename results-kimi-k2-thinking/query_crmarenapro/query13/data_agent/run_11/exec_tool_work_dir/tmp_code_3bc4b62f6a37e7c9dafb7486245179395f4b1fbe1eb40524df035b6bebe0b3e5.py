code = """import json
import re
from datetime import datetime

# Read the full results from the file
result_key = 'var_functions.query_db:8'
result_file = locals()[result_key]

# Load the full results if it's a file path
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        orders_data = json.load(f)
else:
    orders_data = result_file

print('Total order items retrieved: ' + str(len(orders_data)))

# Calculate sales amount for each order item
for item in orders_data:
    try:
        quantity = float(item['Quantity'])
        unit_price = float(item['UnitPrice'])
        item['SalesAmount'] = quantity * unit_price
    except:
        item['SalesAmount'] = 0

# Aggregate sales by OwnerId
from collections import defaultdict
sales_by_owner = defaultdict(float)

for item in orders_data:
    owner_id = item['OwnerId']
    sales_by_owner[owner_id] += item['SalesAmount']

# Sort by sales amount
sorted_owners = sorted(sales_by_owner.items(), key=lambda x: x[1], reverse=True)

print('Top 10 agents by total sales:')
for i in range(min(10, len(sorted_owners))):
    owner_id = sorted_owners[i][0]
    sales = sorted_owners[i][1]
    print(str(i+1) + '. ' + str(owner_id) + ': $' + format(sales, '.2f'))

if sorted_owners:
    top_agent = sorted_owners[0][0]
    top_sales = sorted_owners[0][1]
    print('Top agent: ' + str(top_agent) + ' with $' + format(top_sales, '.2f') + ' in sales')
    
    # Output result in required format
    print('__RESULT__:')
    print(json.dumps(top_agent))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_functions.query_db:5': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_functions.list_db:6': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
