code = """import pandas as pd
import json
from datetime import datetime

opportunities_data = locals()['var_function-call-16702356047967633912']
contracts_data = locals()['var_function-call-8919695549515934865']

df_opportunities = pd.DataFrame(opportunities_data)
df_contracts = pd.DataFrame(contracts_data)

# Clean IDs by removing "#" and stripping whitespace
df_opportunities["Id"] = df_opportunities["Id"].str.replace("#", "").str.strip()
df_opportunities["OwnerId"] = df_opportunities["OwnerId"].str.replace("#", "").str.strip()
df_opportunities["ContractID__c"] = df_opportunities["ContractID__c"].astype(str).str.replace("#", "").str.strip()
df_contracts["Id"] = df_contracts["Id"].str.replace("#", "").str.strip()

# Filter opportunities with valid ContractID__c
df_opportunities_filtered = df_opportunities[df_opportunities["ContractID__c"].notna() & (df_opportunities["ContractID__c"] != 'None')]

# Merge opportunities with contracts
merged_df = pd.merge(df_opportunities_filtered, df_contracts, left_on="ContractID__c", right_on="Id", suffixes=("_opportunity", "_contract"))

# Convert date columns to datetime objects
merged_df["CreatedDate"] = pd.to_datetime(merged_df["CreatedDate"].str.split("T").str[0])
merged_df["CompanySignedDate"] = pd.to_datetime(merged_df["CompanySignedDate"])

# Calculate turnaround time in days
merged_df["TurnaroundTime"] = (merged_df["CompanySignedDate"] - merged_df["CreatedDate"]).dt.days

# Calculate average turnaround time per agent
avg_turnaround_time = merged_df.groupby("OwnerId")["TurnaroundTime"].mean().reset_index()

# Find the agent with the quickest average turnaround time
quickest_agent = avg_turnaround_time.loc[avg_turnaround_time["TurnaroundTime"].idxmin()]

# Get the Id of the agent
agent_id = quickest_agent["OwnerId"]

print("__RESULT__:")
print(json.dumps(agent_id.strip()))"""

env_args = {'var_function-call-16702356047967633912': [{'Id': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T09:00:34.000+0000'}, {'Id': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-25T14:32:51.000+0000'}, {'Id': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-04T10:15:30.000+0000'}, {'Id': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-25T09:45:30.000+0000'}, {'Id': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:20:30.000+0000'}, {'Id': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:45.000+0000'}, {'Id': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T09:30:45.000+0000'}, {'Id': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-02T10:15:30.000+0000'}, {'Id': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-01T14:47:23.000+0000'}, {'Id': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-19T15:30:45.000+0000'}, {'Id': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:15:32.000+0000'}, {'Id': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T10:30:15.000+0000'}, {'Id': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:14:32.000+0000'}, {'Id': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-27T11:22:30.000+0000'}, {'Id': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-20T11:15:33.000+0000'}, {'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'ContractID__c': '800Wt00000DE9FFIA1', 'CreatedDate': '2023-04-25T10:45:30.000+0000'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'ContractID__c': '800Wt00000DE8sgIAD', 'CreatedDate': '2023-04-10T10:15:30.000+0000'}, {'Id': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:45:00.000+0000'}, {'Id': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:32:45.000+0000'}, {'Id': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-20T11:34:22.000+0000'}, {'Id': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'ContractID__c': 'None', 'CreatedDate': '2023-04-05T14:23:45.000+0000'}, {'Id': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-05T10:15:30.000+0000'}, {'Id': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'ContractID__c': 'None', 'CreatedDate': '2023-04-11T12:45:33.000+0000'}, {'Id': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T11:20:45.000+0000'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'ContractID__c': '800Wt00000DE9ryIAD', 'CreatedDate': '2023-04-15T09:12:34.000+0000'}, {'Id': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-10T14:25:30.000+0000'}, {'Id': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-17T14:37:45.000+0000'}, {'Id': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'ContractID__c': 'None', 'CreatedDate': '2023-04-01T09:45:23.000+0000'}], 'var_function-call-8919695549515934865': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
