code = """import json
import pandas as pd

# Load orders data 
orders_result = locals().get('var_functions.query_db:8')
if isinstance(orders_result, str):
    with open(orders_result, 'r') as f:
        orders_result = json.load(f)

# Load order items data
order_items_file = locals().get('var_functions.query_db:2')
order_items_result = []
if order_items_file and isinstance(order_items_file, str):
    with open(order_items_file, 'r') as f:
        order_items_result = json.load(f)

# Debug: check the first few records
print("Orders sample:", orders_result[:3])
print("OrderItems sample:", order_items_result[:3])

# Convert to DataFrames
orders_df = pd.DataFrame(orders_result)
order_items_df = pd.DataFrame(order_items_result)

print(f"Orders count: {len(orders_df)}")
print(f"OrderItems count: {len(order_items_df)}")

# Clean ID fields - remove leading # and trim whitespace
def clean_id(id_value):
    if id_value is None:
        return None
    return str(id_value).lstrip('#').strip()

orders_df['OrderId_clean'] = orders_df['Id'].apply(clean_id)
orders_df['OwnerId_clean'] = orders_df['OwnerId'].apply(clean_id)
order_items_df['OrderId_clean'] = order_items_df['OrderId'].apply(clean_id)

# Convert numeric fields in OrderItem
order_items_df['Quantity'] = pd.to_numeric(order_items_df['Quantity'], errors='coerce')
order_items_df['UnitPrice'] = pd.to_numeric(order_items_df['UnitPrice'], errors='coerce')

# Calculate sales amount per order item
order_items_df['SalesAmount'] = order_items_df['Quantity'] * order_items_df['UnitPrice']

# Merge to get OwnerId for each order item
merged_df = pd.merge(order_items_df, orders_df[['OrderId_clean', 'OwnerId_clean']], 
                     on='OrderId_clean', how='inner')

print(f"Merged records count: {len(merged_df)}")

# Group by agent (OwnerId) and sum sales amounts
agent_sales = merged_df.groupby('OwnerId_clean')['SalesAmount'].sum().reset_index()

# Sort to get top agent
top_agents = agent_sales.sort_values('SalesAmount', ascending=False).head(10)
print("Top 10 agents by sales:")
for idx, row in top_agents.iterrows():
    print(f"Agent: {row['OwnerId_clean']}, Sales: {row['SalesAmount']:.2f}")

# Get the top agent
top_agent_id = top_agents.iloc[0]['OwnerId_clean'] if not top_agents.empty else None

print('__RESULT__:')
print(json.dumps(top_agent_id))"""

env_args = {'var_functions.query_db:0': [{'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'Status': 'Activated', 'EffectiveDate': '2022-07-10', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'Status': 'Activated', 'EffectiveDate': '2022-10-01', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'AccountId': '001Wt00000PHHXXIA5', 'Status': 'Activated', 'EffectiveDate': '2022-09-01', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'AccountId': '#001Wt00000PGdzxIAD', 'Status': 'Activated', 'EffectiveDate': '2022-10-15', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'AccountId': '#001Wt00000PGZmfIAH', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'AccountId': '#001Wt00000PHVtpIAH', 'Status': 'Activated', 'EffectiveDate': '2022-08-01', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'Status': 'Activated  ', 'EffectiveDate': '2022-09-15', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'Status': 'Activated', 'EffectiveDate': '2022-07-01', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2022-08-15', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'AccountId': '#001Wt00000PGzM9IAL', 'Status': 'Activated ', 'EffectiveDate': '2022-09-20', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'Status': 'Activated', 'EffectiveDate': '2022-09-25', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': '005Wt000003NIXCIA4', 'var_functions.query_db:5': [{'Id': '005Wt000003NIXCIA4', 'FirstName': 'Zanele', 'LastName': 'Mofokeng   ', 'Email': 'zanele.mofokeng@techagents.com'}], 'var_functions.query_db:8': [{'Id': '#801Wt00000PFt7UIAT', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFyITIA1', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '801Wt00000PGGhBIAX', 'OwnerId': '005Wt000003NIaRIAW'}, {'Id': '#801Wt00000PGbLTIA1', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '#801Wt00000PGbdMIAT', 'OwnerId': '#005Wt000003NGtcIAG'}, {'Id': '#801Wt00000PGtiAIAT', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PH4FMIA1', 'OwnerId': '#005Wt000003NJmbIAG'}, {'Id': '801Wt00000PH8yvIAD', 'OwnerId': '005Wt000003NIXCIA4'}, {'Id': '801Wt00000PHHMFIA5', 'OwnerId': '005Wt000003NJ9uIAG'}, {'Id': '801Wt00000PHHhDIAX', 'OwnerId': '#005Wt000003NITxIAO'}, {'Id': '801Wt00000PHLzNIAX', 'OwnerId': '005Wt000003NEoYIAW'}, {'Id': '801Wt00000PHRFAIA5', 'OwnerId': '#005Wt000003NIx1IAG'}, {'Id': '#801Wt00000PHVkDIAX', 'OwnerId': '005Wt000003NJt3IAG'}, {'Id': '801Wt00000PHVqfIAH', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '#801Wt00000PHWptIAH', 'OwnerId': '005Wt000003NJ0EIAW'}]}

exec(code, env_args)
