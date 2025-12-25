code = """import pandas as pd
import json

contracts_data = locals()['var_function-call-8882953471666003693']
with open(locals()['var_function-call-8882953471666002530'], 'r') as f:
    opportunities_data = json.load(f)

df_contracts = pd.DataFrame(contracts_data)
df_opps = pd.DataFrame(opportunities_data)

def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#').strip()
    return x

df_contracts['Id'] = df_contracts['Id'].apply(clean_id)
df_opps['ContractID__c'] = df_opps['ContractID__c'].apply(clean_id)
df_opps['OwnerId'] = df_opps['OwnerId'].apply(clean_id)

merged = pd.merge(df_opps, df_contracts, left_on='ContractID__c', right_on='Id', how='inner')

# Convert dates
# CreatedDate is like "2023-08-14T10:30:00.000+0000"
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
# CompanySignedDate is "2023-04-15"
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# Calculate days difference using dates (naive)
merged['CreatedDate_date'] = merged['CreatedDate'].dt.date
merged['CompanySignedDate_date'] = merged['CompanySignedDate'].dt.date

merged['DurationDays'] = (merged['CompanySignedDate_date'] - merged['CreatedDate_date']).apply(lambda x: x.days)

# Filter out negative durations just in case
merged = merged[merged['DurationDays'] >= 0]

# Filter for April 2023 signing
merged = merged[
    (merged['CompanySignedDate'] >= '2023-04-01') & 
    (merged['CompanySignedDate'] <= '2023-04-30')
]

agent_performance = merged.groupby('OwnerId')['DurationDays'].mean().reset_index()

if not agent_performance.empty:
    best_agent = agent_performance.loc[agent_performance['DurationDays'].idxmin()]
    result = best_agent['OwnerId']
else:
    result = "No data found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8882953471666003693': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-8882953471666002530': 'file_storage/function-call-8882953471666002530.json'}

exec(code, env_args)
