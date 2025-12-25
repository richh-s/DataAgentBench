code = """import pandas as pd
import json

# Load data
contracts_data = locals()['var_function-call-8882953471666003693']
# Opportunity data is in a file
with open(locals()['var_function-call-8882953471666002530'], 'r') as f:
    opportunities_data = json.load(f)

# Create DataFrames
df_contracts = pd.DataFrame(contracts_data)
df_opps = pd.DataFrame(opportunities_data)

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

df_contracts['Id'] = df_contracts['Id'].apply(clean_id)
df_opps['ContractID__c'] = df_opps['ContractID__c'].apply(clean_id)
df_opps['OwnerId'] = df_opps['OwnerId'].apply(clean_id)

# Merge
# Inner join because we only care about closed deals (signed contracts)
merged = pd.merge(df_opps, df_contracts, left_on='ContractID__c', right_on='Id', how='inner')

# Convert dates
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])

# Calculate Duration
# Policy: number of days between creation and signed date.
# We'll use the difference in days. 
# Since CompanySignedDate has no time (defaults to 00:00:00), and CreatedDate has time.
# If we treat CompanySignedDate as the date the event happened, it's effectively that day.
# To be consistent with "days between dates", we often use Date - Date.
merged['Duration'] = (merged['CompanySignedDate'] - merged['CreatedDate']).dt.total_seconds() / (24 * 3600)
# Alternatively, if we align to dates:
merged['DurationDays'] = (merged['CompanySignedDate'].dt.date - merged['CreatedDate'].dt.date).apply(lambda x: x.days)

# I will use DurationDays as it's more standard for "number of days". 
# If CreatedDate > SignedDate (data error), we should filter or handle? 
# Let's check for negative values.
merged = merged[merged['DurationDays'] >= 0]

# Filter for April 2023 signing (already done in query but double check)
# Signed in April 2023
merged = merged[
    (merged['CompanySignedDate'] >= '2023-04-01') & 
    (merged['CompanySignedDate'] <= '2023-04-30')
]

# Group by Agent (OwnerId) and calculate average
agent_performance = merged.groupby('OwnerId')['DurationDays'].mean().reset_index()

# Find quickest (minimum average duration)
if not agent_performance.empty:
    best_agent = agent_performance.loc[agent_performance['DurationDays'].idxmin()]
    result = best_agent['OwnerId']
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8882953471666003693': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-8882953471666002530': 'file_storage/function-call-8882953471666002530.json'}

exec(code, env_args)
