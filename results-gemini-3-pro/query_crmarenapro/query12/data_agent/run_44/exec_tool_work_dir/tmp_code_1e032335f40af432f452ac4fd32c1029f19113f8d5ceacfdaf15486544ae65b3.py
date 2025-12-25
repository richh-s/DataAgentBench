code = """import pandas as pd
import json

# Get file paths from storage
opps_path = locals()['var_function-call-10820855826992647047']
contracts_path = locals()['var_function-call-10820855826992644952']

# Load data
with open(opps_path, 'r') as f:
    opps = json.load(f)
with open(contracts_path, 'r') as f:
    contracts = json.load(f)

# Create DataFrames
df_opps = pd.DataFrame(opps)
df_contracts = pd.DataFrame(contracts)

# Clean IDs function
def clean_id(x):
    if x is None: return None
    x = str(x).strip()
    if x.lower() == 'none': return None
    if x.startswith('#'):
        x = x[1:]
    return x

# Apply cleaning
df_opps['ContractID__c'] = df_opps['ContractID__c'].apply(clean_id)
df_opps['OwnerId'] = df_opps['OwnerId'].apply(clean_id)
df_contracts['Id'] = df_contracts['Id'].apply(clean_id)

# Filter Contracts for April 2023
df_contracts['CompanySignedDate'] = pd.to_datetime(df_contracts['CompanySignedDate'], errors='coerce')
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')
df_contracts_apr = df_contracts[(df_contracts['CompanySignedDate'] >= start_date) & (df_contracts['CompanySignedDate'] <= end_date)].copy()

# Join
merged = pd.merge(df_opps, df_contracts_apr, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate duration
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'], errors='coerce')

# Normalize to date
merged['CreatedDate_dt'] = merged['CreatedDate'].dt.date
merged['SignedDate_dt'] = merged['CompanySignedDate'].dt.date

# Calculate days
merged['duration'] = (pd.to_datetime(merged['SignedDate_dt']) - pd.to_datetime(merged['CreatedDate_dt'])).dt.days

# Group by OwnerId
if merged.empty:
    result = "No records found"
else:
    avg_turnaround = merged.groupby('OwnerId')['duration'].mean().reset_index()
    # Sort by duration ascending
    avg_turnaround = avg_turnaround.sort_values(by='duration')
    # Get top 1
    best_agent = avg_turnaround.iloc[0]['OwnerId']
    result = best_agent

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10820855826992647047': 'file_storage/function-call-10820855826992647047.json', 'var_function-call-10820855826992644952': 'file_storage/function-call-10820855826992644952.json'}

exec(code, env_args)
