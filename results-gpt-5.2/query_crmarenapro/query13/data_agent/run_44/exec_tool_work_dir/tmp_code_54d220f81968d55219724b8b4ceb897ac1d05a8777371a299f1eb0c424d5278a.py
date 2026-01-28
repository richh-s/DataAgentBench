code = """import json, pandas as pd

# contracts accounts
contracts = pd.DataFrame(var_call_OU3Ulq42ELb0ZScNGyDCoWcg)
contract_accounts = set(contracts['AccountId_clean'].dropna().astype(str))

# orders/items (large) load from json file
path = var_call_3VXAf3iLSp0R5BV7Y88C8sLx
with open(path, 'r', encoding='utf-8') as f:
    orders_items = json.load(f)

df = pd.DataFrame(orders_items)
# filter eligible by account
eligible = df[df['AccountId_clean'].astype(str).isin(contract_accounts)].copy()
eligible['Quantity'] = pd.to_numeric(eligible['Quantity'], errors='coerce')
eligible['UnitPrice'] = pd.to_numeric(eligible['UnitPrice'], errors='coerce')
eligible['Sales'] = eligible['Quantity'] * eligible['UnitPrice']

grp = eligible.groupby('AgentId_clean', dropna=True)['Sales'].sum().sort_values(ascending=False)
agent_id = None
if len(grp) > 0:
    agent_id = grp.index[0]

result = json.dumps(agent_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_3VXAf3iLSp0R5BV7Y88C8sLx': 'file_storage/call_3VXAf3iLSp0R5BV7Y88C8sLx.json', 'var_call_OU3Ulq42ELb0ZScNGyDCoWcg': [{'AccountId_clean': '001Wt00000PGtdJIAT'}, {'AccountId_clean': '001Wt00000PGYx5IAH'}, {'AccountId_clean': '001Wt00000PHVtpIAH'}, {'AccountId_clean': '001Wt00000PHVqdIAH'}, {'AccountId_clean': '001Wt00000PHHXXIA5'}, {'AccountId_clean': '001Wt00000PGZZoIAP'}, {'AccountId_clean': '001Wt00000PGZmfIAH'}, {'AccountId_clean': '001Wt00000PGovMIAT'}, {'AccountId_clean': '001Wt00000PGtdJIAT'}, {'AccountId_clean': '001Wt00000PGRnYIAX'}, {'AccountId_clean': '001Wt00000PGzM9IAL'}, {'AccountId_clean': '001Wt00000PGdzxIAD'}, {'AccountId_clean': '001Wt00000PHRTfIAP'}, {'AccountId_clean': '001Wt00000PFsjOIAT'}, {'AccountId_clean': '001Wt00000PGzSaIAL'}, {'AccountId_clean': '001Wt00000PHVtpIAH'}]}

exec(code, env_args)
