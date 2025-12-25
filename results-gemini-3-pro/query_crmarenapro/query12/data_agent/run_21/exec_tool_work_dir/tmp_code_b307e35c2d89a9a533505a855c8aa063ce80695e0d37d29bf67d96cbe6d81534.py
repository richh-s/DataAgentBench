code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-9859197109537300248'], 'r') as f:
    opp_data = json.load(f)
with open(locals()['var_function-call-6844187562145716595'], 'r') as f:
    contract_data = json.load(f)

# Convert to DataFrame
df_opp = pd.DataFrame(opp_data)
df_contract = pd.DataFrame(contract_data)

# Clean IDs function
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

# Apply cleaning
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_contract['Id'] = df_contract['Id'].apply(clean_id)

# Filter Contracts for April 2023
# CompanySignedDate format is YYYY-MM-DD
df_contract['CompanySignedDate'] = pd.to_datetime(df_contract['CompanySignedDate'])
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

df_contract_apr = df_contract[(df_contract['CompanySignedDate'] >= start_date) & (df_contract['CompanySignedDate'] <= end_date)].copy()

# Merge
# Opportunity.ContractID__c -> Contract.Id
merged = pd.merge(df_opp, df_contract_apr, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate duration
# Opportunity.CreatedDate format example: "2023-09-05T11:32:46.000+0000"
# We need to handle the format.
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])

# Calculate difference in days
# Since CompanySignedDate is just date (midnight), and CreatedDate has time.
# Usually sales cycle is days. So we can convert CreatedDate to date or keep both as timestamps (normalizing signed date).
# Let's normalize CreatedDate to normalize date or just subtract.
# Subtracting timestamp from timestamp gives timedelta.
merged['Duration'] = (merged['CompanySignedDate'] - merged['CreatedDate']).dt.total_seconds() / (24 * 3600)

# Filter out valid durations if any negative?
# merged = merged[merged['Duration'] >= 0] 
# (If created date is after signed date, that's data issue, but we compute average).
# Let's check for negative values later if needed.

# Group by OwnerId and calculate average
result = merged.groupby('OwnerId')['Duration'].mean().reset_index()

# Find min
min_avg = result.loc[result['Duration'].idxmin()]

print("__RESULT__:")
print(json.dumps({
    "BestAgentId": min_avg['OwnerId'],
    "AverageDays": min_avg['Duration'],
    "AllResults": result.to_dict(orient='records')
}))"""

env_args = {'var_function-call-11044286556284228626': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-9859197109537300248': 'file_storage/function-call-9859197109537300248.json', 'var_function-call-6844187562145716595': 'file_storage/function-call-6844187562145716595.json'}

exec(code, env_args)
