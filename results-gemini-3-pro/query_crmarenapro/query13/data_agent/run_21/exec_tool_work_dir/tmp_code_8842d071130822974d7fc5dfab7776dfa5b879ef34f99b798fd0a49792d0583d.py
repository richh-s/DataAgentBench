code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-10444868833285863650'], 'r') as f:
    orders = json.load(f)
with open(locals()['var_function-call-10444868833285861675'], 'r') as f:
    order_items = json.load(f)

# Convert to DataFrame
df_orders = pd.DataFrame(orders)
df_items = pd.DataFrame(order_items)

# Clean IDs
def clean_id(x):
    if isinstance(x, str) and x.startswith('#'):
        return x[1:]
    return x

df_orders['Id'] = df_orders['Id'].apply(clean_id)
df_orders['OwnerId'] = df_orders['OwnerId'].apply(clean_id)
df_items['OrderId'] = df_items['OrderId'].apply(clean_id)

# Convert types
df_items['Quantity'] = pd.to_numeric(df_items['Quantity'])
df_items['UnitPrice'] = pd.to_numeric(df_items['UnitPrice'])

# Filter Orders by date
# Today: 2022-11-25. Past 5 months: 2022-06-25 to 2022-11-25.
start_date = '2022-06-25'
end_date = '2022-11-25'

# EffectiveDate is string YYYY-MM-DD
df_orders = df_orders[(df_orders['EffectiveDate'] >= start_date) & (df_orders['EffectiveDate'] <= end_date)]

# Merge
merged = pd.merge(df_orders, df_items, left_on='Id', right_on='OrderId', how='inner')

# Calculate Sales
merged['Sales'] = merged['Quantity'] * merged['UnitPrice']

# Group by OwnerId (Agent)
agent_sales = merged.groupby('OwnerId')['Sales'].sum().reset_index()

# Find top agent
if not agent_sales.empty:
    top_agent = agent_sales.sort_values(by='Sales', ascending=False).iloc[0]
    result = top_agent['OwnerId']
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8776708676778769183': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-8776708676778768470': [{'Id': '802Wt0000078wz3IAA', 'OrderId': '801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVTJIA2', 'Quantity': '15.0', 'UnitPrice': '476.991', 'PriceBookEntryId': '01uWt0000027Pa1IAE'}], 'var_function-call-15341048569440494199': [{'COUNT(*)': '163'}], 'var_function-call-15341048569440495182': [{'COUNT(*)': '689'}], 'var_function-call-10444868833285863650': 'file_storage/function-call-10444868833285863650.json', 'var_function-call-10444868833285861675': 'file_storage/function-call-10444868833285861675.json'}

exec(code, env_args)
