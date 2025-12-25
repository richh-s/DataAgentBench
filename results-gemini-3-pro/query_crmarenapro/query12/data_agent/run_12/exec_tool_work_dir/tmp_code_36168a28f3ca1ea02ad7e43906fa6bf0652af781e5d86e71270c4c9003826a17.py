code = """import json
import pandas as pd
from datetime import datetime

# Load Opportunity data
with open('var_function-call-13183294150186973771.json', 'r') as f:
    opp_data = json.load(f)
df_opp = pd.DataFrame(opp_data)

# Load Contract data
with open('var_function-call-13183294150186975218.json', 'r') as f:
    cont_data = json.load(f)
df_cont = pd.DataFrame(cont_data)

# Clean IDs function
def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Clean columns
df_opp['ContractID__c'] = df_opp['ContractID__c'].apply(clean_id)
df_opp['OwnerId'] = df_opp['OwnerId'].apply(clean_id)
df_cont['Id'] = df_cont['Id'].apply(clean_id)

# Filter valid contracts in opp
df_opp = df_opp[df_opp['ContractID__c'].notnull() & (df_opp['ContractID__c'] != 'None') & (df_opp['ContractID__c'] != '')]

# Merge
merged = pd.merge(df_opp, df_cont, left_on='ContractID__c', right_on='Id', how='inner')

# Parse dates
# CreatedDate: 2023-09-05T11:32:46.000+0000
# CompanySignedDate: 2021-07-16
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate']).dt.tz_convert(None) # Remove timezone for subtraction if needed or keep consistent
# CompanySignedDate is just date, convert to datetime
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'])

# We need rows where CompanySignedDate is in April 2023
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

# Filter
filtered = merged[(merged['CompanySignedDate'] >= start_date) & (merged['CompanySignedDate'] <= end_date)].copy()

# Calculate turnaround
# Definition: number of days between creation and signed date
# We will use the difference in days. Since CreatedDate has time, we can normalize it to date or keep it.
# Usually "days between date A and date B" = B - A.
# If we treat CompanySignedDate as midnight, and CreatedDate is noon, result is X days - 12 hours.
# Let's normalize CreatedDate to midnight (start of the day) to get integer days, or full float days.
# "Number of days between" typically implies DateDiff(day, start, end).
# I'll normalize CreatedDate to date.
filtered['Turnaround'] = (filtered['CompanySignedDate'] - filtered['CreatedDate'].dt.normalize()).dt.days

# Check for negatives
# filtered = filtered[filtered['Turnaround'] >= 0] # Optional, but good practice

# Group by OwnerId
grouped = filtered.groupby('OwnerId')['Turnaround'].mean().reset_index()
grouped = grouped.sort_values('Turnaround')

print("__RESULT__:")
print(grouped.to_json(orient='records'))"""

env_args = {'var_function-call-8065358297862811880': [{'Id': '006Wt000007AvVeIAK', 'OwnerId': '005Wt000003NIqXIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-09-05T11:32:46.000+0000'}, {'Id': '006Wt000007Aw3WIAS', 'OwnerId': '005Wt000003NIc1IAG', 'ContractID__c': 'None', 'CreatedDate': '2024-04-05T12:15:30.000+0000'}, {'Id': '006Wt000007Aw3XIAS', 'OwnerId': '#005Wt000003NJZhIAO', 'ContractID__c': 'None', 'CreatedDate': '2021-02-10T14:23:45.000+0000'}, {'Id': '006Wt000007Aya9IAC', 'OwnerId': '005Wt000003NDJ0IAO', 'ContractID__c': 'None', 'CreatedDate': '2023-08-11T09:30:00.000+0000'}, {'Id': '006Wt000007AyaAIAS', 'OwnerId': '005Wt000003NJxtIAG', 'ContractID__c': 'None', 'CreatedDate': '2022-07-20T14:13:45.000+0000'}, {'Id': '006Wt000007AyaBIAS', 'OwnerId': '005Wt000003NErnIAG', 'ContractID__c': '800Wt00000DE9DdIAL', 'CreatedDate': '2023-08-14T10:30:00.000+0000'}, {'Id': '#006Wt000007AyaCIAS', 'OwnerId': '005Wt000003NEdJIAW', 'ContractID__c': 'None', 'CreatedDate': '2020-12-18T14:35:47.000+0000'}, {'Id': '#006Wt000007AyaDIAS', 'OwnerId': '005Wt000003NIybIAG', 'ContractID__c': 'None', 'CreatedDate': '2021-05-13T10:30:45.000+0000'}, {'Id': '006Wt000007Ayi2IAC', 'OwnerId': '005Wt000003NIdeIAG', 'ContractID__c': 'None', 'CreatedDate': '2021-03-02T10:45:30.000+0000'}, {'Id': '006Wt000007AywiIAC', 'OwnerId': '005Wt000003NBsIIAW', 'ContractID__c': '800Wt00000DE45uIAD', 'CreatedDate': '2021-11-05T10:15:30.000+0000'}], 'var_function-call-8065358297862814401': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDNFVIA5', 'CompanySignedDate': '2021-06-26'}, {'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDPXRIA5', 'CompanySignedDate': '2022-04-22'}, {'Id': '800Wt00000DDPXSIA5', 'CompanySignedDate': '2023-02-25'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}], 'var_function-call-13183294150186973771': 'file_storage/function-call-13183294150186973771.json', 'var_function-call-13183294150186975218': 'file_storage/function-call-13183294150186975218.json'}

exec(code, env_args)
