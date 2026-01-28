code = """import json, pandas as pd

# Load large json lists
orders_path = var_call_52vYWyAKdBpC5XGpgVaAyD1P
items_path = var_call_9ANeZTaXK8202a3wupYFWBxf

with open(orders_path, 'r') as f:
    orders = json.load(f)
with open(items_path, 'r') as f:
    items = json.load(f)
contracts = var_call_ISbXW8UwamAfLAYRmwSYvFvh

def norm(s):
    if s is None:
        return None
    return str(s).replace('#','').strip()

contracts_df = pd.DataFrame(contracts)
contracts_df['AccountId_n'] = contracts_df['AccountId'].map(norm)
eligible_accounts = set(contracts_df['AccountId_n'].dropna().unique().tolist())

orders_df = pd.DataFrame(orders)
orders_df['OrderId_n'] = orders_df['OrderId'].map(norm)
orders_df['AccountId_n'] = orders_df['AccountId'].map(norm)
orders_df['OwnerId_n'] = orders_df['OwnerId'].map(norm)
orders_eligible = orders_df[orders_df['AccountId_n'].isin(eligible_accounts)][['OrderId_n','OwnerId_n']]

items_df = pd.DataFrame(items)
items_df['OrderId_n'] = items_df['OrderId'].map(norm)
items_df['Quantity'] = pd.to_numeric(items_df['Quantity'], errors='coerce')
items_df['UnitPrice'] = pd.to_numeric(items_df['UnitPrice'], errors='coerce')
items_df['Sales'] = items_df['Quantity'] * items_df['UnitPrice']

merged = items_df.merge(orders_eligible, on='OrderId_n', how='inner')
by_agent = merged.groupby('OwnerId_n', dropna=True)['Sales'].sum().reset_index()
by_agent = by_agent.sort_values('Sales', ascending=False)

top_agent = None
if len(by_agent) > 0:
    top_agent = by_agent.iloc[0]['OwnerId_n']

print('__RESULT__:')
print(json.dumps({'top_agent_id': top_agent}))"""

env_args = {'var_call_52vYWyAKdBpC5XGpgVaAyD1P': 'file_storage/call_52vYWyAKdBpC5XGpgVaAyD1P.json', 'var_call_9ANeZTaXK8202a3wupYFWBxf': 'file_storage/call_9ANeZTaXK8202a3wupYFWBxf.json', 'var_call_ISbXW8UwamAfLAYRmwSYvFvh': [{'Id': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'AccountId': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'AccountId': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'AccountId': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'AccountId': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'AccountId': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'AccountId': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}]}

exec(code, env_args)
