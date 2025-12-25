code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-7482937184921980704'], 'r') as f:
    opportunities = json.load(f)

with open(locals()['var_function-call-7482937184921978201'], 'r') as f:
    contracts = json.load(f)

# Create DataFrames
df_opp = pd.DataFrame(opportunities)
df_con = pd.DataFrame(contracts)

# Clean IDs
def clean_id(x):
    if x is None:
        return None
    return str(x).strip().lstrip('#')

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_con['Id'] = df_con['Id'].apply(clean_id)

# Filter Contracts for April 2023
df_con['CompanySignedDate'] = pd.to_datetime(df_con['CompanySignedDate'], errors='coerce')
df_con = df_con[
    (df_con['CompanySignedDate'] >= '2023-04-01') & 
    (df_con['CompanySignedDate'] <= '2023-04-30')
]

# Merge
merged = pd.merge(df_opp, df_con, left_on='ContractID__c', right_on='Id', how='inner')

# Parse CreatedDate
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'], errors='coerce')

# Make CreatedDate timezone-naive
merged['CreatedDate'] = merged['CreatedDate'].dt.tz_localize(None)

# Check for invalid dates
merged = merged.dropna(subset=['CreatedDate', 'CompanySignedDate'])

# Calculate days difference
merged['days_diff'] = (merged['CompanySignedDate'] - merged['CreatedDate'].dt.normalize()).dt.days

# Group by Agent (OwnerId)
agent_stats = merged.groupby('OwnerId')['days_diff'].mean().reset_index()

# Find quickest (min average)
if not agent_stats.empty:
    quickest_agent = agent_stats.loc[agent_stats['days_diff'].idxmin()]
    result = quickest_agent['OwnerId']
else:
    result = "No data found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-504095308823504375': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-7482937184921980704': 'file_storage/function-call-7482937184921980704.json', 'var_function-call-7482937184921978201': 'file_storage/function-call-7482937184921978201.json'}

exec(code, env_args)
