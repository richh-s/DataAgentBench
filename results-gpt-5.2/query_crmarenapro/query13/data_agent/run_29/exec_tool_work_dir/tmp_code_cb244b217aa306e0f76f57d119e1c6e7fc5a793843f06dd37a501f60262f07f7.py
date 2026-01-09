code = """import json, pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

contracts = pd.DataFrame(var_call_iDWPalPiA991biWQN1YRRkUX)
opps = pd.DataFrame(load_records(var_call_R2XQbqUGmEWHSDml6S4bL03S))
orders = pd.DataFrame(load_records(var_call_uT3jLJ7J1P93rRpVA0MQXCpA))
orderitems = pd.DataFrame(load_records(var_call_Y88ZXdw4trFWOd3m9AZo0wMC))

# eligible accounts via contracts in last 5 months
eligible_accounts = set(contracts['account_id'].dropna().astype(str))

orders_elig = orders[orders['account_id'].astype(str).isin(eligible_accounts)].copy()

# compute sales per order
orderitems['quantity'] = pd.to_numeric(orderitems['quantity'], errors='coerce')
orderitems['unit_price'] = pd.to_numeric(orderitems['unit_price'], errors='coerce')
orderitems['sales'] = orderitems['quantity'] * orderitems['unit_price']

order_sales = orderitems.groupby('order_id', as_index=False)['sales'].sum()

orders_elig = orders_elig.merge(order_sales, on='order_id', how='left')
orders_elig['sales'] = orders_elig['sales'].fillna(0.0)

# top agent by total sales across eligible orders
agent_sales = orders_elig.groupby('owner_id', as_index=False)['sales'].sum()
agent_sales = agent_sales.sort_values(['sales','owner_id'], ascending=[False, True])

top_agent_id = None
if len(agent_sales) > 0:
    top_agent_id = agent_sales.iloc[0]['owner_id']

print('__RESULT__:')
print(json.dumps(top_agent_id))"""

env_args = {'var_call_iDWPalPiA991biWQN1YRRkUX': [{'contract_id': '800Wt00000DDNlnIAH', 'account_id': '001Wt00000PGtdJIAT', 'company_signed_date': '2022-09-02'}, {'contract_id': '800Wt00000DDe3OIAT', 'account_id': '001Wt00000PGYx5IAH', 'company_signed_date': '2022-09-20'}, {'contract_id': '800Wt00000DDeg6IAD', 'account_id': '001Wt00000PHVtpIAH', 'company_signed_date': '2022-07-18'}, {'contract_id': '800Wt00000DDzZLIA1', 'account_id': '001Wt00000PHVqdIAH', 'company_signed_date': '2022-10-26'}, {'contract_id': '#800Wt00000DDzvrIAD', 'account_id': '001Wt00000PHHXXIA5', 'company_signed_date': '2022-08-30'}, {'contract_id': '800Wt00000DE0FHIA1', 'account_id': '001Wt00000PGZZoIAP', 'company_signed_date': '2022-08-02'}, {'contract_id': '800Wt00000DE0TiIAL', 'account_id': '001Wt00000PGZmfIAH', 'company_signed_date': '2022-09-10'}, {'contract_id': '800Wt00000DE2vLIAT', 'account_id': '001Wt00000PGovMIAT', 'company_signed_date': '2022-06-29'}, {'contract_id': '800Wt00000DE98oIAD', 'account_id': '001Wt00000PGtdJIAT', 'company_signed_date': '2022-11-10'}, {'contract_id': '800Wt00000DE9GrIAL', 'account_id': '001Wt00000PGRnYIAX', 'company_signed_date': '2022-06-30'}, {'contract_id': '#800Wt00000DE9ITIA1', 'account_id': '001Wt00000PGzM9IAL', 'company_signed_date': '2022-09-11'}, {'contract_id': '#800Wt00000DE9SAIA1', 'account_id': '001Wt00000PGdzxIAD', 'company_signed_date': '2022-09-30'}, {'contract_id': '800Wt00000DE9YbIAL', 'account_id': '001Wt00000PHRTfIAP', 'company_signed_date': '2022-11-22'}, {'contract_id': '#800Wt00000DE9lVIAT', 'account_id': '001Wt00000PFsjOIAT', 'company_signed_date': '2022-06-26'}, {'contract_id': '800Wt00000DE9qLIAT', 'account_id': '001Wt00000PGzSaIAL', 'company_signed_date': '2022-09-01'}, {'contract_id': '800Wt00000DE9rxIAD', 'account_id': '001Wt00000PHVtpIAH', 'company_signed_date': '2022-09-19'}], 'var_call_R2XQbqUGmEWHSDml6S4bL03S': 'file_storage/call_R2XQbqUGmEWHSDml6S4bL03S.json', 'var_call_Y88ZXdw4trFWOd3m9AZo0wMC': 'file_storage/call_Y88ZXdw4trFWOd3m9AZo0wMC.json', 'var_call_uT3jLJ7J1P93rRpVA0MQXCpA': 'file_storage/call_uT3jLJ7J1P93rRpVA0MQXCpA.json'}

exec(code, env_args)
