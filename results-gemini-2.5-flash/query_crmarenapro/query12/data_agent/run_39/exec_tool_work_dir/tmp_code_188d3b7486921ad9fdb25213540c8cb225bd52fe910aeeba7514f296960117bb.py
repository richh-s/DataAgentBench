code = """import pandas as pd

opportunities_df = pd.DataFrame(locals()['var_function-call-13526798330329408712'])
contracts_df = pd.DataFrame(locals()['var_function-call-16026548743202574846'])

# Clean 'Id' and 'OwnerId' in opportunities_df
opportunities_df['Id'] = opportunities_df['Id'].str.replace("#", "", regex=False).str.strip()
opportunities_df['OwnerId'] = opportunities_df['OwnerId'].str.replace("#", "", regex=False).str.strip()

# Filter for opportunities with a contract
opportunities_with_contracts = opportunities_df[opportunities_df['ContractID__c'] != 'None'].copy()

# Merge opportunities with contracts on ContractID__c and Id
merged_df = pd.merge(opportunities_with_contracts, contracts_df, left_on='ContractID__c', right_on='Id', suffixes=('_opp', '_contract'))

# Convert date columns to datetime objects directly
merged_df['CreatedDate'] = pd.to_datetime(merged_df['CreatedDate'])
merged_df['CompanySignedDate'] = pd.to_datetime(merged_df['CompanySignedDate'])

# Calculate turnaround time in days
merged_df['TurnaroundTime'] = (merged_df['CompanySignedDate'] - merged_df['CreatedDate']).dt.days

# Group by OwnerId and calculate the average turnaround time
average_turnaround = merged_df.groupby('OwnerId')['TurnaroundTime'].mean().reset_index()

# Find the agent with the quickest average turnaround
quickest_agent = average_turnaround.loc[average_turnaround['TurnaroundTime'].idxmin()]

print("__RESULT__:")
print(pd.Series(quickest_agent['OwnerId']).to_json())"""

env_args = {'var_function-call-14334648505007096516': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_function-call-13526798330329408712': [{'Id': '#006Wt000007B1klIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000'}, {'Id': '006Wt000007B49NIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000'}, {'Id': '006Wt000007B62sIAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000'}, {'Id': '006Wt000007B6itIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000'}, {'Id': '#006Wt000007B7tQIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000'}, {'Id': '#006Wt000007B7yJIAS', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000'}, {'Id': '006Wt000007B8CqIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000'}, {'Id': '#006Wt000007B8FyIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '#006Wt000007BA3JIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000'}, {'Id': '006Wt000007BABLIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000'}, {'Id': '006Wt000007BAHlIAO', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000'}, {'Id': '006Wt000007BAPrIAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000'}, {'Id': '006Wt000007BBDrIAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000'}, {'Id': '006Wt000007BBc1IAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000'}, {'Id': '006Wt000007BCLEIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000'}, {'Id': '006Wt000007BCTFIA4', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000'}, {'Id': '#006Wt000007BChmIAG', 'ContractID__c': '800Wt00000DE9FFIA1', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000'}, {'Id': '006Wt000007BDApIAO', 'ContractID__c': '800Wt00000DE8sgIAD', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000'}, {'Id': '#006Wt000007BDXPIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000'}, {'Id': '006Wt000007BDcEIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000'}, {'Id': '006Wt000007BDpAIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '006Wt000007BETVIA4', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000'}, {'Id': '#006Wt000007BEV4IAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000'}, {'Id': '006Wt000007BFUOIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000'}, {'Id': '006Wt000007BGAIIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000'}, {'Id': '#006Wt000007BGDVIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000'}, {'Id': '006Wt000007BHPhIAO', 'ContractID__c': '800Wt00000DE9ryIAD', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000'}, {'Id': '#006Wt000007BHZNIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000'}, {'Id': '#006Wt000007BHfpIAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000'}, {'Id': '006Wt000007BHr7IAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000'}], 'var_function-call-17142474302995468068': ['800Wt00000DE9FFIA1', '800Wt00000DE8sgIAD', '800Wt00000DE9ryIAD'], 'var_function-call-16026548743202574846': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
