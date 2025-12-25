code = """import pandas as pd
import json

path_opp = locals()['var_function-call-8541669410738994321']
path_cont = locals()['var_function-call-8541669410738991182']

with open(path_opp, 'r') as f:
    opps = json.load(f)
with open(path_cont, 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

df_opp['ContractID__c_clean'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId_clean'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id_clean'] = df_cont['Id'].apply(clean_id)

df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'], errors='coerce')
df_cont_april = df_cont[
    (df_cont['CompanySignedDate'] >= '2023-04-01') & 
    (df_cont['CompanySignedDate'] <= '2023-04-30')
]

merged = pd.merge(df_opp, df_cont_april, left_on='ContractID__c_clean', right_on='Id_clean', how='inner')

merged['CreatedDate_dt'] = pd.to_datetime(merged['CreatedDate'], errors='coerce').dt.tz_convert(None)
merged['cycle_days'] = (merged['CompanySignedDate'] - merged['CreatedDate_dt']).dt.total_seconds() / (24 * 3600)

# Filter out invalid cycles (negative days)
valid_cycles = merged[merged['cycle_days'] >= 0].copy()

# Group by Agent
avg_cycle = valid_cycles.groupby('OwnerId_clean')['cycle_days'].mean().reset_index()
avg_cycle = avg_cycle.sort_values('cycle_days')

print("__RESULT__:")
print(json.dumps({
    "top_agent": avg_cycle.head(1).to_dict(orient='records'),
    "num_agents": len(avg_cycle),
    "all_agents_head": avg_cycle.head(5).to_dict(orient='records')
}))"""

env_args = {'var_function-call-7295838422035824403': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-8541669410738994321': 'file_storage/function-call-8541669410738994321.json', 'var_function-call-8541669410738991182': 'file_storage/function-call-8541669410738991182.json', 'var_function-call-6173624232980906063': [{'OwnerId_clean': '005Wt000003NDEBIA4', 'cycle_days': 303.5690972222}]}

exec(code, env_args)
