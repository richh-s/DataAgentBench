code = """import json
import pandas as pd

# Get data from storage
orders_data = locals()['var_functions.query_db:14']
order_items_full = locals()['var_functions.query_db:16']

# Load order items if it's a file path, otherwise use directly
if isinstance(order_items_full, str):
    with open(order_items_full, 'r') as f:
        order_items_data = json.load(f)
else:
    order_items_data = order_items_full

# Create DataFrames
df_orders = pd.DataFrame(orders_data)
df_order_items = pd.DataFrame(order_items_data)

# Clean IDs: remove leading # and trailing whitespace
def clean_id(id_val):
    if isinstance(id_val, str):
        return id_val.lstrip('#').strip()
    return id_val

df_orders['Id_clean'] = df_orders['Id'].apply(clean_id)
df_orders['OwnerId_clean'] = df_orders['OwnerId'].apply(clean_id)
df_order_items['OrderId_clean'] = df_order_items['OrderId'].apply(clean_id)

# Merge orders with order items
df_merged = df_orders.merge(
    df_order_items, 
    left_on='Id_clean', 
    right_on='OrderId_clean', 
    how='inner',
    suffixes=('_order', '_item')
)

# Calculate sales amount per order item
df_merged['Quantity'] = pd.to_numeric(df_merged['Quantity'])
df_merged['UnitPrice'] = pd.to_numeric(df_merged['UnitPrice'])
df_merged['SalesAmount'] = df_merged['Quantity'] * df_merged['UnitPrice']

# Sum sales per agent (OwnerId)
agent_sales = df_merged.groupby('OwnerId_clean')['SalesAmount'].sum()

# Find top agent
top_agent_id = agent_sales.idxmax()
top_agent_sales = agent_sales.max()

print("__RESULT__:")
print(json.dumps({
    'top_agent_id': top_agent_id
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'CompanySignedDate': '2023-07-02'}], 'var_functions.list_db:2': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:6': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_functions.query_db:8': [{'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01'}, {'Id': '#801Wt00000PGbLTIA1', 'OwnerId': '005Wt000003NFRKIA4', 'EffectiveDate': '2022-09-01'}, {'Id': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01'}, {'Id': '#801Wt00000PGtiAIAT', 'OwnerId': '005Wt000003NIljIAG', 'EffectiveDate': '2022-10-15'}, {'Id': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01'}, {'Id': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01'}], 'var_functions.query_db:10': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Quantity': '15.0', 'UnitPrice': '476.991'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Quantity': '3.0', 'UnitPrice': '549.99'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Quantity': '9.0', 'UnitPrice': '503.4905'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Quantity': '10.0', 'UnitPrice': '476.991'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Quantity': '1.0', 'UnitPrice': '299.99'}, {'Id': '802Wt0000078xACIAY', 'OrderId': '#801Wt00000PH48GIAT', 'Quantity': '12.0', 'UnitPrice': '494.991'}, {'Id': '#802Wt0000078xADIAY', 'OrderId': '801Wt00000PFyIUIA1', 'Quantity': '12.0', 'UnitPrice': '305.991'}, {'Id': '802Wt0000078xAEIAY', 'OrderId': '801Wt00000PGyzXIAT', 'Quantity': '12.0', 'UnitPrice': '431.991'}, {'Id': '802Wt0000078xAFIAY', 'OrderId': '801Wt00000PHWhpIAH', 'Quantity': '6.0', 'UnitPrice': '569.9905'}, {'Id': '802Wt0000078xq6IAA', 'OrderId': '#801Wt00000PFt7UIAT', 'Quantity': '8.0', 'UnitPrice': '569.9905'}], 'var_functions.execute_python:12': {'orders_count': 10, 'order_items_count': 10}, 'var_functions.query_db:14': [{'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'type': 'list', 'length': 689}}

exec(code, env_args)
