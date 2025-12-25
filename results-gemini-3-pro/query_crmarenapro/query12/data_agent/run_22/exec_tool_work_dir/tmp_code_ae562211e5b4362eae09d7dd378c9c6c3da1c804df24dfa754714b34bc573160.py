code = """import pandas as pd
import json

# Load data
with open(locals()['var_function_call_14848741335113478821'], 'r') as f:
    contracts_data = json.load(f)
with open(locals()['var_function_call_14524369767035541979'], 'r') as f:
    opps_data = json.load(f)

df_contracts = pd.DataFrame(contracts_data)
df_opps = pd.DataFrame(opps_data)

# Clean IDs function
def clean_id(x):
    if x is None:
        return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

df_contracts['clean_id'] = df_contracts['Id'].apply(clean_id)
df_opps['clean_contract_id'] = df_opps['ContractID__c'].apply(clean_id)

# Filter Contracts for April 2023
df_contracts['signed_date'] = pd.to_datetime(df_contracts['CompanySignedDate'], errors='coerce')
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

# Filter contracts signed in April 2023
df_contracts_april = df_contracts[(df_contracts['signed_date'] >= start_date) & (df_contracts['signed_date'] <= end_date)]

# Join
merged = pd.merge(df_opps, df_contracts_april, left_on='clean_contract_id', right_on='clean_id', how='inner')

# Calculate turnaround
merged['created_date_dt'] = pd.to_datetime(merged['CreatedDate'], format='mixed', errors='coerce') # format='mixed' helps with various ISO formats if present

# Ensure valid dates
merged = merged.dropna(subset=['created_date_dt', 'signed_date'])

# Calculate days difference based on dates (ignoring time)
merged['days_diff'] = (merged['signed_date'].dt.date - merged['created_date_dt'].dt.date).apply(lambda x: x.days)

# Clean OwnerId
merged['clean_owner_id'] = merged['OwnerId'].apply(clean_id)

# Group by Agent
grouped = merged.groupby('clean_owner_id')['days_diff'].mean().reset_index()

# Find quickest (minimum average days)
if not grouped.empty:
    best_agent_row = grouped.loc[grouped['days_diff'].idxmin()]
    best_agent = best_agent_row['clean_owner_id']
    avg_days = best_agent_row['days_diff']
    # Debug print
    # print(f"Best agent: {best_agent}, Avg days: {avg_days}")
else:
    best_agent = "No data"

print("__RESULT__:")
print(json.dumps(best_agent))"""

env_args = {'var_function-call-9489093488560635064': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-9820404770155361762': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}], 'var_function-call-14848741335113478821': 'file_storage/function-call-14848741335113478821.json', 'var_function-call-14524369767035541979': 'file_storage/function-call-14524369767035541979.json'}

exec(code, env_args)
