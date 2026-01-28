code = """import json
import pandas as pd

# Load orders from past 5 months
orders_data = locals().get('var_functions.query_db:0', [])
if isinstance(orders_data, str):
    # If it's a file path, load from file
    with open(orders_data, 'r') as f:
        orders_data = json.load(f)

# Load order items
order_items_file = locals().get('var_functions.query_db:2')
order_items_data = []
if order_items_file and isinstance(order_items_file, str):
    with open(order_items_file, 'r') as f:
        order_items_data = json.load(f)

# Convert to DataFrames
orders_df = pd.DataFrame(orders_data)
order_items_df = pd.DataFrame(order_items_data)

# Clean ID fields - remove leading # and trailing whitespace
def clean_id(id_value):
    if id_value is None:
        return None
    return str(id_value).replace('#', '').strip()

# Clean the ID fields that we'll use for joining
orders_df['Id_clean'] = orders_df['Id'].apply(clean_id)
orders_df['OwnerId_clean'] = orders_df['OwnerId'].apply(clean_id)
order_items_df['OrderId_clean'] = order_items_df['OrderId'].apply(clean_id)

# Convert Quantity and UnitPrice to numeric
order_items_df['Quantity'] = pd.to_numeric(order_items_df['Quantity'], errors='coerce')
order_items_df['UnitPrice'] = pd.to_numeric(order_items_df['UnitPrice'], errors='coerce')

# Merge orders with order items
merged_df = pd.merge(orders_df, order_items_df, left_on='Id_clean', right_on='OrderId_clean', how='inner')

# Calculate sales amount for each order item
merged_df['SalesAmount'] = merged_df['Quantity'] * merged_df['UnitPrice']

# Group by OwnerId (agent) and sum sales amounts
agent_sales = merged_df.groupby('OwnerId_clean')['SalesAmount'].sum().reset_index()

# Sort by sales amount descending and get top agent
top_agent = agent_sales.sort_values('SalesAmount', ascending=False).head(1)

if not top_agent.empty:
    top_agent_id = top_agent.iloc[0]['OwnerId_clean']
    top_agent_sales = top_agent.iloc[0]['SalesAmount']
    result = top_agent_id
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'Status': 'Activated', 'EffectiveDate': '2022-07-10', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'Status': 'Activated', 'EffectiveDate': '2022-10-01', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'AccountId': '001Wt00000PHHXXIA5', 'Status': 'Activated', 'EffectiveDate': '2022-09-01', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'AccountId': '#001Wt00000PGdzxIAD', 'Status': 'Activated', 'EffectiveDate': '2022-10-15', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'AccountId': '#001Wt00000PGZmfIAH', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'AccountId': '#001Wt00000PHVtpIAH', 'Status': 'Activated', 'EffectiveDate': '2022-08-01', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'Status': 'Activated  ', 'EffectiveDate': '2022-09-15', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2022-08-15', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'AccountId': '#001Wt00000PGzM9IAL', 'Status': 'Activated ', 'EffectiveDate': '2022-09-20', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'Status': 'Activated', 'EffectiveDate': '2022-09-25', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
