code = """import pandas as pd
import json

# Load data
opps = pd.DataFrame(json.loads(locals()['var_function-call-9056824396102129480']))
contracts = pd.DataFrame(json.loads(locals()['var_function-call-16936274566812186692']))

# Helper function to clean IDs
def clean_id(x):
    if pd.isna(x):
        return None
    return str(x).strip().lstrip('#')

# Clean columns
opps['clean_ContractID'] = opps['ContractID__c'].apply(clean_id)
opps['clean_OwnerId'] = opps['OwnerId'].apply(clean_id)
contracts['clean_Id'] = contracts['Id'].apply(clean_id)

# Filter out opps with no contract
opps = opps[opps['clean_ContractID'] != 'None']
opps = opps[opps['clean_ContractID'].notna()]

# Convert dates
# Opportunity CreatedDate: "2023-04-15T09:00:34.000+0000"
opps['CreatedDate_dt'] = pd.to_datetime(opps['CreatedDate']).dt.date
# Contract CompanySignedDate: "2023-07-12"
contracts['CompanySignedDate_dt'] = pd.to_datetime(contracts['CompanySignedDate']).dt.date

# Merge
merged = pd.merge(opps, contracts, left_on='clean_ContractID', right_on='clean_Id', how='inner')

# Calculate duration
merged['duration'] = (pd.to_datetime(merged['CompanySignedDate_dt']) - pd.to_datetime(merged['CreatedDate_dt'])).dt.days

# Group by OwnerId and calculate average duration
avg_duration = merged.groupby('clean_OwnerId')['duration'].mean().reset_index()

# Find minimum
min_avg = avg_duration.sort_values('duration').iloc[0]

print("__RESULT__:")
print(json.dumps({
    "AgentId": min_avg['clean_OwnerId'],
    "AverageDuration": min_avg['duration'],
    "AllDurations": avg_duration.to_dict(orient='records')
}))"""

env_args = {'var_function-call-9056824396102129480': [{'Id': '#006Wt000007B1klIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000'}, {'Id': '006Wt000007B49NIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000'}, {'Id': '006Wt000007B62sIAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000'}, {'Id': '006Wt000007B6itIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000'}, {'Id': '#006Wt000007B7tQIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000'}, {'Id': '#006Wt000007B7yJIAS', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000'}, {'Id': '006Wt000007B8CqIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000'}, {'Id': '#006Wt000007B8FyIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '#006Wt000007BA3JIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000'}, {'Id': '006Wt000007BABLIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000'}, {'Id': '006Wt000007BAHlIAO', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000'}, {'Id': '006Wt000007BAPrIAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000'}, {'Id': '006Wt000007BBDrIAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000'}, {'Id': '006Wt000007BBc1IAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000'}, {'Id': '006Wt000007BCLEIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000'}, {'Id': '006Wt000007BCTFIA4', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000'}, {'Id': '#006Wt000007BChmIAG', 'ContractID__c': '800Wt00000DE9FFIA1', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000'}, {'Id': '006Wt000007BDApIAO', 'ContractID__c': '800Wt00000DE8sgIAD', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000'}, {'Id': '#006Wt000007BDXPIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000'}, {'Id': '006Wt000007BDcEIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000'}, {'Id': '006Wt000007BDpAIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '006Wt000007BETVIA4', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000'}, {'Id': '#006Wt000007BEV4IAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000'}, {'Id': '006Wt000007BFUOIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000'}, {'Id': '006Wt000007BGAIIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000'}, {'Id': '#006Wt000007BGDVIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000'}, {'Id': '006Wt000007BHPhIAO', 'ContractID__c': '800Wt00000DE9ryIAD', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000'}, {'Id': '#006Wt000007BHZNIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000'}, {'Id': '#006Wt000007BHfpIAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000'}, {'Id': '006Wt000007BHr7IAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000'}], 'var_function-call-16936274566812186692': [{'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}, {'Id': '#800Wt00000DDZa2IAH', 'CompanySignedDate': '2024-03-19'}, {'Id': '#800Wt00000DDeUqIAL', 'CompanySignedDate': '2023-09-25'}, {'Id': '800Wt00000DDekwIAD', 'CompanySignedDate': '2024-05-17'}, {'Id': '#800Wt00000DDfKSIA1', 'CompanySignedDate': '2023-08-24'}, {'Id': '#800Wt00000DDfKTIA1', 'CompanySignedDate': '2023-06-21'}, {'Id': '800Wt00000DDg3bIAD', 'CompanySignedDate': '2023-07-25'}, {'Id': '800Wt00000DDsBEIA1', 'CompanySignedDate': '2024-07-01'}, {'Id': '800Wt00000DDt5fIAD', 'CompanySignedDate': '2023-08-23'}, {'Id': '800Wt00000DDt8sIAD', 'CompanySignedDate': '2024-04-26'}, {'Id': '800Wt00000DDt8uIAD', 'CompanySignedDate': '2023-12-20'}, {'Id': '800Wt00000DDtNUIA1', 'CompanySignedDate': '2023-05-30'}, {'Id': '800Wt00000DDxHMIA1', 'CompanySignedDate': '2023-09-13'}, {'Id': '800Wt00000DDxR4IAL', 'CompanySignedDate': '2024-08-30'}, {'Id': '800Wt00000DDxZ5IAL', 'CompanySignedDate': '2023-06-22'}, {'Id': '800Wt00000DDyKWIA1', 'CompanySignedDate': '2023-10-06'}, {'Id': '800Wt00000DDyKXIA1', 'CompanySignedDate': '2024-07-06'}, {'Id': '800Wt00000DDyuzIAD', 'CompanySignedDate': '2023-10-18'}, {'Id': '800Wt00000DE0FFIA1', 'CompanySignedDate': '2024-04-21'}, {'Id': '800Wt00000DE0n7IAD', 'CompanySignedDate': '2023-10-31'}, {'Id': '#800Wt00000DE0rxIAD', 'CompanySignedDate': '2024-01-26'}, {'Id': '#800Wt00000DE0ryIAD', 'CompanySignedDate': '2023-05-12'}, {'Id': '#800Wt00000DE0s0IAD', 'CompanySignedDate': '2023-12-06'}, {'Id': '800Wt00000DE0s1IAD', 'CompanySignedDate': '2024-09-27'}, {'Id': '800Wt00000DE0wkIAD', 'CompanySignedDate': '2024-07-21'}, {'Id': '800Wt00000DE1JKIA1', 'CompanySignedDate': '2023-10-06'}, {'Id': '800Wt00000DE2QgIAL', 'CompanySignedDate': '2024-02-17'}, {'Id': '800Wt00000DE2qVIAT', 'CompanySignedDate': '2024-07-13'}, {'Id': '800Wt00000DE3kwIAD', 'CompanySignedDate': '2023-11-11'}, {'Id': '800Wt00000DE4NgIAL', 'CompanySignedDate': '2023-11-26'}, {'Id': '800Wt00000DE4YwIAL', 'CompanySignedDate': '2023-11-27'}, {'Id': '#800Wt00000DE4YxIAL', 'CompanySignedDate': '2024-05-07'}, {'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE90kIAD', 'CompanySignedDate': '2023-10-15'}, {'Id': '800Wt00000DE93xIAD', 'CompanySignedDate': '2024-04-07'}, {'Id': '800Wt00000DE97BIAT', 'CompanySignedDate': '2023-05-16'}, {'Id': '800Wt00000DE97DIAT', 'CompanySignedDate': '2023-09-15'}, {'Id': '800Wt00000DE9C2IAL', 'CompanySignedDate': '2023-07-19'}, {'Id': '800Wt00000DE9DdIAL', 'CompanySignedDate': '2023-11-23'}, {'Id': '#800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13'}, {'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}, {'Id': '800Wt00000DE9OvIAL', 'CompanySignedDate': '2023-08-29'}, {'Id': '800Wt00000DE9QXIA1', 'CompanySignedDate': '2023-08-23'}, {'Id': '800Wt00000DE9S9IAL', 'CompanySignedDate': '2023-10-16'}, {'Id': '800Wt00000DE9VNIA1', 'CompanySignedDate': '2023-06-21'}, {'Id': '800Wt00000DE9VOIA1', 'CompanySignedDate': '2024-06-17'}, {'Id': '800Wt00000DE9WzIAL', 'CompanySignedDate': '2024-09-16'}, {'Id': '800Wt00000DE9bpIAD', 'CompanySignedDate': '2023-08-29'}, {'Id': '#800Wt00000DE9dSIAT', 'CompanySignedDate': '2023-10-20'}, {'Id': '800Wt00000DE9f3IAD', 'CompanySignedDate': '2024-02-14'}, {'Id': '800Wt00000DE9iHIAT', 'CompanySignedDate': '2024-07-14'}, {'Id': '#800Wt00000DE9jtIAD', 'CompanySignedDate': '2023-12-21'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
