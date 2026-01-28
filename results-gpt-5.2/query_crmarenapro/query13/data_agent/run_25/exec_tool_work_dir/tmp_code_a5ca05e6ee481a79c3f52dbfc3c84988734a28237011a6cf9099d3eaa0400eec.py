code = """import json, pandas as pd, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

def norm_id(x):
    if x is None:
        return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x.strip()

contracts = pd.DataFrame(load_records(var_call_P3bOYtXk7GSJru0XRTwlRrlt))
contracts['ContractId_n'] = contracts['ContractId'].map(norm_id)
eligible_contracts = set(contracts['ContractId_n'].dropna().unique())

opps = pd.DataFrame(load_records(var_call_V8UuKXdNAKnC1WIMVvCSct5j))
opps['ContractID__c_n'] = opps['ContractID__c'].map(norm_id)
opps_elig = opps[opps['ContractID__c_n'].isin(eligible_contracts)].copy()
opps_elig['OwnerId_n'] = opps_elig['OwnerId'].map(norm_id)
elig_owner_ids = set(opps_elig['OwnerId_n'].dropna().unique())

orders = pd.DataFrame(load_records(var_call_D6bshUk8STJJGryewgZtlpT8))
orderitems = pd.DataFrame(load_records(var_call_606a5HgUf96q07GGrQz9hZP2))
orders['OrderId_n'] = orders['OrderId'].map(norm_id)
orders['OwnerId_n'] = orders['OwnerId'].map(norm_id)
orderitems['OrderId_n'] = orderitems['OrderId'].map(norm_id)
orderitems['Quantity'] = pd.to_numeric(orderitems['Quantity'], errors='coerce').fillna(0)
orderitems['UnitPrice'] = pd.to_numeric(orderitems['UnitPrice'], errors='coerce').fillna(0)
orderitems['SalesAmount'] = orderitems['Quantity'] * orderitems['UnitPrice']

sales_by_order = orderitems.groupby('OrderId_n', as_index=False)['SalesAmount'].sum()
merged = orders.merge(sales_by_order, on='OrderId_n', how='left')
merged['SalesAmount'] = merged['SalesAmount'].fillna(0)
merged_elig = merged[merged['OwnerId_n'].isin(elig_owner_ids)]

sales_by_agent = merged_elig.groupby('OwnerId_n', as_index=False)['SalesAmount'].sum().sort_values('SalesAmount', ascending=False)

agent_id = None
if len(sales_by_agent) > 0:
    agent_id = sales_by_agent.iloc[0]['OwnerId_n']

print('__RESULT__:')
print(json.dumps({'agent_id': agent_id}))"""

env_args = {'var_call_D6bshUk8STJJGryewgZtlpT8': 'file_storage/call_D6bshUk8STJJGryewgZtlpT8.json', 'var_call_606a5HgUf96q07GGrQz9hZP2': 'file_storage/call_606a5HgUf96q07GGrQz9hZP2.json', 'var_call_P3bOYtXk7GSJru0XRTwlRrlt': [{'ContractId': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'ContractId': '800Wt00000DDe3OIAT', 'CompanySignedDate': '2022-09-20'}, {'ContractId': '800Wt00000DDeg6IAD', 'CompanySignedDate': '2022-07-18'}, {'ContractId': '800Wt00000DDzZLIA1', 'CompanySignedDate': '2022-10-26'}, {'ContractId': '#800Wt00000DDzvrIAD', 'CompanySignedDate': '2022-08-30'}, {'ContractId': '800Wt00000DE0FHIA1', 'CompanySignedDate': '2022-08-02'}, {'ContractId': '800Wt00000DE0TiIAL', 'CompanySignedDate': '2022-09-10'}, {'ContractId': '800Wt00000DE2vLIAT', 'CompanySignedDate': '2022-06-29'}, {'ContractId': '800Wt00000DE98oIAD', 'CompanySignedDate': '2022-11-10'}, {'ContractId': '800Wt00000DE9GrIAL', 'CompanySignedDate': '2022-06-30'}, {'ContractId': '#800Wt00000DE9ITIA1', 'CompanySignedDate': '2022-09-11'}, {'ContractId': '#800Wt00000DE9SAIA1', 'CompanySignedDate': '2022-09-30'}, {'ContractId': '800Wt00000DE9YbIAL', 'CompanySignedDate': '2022-11-22'}, {'ContractId': '#800Wt00000DE9lVIAT', 'CompanySignedDate': '2022-06-26'}, {'ContractId': '800Wt00000DE9qLIAT', 'CompanySignedDate': '2022-09-01'}, {'ContractId': '800Wt00000DE9rxIAD', 'CompanySignedDate': '2022-09-19'}], 'var_call_V8UuKXdNAKnC1WIMVvCSct5j': 'file_storage/call_V8UuKXdNAKnC1WIMVvCSct5j.json'}

exec(code, env_args)
