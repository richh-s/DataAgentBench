code = """import pandas as pd

opportunities_data = locals()['var_function-call-16834093609617842552']
contracts_data = locals()['var_function-call-2927072685243875421']


opportunities_df = pd.DataFrame(opportunities_data)
contracts_df = pd.DataFrame(contracts_data)

# Clean IDs by removing leading '#' and stripping whitespace
opportunities_df['Id'] = opportunities_df['Id'].astype(str).str.replace('#', '').str.strip()
opportunities_df['OwnerId'] = opportunities_df['OwnerId'].astype(str).str.replace('#', '').str.strip()
opportunities_df['ContractID__c'] = opportunities_df['ContractID__c'].astype(str).str.replace('#', '').str.strip()
contracts_df['Id'] = contracts_df['Id'].astype(str).str.replace('#', '').str.strip()


# Convert date columns to datetime objects
opportunities_df['CreatedDate'] = pd.to_datetime(opportunities_df['CreatedDate'])
contracts_df['CompanySignedDate'] = pd.to_datetime(contracts_df['CompanySignedDate'])


# Merge opportunities and contracts DataFrames
merged_df = pd.merge(opportunities_df, contracts_df, left_on='ContractID__c', right_on='Id', how='inner', suffixes=('_opp', '_contract'))


# Calculate turnaround time
merged_df['turnaround_days'] = (merged_df['CompanySignedDate'] - merged_df['CreatedDate']).dt.days


# Calculate average turnaround time per agent
average_turnaround = merged_df.groupby('OwnerId')['turnaround_days'].mean().reset_index()


# Find the agent with the quickest average turnaround
quickest_agent = average_turnaround.sort_values(by='turnaround_days', ascending=True).iloc[0]


print('__RESULT__:')
print(quickest_agent['OwnerId'])"""

env_args = {'var_function-call-16834093609617842552': [{'Id': '#006Wt000007B1klIAC', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBylIAG'}, {'Id': '006Wt000007B49NIAS', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIs9IAG'}, {'Id': '006Wt000007B62sIAC', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJZhIAO'}, {'Id': '006Wt000007B6itIAC', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJMnIAO'}, {'Id': '#006Wt000007B7tQIAS', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW'}, {'Id': '#006Wt000007B7yJIAS', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NEdJIAW'}, {'Id': '006Wt000007B8CqIAK', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NInKIAW'}, {'Id': '#006Wt000007B8FyIAK', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIovIAG'}, {'Id': '#006Wt000007BA3JIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NF9WIAW'}, {'Id': '006Wt000007BABLIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDEBIA4'}, {'Id': '006Wt000007BAHlIAO', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NFhPIAW'}, {'Id': '006Wt000007BAPrIAO', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG'}, {'Id': '006Wt000007BBDrIAO', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ1pIAG'}, {'Id': '006Wt000007BBc1IAG', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW'}, {'Id': '006Wt000007BCLEIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJBVIA4'}, {'Id': '006Wt000007BCTFIA4', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBcBIAW'}, {'Id': '#006Wt000007BChmIAG', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1', 'OwnerId': '005Wt000003NJgAIAW'}, {'Id': '006Wt000007BDApIAO', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD', 'OwnerId': '005Wt000003NISMIA4'}, {'Id': '#006Wt000007BDXPIA4', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ0EIAW'}, {'Id': '006Wt000007BDcEIAW', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIAbIAO'}, {'Id': '006Wt000007BDpAIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW'}, {'Id': '006Wt000007BETVIA4', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJjNIAW'}, {'Id': '#006Wt000007BEV4IAO', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NFRKIA4'}, {'Id': '006Wt000007BFUOIA4', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NHpdIAG'}, {'Id': '006Wt000007BGAIIA4', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG'}, {'Id': '#006Wt000007BGDVIA4', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NBcBIAW'}, {'Id': '006Wt000007BHPhIAO', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD', 'OwnerId': '#005Wt000003NEa3IAG'}, {'Id': '#006Wt000007BHZNIA4', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIaPIAW'}, {'Id': '#006Wt000007BHfpIAG', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW'}, {'Id': '006Wt000007BHr7IAG', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW'}], 'var_function-call-5256641209249845914': ['800Wt00000DE9FFIA1', '800Wt00000DE8sgIAD', '800Wt00000DE9ryIAD'], 'var_function-call-2927072685243875421': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
