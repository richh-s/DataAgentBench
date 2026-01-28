code = """import json, pandas as pd

orders = pd.DataFrame(var_call_YXYvH8E3LT9vbdW5Z9yXxRpb)
# load large orderitems
path = var_call_rinfOE96imiP8qtfG1qlKPRr
with open(path, 'r') as f:
    orderitems = pd.DataFrame(json.load(f))

# normalize ids by stripping leading '#'
def norm(s):
    if pd.isna(s):
        return s
    return str(s).lstrip('#').strip()

orders['OrderId_norm'] = orders['OrderId'].map(norm)
orders['AgentId_norm'] = orders['AgentId'].map(norm)
orderitems['OrderId_norm'] = orderitems['OrderId'].map(norm)

# numeric
orderitems['Quantity'] = pd.to_numeric(orderitems['Quantity'], errors='coerce')
orderitems['UnitPrice'] = pd.to_numeric(orderitems['UnitPrice'], errors='coerce')
orderitems['Sales'] = orderitems['Quantity'] * orderitems['UnitPrice']

merged = orders.merge(orderitems[['OrderId_norm','Sales']], on='OrderId_norm', how='inner')
agg = merged.groupby('AgentId_norm', as_index=False)['Sales'].sum()
agg = agg.sort_values('Sales', ascending=False)

top_agent = None
if len(agg):
    top_agent = agg.iloc[0]['AgentId_norm']

print('__RESULT__:')
print(json.dumps(top_agent))"""

env_args = {'var_call_ZzYKR6zCYh1AyAV2Xu2q1McU': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}], 'var_call_YXYvH8E3LT9vbdW5Z9yXxRpb': [{'OrderId': '#801Wt00000PFt7UIAT', 'AccountId': '001Wt00000PGzSaIAL', 'AgentId': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PFyITIA1', 'AccountId': '001Wt00000PGRnYIAX', 'AgentId': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10'}, {'OrderId': '801Wt00000PGGhBIAX', 'AccountId': '001Wt00000PHVtpIAH', 'AgentId': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01'}, {'OrderId': '#801Wt00000PGbLTIA1', 'AccountId': '001Wt00000PHHXXIA5', 'AgentId': '005Wt000003NFRKIA4', 'EffectiveDate': '2022-09-01'}, {'OrderId': '#801Wt00000PGbdMIAT', 'AccountId': '#001Wt00000PGZgHIAX', 'AgentId': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PGtiAIAT', 'AccountId': '#001Wt00000PGdzxIAD', 'AgentId': '005Wt000003NIljIAG', 'EffectiveDate': '2022-10-15'}, {'OrderId': '801Wt00000PH4FMIA1', 'AccountId': '#001Wt00000PGZmfIAH', 'AgentId': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PH8yvIAD', 'AccountId': '001Wt00000PGovMIAT', 'AgentId': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHMFIA5', 'AccountId': '001Wt00000PFsjOIAT', 'AgentId': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01'}, {'OrderId': '801Wt00000PHHhDIAX', 'AccountId': '#001Wt00000PHVtpIAH', 'AgentId': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01'}, {'OrderId': '801Wt00000PHLzNIAX', 'AccountId': '001Wt00000PGtdJIAT', 'AgentId': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15'}, {'OrderId': '801Wt00000PHRFAIA5', 'AccountId': '001Wt00000PGdwiIAD', 'AgentId': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01'}, {'OrderId': '#801Wt00000PHVkDIAX', 'AccountId': '001Wt00000PGZZoIAP', 'AgentId': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15'}, {'OrderId': '801Wt00000PHVqfIAH', 'AccountId': '#001Wt00000PGzM9IAL', 'AgentId': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20'}, {'OrderId': '#801Wt00000PHWptIAH', 'AccountId': '#001Wt00000PGYx5IAH', 'AgentId': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25'}], 'var_call_rinfOE96imiP8qtfG1qlKPRr': 'file_storage/call_rinfOE96imiP8qtfG1qlKPRr.json'}

exec(code, env_args)
