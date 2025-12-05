code = """import json, pandas as pd
from pathlib import Path

# Load big orders+items file
path = Path(var_call_baaznr2RIRnacF13QhTnmrF9)
orders_items = json.loads(path.read_text())
contracts = var_call_bBnbExLRAwZ8AA36QzFsFujD

orders_df = pd.DataFrame(orders_items)
contracts_df = pd.DataFrame(contracts)

# Normalize AccountId by stripping leading '#'
orders_df['AccountId_norm'] = orders_df['AccountId'].astype(str).str.lstrip('#')
contracts_df['AccountId_norm'] = contracts_df['AccountId'].astype(str).str.lstrip('#')

merged = orders_df.merge(contracts_df[['AccountId_norm']], on='AccountId_norm', how='inner')

merged['Quantity'] = merged['Quantity'].astype(float)
merged['UnitPrice'] = merged['UnitPrice'].astype(float)
merged['SalesAmount'] = merged['Quantity'] * merged['UnitPrice']

agg = merged.groupby('OwnerId', as_index=False)['SalesAmount'].sum()

if agg.empty:
    result = None
else:
    top = agg.sort_values('SalesAmount', ascending=False).iloc[0]
    result = top['OwnerId']

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_baaznr2RIRnacF13QhTnmrF9': 'file_storage/call_baaznr2RIRnacF13QhTnmrF9.json', 'var_call_bBnbExLRAwZ8AA36QzFsFujD': [{'Id': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'AccountId': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'AccountId': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'AccountId': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'AccountId': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'AccountId': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'AccountId': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}]}

exec(code, env_args)
