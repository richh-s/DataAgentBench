code = """import json
import pandas as pd
from datetime import datetime

# Load data using locals()
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
df_opp['clean_owner_id'] = df_opp['OwnerId'].apply(clean_id)

merged = pd.merge(df_opp, df_cont, left_on='clean_contract_id', right_on='clean_id', how='inner')

merged['created_dt'] = pd.to_datetime(merged['CreatedDate'], errors='coerce')
merged['signed_dt'] = pd.to_datetime(merged['CompanySignedDate'], errors='coerce')

merged['created_date_only'] = merged['created_dt'].dt.date
merged['signed_date_only'] = merged['signed_dt'].dt.date

april_mask = (merged['signed_dt'] >= '2023-04-01') & (merged['signed_dt'] <= '2023-04-30')
april_deals = merged[april_mask].copy()

if not april_deals.empty:
    april_deals['turnaround_days'] = (pd.to_datetime(april_deals['signed_date_only']) - pd.to_datetime(april_deals['created_date_only'])).dt.days
    
    # Check for negative days
    negatives = april_deals[april_deals['turnaround_days'] < 0]
    
    # Group by
    agent_stats = april_deals.groupby('clean_owner_id')['turnaround_days'].mean().reset_index()
    agent_stats.columns = ['AgentId', 'AvgTurnaround']
    agent_stats = agent_stats.sort_values(by='AvgTurnaround', ascending=True)
    
    print("__RESULT__:")
    result = {
        "top_5": agent_stats.head(5).to_dict(orient='records'),
        "negative_count": len(negatives),
        "total_april_deals": len(april_deals)
    }
    print(json.dumps(result))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "No deals"}))"""

env_args = {'var_function-call-3175577286205354846': 'file_storage/function-call-3175577286205354846.json', 'var_function-call-3175577286205357479': 'file_storage/function-call-3175577286205357479.json', 'var_function-call-1133549621745830744': {'AgentId': '005Wt000003NDEBIA4', 'AvgTurnaround': 304.0}}

exec(code, env_args)
