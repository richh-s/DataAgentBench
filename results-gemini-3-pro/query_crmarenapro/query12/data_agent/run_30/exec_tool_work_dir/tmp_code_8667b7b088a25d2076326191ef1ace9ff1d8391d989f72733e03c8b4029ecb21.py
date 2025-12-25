code = """import json
import pandas as pd

# Load data
opp_path = locals()['var_function-call-3175577286205354846']
cont_path = locals()['var_function-call-3175577286205357479']

with open(opp_path, 'r') as f:
    opp_data = json.load(f)

with open(cont_path, 'r') as f:
    cont_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_cont = pd.DataFrame(cont_data)

def clean_id(x):
    if pd.isna(x):
        return None
    return str(x).replace('#', '').strip()

df_opp['clean_contract_id'] = df_opp['ContractID__c'].apply(clean_id)
df_cont['clean_id'] = df_cont['Id'].apply(clean_id)

merged = pd.merge(df_opp, df_cont, left_on='clean_contract_id', right_on='clean_id', how='inner')

merged['signed_dt'] = pd.to_datetime(merged['CompanySignedDate'], errors='coerce')

print("__RESULT__:")
print(json.dumps({
    "opp_count": len(df_opp),
    "cont_count": len(df_cont),
    "merged_count": len(merged),
    "min_signed": str(merged['signed_dt'].min()),
    "max_signed": str(merged['signed_dt'].max())
}))"""

env_args = {'var_function-call-3175577286205354846': 'file_storage/function-call-3175577286205354846.json', 'var_function-call-3175577286205357479': 'file_storage/function-call-3175577286205357479.json', 'var_function-call-1133549621745830744': {'AgentId': '005Wt000003NDEBIA4', 'AvgTurnaround': 304.0}, 'var_function-call-6439797662281078132': {'top_5': [{'AgentId': '005Wt000003NDEBIA4', 'AvgTurnaround': 304.0}], 'negative_count': 0, 'total_april_deals': 1}}

exec(code, env_args)
