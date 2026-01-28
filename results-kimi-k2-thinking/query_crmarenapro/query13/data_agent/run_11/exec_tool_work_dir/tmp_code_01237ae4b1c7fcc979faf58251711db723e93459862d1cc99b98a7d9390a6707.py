code = """import json
from collections import defaultdict

result_key = 'var_functions.query_db:8'
result_file = locals()[result_key]

# Load full results if it's a file path
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        orders_data = json.load(f)
else:
    orders_data = result_file

# Show data structure and date range
print('Total records: ' + str(len(orders_data)))
if orders_data:
    print('Sample record: ' + str(orders_data[0]))
    
# Debug: Show unique dates
from datetime import datetime
dates = []
for item in orders_data:
    try:
        dates.append(item['EffectiveDate'])
    except:
        pass

unique_dates = sorted(list(set(dates)))
print('Unique dates found: ' + str(len(unique_dates)))
print('First 10 dates: ' + str(unique_dates[:10]))
print('Last 10 dates: ' + str(unique_dates[-10:]))

# Filter for past 5 months from 2022-11-25 (2022-06-25 to 2022-11-25)
cutoff_start = datetime.strptime('2022-06-25', '%Y-%m-%d')
cutoff_end = datetime.strptime('2022-11-25', '%Y-%m-%d')

filtered_orders = []
for item in orders_data:
    try:
        effective_date = datetime.strptime(item['EffectiveDate'], '%Y-%m-%d')
        if cutoff_start <= effective_date <= cutoff_end:
            filtered_orders.append(item)
    except:
        pass

print('Records in 5-month range: ' + str(len(filtered_orders)))

# Calculate sales and aggregate by agent
sales_by_agent = defaultdict(float)
for item in filtered_orders:
    try:
        quantity = float(item['Quantity'])
        unit_price = float(item['UnitPrice'])
        sales_amount = quantity * unit_price
        agent_id = item['OwnerId']
        sales_by_agent[agent_id] += sales_amount
    except:
        pass

print('Number of agents: ' + str(len(sales_by_agent)))

# Sort and find top agent
if sales_by_agent:
    sorted_agents = sorted(sales_by_agent.items(), key=lambda x: x[1], reverse=True)
    print('Top 5 agents:')
    for i in range(min(5, len(sorted_agents))):
        agent_id = sorted_agents[i][0]
        sales = sorted_agents[i][1]
        print(str(i+1) + '. ' + str(agent_id) + ': $' + format(sales, '.2f'))
    
    top_agent = sorted_agents[0][0]
    print('Top agent ID: ' + top_agent)
    
    print('__RESULT__:')
    print(json.dumps(top_agent))
else:
    print('No sales found in range')
    print('__RESULT__:')
    print(json.dumps(None))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_functions.query_db:5': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_functions.list_db:6': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': '005Wt000003NJg9IAG'}

exec(code, env_args)
