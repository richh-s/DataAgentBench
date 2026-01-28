code = """import json, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

def norm_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

contracts = pd.DataFrame(load(var_call_ZdmH6ViiEvaFJbsBlnb5Jkso))
opps = pd.DataFrame(load(var_call_lYDzG9PyiWngOgzD3cJSJWtv))
order_items = pd.DataFrame(load(var_call_FhCdaPF77JYZ8B1oxqj4NWlY))
orders = pd.DataFrame(load(var_call_qWuH9oSBohlDBISHr1duK8S8))

contracts['contract_id_n'] = contracts['contract_id'].map(norm_id)
contracts['account_id_n'] = contracts['contract_account_id'].map(norm_id)

opps['contract_id_n'] = opps['contract_id'].map(norm_id)
opps['agent_id_n'] = opps['agent_id'].map(norm_id)

# eligible accounts via opportunities linked to eligible contracts
eligible_opps = opps.merge(contracts[['contract_id_n']], on='contract_id_n', how='inner')
eligible_accounts = set(eligible_opps.merge(contracts[['contract_id_n','account_id_n']], on='contract_id_n', how='left')['account_id_n'].dropna().unique())

orders['order_id_n'] = orders['order_id'].map(norm_id)
orders['account_id_n'] = orders['account_id'].map(norm_id)

eligible_orders = orders[orders['account_id_n'].isin(eligible_accounts)][['order_id_n']]

order_items['order_id_n'] = order_items['order_id'].map(norm_id)
order_items['agent_id_n'] = order_items['agent_id'].map(norm_id)
order_items['Quantity'] = pd.to_numeric(order_items['Quantity'], errors='coerce')
order_items['UnitPrice'] = pd.to_numeric(order_items['UnitPrice'], errors='coerce')
order_items['sales_amount'] = order_items['Quantity'].fillna(0) * order_items['UnitPrice'].fillna(0)

eligible_items = order_items.merge(eligible_orders, on='order_id_n', how='inner')

sales_by_agent = eligible_items.groupby('agent_id_n', dropna=True)['sales_amount'].sum().reset_index()
sales_by_agent = sales_by_agent.sort_values(['sales_amount','agent_id_n'], ascending=[False, True])

best_agent = None
if len(sales_by_agent) > 0:
    best_agent = sales_by_agent.iloc[0]['agent_id_n']

print('__RESULT__:')
print(json.dumps(best_agent))"""

env_args = {'var_call_ZdmH6ViiEvaFJbsBlnb5Jkso': [{'contract_id': '800Wt00000DDNlnIAH', 'contract_account_id': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'contract_id': '800Wt00000DDe3OIAT', 'contract_account_id': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'contract_id': '800Wt00000DDeg6IAD', 'contract_account_id': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'contract_id': '800Wt00000DDzZLIA1', 'contract_account_id': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'contract_id': '#800Wt00000DDzvrIAD', 'contract_account_id': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'contract_id': '800Wt00000DE0FHIA1', 'contract_account_id': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'contract_id': '800Wt00000DE0TiIAL', 'contract_account_id': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'contract_id': '800Wt00000DE2vLIAT', 'contract_account_id': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'contract_id': '800Wt00000DE98oIAD', 'contract_account_id': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'contract_id': '800Wt00000DE9GrIAL', 'contract_account_id': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'contract_id': '#800Wt00000DE9ITIA1', 'contract_account_id': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'contract_id': '#800Wt00000DE9SAIA1', 'contract_account_id': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'contract_id': '800Wt00000DE9YbIAL', 'contract_account_id': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'contract_id': '#800Wt00000DE9lVIAT', 'contract_account_id': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'contract_id': '800Wt00000DE9qLIAT', 'contract_account_id': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'contract_id': '800Wt00000DE9rxIAD', 'contract_account_id': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}], 'var_call_lYDzG9PyiWngOgzD3cJSJWtv': 'file_storage/call_lYDzG9PyiWngOgzD3cJSJWtv.json', 'var_call_FhCdaPF77JYZ8B1oxqj4NWlY': 'file_storage/call_FhCdaPF77JYZ8B1oxqj4NWlY.json', 'var_call_qWuH9oSBohlDBISHr1duK8S8': 'file_storage/call_qWuH9oSBohlDBISHr1duK8S8.json'}

exec(code, env_args)
