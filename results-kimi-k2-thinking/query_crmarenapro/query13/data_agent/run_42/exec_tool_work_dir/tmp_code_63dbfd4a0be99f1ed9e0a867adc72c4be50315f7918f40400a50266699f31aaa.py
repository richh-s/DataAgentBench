code = """import json
import pandas as pd

# Get the query results
orders_data = locals()['var_functions.query_db:5']

# Convert to DataFrame
df = pd.DataFrame(orders_data)

# Clean the data - remove leading # from IDs and convert to numeric
df['OwnerId'] = df['OwnerId'].str.replace('#', '')
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'])

# Calculate sales amount for each order line item
df['SalesAmount'] = df['Quantity'] * df['UnitPrice']

# Group by OwnerId (agent) and sum the sales amounts
agent_sales = df.groupby('OwnerId')['SalesAmount'].sum().reset_index()

# Sort by sales amount descending
agent_sales_sorted = agent_sales.sort_values('SalesAmount', ascending=False)

# Get the top agent
top_agent = agent_sales_sorted.iloc[0]

# Print the result
result = top_agent['OwnerId']
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.list_db:2': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:5': [{'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'Id': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'Id': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'Id': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'Id': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'Id': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'Id': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'Id': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'Id': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15', 'Quantity': '3.0', 'UnitPrice': '599.99'}, {'Id': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'Id': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'Id': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25', 'Quantity': '3.0', 'UnitPrice': '529.99'}]}

exec(code, env_args)
