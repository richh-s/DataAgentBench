code = """import pandas as pd
import json

# Load data
opp_file = locals()['var_function-call-4712470569421540394']
contract_file = locals()['var_function-call-6485666177909089622']

with open(opp_file, 'r') as f:
    opp_data = json.load(f)
with open(contract_file, 'r') as f:
    contract_data = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_contract = pd.DataFrame(contract_data)

# Helper function to clean IDs
def clean_id(x):
    if pd.isna(x):
        return x
    return str(x).strip().lstrip('#')

# Clean columns
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_contract['Id'] = df_contract['Id'].apply(clean_id)

# Convert dates
df_opp['CreatedDate'] = pd.to_datetime(df_opp['CreatedDate'])
df_contract['CompanySignedDate'] = pd.to_datetime(df_contract['CompanySignedDate'])

# Filter Contracts for April 2023
start_date = pd.Timestamp('2023-04-01').tz_localize(None)
end_date = pd.Timestamp('2023-04-30').tz_localize(None)

# Contracts don't have time usually, but let's ensure tz naive for comparison or handle it.
# The data preview shows "YYYY-MM-DD" for CompanySignedDate, so it's naive.
# CreatedDate is tz-aware. We should probably make CompanySignedDate tz-aware or CreatedDate tz-naive.
# CreatedDate has +0000. Let's convert CreatedDate to naive UTC or just naive.
df_opp['CreatedDate'] = df_opp['CreatedDate'].dt.tz_convert(None)

# Filter contracts
df_contract_april = df_contract[
    (df_contract['CompanySignedDate'] >= start_date) & 
    (df_contract['CompanySignedDate'] <= end_date)
]

# Merge
merged = pd.merge(df_opp, df_contract_april, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate turnaround
# sales cycle: days between opportunity's creation date and company signed date
merged['turnaround'] = (merged['CompanySignedDate'] - merged['CreatedDate']).dt.total_seconds() / (24 * 3600)

# Group by OwnerId (Agent) and calculate average
avg_turnaround = merged.groupby('OwnerId')['turnaround'].mean().reset_index()

# Find quickest (minimum)
if not avg_turnaround.empty:
    min_row = avg_turnaround.loc[avg_turnaround['turnaround'].idxmin()]
    result = min_row['OwnerId']
else:
    result = "No opportunities closed in April 2023"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5433573454183969237': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-4712470569421540394': 'file_storage/function-call-4712470569421540394.json', 'var_function-call-6485666177909089622': 'file_storage/function-call-6485666177909089622.json'}

exec(code, env_args)
