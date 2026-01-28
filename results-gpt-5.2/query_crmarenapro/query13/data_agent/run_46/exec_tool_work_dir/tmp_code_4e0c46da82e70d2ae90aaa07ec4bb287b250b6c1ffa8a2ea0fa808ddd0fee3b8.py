code = """import json, pandas as pd
from datetime import date

def load_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r') as f:
            return json.load(f)
    return path_or_obj

def norm_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

contracts = pd.DataFrame(load_maybe(var_call_kYi0B57ScXH6xYlDBhO0XNUp))
contract_ids = set(contracts['Id'].map(norm_id))

opp = pd.DataFrame(load_maybe(var_call_R0vdz8ELSdsCq7TwZyTw82DZ))
opp['ContractNorm'] = opp['ContractID__c'].map(norm_id)
opp = opp[opp['ContractNorm'].isin(contract_ids)]
opp_ids = set(opp['Id'].map(norm_id))

orders = pd.DataFrame(load_maybe(var_call_lPhOW8dveU6WKvcFBmZSb59e))
orders['OrderNorm'] = orders['OrderId'].map(norm_id)
orders['AccountNorm'] = orders['AccountId'].map(norm_id)
orders['EffDate'] = pd.to_datetime(orders['EffectiveDate'], errors='coerce').dt.date
orders = orders.dropna(subset=['EffDate'])
start = date(2022,6,25)
end = date(2022,11,25)
orders = orders[(orders['EffDate']>=start) & (orders['EffDate']<=end)]

# eligible orders are those whose AccountId matches any eligible contract's AccountId
eligible_accounts = set(contracts['AccountId'].map(norm_id))
orders = orders[orders['AccountNorm'].isin(eligible_accounts)]
eligible_order_ids = set(orders['OrderNorm'])

items = pd.DataFrame(load_maybe(var_call_i4HBUxA4GM3gkbdErQJIfxOi))
items['OrderNorm'] = items['OrderId'].map(norm_id)
items['AgentNorm'] = items['AgentId'].map(norm_id)
items = items[items['OrderNorm'].isin(eligible_order_ids)]

items['Quantity'] = pd.to_numeric(items['Quantity'], errors='coerce')
items['UnitPrice'] = pd.to_numeric(items['UnitPrice'], errors='coerce')
items['Sales'] = items['Quantity'] * items['UnitPrice']

grp = items.groupby('AgentNorm', dropna=True)['Sales'].sum().sort_values(ascending=False)
agent_id = None
if len(grp):
    agent_id = grp.index[0]

print('__RESULT__:')
print(json.dumps(agent_id))"""

env_args = {'var_call_kYi0B57ScXH6xYlDBhO0XNUp': [{'Id': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'AccountId': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'AccountId': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'AccountId': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'AccountId': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'AccountId': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'AccountId': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}], 'var_call_R0vdz8ELSdsCq7TwZyTw82DZ': 'file_storage/call_R0vdz8ELSdsCq7TwZyTw82DZ.json', 'var_call_i4HBUxA4GM3gkbdErQJIfxOi': 'file_storage/call_i4HBUxA4GM3gkbdErQJIfxOi.json', 'var_call_lPhOW8dveU6WKvcFBmZSb59e': 'file_storage/call_lPhOW8dveU6WKvcFBmZSb59e.json'}

exec(code, env_args)
