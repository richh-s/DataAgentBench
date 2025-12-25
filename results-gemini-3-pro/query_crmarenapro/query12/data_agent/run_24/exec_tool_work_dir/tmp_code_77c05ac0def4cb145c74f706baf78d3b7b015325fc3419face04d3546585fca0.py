code = """import pandas as pd
import json
from datetime import datetime, date

# Load data
with open(locals()['var_function-call-2997551485273360769'], 'r') as f:
    opportunities = json.load(f)

with open(locals()['var_function-call-2997551485273358500'], 'r') as f:
    contracts = json.load(f)

# Create DataFrame
df_opp = pd.DataFrame(opportunities)
df_cont = pd.DataFrame(contracts)

# Clean IDs
df_opp['ContractID__c'] = df_opp['ContractID__c'].astype(str).str.strip().str.lstrip('#')
df_opp['OwnerId'] = df_opp['OwnerId'].astype(str).str.strip().str.lstrip('#')
df_cont['Id'] = df_cont['Id'].astype(str).str.strip().str.lstrip('#')

# Merge
merged = pd.merge(df_opp, df_cont, left_on='ContractID__c', right_on='Id', how='inner')

# Parse dates
# CreatedDate format: 2023-09-05T11:32:46.000+0000
# CompanySignedDate format: 2021-07-16
# We need to be careful with timezones. CreatedDate has offset. CompanySignedDate is naive.
# We will convert CreatedDate to naive UTC (or just strip tz) or normalize to date.
merged['CreatedDate_dt'] = pd.to_datetime(merged['CreatedDate']).dt.tz_convert(None).dt.normalize()
merged['CompanySignedDate_dt'] = pd.to_datetime(merged['CompanySignedDate'])

# Filter for April 2023 based on CompanySignedDate
start_date = pd.Timestamp('2023-04-01')
end_date = pd.Timestamp('2023-04-30')

filtered = merged[
    (merged['CompanySignedDate_dt'] >= start_date) & 
    (merged['CompanySignedDate_dt'] <= end_date)
].copy()

# Calculate duration
filtered['Duration'] = (filtered['CompanySignedDate_dt'] - filtered['CreatedDate_dt']).dt.days

# Filter out invalid durations (negative)
filtered = filtered[filtered['Duration'] >= 0]

if filtered.empty:
    print("__RESULT__:")
    print(json.dumps({"error": "No data found for April 2023"}))
else:
    # Group by OwnerId and calc mean
    avg_duration = filtered.groupby('OwnerId')['Duration'].mean().reset_index()

    # Find min
    min_row = avg_duration.sort_values('Duration').iloc[0]

    result = {
        "OwnerId": min_row['OwnerId'],
        "AverageDuration": min_row['Duration']
    }
    
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-14128943283985432638': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-09-05T11:32:46.000+0000'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIc1IAG', 'CreatedDate': '2024-04-05T12:15:30.000+0000'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJZhIAO', 'CreatedDate': '2021-02-10T14:23:45.000+0000'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDJ0IAO', 'CreatedDate': '2023-08-11T09:30:00.000+0000'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2022-07-20T14:13:45.000+0000'}, {'Id': '006Wt000007AyaBIAS', 'ContractID__c': '800Wt00000DE9DdIAL', 'OwnerId': '005Wt000003NErnIAG', 'CreatedDate': '2023-08-14T10:30:00.000+0000'}, {'Id': '#006Wt000007AyaCIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEdJIAW', 'CreatedDate': '2020-12-18T14:35:47.000+0000'}, {'Id': '#006Wt000007AyaDIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIybIAG', 'CreatedDate': '2021-05-13T10:30:45.000+0000'}, {'Id': '006Wt000007Ayi2IAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2021-03-02T10:45:30.000+0000'}, {'Id': '006Wt000007AywiIAC', 'ContractID__c': '800Wt00000DE45uIAD', 'OwnerId': '005Wt000003NBsIIAW', 'CreatedDate': '2021-11-05T10:15:30.000+0000'}], 'var_function-call-14128943283985432999': [{'Id': '#800Wt00000DD0SZIA1', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDNFVIA5', 'CompanySignedDate': '2021-06-26'}, {'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDPXRIA5', 'CompanySignedDate': '2022-04-22'}, {'Id': '800Wt00000DDPXSIA5', 'CompanySignedDate': '2023-02-25'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}], 'var_function-call-2997551485273360769': 'file_storage/function-call-2997551485273360769.json', 'var_function-call-2997551485273358500': 'file_storage/function-call-2997551485273358500.json'}

exec(code, env_args)
