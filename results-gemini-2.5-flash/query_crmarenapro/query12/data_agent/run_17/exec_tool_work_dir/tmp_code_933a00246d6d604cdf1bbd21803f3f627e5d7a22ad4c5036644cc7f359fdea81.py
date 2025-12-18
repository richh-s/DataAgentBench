code = """import pandas as pd
import json

opportunities = pd.DataFrame(locals()['var_function-call-6215996879606262250'])
contracts = pd.DataFrame(locals()['var_function-call-13473625528513089074'])

# Convert date columns to datetime objects
opportunities['CreatedDate'] = pd.to_datetime(opportunities['CreatedDate'])
contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'])

# Merge the two dataframes on ContractId
merged_df = pd.merge(opportunities, contracts, left_on='ContractId', right_on='ContractId', how='inner')

# Calculate turnaround time in days
merged_df['TurnaroundTime'] = (merged_df['CompanySignedDate'] - merged_df['CreatedDate']).dt.days

# Calculate average turnaround time for each agent
average_turnaround = merged_df.groupby('OwnerId')['TurnaroundTime'].mean().reset_index()

# Find the agent with the quickest average turnaround
quickest_agent = average_turnaround.loc[average_turnaround['TurnaroundTime'].idxmin()]

print("__RESULT__:")
print(json.dumps(quickest_agent['OwnerId']))"""

env_args = {'var_function-call-6215996879606262250': [{'OpportunityId': '006Wt000007B1klIAC', 'OwnerId': '005Wt000003NBylIAG', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007B6itIAC', 'OwnerId': '005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007B7yJIAS', 'OwnerId': '005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BAHlIAO', 'OwnerId': '005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BCTFIA4', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25 00:00:00', 'ContractId': '800Wt00000DE9FFIA1'}, {'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10 00:00:00', 'ContractId': '800Wt00000DE8sgIAD'}, {'OpportunityId': '006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BETVIA4', 'OwnerId': '005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15 00:00:00', 'ContractId': '800Wt00000DE9ryIAD'}, {'OpportunityId': '006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17 00:00:00', 'ContractId': 'None'}, {'OpportunityId': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01 00:00:00', 'ContractId': 'None'}], 'var_function-call-13473625528513089074': [{'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13 00:00:00'}, {'ContractId': '800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13 00:00:00'}, {'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30 00:00:00'}]}

exec(code, env_args)
