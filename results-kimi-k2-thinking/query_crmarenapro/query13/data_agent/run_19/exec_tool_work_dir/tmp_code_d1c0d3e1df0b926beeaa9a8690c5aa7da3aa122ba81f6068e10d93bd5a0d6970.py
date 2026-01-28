code = """import pandas as pd
import json

# Load the query results
orders_data = locals()['var_functions.query_db:10']
order_items_data = locals()['var_functions.query_db:12']

# Convert to DataFrames
orders_df = pd.DataFrame(orders_data)
order_items_df = pd.DataFrame(order_items_data)

# Clean the data - handle potential # in IDs and whitespace
orders_df['Id'] = orders_df['Id'].str.replace('#', '').str.strip()
orders_df['OwnerId'] = orders_df['OwnerId'].str.replace('#', '').str.strip()
order_items_df['OrderId'] = order_items_df['OrderId'].str.replace('#', '').str.strip()

# Convert Quantity and UnitPrice to numeric (handle potential string types)
order_items_df['Quantity'] = pd.to_numeric(order_items_df['Quantity'], errors='coerce')
order_items_df['UnitPrice'] = pd.to_numeric(order_items_df['UnitPrice'], errors='coerce')

# Calculate sales amount per order item
order_items_df['SalesAmount'] = order_items_df['Quantity'] * order_items_df['UnitPrice']

# Merge orders with order items to get agent info
merged_df = orders_df.merge(order_items_df, left_on='Id', right_on='OrderId', how='inner')

# Group by agent and sum sales amounts
agent_sales = merged_df.groupby('OwnerId')['SalesAmount'].sum().reset_index()
agent_sales = agent_sales.sort_values('SalesAmount', ascending=False)

# Get top agent
top_agent = agent_sales.iloc[0]

top_agent_id = top_agent['OwnerId']
top_agent_sales = top_agent['SalesAmount']

result = {
    'agent_id': top_agent_id,
    'total_sales': top_agent_sales
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:5': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.query_db:6': [{'Id': '801Wt00000PFsjPIAT', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2023-06-25'}, {'Id': '801Wt00000PFsjQIAT', 'OwnerId': '005Wt000003NGjwIAG', 'EffectiveDate': '2021-09-30'}, {'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PFtAmIAL', 'OwnerId': '005Wt000003NIljIAG', 'EffectiveDate': '2020-09-01'}, {'Id': '801Wt00000PFtAnIAL', 'OwnerId': '005Wt000003NEdJIAW', 'EffectiveDate': '2023-06-01'}], 'var_functions.query_db:8': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'OrderId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Product2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'Quantity', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'UnitPrice', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'PriceBookEntryId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_functions.query_db:10': [{'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'Status': 'Activated', 'EffectiveDate': '2022-07-10', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'Status': 'Activated', 'EffectiveDate': '2022-10-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'AccountId': '001Wt00000PHHXXIA5', 'Status': 'Activated', 'EffectiveDate': '2022-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'AccountId': '#001Wt00000PGdzxIAD', 'Status': 'Activated', 'EffectiveDate': '2022-10-15', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'AccountId': '#001Wt00000PGZmfIAH', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'AccountId': '#001Wt00000PHVtpIAH', 'Status': 'Activated', 'EffectiveDate': '2022-08-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'Status': 'Activated  ', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2022-08-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'AccountId': '#001Wt00000PGzM9IAL', 'Status': 'Activated ', 'EffectiveDate': '2022-09-20', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'Status': 'Activated', 'EffectiveDate': '2022-09-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_functions.query_db:12': [{'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PHVqfIAH', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '801Wt00000PH4FMIA1', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PHHhDIAX', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '3.0', 'UnitPrice': '529.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '#801Wt00000PHVkDIAX', 'Quantity': '3.0', 'UnitPrice': '599.99'}]}

exec(code, env_args)
