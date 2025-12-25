code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open('var_function-call-17973372094163373365.json', 'r') as f:
    opportunities = json.load(f)

with open('var_function-call-8515508793061584721.json', 'r') as f:
    contracts = json.load(f)

# Convert to DataFrames
df_opp = pd.DataFrame(opportunities)
df_cont = pd.DataFrame(contracts)

# Clean IDs function
def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

# Clean IDs in Opportunity
df_opp['Id'] = df_opp['Id'].apply(clean_id)
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)

# Clean IDs in Contract
df_cont['Id'] = df_cont['Id'].apply(clean_id)
df_cont['CompanySignedDate'] = df_cont['CompanySignedDate'].astype(str).str.strip()

# Filter Contracts for April 2023
# Format is YYYY-MM-DD
df_cont['SignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'], errors='coerce')
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

# Filter contracts
df_cont_apr = df_cont[(df_cont['SignedDate'] >= start_date) & (df_cont['SignedDate'] <= end_date)].copy()

print(f"Contracts in April 2023: {len(df_cont_apr)}")
# print(df_cont_apr[['Id', 'CompanySignedDate']].head())

# Join Opportunity and Contract
# Opportunity.ContractID__c -> Contract.Id
merged = pd.merge(df_opp, df_cont_apr, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_cont'))

print(f"Merged records: {len(merged)}")

if len(merged) > 0:
    # Calculate turnaround
    # Parse CreatedDate
    # CreatedDate format: 2023-09-05T11:32:46.000+0000
    # We need to handle the timezone or ignore it.
    # We will convert to date object for difference calculation.
    
    # Simple parse
    merged['CreatedDate_dt'] = pd.to_datetime(merged['CreatedDate'], errors='coerce')
    
    # Check for NaT
    merged = merged.dropna(subset=['CreatedDate_dt', 'SignedDate'])
    
    # Calculate days difference
    # Normalize to date (remove time)
    merged['CreatedDate_date'] = merged['CreatedDate_dt'].dt.date
    merged['SignedDate_date'] = merged['SignedDate'].dt.date
    
    merged['TurnaroundDays'] = (pd.to_datetime(merged['SignedDate_date']) - pd.to_datetime(merged['CreatedDate_date'])).dt.days
    
    # Group by OwnerId and calculate average
    agent_perf = merged.groupby('OwnerId')['TurnaroundDays'].mean().reset_index()
    agent_perf = agent_perf.sort_values(by='TurnaroundDays')
    
    print("Agent Performance:")
    print(agent_perf.head())
    
    best_agent = agent_perf.iloc[0]['OwnerId']
    print("__RESULT__:")
    print(json.dumps(best_agent))
else:
    print("No closed opportunities found in April 2023.")
    print("__RESULT__:")
    print(json.dumps("No agent found"))"""

env_args = {'var_function-call-17973372094163373365': 'file_storage/function-call-17973372094163373365.json', 'var_function-call-17973372094163371866': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-15667071576463263050': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDNFVIA5', 'CompanySignedDate': '2021-06-26'}, {'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDPXRIA5', 'CompanySignedDate': '2022-04-22'}, {'Id': '800Wt00000DDPXSIA5', 'CompanySignedDate': '2023-02-25'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}], 'var_function-call-8515508793061584721': 'file_storage/function-call-8515508793061584721.json'}

exec(code, env_args)
