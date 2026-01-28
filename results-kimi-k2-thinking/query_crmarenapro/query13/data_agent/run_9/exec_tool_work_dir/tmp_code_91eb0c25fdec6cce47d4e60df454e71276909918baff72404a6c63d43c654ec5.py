code = """import json
import pandas as pd

# Get the query results
order_data = var_functions.query_db:4

# Convert to DataFrame
df = pd.DataFrame(order_data)

# Display initial data preview
print("Initial data preview:")
print(df.head())
print(f"Total rows: {len(df)}")

# Clean the data: remove leading # and trailing whitespace
df['OrderId'] = df['OrderId'].str.lstrip('#').str.strip()
df['OwnerId'] = df['OwnerId'].str.lstrip('#').str.strip()
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'])

print("\nAfter cleaning:")
print(df.head())

# Calculate sales amount for each order item
df['SalesAmount'] = df['Quantity'] * df['UnitPrice']

# Group by OwnerId and sum sales amounts
agent_sales = df.groupby('OwnerId')['SalesAmount'].sum().reset_index()
agent_sales = agent_sales.sort_values('SalesAmount', ascending=False)

print("\nAgent sales top 5:")
print(agent_sales.head())

# Get top agent
if not agent_sales.empty:
    top_agent_id = agent_sales.iloc[0]['OwnerId']
    top_sales_amount = agent_sales.iloc[0]['SalesAmount']
    print(f"\nTop agent: {top_agent_id} with sales: {top_sales_amount}")
else:
    print("No data found")

result = {"top_agent_id": top_agent_id} if not agent_sales.empty else {"top_agent_id": None}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:4': [{'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '15.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-07-10'}, {'OrderId': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'Quantity': '8.0', 'UnitPrice': '503.4905', 'EffectiveDate': '2022-07-10'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '10.0', 'UnitPrice': '359.991', 'EffectiveDate': '2022-10-01'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '14.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-10-01'}, {'OrderId': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-10-01'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '20.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'Quantity': '30.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'Quantity': '10.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '20.0', 'UnitPrice': '390.9915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'Quantity': '50.0', 'UnitPrice': '450.4915', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '1.0', 'UnitPrice': '399.99', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '3.0', 'UnitPrice': '499.99', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '5.0', 'UnitPrice': '427.4905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'Quantity': '7.0', 'UnitPrice': '455.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'Quantity': '12.0', 'UnitPrice': '314.991', 'EffectiveDate': '2022-08-01'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '10.0', 'UnitPrice': '449.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '12.0', 'UnitPrice': '476.991', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '16.0', 'UnitPrice': '440.991', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '5.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '7.0', 'UnitPrice': '379.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG', 'Quantity': '8.0', 'UnitPrice': '569.9905', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG', 'Quantity': '3.0', 'UnitPrice': '599.99', 'EffectiveDate': '2022-08-15'}, {'OrderId': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4', 'Quantity': '10.0', 'UnitPrice': '539.991', 'EffectiveDate': '2022-09-20'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '2.0', 'UnitPrice': '339.99', 'EffectiveDate': '2022-09-25'}, {'OrderId': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW', 'Quantity': '3.0', 'UnitPrice': '529.99', 'EffectiveDate': '2022-09-25'}]}

exec(code, env_args)
