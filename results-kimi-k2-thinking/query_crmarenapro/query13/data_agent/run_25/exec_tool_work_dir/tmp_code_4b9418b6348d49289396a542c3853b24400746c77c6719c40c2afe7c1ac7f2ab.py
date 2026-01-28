code = """import json
import pandas as pd

# Get the order data from storage
order_data = locals()['var_functions.query_db:6']

# Create DataFrame
df = pd.DataFrame(order_data)

# Calculate sales amount for each order item
df['SalesAmount'] = df['Quantity'].astype(float) * df['UnitPrice'].astype(float)

# Clean OwnerId by removing leading # if present
df['OwnerId_clean'] = df['OwnerId'].str.replace('^#', '', regex=True)

# Group by OwnerId and sum sales amounts
sales_by_agent = df.groupby('OwnerId_clean')['SalesAmount'].sum().reset_index()

# Sort by sales amount descending
sales_by_agent = sales_by_agent.sort_values('SalesAmount', ascending=False)

# Get top agent
top_agent = sales_by_agent.iloc[0]

# Prepare result
top_agent_id = top_agent['OwnerId_clean']
top_sales = top_agent['SalesAmount']

print('__RESULT__:')
print(json.dumps(top_agent_id))"""

env_args = {'var_functions.query_db:2': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_functions.list_db:5': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:6': [{'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '15.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-07-10'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '8.0', 'UnitPrice': '503.4905', 'EffectiveDate': '2022-07-10'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-10-01'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '14.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-10-01'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-10-01'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '20.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '30.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'Quantity': '10.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '20.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '50.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '1.0', 'UnitPrice': '399.99', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '3.0', 'UnitPrice': '499.99', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '5.0', 'UnitPrice': '427.4905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '7.0', 'UnitPrice': '455.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'Quantity': '12.0', 'UnitPrice': '314.991', 'EffectiveDate': '2022-08-01'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '10.0', 'UnitPrice': '449.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '12.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '16.0', 'UnitPrice': '440.991', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '5.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '7.0', 'UnitPrice': '379.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'Quantity': '3.0', 'UnitPrice': '599.99', 'EffectiveDate': '2022-08-15'}, {'OrderId': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '10.0', 'UnitPrice': '539.991', 'EffectiveDate': '2022-09-20'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '2.0', 'UnitPrice': '339.99', 'EffectiveDate': '2022-09-25'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '3.0', 'UnitPrice': '529.99', 'EffectiveDate': '2022-09-25'}]}

exec(code, env_args)
