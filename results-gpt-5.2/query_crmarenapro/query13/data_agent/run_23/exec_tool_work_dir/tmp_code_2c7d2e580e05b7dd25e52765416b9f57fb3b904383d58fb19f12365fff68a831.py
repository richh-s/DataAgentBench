code = """import json, pandas as pd

contracts = pd.DataFrame(var_call_OTxI5HDakXWwgtyl19i0UNdO)

# orders in past 5 months (already filtered)
orders = pd.DataFrame(var_call_0RLl5i5n0SjAg1Cl0bAijB1p)

# load order items full
path = var_call_kGIQahVVke2cY26fo5lK05RZ
with open(path, 'r', encoding='utf-8') as f:
    order_items = pd.DataFrame(json.load(f))

# normalize ids: strip, remove leading '#'
def norm(s):
    if pd.isna(s):
        return s
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

orders['order_id_n'] = orders['order_id'].map(norm)
orders['agent_id_n'] = orders['agent_id'].map(norm)
order_items['order_id_n'] = order_items['order_id'].map(norm)

# compute sales amount per order item
order_items['qty'] = pd.to_numeric(order_items['Quantity'], errors='coerce').fillna(0.0)
order_items['unit'] = pd.to_numeric(order_items['UnitPrice'], errors='coerce').fillna(0.0)
order_items['sales'] = order_items['qty'] * order_items['unit']

# only include order items for eligible orders
eligible_items = order_items.merge(orders[['order_id_n','agent_id_n']], on='order_id_n', how='inner')

a_sales = eligible_items.groupby('agent_id_n', as_index=False)['sales'].sum()

# pick top agent
if len(a_sales)==0:
    top_agent = None
else:
    top_agent = a_sales.sort_values(['sales','agent_id_n'], ascending=[False, True]).iloc[0]['agent_id_n']

print('__RESULT__:')
print(json.dumps(top_agent))"""

env_args = {'var_call_OTxI5HDakXWwgtyl19i0UNdO': [{'contract_id': '800Wt00000DDNlnIAH', 'contract_account_id': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'contract_id': '800Wt00000DDe3OIAT', 'contract_account_id': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'contract_id': '800Wt00000DDeg6IAD', 'contract_account_id': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'contract_id': '800Wt00000DDzZLIA1', 'contract_account_id': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'contract_id': '#800Wt00000DDzvrIAD', 'contract_account_id': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'contract_id': '800Wt00000DE0FHIA1', 'contract_account_id': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'contract_id': '800Wt00000DE0TiIAL', 'contract_account_id': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'contract_id': '800Wt00000DE2vLIAT', 'contract_account_id': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'contract_id': '800Wt00000DE98oIAD', 'contract_account_id': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'contract_id': '800Wt00000DE9GrIAL', 'contract_account_id': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'contract_id': '#800Wt00000DE9ITIA1', 'contract_account_id': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'contract_id': '#800Wt00000DE9SAIA1', 'contract_account_id': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'contract_id': '800Wt00000DE9YbIAL', 'contract_account_id': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'contract_id': '#800Wt00000DE9lVIAT', 'contract_account_id': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'contract_id': '800Wt00000DE9qLIAT', 'contract_account_id': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'contract_id': '800Wt00000DE9rxIAD', 'contract_account_id': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}], 'var_call_ePigh4fXAYf9oXjNKh2oQXXC': 'file_storage/call_ePigh4fXAYf9oXjNKh2oQXXC.json', 'var_call_0RLl5i5n0SjAg1Cl0bAijB1p': [{'order_id': '#801Wt00000PFt7UIAT', 'agent_id': '005Wt000003NIiUIAW', 'EffectiveDate': '2022-09-15'}, {'order_id': '801Wt00000PFyITIA1', 'agent_id': '005Wt000003NDJ0IAO', 'EffectiveDate': '2022-07-10'}, {'order_id': '801Wt00000PGGhBIAX', 'agent_id': '005Wt000003NIaRIAW', 'EffectiveDate': '2022-10-01'}, {'order_id': '#801Wt00000PGbLTIA1', 'agent_id': '005Wt000003NFRKIA4', 'EffectiveDate': '2022-09-01'}, {'order_id': '#801Wt00000PGbdMIAT', 'agent_id': '#005Wt000003NGtcIAG', 'EffectiveDate': '2022-07-01'}, {'order_id': '#801Wt00000PGtiAIAT', 'agent_id': '005Wt000003NIljIAG', 'EffectiveDate': '2022-10-15'}, {'order_id': '801Wt00000PH4FMIA1', 'agent_id': '#005Wt000003NJmbIAG', 'EffectiveDate': '2022-09-15'}, {'order_id': '801Wt00000PH8yvIAD', 'agent_id': '005Wt000003NIXCIA4', 'EffectiveDate': '2022-07-01'}, {'order_id': '801Wt00000PHHMFIA5', 'agent_id': '005Wt000003NJ9uIAG', 'EffectiveDate': '2022-07-01'}, {'order_id': '801Wt00000PHHhDIAX', 'agent_id': '#005Wt000003NITxIAO', 'EffectiveDate': '2022-08-01'}, {'order_id': '801Wt00000PHLzNIAX', 'agent_id': '005Wt000003NEoYIAW', 'EffectiveDate': '2022-09-15'}, {'order_id': '801Wt00000PHRFAIA5', 'agent_id': '#005Wt000003NIx1IAG', 'EffectiveDate': '2022-07-01'}, {'order_id': '#801Wt00000PHVkDIAX', 'agent_id': '005Wt000003NJt3IAG', 'EffectiveDate': '2022-08-15'}, {'order_id': '801Wt00000PHVqfIAH', 'agent_id': '005Wt000003NDEBIA4', 'EffectiveDate': '2022-09-20'}, {'order_id': '#801Wt00000PHWptIAH', 'agent_id': '005Wt000003NJ0EIAW', 'EffectiveDate': '2022-09-25'}], 'var_call_kGIQahVVke2cY26fo5lK05RZ': 'file_storage/call_kGIQahVVke2cY26fo5lK05RZ.json'}

exec(code, env_args)
