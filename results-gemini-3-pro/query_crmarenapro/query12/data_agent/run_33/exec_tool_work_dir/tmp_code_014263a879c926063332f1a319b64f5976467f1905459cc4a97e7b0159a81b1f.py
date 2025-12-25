code = """import json
import pandas as pd

# Load data
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

# Filter out None contract IDs
df_opp_linked = df_opp.dropna(subset=['ContractID__c'])

merged = pd.merge(df_opp_linked, df_con, left_on='ContractID__c', right_on='Id', how='inner')

merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.date
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate']).dt.date

start_date = pd.to_datetime('2023-04-01').date()
end_date = pd.to_datetime('2023-04-30').date()

filtered = merged[
    (merged['CompanySignedDate'] >= start_date) & 
    (merged['CompanySignedDate'] <= end_date)
]

print("__RESULT__:")
print(json.dumps({
    "total_opps": len(df_opp),
    "opps_with_contract_id": len(df_opp_linked),
    "merged_rows": len(merged),
    "filtered_rows_april_2023": len(filtered),
    "unique_agents_in_filtered": filtered['OwnerId'].unique().tolist(),
    "sample_filtered": filtered[['Id_opp', 'OwnerId', 'CreatedDate', 'CompanySignedDate']].head(5).astype(str).to_dict(orient='records')
}))"""

env_args = {'var_function-call-17208148666135513744': 'file_storage/function-call-17208148666135513744.json', 'var_function-call-17208148666135514927': 'file_storage/function-call-17208148666135514927.json', 'var_function-call-13880517487965175894': {'agent_id': '005Wt000003NDEBIA4', 'average_days': 304.0, 'details': [{'OwnerId': '005Wt000003NDEBIA4', 'Turnaround': 304.0}]}}

exec(code, env_args)
