code = """import json
import pandas as pd

# Read the orders data
orders = locals()['var_functions.query_db:12']

# Read the order items from file
order_items_file = locals()['var_functions.query_db:14']
with open(order_items_file, 'r') as f:
    order_items = json.load(f)

print(f"Orders retrieved: {len(orders)}")
print(f"Order items retrieved: {len(order_items)}")

# Convert to DataFrames
orders_df = pd.DataFrame(orders)
order_items_df = pd.DataFrame(order_items)

# Clean the data - remove leading # from IDs
orders_df['Id'] = orders_df['Id'].str.replace('^#', '', regex=True)
order_items_df['OrderId'] = order_items_df['OrderId'].str.replace('^#', '', regex=True)

# Filter orders by date range (already filtered in query, but explicitly check)
# Orders were filtered for EffectiveDate >= '2022-06-25' AND <= '2022-11-25'

# Merge orders and order items
merged_df = pd.merge(orders_df, order_items_df, left_on='Id', right_on='OrderId', how='inner')

print(f"Merged records: {len(merged_df)}")

if len(merged_df) > 0:
    # Calculate sales amount
    merged_df['SalesAmount'] = merged_df['Quantity'].astype(float) * merged_df['UnitPrice'].astype(float)
    
    # Group by OwnerId (agent) and sum sales amounts
    agent_sales = merged_df.groupby('OwnerId')['SalesAmount'].sum().reset_index()
    
    # Sort by sales amount descending
    agent_sales = agent_sales.sort_values('SalesAmount', ascending=False)
    
    print("Top agents by sales:")
    print(agent_sales.head())
    
    # Get the top agent
    top_agent_id = agent_sales.iloc[0]['OwnerId']
    top_agent_sales = agent_sales.iloc[0]['SalesAmount']
    
    result = {
        'top_agent_id': top_agent_id,
        'sales_amount': top_agent_sales
    }
else:
    result = {'error': 'No matching orders found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}], 'var_functions.list_db:4': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:8': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2023-06-25'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'OwnerId': '005Wt000003NEdJIAW', 'EffectiveDate': '2023-06-01'}, {'Id': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10'}, {'Id': '801Wt00000PFyIUIA1', 'AccountId': '#001Wt00000PGtmwIAD', 'OwnerId': '005Wt000003NJ53IAG', 'EffectiveDate': '2024-09-20'}, {'Id': '801Wt00000PGGTwIAP', 'AccountId': '001Wt00000PFttwIAD', 'OwnerId': '#005Wt000003NJjNIAW', 'EffectiveDate': '2023-09-15'}, {'Id': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01'}, {'Id': '801Wt00000PGGlcIAH', 'AccountId': '001Wt00000PHRTfIAP', 'OwnerId': '#005Wt000003NDXaIAO', 'EffectiveDate': '2022-12-01'}, {'Id': '801Wt00000PGHg8IAH', 'AccountId': '001Wt00000PHVnNIAX', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2023-10-15'}, {'Id': '801Wt00000PGR7WIAX', 'AccountId': '001Wt00000PFrk1IAD', 'OwnerId': '005Wt000003NISNIA4', 'EffectiveDate': '2023-03-20'}], 'var_functions.query_db:10': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Quantity': '15.0', 'UnitPrice': '476.991'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Quantity': '3.0', 'UnitPrice': '549.99'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Quantity': '9.0', 'UnitPrice': '503.4905'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Quantity': '1.0', 'UnitPrice': '299.99'}], 'var_functions.query_db:12': [{'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01'}, {'Id': '#801Wt00000PGbLTIA1', 'OwnerId': '005Wt000003NFRKIA4', 'EffectiveDate': '2022-09-01'}, {'Id': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01'}, {'Id': '#801Wt00000PGtiAIAT', 'OwnerId': '005Wt000003NIljIAG', 'EffectiveDate': '2022-10-15'}, {'Id': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01'}, {'Id': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01'}, {'Id': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01'}, {'Id': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15'}, {'Id': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20'}, {'Id': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
