code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-17208148666135513744'], 'r') as f:
    opps = json.load(f)
with open(locals()['var_function-call-17208148666135514927'], 'r') as f:
    contracts = json.load(f)
with open(locals()['var_function-call-12990900211710221851'], 'r') as f:
    opps_close = json.load(f)

df_opp = pd.DataFrame(opps)
df_close = pd.DataFrame(opps_close)
df_con = pd.DataFrame(contracts)

def clean_id(x):
    if pd.isna(x) or str(x) == "None":
        return None
    return str(x).lstrip('#').strip()

df_opp['Id'] = df_opp['Id'].apply(clean_id)
df_close['Id'] = df_close['Id'].apply(clean_id)
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

# Join Opps and CloseDate
df_opp = pd.merge(df_opp, df_close, on='Id', how='left')

# Join with Contracts
df_opp_linked = df_opp.dropna(subset=['ContractID__c'])
merged = pd.merge(df_opp_linked, df_con, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_con'))

# Convert dates
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.date
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate']).dt.date
merged['CloseDate'] = pd.to_datetime(merged['CloseDate']).dt.date

start_date = pd.to_datetime('2023-04-01').date()
end_date = pd.to_datetime('2023-04-30').date()

# Filter: CloseDate in April 2023
filtered_close = merged[
    (merged['CloseDate'] >= start_date) & 
    (merged['CloseDate'] <= end_date)
].copy()

filtered_close['Turnaround'] = (filtered_close['CompanySignedDate'] - filtered_close['CreatedDate']).apply(lambda x: x.days)

print("__RESULT__:")
print(json.dumps({
    "filtered_rows_close_date_april_2023": len(filtered_close),
    "sample_filtered_close": filtered_close[['Id_opp', 'OwnerId', 'CloseDate', 'CompanySignedDate', 'Turnaround']].head(5).astype(str).to_dict(orient='records'),
    "unique_agents": filtered_close['OwnerId'].unique().tolist()
}))"""

env_args = {'var_function-call-17208148666135513744': 'file_storage/function-call-17208148666135513744.json', 'var_function-call-17208148666135514927': 'file_storage/function-call-17208148666135514927.json', 'var_function-call-13880517487965175894': {'agent_id': '005Wt000003NDEBIA4', 'average_days': 304.0, 'details': [{'OwnerId': '005Wt000003NDEBIA4', 'Turnaround': 304.0}]}, 'var_function-call-13557595782984079283': {'total_opps': 1170, 'opps_with_contract_id': 163, 'merged_rows': 163, 'filtered_rows_april_2023': 1, 'unique_agents_in_filtered': ['005Wt000003NDEBIA4'], 'sample_filtered': [{'Id_opp': '006Wt000007BI41IAG', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15', 'CompanySignedDate': '2023-04-15', 'Turnaround': '304'}]}, 'var_function-call-3021931554888125189': {'contracts_signed_apr_2023_count': 1, 'sample_ids': ['800Wt00000DE9FGIA1']}, 'var_function-call-15923932452364500727': {'count_created_apr_2023': 3, 'sample': [{'Id_opp': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25', 'CompanySignedDate': '2023-06-13'}, {'Id_opp': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10', 'CompanySignedDate': '2023-10-13'}, {'Id_opp': '006Wt000007BHPhIAO', 'OwnerId': '005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15', 'CompanySignedDate': '2023-09-30'}]}, 'var_function-call-12990900211710221851': 'file_storage/function-call-12990900211710221851.json'}

exec(code, env_args)
