code = """import json, pandas as pd

contracts = pd.DataFrame(var_call_znnYYypog2Od7WvEllIcXDpp)
# load large ordersitems file
path = var_call_Pgj0BZ1QIRSEivUmjyKUwQsF
with open(path, 'r', encoding='utf-8') as f:
    orders = pd.DataFrame(json.load(f))

# inner join on AccountIdClean (eligible contracts)
elig = orders.merge(contracts[['AccountIdClean']].drop_duplicates(), on='AccountIdClean', how='inner')

# compute sales amount
elig['Quantity'] = pd.to_numeric(elig['Quantity'], errors='coerce')
elig['UnitPrice'] = pd.to_numeric(elig['UnitPrice'], errors='coerce')
elig['Sales'] = elig['Quantity'] * elig['UnitPrice']

by_agent = elig.groupby('AgentId', as_index=False)['Sales'].sum().sort_values('Sales', ascending=False)
agent_id = None
if len(by_agent):
    agent_id = by_agent.iloc[0]['AgentId']

print('__RESULT__:')
print(json.dumps({'AgentId': agent_id}))"""

env_args = {'var_call_Pgj0BZ1QIRSEivUmjyKUwQsF': 'file_storage/call_Pgj0BZ1QIRSEivUmjyKUwQsF.json', 'var_call_znnYYypog2Od7WvEllIcXDpp': [{'AccountIdClean': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02 00:00:00'}, {'AccountIdClean': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20 00:00:00'}, {'AccountIdClean': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18 00:00:00'}, {'AccountIdClean': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26 00:00:00'}, {'AccountIdClean': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30 00:00:00'}, {'AccountIdClean': '001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02 00:00:00'}, {'AccountIdClean': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10 00:00:00'}, {'AccountIdClean': '001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29 00:00:00'}, {'AccountIdClean': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10 00:00:00'}, {'AccountIdClean': '001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30 00:00:00'}, {'AccountIdClean': '001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11 00:00:00'}, {'AccountIdClean': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30 00:00:00'}, {'AccountIdClean': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22 00:00:00'}, {'AccountIdClean': '001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26 00:00:00'}, {'AccountIdClean': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01 00:00:00'}, {'AccountIdClean': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19 00:00:00'}]}

exec(code, env_args)
