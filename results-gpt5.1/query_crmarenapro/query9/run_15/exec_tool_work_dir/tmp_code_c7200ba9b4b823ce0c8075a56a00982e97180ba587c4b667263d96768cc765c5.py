code = """import json, pandas as pd
from datetime import datetime, timezone

# Load full cases data
path = var_call_gSStRaWwZsBU4mPVQHPXYvQp
with open(path, 'r') as f:
    cases = json.load(f)

accounts = pd.DataFrame(var_call_QZYPSQ8d1yQKofISpOIzpYR7)
accounts['clean_id'] = accounts['Id'].str.lstrip('#')

cases_df = pd.DataFrame(cases)

for col in ['createddate','closeddate']:
    cases_df[col] = pd.to_datetime(cases_df[col], errors='coerce')

cutoff = datetime(2022, 10, 26, tzinfo=timezone.utc)
start = datetime(2021, 4, 26, tzinfo=timezone.utc)

mask = (cases_df['closeddate'].notna()) & (cases_df['createddate'] >= start) & (cases_df['createddate'] < cutoff)
cases_df = cases_df[mask].copy()

cases_df['clean_accountid'] = cases_df['accountid'].str.lstrip('#')

merged = cases_df.merge(accounts[['clean_id','state']], left_on='clean_accountid', right_on='clean_id', how='left')
merged = merged[merged['state'].notna()].copy()

merged['duration_hours'] = (merged['closeddate'] - merged['createddate']).dt.total_seconds() / 3600.0

state_stats = merged.groupby('state')['duration_hours'].median().reset_index().sort_values('duration_hours')

best_state = state_stats.iloc[0]['state'] if len(state_stats)>0 else None

result = json.dumps(best_state)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_gSStRaWwZsBU4mPVQHPXYvQp': 'file_storage/call_gSStRaWwZsBU4mPVQHPXYvQp.json', 'var_call_QZYPSQ8d1yQKofISpOIzpYR7': [{'Id': '001Wt00000PFj4zIAD', 'state': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'state': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'state': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'state': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'state': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'state': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'state': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'state': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'state': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'state': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'state': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'state': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'state': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'state': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'state': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'state': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'state': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'state': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'state': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'state': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'state': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'state': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'state': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'state': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'state': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'state': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'state': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'state': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'state': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'state': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'state': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'state': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'state': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'state': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'state': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'state': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'state': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'state': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'state': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'state': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'state': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'state': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'state': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'state': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'state': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'state': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'state': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'state': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'state': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'state': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'state': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'state': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'state': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'state': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'state': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'state': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'state': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'state': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'state': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'state': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'state': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'state': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'state': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'state': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'state': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'state': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'state': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'state': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'state': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'state': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'state': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'state': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'state': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'state': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'state': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'state': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'state': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'state': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'state': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'state': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'state': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'state': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'state': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'state': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'state': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'state': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'state': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'state': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'state': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'state': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'state': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'state': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'state': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'state': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'state': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'state': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'state': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'state': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'state': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'state': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'state': 'NY'}]}

exec(code, env_args)
