code = """import json
import pandas as pd

# Get file paths from locals
opps_path = locals()['var_function-call-13290033183122185402']
cont_path = locals()['var_function-call-1685652105295308624']

# Load data
with open(opps_path, 'r') as f:
    opps = json.load(f)
with open(cont_path, 'r') as f:
    contracts = json.load(f)

df_opp = pd.DataFrame(opps)
df_cont = pd.DataFrame(contracts)

# Clean IDs
def clean_id(x):
    if pd.isna(x): return x
    return str(x).replace('#', '').strip()

df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id'] = df_cont['Id'].apply(clean_id)

# Parse dates
df_opp['CreatedDate'] = pd.to_datetime(df_opp['CreatedDate'])
df_cont['CompanySignedDate'] = pd.to_datetime(df_cont['CompanySignedDate'])

# Filter Contracts for April 2023
# Closing date in April 2023
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

df_cont_apr = df_cont[(df_cont['CompanySignedDate'] >= start_date) & (df_cont['CompanySignedDate'] <= end_date)].copy()

# Join
merged = pd.merge(df_opp, df_cont_apr, left_on='ContractID__c', right_on='Id', how='inner')

# Calculate duration
# Normalize CreatedDate to midnight to calculate date difference
merged['CreatedDate_date'] = merged['CreatedDate'].dt.normalize()
merged['Duration'] = (merged['CompanySignedDate'] - merged['CreatedDate_date']).dt.days

# Group by Agent
res = merged.groupby('OwnerId')['Duration'].mean().reset_index()
res = res.sort_values('Duration', ascending=True)

print("__RESULT__:")
print(res.to_json(orient='records'))"""

env_args = {'var_function-call-1884381200923402192': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-9607055922851127303': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'OwnerId': '005Wt000003NIqXIAW'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'OwnerId': '005Wt000003NIc1IAG'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'OwnerId': '#005Wt000003NJZhIAO'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'OwnerId': '005Wt000003NDJ0IAO'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'OwnerId': '005Wt000003NJxtIAG'}], 'var_function-call-6901725502628215460': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}], 'var_function-call-8858652224088214842': [{'cnt': '1170'}], 'var_function-call-13290033183122185402': 'file_storage/function-call-13290033183122185402.json', 'var_function-call-1685652105295308624': 'file_storage/function-call-1685652105295308624.json'}

exec(code, env_args)
