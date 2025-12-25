code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-2221653753642693092']) as f:
    opps = json.load(f)
with open(locals()['var_function-call-2221653753642695317']) as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_con = pd.DataFrame(contracts)

# Clean IDs function
def clean_id(x):
    if pd.isna(x): return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Apply cleaning
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

# Merge on ContractID
# Inner join to get only opportunities with contracts
merged = pd.merge(df_opp, df_con, left_on='ContractID__c', right_on='Id', how='inner')

# Convert dates
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
# Handle timezone in CreatedDate (it has +0000). Convert to tz-naive or normalize.
merged['CreatedDate'] = merged['CreatedDate'].dt.tz_convert(None)

merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# Filter for April 2023 Closing (Signed Date)
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

filtered = merged[(merged['CompanySignedDate'] >= start_date) & (merged['CompanySignedDate'] <= end_date)].copy()

# Calculate Turnaround (Signed - Created) in days
# Normalize CreatedDate to remove time component for day calculation
filtered['Turnaround'] = (filtered['CompanySignedDate'] - filtered['CreatedDate'].dt.normalize()).dt.days

# Group by Agent (OwnerId) and calculate mean turnaround
if not filtered.empty:
    agent_stats = filtered.groupby('OwnerId')['Turnaround'].mean().reset_index()
    # Sort by Turnaround ascending (quickest)
    best_agent = agent_stats.sort_values('Turnaround', ascending=True).iloc[0]
    result = best_agent['OwnerId']
else:
    result = "No matching records"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-2221653753642693092': 'file_storage/function-call-2221653753642693092.json', 'var_function-call-2221653753642695317': 'file_storage/function-call-2221653753642695317.json'}

exec(code, env_args)
