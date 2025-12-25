code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-15154852210934147284'], 'r') as f:
    orders_data = json.load(f)
with open(locals()['var_function-call-15154852210934148223'], 'r') as f:
    order_items_data = json.load(f)

# Create DataFrames
df_orders = pd.DataFrame(orders_data)
df_items = pd.DataFrame(order_items_data)

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

df_orders['Id'] = df_orders['Id'].apply(clean_id)
df_orders['OwnerId'] = df_orders['OwnerId'].apply(clean_id)
df_items['OrderId'] = df_items['OrderId'].apply(clean_id)

# Convert dates
df_orders['EffectiveDate'] = pd.to_datetime(df_orders['EffectiveDate'], errors='coerce')

# Filter by date
start_date = pd.Timestamp('2022-06-25')
end_date = pd.Timestamp('2022-11-25')

# Check date range validity
mask = (df_orders['EffectiveDate'] >= start_date) & (df_orders['EffectiveDate'] <= end_date)
df_filtered_orders = df_orders[mask].copy()

# Join with OrderItem
# Merge df_filtered_orders (Id) with df_items (OrderId)
df_merged = pd.merge(df_filtered_orders, df_items, left_on='Id', right_on='OrderId', how='inner')

# Calculate Amount
# UnitPrice and Quantity are strings in the JSON, need conversion
df_merged['Quantity'] = pd.to_numeric(df_merged['Quantity'], errors='coerce')
df_merged['UnitPrice'] = pd.to_numeric(df_merged['UnitPrice'], errors='coerce')
df_merged['Amount'] = df_merged['Quantity'] * df_merged['UnitPrice']

# Group by OwnerId (Agent)
agent_sales = df_merged.groupby('OwnerId')['Amount'].sum().reset_index()
agent_sales = agent_sales.sort_values(by='Amount', ascending=False)

if not agent_sales.empty:
    top_agent = agent_sales.iloc[0]['OwnerId']
    top_amount = agent_sales.iloc[0]['Amount']
else:
    top_agent = None
    top_amount = 0

print("__RESULT__:")
print(json.dumps({"top_agent_id": top_agent, "top_amount": top_amount, "num_orders": len(df_filtered_orders)}))"""

env_args = {'var_function-call-1835607699471333538': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '801Wt00000PFsjQIAT', 'AccountId': '#001Wt00000PHVqdIAH', 'Status': 'Activated', 'EffectiveDate': '2021-09-30', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NGjwIAG'}, {'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'Status': 'Activated', 'EffectiveDate': '2022-09-15', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIiUIAW'}, {'Id': '801Wt00000PFtAmIAL', 'AccountId': '001Wt00000PHVdhIAH', 'Status': 'Activated  ', 'EffectiveDate': '2020-09-01', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NIljIAG'}, {'Id': '801Wt00000PFtAnIAL', 'AccountId': '#001Wt00000PGaNjIAL', 'Status': 'Activated', 'EffectiveDate': '2023-06-01', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NEdJIAW'}], 'var_function-call-1835607699471334947': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}, {'Id': '802Wt0000078wz4IAA', 'OrderId': '801Wt00000PHVkDIAX', 'Product2Id': '01tWt000006hVDBIA2', 'Quantity': '3.0', 'UnitPrice': '549.99', 'PriceBookEntryId': '01uWt0000027PF3IAM'}, {'Id': '802Wt0000078wz5IAA', 'OrderId': '801Wt00000PHQuFIAX', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '9.0', 'UnitPrice': '503.4905', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '802Wt0000078xAAIAY', 'OrderId': '801Wt00000PGHg7IAH', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027P8cIAE'}, {'Id': '#802Wt0000078xABIAY', 'OrderId': '801Wt00000PHVicIAH', 'Product2Id': '01tWt000006hVMrIAM', 'Quantity': '1.0', 'UnitPrice': '299.99', 'PriceBookEntryId': '01uWt0000027POjIAM'}], 'var_function-call-417426447453699731': [{'COUNT(*)': '163'}], 'var_function-call-6806825282377861857': [{'COUNT(*)': '689'}], 'var_function-call-15154852210934147284': 'file_storage/function-call-15154852210934147284.json', 'var_function-call-15154852210934148223': 'file_storage/function-call-15154852210934148223.json'}

exec(code, env_args)
