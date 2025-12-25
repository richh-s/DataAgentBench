code = """import pandas as pd
import json

# Load contracts
contracts_data = locals()['var_function-call-7531152781383160862']
# contracts_data is a list of dicts

# Load opportunities
with open(locals()['var_function-call-7531152781383163213'], 'r') as f:
    opportunities_data = json.load(f)

df_contracts = pd.DataFrame(contracts_data)
df_opportunities = pd.DataFrame(opportunities_data)

# Clean IDs
def clean_id(x):
    if pd.isna(x):
        return x
    return str(x).lstrip('#').strip()

df_contracts['CleanId'] = df_contracts['Id'].apply(clean_id)
df_opportunities['CleanContractId'] = df_opportunities['ContractID__c'].apply(clean_id)
df_opportunities['CleanOwnerId'] = df_opportunities['OwnerId'].apply(clean_id)

# Merge
merged = pd.merge(df_opportunities, df_contracts, left_on='CleanContractId', right_on='CleanId', how='inner')

# Parse dates
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'])
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# Filter for April 2023 (just to be safe and precise)
merged = merged[
    (merged['CompanySignedDate'] >= '2023-04-01') & 
    (merged['CompanySignedDate'] <= '2023-04-30')
]

# Calculate turnaround in days
merged['TurnaroundDays'] = (merged['CompanySignedDate'] - merged['CreatedDate']).dt.total_seconds() / (24 * 3600)

# Group by OwnerId and calculate average
avg_turnaround = merged.groupby('CleanOwnerId')['TurnaroundDays'].mean().reset_index()

# Find the minimum
if not avg_turnaround.empty:
    min_turnaround = avg_turnaround.loc[avg_turnaround['TurnaroundDays'].idxmin()]
    result = {
        "AgentId": min_turnaround['CleanOwnerId'],
        "AverageTurnaroundDays": min_turnaround['TurnaroundDays']
    }
else:
    result = "No data found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8590979690933556904': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'OwnerId': '005Wt000003NIqXIAW'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'OwnerId': '005Wt000003NIc1IAG'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'OwnerId': '#005Wt000003NJZhIAO'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'OwnerId': '005Wt000003NJxtIAG'}], 'var_function-call-8590979690933557055': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}], 'var_function-call-7531152781383160862': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}], 'var_function-call-7531152781383163213': 'file_storage/function-call-7531152781383163213.json'}

exec(code, env_args)
