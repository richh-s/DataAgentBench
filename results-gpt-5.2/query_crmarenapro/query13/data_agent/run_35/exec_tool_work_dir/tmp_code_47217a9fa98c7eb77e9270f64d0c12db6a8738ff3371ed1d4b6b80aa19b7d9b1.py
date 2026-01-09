code = """import json, pandas as pd

# Load orders sales (may be file path)
orders_src = var_call_G58qx69O6v9aF7VbdynLnVKo
if isinstance(orders_src, str):
    with open(orders_src, 'r', encoding='utf-8') as f:
        orders = json.load(f)
else:
    orders = orders_src

contracts = var_call_N59oYat67ZFlH68ViwtCqiQW

df_orders = pd.DataFrame(orders)
df_contracts = pd.DataFrame(contracts)

# normalize ids by removing leading '#'
for col in ['AccountId','AgentId']:
    if col in df_orders.columns:
        df_orders[col] = df_orders[col].astype(str).str.replace('#','', regex=False).str.strip()

df_contracts['AccountId'] = df_contracts['AccountId'].astype(str).str.replace('#','', regex=False).str.strip()

eligible_accounts = set(df_contracts['AccountId'].dropna().unique().tolist())

# filter orders to eligible accounts
f = df_orders[df_orders['AccountId'].isin(eligible_accounts)].copy()

# sum per agent
f['OrderSales'] = pd.to_numeric(f['OrderSales'], errors='coerce').fillna(0.0)
res = f.groupby('AgentId', as_index=False)['OrderSales'].sum().sort_values('OrderSales', ascending=False).head(1)
agent_id = None
if len(res):
    agent_id = res.iloc[0]['AgentId']

print('__RESULT__:')
print(json.dumps({'AgentId': agent_id}))"""

env_args = {'var_call_G58qx69O6v9aF7VbdynLnVKo': 'file_storage/call_G58qx69O6v9aF7VbdynLnVKo.json', 'var_call_N59oYat67ZFlH68ViwtCqiQW': [{'ContractId': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'ContractId': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'ContractId': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'ContractId': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'ContractId': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'ContractId': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'ContractId': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'ContractId': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'ContractId': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'ContractId': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'ContractId': '#800Wt00000DE9ITIA1', 'AccountId': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'ContractId': '#800Wt00000DE9SAIA1', 'AccountId': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'ContractId': '800Wt00000DE9YbIAL', 'AccountId': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'ContractId': '#800Wt00000DE9lVIAT', 'AccountId': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'ContractId': '800Wt00000DE9qLIAT', 'AccountId': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'ContractId': '800Wt00000DE9rxIAD', 'AccountId': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}]}

exec(code, env_args)
