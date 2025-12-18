code = """import pandas as pd
import json

orders_data = locals()['var_function-call-1000994512058464474']
order_items_data = locals()['var_function-call-11848176339172514074']

orders_df = pd.DataFrame(orders_data)
order_items_df = pd.DataFrame(order_items_data)

# Clean IDs by removing leading '#' and stripping spaces
orders_df['Id'] = orders_df['Id'].astype(str).str.replace('#', '', regex=False).str.strip()
orders_df['OwnerId'] = orders_df['OwnerId'].astype(str).str.replace('#', '', regex=False).str.strip()
order_items_df['OrderId'] = order_items_df['OrderId'].astype(str).str.replace('#', '', regex=False).str.strip()

# Convert Quantity and UnitPrice to numeric
order_items_df['Quantity'] = pd.to_numeric(order_items_df['Quantity'], errors='coerce')
order_items_df['UnitPrice'] = pd.to_numeric(order_items_df['UnitPrice'], errors='coerce')

# Calculate sales amount for each order item
order_items_df['SalesAmount'] = order_items_df['Quantity'] * order_items_df['UnitPrice']

# Group by OrderId to get total sales per order
order_sales = order_items_df.groupby('OrderId')['SalesAmount'].sum().reset_index()
order_sales.rename(columns={'OrderId': 'Id', 'SalesAmount': 'TotalOrderSales'}, inplace=True)

# Merge with orders_df to link sales to OwnerId
merged_df = pd.merge(orders_df, order_sales, on='Id', how='inner')

# Group by OwnerId and sum total sales for each owner
agent_sales = merged_df.groupby('OwnerId')['TotalOrderSales'].sum().reset_index()

# Find the agent with the top sales
top_agent = agent_sales.loc[agent_sales['TotalOrderSales'].idxmax()]

print("__RESULT__:")
print(json.dumps(top_agent['OwnerId']))"""

env_args = {'var_function-call-1000994512058464474': [{'Id': '#801Wt00000PFt7UIAT', 'EffectiveDate': '2022-09-15', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'EffectiveDate': '2022-07-10', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'EffectiveDate': '2022-10-01', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'EffectiveDate': '2022-09-01', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'EffectiveDate': '2022-07-01', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'EffectiveDate': '2022-10-15', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'EffectiveDate': '2022-09-15', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'EffectiveDate': '2022-07-01', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'EffectiveDate': '2022-07-01', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'EffectiveDate': '2022-08-01', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'EffectiveDate': '2022-09-15', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'EffectiveDate': '2022-07-01', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'EffectiveDate': '2022-08-15', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'EffectiveDate': '2022-09-20', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'EffectiveDate': '2022-09-25', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-11848176339172514074': [{'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '7.0', 'UnitPrice': '379.9905'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '12.0', 'UnitPrice': '476.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '30.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PHVqfIAH', 'Quantity': '10.0', 'UnitPrice': '539.991'}, {'OrderId': '#801Wt00000PGbdMIAT', 'Quantity': '20.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '20.0', 'UnitPrice': '390.9915'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '14.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '3.0', 'UnitPrice': '499.99'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '2.0', 'UnitPrice': '339.99'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '50.0', 'UnitPrice': '450.4915'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '16.0', 'UnitPrice': '440.991'}, {'OrderId': '801Wt00000PH4FMIA1', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '1.0', 'UnitPrice': '399.99'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '10.0', 'UnitPrice': '449.991'}, {'OrderId': '801Wt00000PHLzNIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PHRFAIA5', 'Quantity': '5.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '15.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PFyITIA1', 'Quantity': '8.0', 'UnitPrice': '503.4905'}, {'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'OrderId': '801Wt00000PHHhDIAX', 'Quantity': '12.0', 'UnitPrice': '314.991'}, {'OrderId': '#801Wt00000PHWptIAH', 'Quantity': '3.0', 'UnitPrice': '529.99'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '7.0', 'UnitPrice': '455.9905'}, {'OrderId': '801Wt00000PHHMFIA5', 'Quantity': '5.0', 'UnitPrice': '427.4905'}, {'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '8.0', 'UnitPrice': '569.9905'}, {'OrderId': '801Wt00000PGGhBIAX', 'Quantity': '10.0', 'UnitPrice': '359.991'}, {'OrderId': '#801Wt00000PHVkDIAX', 'Quantity': '3.0', 'UnitPrice': '599.99'}]}

exec(code, env_args)
