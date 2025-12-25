code = """import pandas as pd

opportunities = locals()['var_function-call-7798883519137761724']
df_opportunities = pd.DataFrame(opportunities)
df_opportunities_cleaned = df_opportunities.copy()

df_opportunities_cleaned['Id'] = df_opportunities_cleaned['Id'].str.replace('#', '').str.strip()
df_opportunities_cleaned['OwnerId'] = df_opportunities_cleaned['OwnerId'].str.replace('#', '').str.strip()
df_opportunities_cleaned['ContractID__c'] = df_opportunities_cleaned['ContractID__c'].str.replace('#', '').str.strip()

contracts = locals()['var_function-call-11690341089797404084']
df_contracts = pd.DataFrame(contracts)
df_contracts_cleaned = df_contracts.copy()
df_contracts_cleaned['Id'] = df_contracts_cleaned['Id'].str.replace('#', '').str.strip()


merged_df = pd.merge(
    df_opportunities_cleaned,
    df_contracts_cleaned,
    left_on='ContractID__c',
    right_on='Id',
    suffixes=('_opportunity', '_contract')
)

merged_df['CreatedDate'] = pd.to_datetime(merged_df['CreatedDate'])
merged_df['CompanySignedDate'] = pd.to_datetime(merged_df['CompanySignedDate'])

merged_df['TurnaroundTime'] = (merged_df['CompanySignedDate'] - merged_df['CreatedDate']).dt.days

average_turnaround_by_agent = merged_df.groupby('OwnerId')['TurnaroundTime'].mean().reset_index()

quickest_agent = average_turnaround_by_agent.loc[average_turnaround_by_agent['TurnaroundTime'].idxmin()]

print("__RESULT__:")
print(quickest_agent['OwnerId'])"""

env_args = {'var_function-call-7798883519137761724': [{'Id': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD'}, {'Id': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD'}, {'Id': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'ContractID__c': 'None'}], 'var_function-call-7248244891082751828': {'0': 'None', '1': 'None', '2': 'None', '3': 'None', '4': 'None', '5': 'None', '6': 'None', '7': 'None', '8': 'None', '9': 'None', '10': 'None', '11': 'None', '12': 'None', '13': 'None', '14': 'None', '15': 'None', '16': '800Wt00000DE9FFIA1', '17': '800Wt00000DE8sgIAD', '18': 'None', '19': 'None', '20': 'None', '21': 'None', '22': 'None', '23': 'None', '24': 'None', '25': 'None', '26': '800Wt00000DE9ryIAD', '27': 'None', '28': 'None', '29': 'None'}, 'var_function-call-8786268986537908891': {'0': '800Wt00000DE9FFIA1', '1': '800Wt00000DE8sgIAD', '2': '800Wt00000DE9ryIAD'}, 'var_function-call-11690341089797404084': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}], 'var_function-call-5122686581470028590': {'0': '800Wt00000DE9FFIA1', '1': '800Wt00000DE8sgIAD', '2': '800Wt00000DE9ryIAD'}}

exec(code, env_args)
