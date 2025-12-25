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

# Filter 2023
deals_2023 = merged[merged['signed_dt'].dt.year == 2023][['CompanySignedDate']].sort_values('CompanySignedDate')

print("__RESULT__:")
print(json.dumps(deals_2023['CompanySignedDate'].tolist()))"""

env_args = {'var_function-call-3175577286205354846': 'file_storage/function-call-3175577286205354846.json', 'var_function-call-3175577286205357479': 'file_storage/function-call-3175577286205357479.json', 'var_function-call-1133549621745830744': {'AgentId': '005Wt000003NDEBIA4', 'AvgTurnaround': 304.0}, 'var_function-call-6439797662281078132': {'top_5': [{'AgentId': '005Wt000003NDEBIA4', 'AvgTurnaround': 304.0}], 'negative_count': 0, 'total_april_deals': 1}, 'var_function-call-5124231795477077752': {'opp_count': 163, 'cont_count': 163, 'merged_count': 163, 'min_signed': '2020-06-15 00:00:00', 'max_signed': '2024-09-27 00:00:00'}}

exec(code, env_args)
