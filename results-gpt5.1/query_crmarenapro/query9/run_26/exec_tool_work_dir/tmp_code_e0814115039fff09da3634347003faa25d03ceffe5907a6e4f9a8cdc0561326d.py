code = """import json, pandas as pd

cases_file = var_call_N17K6zSdtwG0shxMpWsT1jOT
with open(cases_file, 'r') as f:
    cases = json.load(f)
accounts = var_call_fYEoDEnblJqKbPpUyHT0eiH3

cases_df = pd.DataFrame(cases)
acc_df = pd.DataFrame(accounts)

for col in ['id','accountid']:
    cases_df[col] = cases_df[col].astype(str).str.replace('^#','', regex=True)
acc_df['Id'] = acc_df['Id'].astype(str).str.replace('^#','', regex=True)

cases_df['created_ts'] = pd.to_datetime(cases_df['createddate'])
cases_df['closed_ts'] = pd.to_datetime(cases_df['closeddate'])

anchor = pd.Timestamp('2022-10-26')
start = anchor - pd.DateOffset(months=18)

mask = (cases_df['created_ts'] >= start) & (cases_df['created_ts'] <= anchor)
cases_18 = cases_df[mask].copy()

for col in ['Id','ShippingState']:
    if col in acc_df.columns:
        acc_df[col] = acc_df[col].astype(str).str.strip()

merged = cases_18.merge(acc_df[['Id','ShippingState']], left_on='accountid', right_on='Id', how='left')
merged = merged.dropna(subset=['ShippingState'])

merged['dur_hours'] = (merged['closed_ts'] - merged['created_ts']).dt.total_seconds() / 3600.0

quarters = pd.period_range(start=start, end=anchor, freq='Q')[-6:]

merged['quarter'] = merged['created_ts'].dt.to_period('Q')
merged_6q = merged[merged['quarter'].isin(quarters)]

state_q = merged_6q.groupby(['ShippingState','quarter'])['dur_hours'].mean().reset_index()

state_scores = state_q.groupby('ShippingState')['dur_hours'].mean().reset_index()

best_state = state_scores.sort_values('dur_hours').iloc[0]['ShippingState'] if not state_scores.empty else None

import json as _json
result = _json.dumps(best_state)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_fYEoDEnblJqKbPpUyHT0eiH3': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PFluoIAD', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PFlupIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PFrk1IAD', 'ShippingState': 'MO'}, {'Id': '001Wt00000PFsjMIAT', 'ShippingState': 'OH'}, {'Id': '001Wt00000PFsjOIAT', 'ShippingState': 'NY'}, {'Id': '001Wt00000PFsmZIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PFsmaIAD', 'ShippingState': 'MI'}, {'Id': '001Wt00000PFsmbIAD', 'ShippingState': 'NV'}, {'Id': '#001Wt00000PFsmcIAD', 'ShippingState': 'MN'}, {'Id': '001Wt00000PFsmdIAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '#001Wt00000PFttwIAD', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGGTtIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGGTuIAP', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGHsyIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGQzcIAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGR63IAH', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGRqjIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwZIAX', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGXrKIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGXrLIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrMIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGXrNIAX', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGYgxIAH', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGYx4IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PGYx5IAH', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGZZnIAP', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'ShippingState': 'UT'}, {'Id': '#001Wt00000PGZmeIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaHIIA1', 'ShippingState': 'NV'}, {'Id': '001Wt00000PGaNjIAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGaNkIAL', 'ShippingState': 'VA'}, {'Id': '#001Wt00000PGaZCIA1', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGb5MIAT', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PGb5NIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGb5OIAT', 'ShippingState': 'IL'}, {'Id': '#001Wt00000PGcFxIAL', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGccRIAT', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGcpMIAT', 'ShippingState': 'MO'}, {'Id': '#001Wt00000PGdBuIAL', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdwiIAD', 'ShippingState': 'WA'}, {'Id': '#001Wt00000PGdzxIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGeJIIA1', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '#001Wt00000PGovMIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGtdJIAT', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtdKIAT', 'ShippingState': 'VA'}, {'Id': '001Wt00000PGtmwIAD', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGtmxIAD', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGyTIIA1', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGyv0IAD', 'ShippingState': 'MA'}, {'Id': '001Wt00000PGz2nIAD', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGzVpIAL', 'ShippingState': 'TX'}, {'Id': '001Wt00000PGzsMIAT', 'ShippingState': 'CA'}, {'Id': '001Wt00000PH90cIAD', 'ShippingState': 'MA'}, {'Id': '#001Wt00000PH9DRIA1', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PH9ITIA1', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHHXXIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHR75IAH', 'ShippingState': 'OR'}, {'Id': '#001Wt00000PHR8gIAH', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHRF8IAP', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRF9IAP', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHRTeIAP', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHRTfIAP', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRVGIA5', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHRVHIA5', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHRVIIA5', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHRbiIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVaUIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVaVIAX', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVdhIAH', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHVfJIAX', 'ShippingState': 'MN'}, {'Id': '001Wt00000PHVgvIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHViXIAX', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHViYIAX', 'ShippingState': 'MD'}, {'Id': '#001Wt00000PHViZIAX', 'ShippingState': 'PA'}, {'Id': '001Wt00000PHViaIAH', 'ShippingState': 'CO'}, {'Id': '001Wt00000PHVk9IAH', 'ShippingState': 'NY'}, {'Id': '#001Wt00000PHVkAIAX', 'ShippingState': 'VA'}, {'Id': '001Wt00000PHVllIAH', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVnOIAX', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVozIAH', 'ShippingState': 'NY'}, {'Id': '001Wt00000PHVqbIAH', 'ShippingState': 'GA'}, {'Id': '001Wt00000PHVqdIAH', 'ShippingState': 'CA'}, {'Id': '001Wt00000PHVsDIAX', 'ShippingState': 'OR'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVx3IAH', 'ShippingState': 'AZ'}, {'Id': '#001Wt00000PHVyfIAH', 'ShippingState': 'NC'}, {'Id': '001Wt00000PHW0HIAX', 'ShippingState': 'NY'}], 'var_call_zsbd7U6dLfJk95DrL79GFxEn': [{'today': '2025-12-03'}], 'var_call_7cW9P8XucCYG3YHkwynHvNus': [{'ShippingState': 'FL'}, {'ShippingState': 'TX'}, {'ShippingState': 'AZ'}, {'ShippingState': 'CA'}, {'ShippingState': 'MO'}, {'ShippingState': 'OH'}, {'ShippingState': 'NY'}, {'ShippingState': 'CO'}, {'ShippingState': 'MI'}, {'ShippingState': 'NV'}, {'ShippingState': 'MN'}, {'ShippingState': 'MA'}, {'ShippingState': 'WA'}, {'ShippingState': 'IA'}, {'ShippingState': 'OR'}, {'ShippingState': 'UT'}, {'ShippingState': 'GA'}, {'ShippingState': 'VA'}, {'ShippingState': 'IL'}, {'ShippingState': 'NJ'}, {'ShippingState': 'NC'}, {'ShippingState': 'MD'}, {'ShippingState': 'PA'}, {'ShippingState': 'SC'}], 'var_call_ujItEt90rL2PEUyln2nyayMM': [{'min_created': '2020-07-01T15:30:00.000+0000', 'max_closed': '2023-12-02T16:45:51.000+0000'}], 'var_call_FCUInfP5GCGZHfCu3qMWZHjL': [{'cnt': '75'}], 'var_call_nsvaoYfISETl7hrRoXATkcFP': [{'createddate': '2024-05-15T14:45:00.000+0000', 'closeddate': 'None'}, {'createddate': '2024-05-05T10:15:30.000+0000', 'closeddate': 'None'}, {'createddate': '2024-05-02T09:30:00.000+0000', 'closeddate': 'None'}, {'createddate': '2024-05-02T09:00:00.000+0000', 'closeddate': 'None'}, {'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}], 'var_call_N17K6zSdtwG0shxMpWsT1jOT': 'file_storage/call_N17K6zSdtwG0shxMpWsT1jOT.json'}

exec(code, env_args)
