code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-13883184601486277189'], 'r') as f:
    opportunities = json.load(f)

with open(locals()['var_function-call-13883184601486276232'], 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opportunities)
df_con = pd.DataFrame(contracts)

def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.lower() == 'none':
        return None
    return s.lstrip('#')

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

df_opp = df_opp.dropna(subset=['ContractID__c'])
merged = pd.merge(df_opp, df_con, left_on='ContractID__c', right_on='Id', how='inner')

# Convert dates
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.tz_localize(None)
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# Filter for April 2023 (Signed Date)
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

target_deals = merged[
    (merged['CompanySignedDate'] >= start_date) & 
    (merged['CompanySignedDate'] <= end_date)
].copy()

if target_deals.empty:
    print("__RESULT__:")
    print(json.dumps("No deals found"))
else:
    # Normalize CreatedDate to date (floor to midnight)
    target_deals['CreatedDateNormal'] = target_deals['CreatedDate'].dt.floor('D')
    
    # Calculate duration
    target_deals['TurnaroundDays'] = (target_deals['CompanySignedDate'] - target_deals['CreatedDateNormal']).dt.days
    
    # Remove negative days if any (data corruption check)
    target_deals = target_deals[target_deals['TurnaroundDays'] >= 0]
    
    # Group
    agent_stats = target_deals.groupby('OwnerId')['TurnaroundDays'].mean().reset_index()
    
    # Find min
    if agent_stats.empty:
        print("__RESULT__:")
        print(json.dumps("No valid deals"))
    else:
        min_avg = agent_stats['TurnaroundDays'].min()
        best_agents = agent_stats[agent_stats['TurnaroundDays'] == min_avg]
        result_id = best_agents.iloc[0]['OwnerId']
        
        print("__RESULT__:")
        print(json.dumps(result_id))"""

env_args = {'var_function-call-13883184601486277189': 'file_storage/function-call-13883184601486277189.json', 'var_function-call-13883184601486276232': 'file_storage/function-call-13883184601486276232.json', 'var_function-call-4360960261877270382': '005Wt000003NDEBIA4'}

exec(code, env_args)
