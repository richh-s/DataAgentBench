code = """import json
import pandas as pd

# Load the data from the file
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean the data - handle corrupted IDs
df['CleanOwnerId'] = df['CleanOwnerId'].str.replace('#', '').str.strip()

# Ensure numeric columns are properly typed
df['SalesAmount'] = pd.to_numeric(df['SalesAmount'], errors='coerce')

# Group by agent (OwnerId) and sum sales amounts
agent_sales = df.groupby('CleanOwnerId')['SalesAmount'].sum().reset_index()

# Sort by sales amount in descending order
top_agent = agent_sales.sort_values('SalesAmount', ascending=False).head(1)

print('__RESULT__:')
print(top_agent.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.list_db:5': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:6': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_functions.query_db:8': [{'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '359.991', 'SalesAmount': '3599.91'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'SalesAmount': '4559.924'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '15.0', 'UnitPrice': '359.991', 'SalesAmount': '5399.865'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10', 'Quantity': '8.0', 'UnitPrice': '503.4905', 'SalesAmount': '4027.924'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '10.0', 'UnitPrice': '359.991', 'SalesAmount': '3599.91'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '14.0', 'UnitPrice': '476.991', 'SalesAmount': '6677.874'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'SalesAmount': '4559.924'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '20.0', 'UnitPrice': '450.4915', 'SalesAmount': '9009.83'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01', 'Quantity': '30.0', 'UnitPrice': '390.9915', 'SalesAmount': '11729.744999999999'}, {'OrderId': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15', 'Quantity': '10.0', 'UnitPrice': '476.991', 'SalesAmount': '4769.91'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
