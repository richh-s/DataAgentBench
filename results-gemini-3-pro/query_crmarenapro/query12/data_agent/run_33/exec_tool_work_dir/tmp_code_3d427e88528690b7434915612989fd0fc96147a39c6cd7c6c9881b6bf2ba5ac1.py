code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-17208148666135513744'], 'r') as f:
    opps = json.load(f)
with open(locals()['var_function-call-17208148666135514927'], 'r') as f:
    contracts = json.load(f)

# Create DataFrames
df_opp = pd.DataFrame(opps)
df_con = pd.DataFrame(contracts)

# Clean IDs
def clean_id(x):
    if pd.isna(x):
        return x
    return str(x).lstrip('#').strip()

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

# Merge
merged = pd.merge(df_opp, df_con, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_con'))

# Convert dates
# CreatedDate format: 2023-09-05T11:32:46.000+0000
# CompanySignedDate format: 2021-07-16
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.date
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate']).dt.date

# Filter for April 2023
start_date = pd.to_datetime('2023-04-01').date()
end_date = pd.to_datetime('2023-04-30').date()

filtered = merged[
    (merged['CompanySignedDate'] >= start_date) & 
    (merged['CompanySignedDate'] <= end_date)
].copy()

# Calculate Turnaround
filtered['Turnaround'] = (filtered['CompanySignedDate'] - filtered['CreatedDate']).apply(lambda x: x.days)

# Group by Agent (OwnerId)
result = filtered.groupby('OwnerId')['Turnaround'].mean().reset_index()

# Find winner (quickest = min average turnaround)
if not result.empty:
    winner = result.loc[result['Turnaround'].idxmin()]
    final_answer = winner['OwnerId']
    min_days = winner['Turnaround']
    
    print("__RESULT__:")
    print(json.dumps({
        "agent_id": final_answer,
        "average_days": min_days,
        "details": result.to_dict(orient='records')
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"error": "No records found for April 2023"}))"""

env_args = {'var_function-call-17208148666135513744': 'file_storage/function-call-17208148666135513744.json', 'var_function-call-17208148666135514927': 'file_storage/function-call-17208148666135514927.json'}

exec(code, env_args)
