code = """import json, pandas as pd

# Load contract account ids (already small)
acct = pd.DataFrame(var_call_ebt2NYJTuPDdlUX7Kbk5JYbv)
acct_ids = set(acct['AccountIdClean'].dropna().astype(str).str.replace('#','', regex=False).str.strip())

# Load orders
orders_src = var_call_9FDrrmMIlsYFylFuy0qNOOzp
if isinstance(orders_src, str):
    with open(orders_src, 'r') as f:
        orders = json.load(f)
else:
    orders = orders_src
orders_df = pd.DataFrame(orders)
orders_df['AccountIdClean'] = orders_df['AccountIdClean'].astype(str).str.replace('#','', regex=False).str.strip()
orders_df['OrderIdClean'] = orders_df['OrderIdClean'].astype(str).str.replace('#','', regex=False).str.strip()
orders_df['OwnerIdClean'] = orders_df['OwnerId'].astype(str).str.replace('#','', regex=False).str.strip()
orders_f = orders_df[orders_df['AccountIdClean'].isin(acct_ids)][['OrderIdClean','OwnerIdClean']]

# Load order items
items_src = var_call_3dX2RG3AgOfUtXc6vDDebYpc
if isinstance(items_src, str):
    with open(items_src, 'r') as f:
        items = json.load(f)
else:
    items = items_src
items_df = pd.DataFrame(items)
items_df['OrderIdClean'] = items_df['OrderIdClean'].astype(str).str.replace('#','', regex=False).str.strip()
items_df['Quantity'] = pd.to_numeric(items_df['Quantity'], errors='coerce').fillna(0)
items_df['UnitPrice'] = pd.to_numeric(items_df['UnitPrice'], errors='coerce').fillna(0)
items_df['Sales'] = items_df['Quantity'] * items_df['UnitPrice']

# Join and aggregate
merged = items_df.merge(orders_f, on='OrderIdClean', how='inner')
agg = merged.groupby('OwnerIdClean', as_index=False)['Sales'].sum()
agg = agg.sort_values('Sales', ascending=False)
agent_id = None
if len(agg):
    agent_id = agg.iloc[0]['OwnerIdClean']

print('__RESULT__:')
print(json.dumps({'AgentId': agent_id}))"""

env_args = {'var_call_ebt2NYJTuPDdlUX7Kbk5JYbv': [{'AccountIdClean': '001Wt00000PGtdJIAT'}, {'AccountIdClean': '001Wt00000PGYx5IAH'}, {'AccountIdClean': '001Wt00000PHVtpIAH'}, {'AccountIdClean': '001Wt00000PHVqdIAH'}, {'AccountIdClean': '001Wt00000PHHXXIA5'}, {'AccountIdClean': '001Wt00000PGZZoIAP'}, {'AccountIdClean': '001Wt00000PGZmfIAH'}, {'AccountIdClean': '001Wt00000PGovMIAT'}, {'AccountIdClean': '001Wt00000PGtdJIAT'}, {'AccountIdClean': '001Wt00000PGRnYIAX'}, {'AccountIdClean': '001Wt00000PGzM9IAL'}, {'AccountIdClean': '001Wt00000PGdzxIAD'}, {'AccountIdClean': '001Wt00000PHRTfIAP'}, {'AccountIdClean': '001Wt00000PFsjOIAT'}, {'AccountIdClean': '001Wt00000PGzSaIAL'}, {'AccountIdClean': '001Wt00000PHVtpIAH'}], 'var_call_9FDrrmMIlsYFylFuy0qNOOzp': 'file_storage/call_9FDrrmMIlsYFylFuy0qNOOzp.json', 'var_call_3dX2RG3AgOfUtXc6vDDebYpc': 'file_storage/call_3dX2RG3AgOfUtXc6vDDebYpc.json'}

exec(code, env_args)
