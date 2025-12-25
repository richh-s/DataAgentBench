code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-5922732362269708172'], 'r') as f:
    opps = json.load(f)
with open(locals()['var_function-call-8554849976764653737'], 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

# Clean IDs
# Remove leading '#' from ContractID__c in Opportunity and Id in Contract
df_opp['ContractID__c'] = df_opp['ContractID__c'].astype(str).str.lstrip('#')
df_cont['Id'] = df_cont['Id'].astype(str).str.lstrip('#')

# Remove leading '#' from OwnerId in Opportunity
df_opp['OwnerId'] = df_opp['OwnerId'].astype(str).str.lstrip('#')

# Convert dates
# Opportunity CreatedDate is ISO format with timezone likely
df_opp['CreatedDate'] = pd.to_datetime(df_opp['CreatedDate'])
# CloseDate is YYYY-MM-DD
df_opp['CloseDate'] = pd.to_datetime(df_opp['CloseDate'])

# Contract CompanySignedDate is YYYY-MM-DD
df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'])

# Join
# We need opportunities closed in April 2023
# Filter by CloseDate first to reduce size? Or join then filter.
# Let's join first to get SignedDate.
merged = pd.merge(df_opp, df_cont, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_cont'))

# Filter for Closing in April 2023
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

# Check both interpretations?
# Interpretation 1: CloseDate in April 2023 (Standard sales reporting)
# Interpretation 2: CompanySignedDate in April 2023 (Strict adherence to "Cycle" metric timing)
# The prompt says "turnaround from opening to closing opportunities ... in April 2023".
# "Closing opportunities" sounds like the action of closing (CloseDate).
# But the metric definition is strict about SignedDate.
# Let's try Interpretation 1 first, as it matches "Closing opportunities" phrase.
merged_apr = merged[(merged['CloseDate'] >= start_date) & (merged['CloseDate'] <= end_date)].copy()

if merged_apr.empty:
    # If empty, maybe check SignedDate interpretation
    merged_apr = merged[(merged['CompanySignedDate'] >= start_date) & (merged['CompanySignedDate'] <= end_date)].copy()

# Calculate Cycle
# Policy: days between CreatedDate and CompanySignedDate
# CreatedDate has time, SignedDate is just date (midnight).
# We should probably take the difference in days.
# (SignedDate - CreatedDate).days
# Note: CreatedDate is timestamp. If we convert CreatedDate to date(), it might be cleaner.
merged_apr['CreatedDate_dt'] = merged_apr['CreatedDate'].dt.date
merged_apr['CompanySignedDate_dt'] = merged_apr['CompanySignedDate'].dt.date
# Convert back to datetime to subtract or just subtract dates
merged_apr['cycle_days'] = (pd.to_datetime(merged_apr['CompanySignedDate_dt']) - pd.to_datetime(merged_apr['CreatedDate_dt'])).dt.days

# Filter out negative cycles if any (bad data)
merged_apr = merged_apr[merged_apr['cycle_days'] >= 0]

# Group by OwnerId and average
result = merged_apr.groupby('OwnerId')['cycle_days'].mean().reset_index()
result = result.sort_values('cycle_days', ascending=True)

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-13809224892334651697': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-5922732362269708172': 'file_storage/function-call-5922732362269708172.json', 'var_function-call-8554849976764653737': 'file_storage/function-call-8554849976764653737.json'}

exec(code, env_args)
