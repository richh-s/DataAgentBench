code = """import json
import pandas as pd

with open(locals()['var_function-call-17208148666135513744'], 'r') as f:
    opps = json.load(f)
with open(locals()['var_function-call-17208148666135514927'], 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_con = pd.DataFrame(contracts)

def clean_id(x):
    if pd.isna(x) or str(x) == "None":
        return None
    return str(x).lstrip('#').strip()

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

df_opp_linked = df_opp.dropna(subset=['ContractID__c'])
merged = pd.merge(df_opp_linked, df_con, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_con'))

merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.date
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate']).dt.date

start_date = pd.to_datetime('2023-04-01').date()
end_date = pd.to_datetime('2023-04-30').date()

# Check CreatedDate in April 2023
filtered_created = merged[
    (merged['CreatedDate'] >= start_date) & 
    (merged['CreatedDate'] <= end_date)
]

print("__RESULT__:")
print(json.dumps({
    "count_created_apr_2023": len(filtered_created),
    "sample": filtered_created[['Id_opp', 'OwnerId', 'CreatedDate', 'CompanySignedDate']].head(5).astype(str).to_dict(orient='records')
}))"""

env_args = {'var_function-call-17208148666135513744': 'file_storage/function-call-17208148666135513744.json', 'var_function-call-17208148666135514927': 'file_storage/function-call-17208148666135514927.json', 'var_function-call-13880517487965175894': {'agent_id': '005Wt000003NDEBIA4', 'average_days': 304.0, 'details': [{'OwnerId': '005Wt000003NDEBIA4', 'Turnaround': 304.0}]}, 'var_function-call-13557595782984079283': {'total_opps': 1170, 'opps_with_contract_id': 163, 'merged_rows': 163, 'filtered_rows_april_2023': 1, 'unique_agents_in_filtered': ['005Wt000003NDEBIA4'], 'sample_filtered': [{'Id_opp': '006Wt000007BI41IAG', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15', 'CompanySignedDate': '2023-04-15', 'Turnaround': '304'}]}, 'var_function-call-3021931554888125189': {'contracts_signed_apr_2023_count': 1, 'sample_ids': ['800Wt00000DE9FGIA1']}}

exec(code, env_args)
