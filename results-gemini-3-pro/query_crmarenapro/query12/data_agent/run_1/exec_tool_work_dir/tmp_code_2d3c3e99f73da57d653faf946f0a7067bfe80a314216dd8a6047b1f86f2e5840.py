code = """import pandas as pd
import json
import datetime

# Load data
with open(locals()['var_function-call-14699303313641055001'], 'r') as f:
    opp_data = json.load(f)
with open(locals()['var_function-call-14699303313641056710'], 'r') as f:
    contract_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_contract = pd.DataFrame(contract_data)

# Clean IDs function
def clean_id(x):
    if pd.isna(x):
        return None
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

# Apply cleaning
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_contract['Id'] = df_contract['Id'].apply(clean_id)

# Filter out rows with None/Null IDs where strictly needed
df_opp = df_opp.dropna(subset=['ContractID__c'])
df_contract = df_contract.dropna(subset=['Id'])

# Merge
merged = pd.merge(df_opp, df_contract, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_con'))

# Parse dates
# CreatedDate format: "2023-09-05T11:32:46.000+0000"
# CompanySignedDate format: "2021-07-16"

merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# We are interested in April 2023.
# Assuming "turnaround ... in April 2023" means the cycle completed (signed) in April 2023.
start_date = pd.Timestamp("2023-04-01").tz_localize(None)
end_date = pd.Timestamp("2023-04-30").tz_localize(None)

# Handle timezone: Make CreatedDate tz-naive or normalize to date
# It is safer to convert CreatedDate to just date for calculation as per "number of days between dates".
merged['CreatedDate_dt'] = merged['CreatedDate'].dt.date
merged['CompanySignedDate_dt'] = merged['CompanySignedDate'].dt.date

# Filter for April 2023 signings
# Note: Comparing dates
start_date_dt = datetime.date(2023, 4, 1)
end_date_dt = datetime.date(2023, 4, 30)

filtered = merged[
    (merged['CompanySignedDate_dt'] >= start_date_dt) & 
    (merged['CompanySignedDate_dt'] <= end_date_dt)
]

# Calculate Turnaround
# (Signed Date - Created Date).days
filtered['Turnaround'] = (filtered['CompanySignedDate_dt'] - filtered['CreatedDate_dt']).apply(lambda x: x.days)

# Group by OwnerId (Agent) and calculate average
result_df = filtered.groupby('OwnerId')['Turnaround'].mean().reset_index()

# Find the quickest (min turnaround)
min_turnaround = result_df['Turnaround'].min()
best_agents = result_df[result_df['Turnaround'] == min_turnaround]

print("__RESULT__:")
print(best_agents.to_json(orient='records'))"""

env_args = {'var_function-call-14699303313641055001': 'file_storage/function-call-14699303313641055001.json', 'var_function-call-14699303313641056710': 'file_storage/function-call-14699303313641056710.json'}

exec(code, env_args)
