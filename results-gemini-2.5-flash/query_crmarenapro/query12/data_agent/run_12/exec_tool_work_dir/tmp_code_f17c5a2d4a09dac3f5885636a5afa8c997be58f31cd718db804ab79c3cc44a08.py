code = """import pandas as pd

opportunities_data = locals()['var_function-call-15208515023745265741']
contracts_data = locals()['var_function-call-5576841316155544126']

df_opportunities = pd.DataFrame(opportunities_data)
df_contracts = pd.DataFrame(contracts_data)

# Clean Ids by stripping "#" and whitespace
df_opportunities['Id'] = df_opportunities['Id'].astype(str).str.replace("#", "").str.strip()
df_opportunities['ContractID__c'] = df_opportunities['ContractID__c'].astype(str).str.replace("#", "").str.strip()
df_opportunities['OwnerId'] = df_opportunities['OwnerId'].astype(str).str.replace("#", "").str.strip()
df_contracts['Id'] = df_contracts['Id'].astype(str).str.replace("#", "").str.strip()

# Filter out opportunities without a contract, as per the sales cycle definition
df_opportunities_with_contracts = df_opportunities[df_opportunities['ContractID__c'] != 'None']

# Merge dataframes
df_merged = pd.merge(df_opportunities_with_contracts, df_contracts, left_on='ContractID__c', right_on='Id', suffixes=('_opp', '_contract'))

# Convert date columns to datetime objects and make CreatedDate timezone-naive
df_merged['CreatedDate'] = pd.to_datetime(df_merged['CreatedDate']).dt.tz_localize(None) # Remove timezone information
df_merged['CompanySignedDate'] = pd.to_datetime(df_merged['CompanySignedDate'])

# Calculate turnaround time in days
df_merged['TurnaroundTime'] = (df_merged['CompanySignedDate'] - df_merged['CreatedDate']).dt.days

# Calculate average turnaround time per agent
avg_turnaround_per_agent = df_merged.groupby('OwnerId')['TurnaroundTime'].mean().reset_index()

# Find the agent with the quickest average turnaround time
quickest_agent = avg_turnaround_per_agent.loc[avg_turnaround_per_agent['TurnaroundTime'].idxmin()]

print("__RESULT__:")
print(quickest_agent['OwnerId'])"""

env_args = {'var_function-call-15208515023745265741': [{'Id': '#006Wt000007B1klIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000'}, {'Id': '006Wt000007B49NIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000'}, {'Id': '006Wt000007B62sIAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000'}, {'Id': '006Wt000007B6itIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000'}, {'Id': '#006Wt000007B7tQIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000'}, {'Id': '#006Wt000007B7yJIAS', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000'}, {'Id': '006Wt000007B8CqIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000'}, {'Id': '#006Wt000007B8FyIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '#006Wt000007BA3JIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000'}, {'Id': '006Wt000007BABLIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000'}, {'Id': '006Wt000007BAHlIAO', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000'}, {'Id': '006Wt000007BAPrIAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000'}, {'Id': '006Wt000007BBDrIAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000'}, {'Id': '006Wt000007BBc1IAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000'}, {'Id': '006Wt000007BCLEIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000'}, {'Id': '006Wt000007BCTFIA4', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000'}, {'Id': '#006Wt000007BChmIAG', 'ContractID__c': '800Wt00000DE9FFIA1', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000'}, {'Id': '006Wt000007BDApIAO', 'ContractID__c': '800Wt00000DE8sgIAD', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000'}, {'Id': '#006Wt000007BDXPIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000'}, {'Id': '006Wt000007BDcEIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000'}, {'Id': '006Wt000007BDpAIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '006Wt000007BETVIA4', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000'}, {'Id': '#006Wt000007BEV4IAO', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000'}, {'Id': '006Wt000007BFUOIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000'}, {'Id': '006Wt000007BGAIIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000'}, {'Id': '#006Wt000007BGDVIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000'}, {'Id': '006Wt000007BHPhIAO', 'ContractID__c': '800Wt00000DE9ryIAD', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000'}, {'Id': '#006Wt000007BHZNIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000'}, {'Id': '#006Wt000007BHfpIAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000'}, {'Id': '006Wt000007BHr7IAG', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000'}], 'var_function-call-5576841316155544126': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
