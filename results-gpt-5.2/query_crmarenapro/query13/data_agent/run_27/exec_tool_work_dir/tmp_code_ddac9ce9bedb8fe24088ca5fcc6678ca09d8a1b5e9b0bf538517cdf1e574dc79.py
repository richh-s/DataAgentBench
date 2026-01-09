code = """import json, pandas as pd

orders = pd.DataFrame(var_call_mx7Xxkf3fsHsX1u0ccfS1p1l)

# Load full OrderItem list
path = var_call_hqoX81z84bidIoYskkSx4dga
with open(path, 'r') as f:
    order_items = pd.DataFrame(json.load(f))

# Normalize IDs: strip leading '#' and whitespace
for col in ['Id','AccountId','OwnerId']:
    if col in orders.columns:
        orders[col] = orders[col].astype(str).str.strip().str.lstrip('#')
order_items['OrderId'] = order_items['OrderId'].astype(str).str.strip().str.lstrip('#')

# Numeric conversions
order_items['Quantity'] = pd.to_numeric(order_items['Quantity'], errors='coerce').fillna(0)
order_items['UnitPrice'] = pd.to_numeric(order_items['UnitPrice'], errors='coerce').fillna(0)
order_items['sales_amount'] = order_items['Quantity'] * order_items['UnitPrice']

# Join order_items -> orders and aggregate by OwnerId (agent)
merged = order_items.merge(orders[['Id','OwnerId']], left_on='OrderId', right_on='Id', how='inner')
agg = merged.groupby('OwnerId', as_index=False)['sales_amount'].sum()
agg = agg.sort_values(['sales_amount','OwnerId'], ascending=[False, True])

agent_id = None
if len(agg) > 0:
    agent_id = agg.iloc[0]['OwnerId']

print('__RESULT__:')
print(json.dumps({'agent_id': agent_id}))"""

env_args = {'var_call_mx7Xxkf3fsHsX1u0ccfS1p1l': [{'Id': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10'}, {'Id': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01'}, {'Id': '#801Wt00000PGbLTIA1', 'AccountId': '001Wt00000PHHXXIA5', 'OwnerId': '005Wt000003NFRKIA4', 'EffectiveDate': '2022-09-01'}, {'Id': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'OwnerId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01'}, {'Id': '#801Wt00000PGtiAIAT', 'AccountId': '#001Wt00000PGdzxIAD', 'OwnerId': '005Wt000003NIljIAG', 'EffectiveDate': '2022-10-15'}, {'Id': '801Wt00000PH4FMIA1', 'AccountId': '#001Wt00000PGZmfIAH', 'OwnerId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01'}, {'Id': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'OwnerId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01'}, {'Id': '801Wt00000PHHhDIAX', 'AccountId': '#001Wt00000PHVtpIAH', 'OwnerId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01'}, {'Id': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15'}, {'Id': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'OwnerId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01'}, {'Id': '#801Wt00000PHVkDIAX', 'AccountId': '001Wt00000PGZZoIAP', 'OwnerId': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15'}, {'Id': '801Wt00000PHVqfIAH', 'AccountId': '#001Wt00000PGzM9IAL', 'OwnerId': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20'}, {'Id': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'OwnerId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25'}], 'var_call_hqoX81z84bidIoYskkSx4dga': 'file_storage/call_hqoX81z84bidIoYskkSx4dga.json'}

exec(code, env_args)
