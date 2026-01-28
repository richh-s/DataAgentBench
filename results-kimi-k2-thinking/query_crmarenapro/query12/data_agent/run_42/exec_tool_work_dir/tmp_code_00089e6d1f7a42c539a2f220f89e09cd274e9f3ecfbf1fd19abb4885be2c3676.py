code = """import json
import pandas as pd
from datetime import datetime

# Load the opportunity data
opportunity_data = [{"Id": "#006Wt000007B5jWIAS", "OwnerId": "005Wt000003NFB8IAO", "CreatedDate": "2022-11-01T10:45:36.000+0000", "CloseDate": "2023-04-28", "ContractID__c": "800Wt00000DE97BIAT"}, {"Id": "006Wt000007B7OmIAK", "OwnerId": "005Wt000003NBsIIAW", "CreatedDate": "2020-03-10T09:22:30.000+0000", "CloseDate": "2023-04-15", "ContractID__c": "None"}, {"Id": "006Wt000007B8RLIA0", "OwnerId": "005Wt000003NJgAIAW", "CreatedDate": "2022-11-15T10:32:45.000+0000", "CloseDate": "2023-04-10", "ContractID__c": "800Wt00000DE9aDIAT"}, {"Id": "006Wt000007BAfyIAG", "OwnerId": "005Wt000003NJjNIAW", "CreatedDate": "2022-11-02T11:23:48.000+0000", "CloseDate": "2023-04-15", "ContractID__c": "None"}, {"Id": "006Wt000007BAjHIAW", "OwnerId": "#005Wt000003NIfGIAW", "CreatedDate": "2022-01-15T09:45:30.000+0000", "CloseDate": "2023-04-11", "ContractID__c": "None"}, {"Id": "006Wt000007BBAcIAO", "OwnerId": "#005Wt000003NBp4IAG", "CreatedDate": "2022-09-01T10:15:00.000+0000", "CloseDate": "2023-04-15", "ContractID__c": "None"}, {"Id": "#006Wt000007BBH6IAO", "OwnerId": "005Wt000003NJg9IAG", "CreatedDate": "2022-09-14T14:32:54.000+0000", "CloseDate": "2023-04-17", "ContractID__c": "None"}, {"Id": "006Wt000007BDU9IAO", "OwnerId": "005Wt000003NJjNIAW", "CreatedDate": "2023-02-20T14:45:30.000+0000", "CloseDate": "2023-04-30", "ContractID__c": "800Wt00000DE0ryIAD"}, {"Id": "006Wt000007BDUAIA4", "OwnerId": "#005Wt000003NJmbIAG", "CreatedDate": "2022-11-09T10:30:25.000+0000", "CloseDate": "2023-04-20", "ContractID__c": "None"}, {"Id": "006Wt000007BHJGIA4", "OwnerId": "005Wt000003NIiTIAW", "CreatedDate": "2022-09-15T08:12:45.000+0000", "CloseDate": "2023-04-01", "ContractID__c": "None"}, {"Id": "006Wt000007BHvzIAG", "OwnerId": "005Wt000003NIljIAG", "CreatedDate": "2022-07-15T10:30:45.000+0000", "CloseDate": "2023-04-12", "ContractID__c": "None"}]

# Load the contract data
contract_data = [{"Id": "800Wt00000DE97BIAT", "CompanySignedDate": "2023-05-16"}, {"Id": "800Wt00000DE9aDIAT", "CompanySignedDate": "2023-02-28"}]

# Create dataframes
ops_df = pd.DataFrame(opportunity_data)
contracts_df = pd.DataFrame(contract_data)

# Clean and normalize IDs (remove leading # and trailing whitespace)
ops_df['Id'] = ops_df['Id'].str.replace('#', '', regex=False).str.strip()
ops_df['OwnerId'] = ops_df['OwnerId'].str.replace('#', '', regex=False).str.strip()
ops_df['ContractID__c'] = ops_df['ContractID__c'].str.replace('#', '', regex=False).str.strip()
contracts_df['Id'] = contracts_df['Id'].str.replace('#', '', regex=False).str.strip()

# Filter opportunities that have contracts (only these have a valid sales cycle per the policy)
ops_with_contracts = ops_df[ops_df['ContractID__c'] != 'None'].copy()

# Merge with contracts to get company signed dates
merged_df = ops_with_contracts.merge(
    contracts_df,
    left_on='ContractID__c',
    right_on='Id',
    how='inner',
    suffixes=('_opportunity', '_contract')
)

# Parse dates
merged_df['CreatedDate'] = pd.to_datetime(merged_df['CreatedDate'], format='ISO8601', errors='coerce')
merged_df['CompanySignedDate'] = pd.to_datetime(merged_df['CompanySignedDate'], errors='coerce')

# Calculate sales cycle in days
merged_df['SalesCycleDays'] = (merged_df['CompanySignedDate'] - merged_df['CreatedDate']).dt.days

# Filter for April 2023 opportunities that closed in April (based on CloseDate)
merged_df['CloseDate'] = pd.to_datetime(merged_df['CloseDate'], errors='coerce')
merged_df = merged_df[(merged_df['CloseDate'] >= '2023-04-01') & (merged_df['CloseDate'] < '2023-05-01')]

# Remove any rows where sales cycle calculation failed
merged_df = merged_df[merged_df['SalesCycleDays'].notna()]

# Group by agent and calculate average turnaround
agent_stats = merged_df.groupby('OwnerId').agg({
    'SalesCycleDays': ['mean', 'count']
}).round(2)

agent_stats.columns = ['AvgSalesCycle', 'OpportunityCount']
agent_stats = agent_stats.reset_index()

# Find the agent with the quickest average turnaround
if not agent_stats.empty:
    quickest_agent = agent_stats.loc[agent_stats['AvgSalesCycle'].idxmin()]
    result_id = str(quickest_agent['OwnerId'])
    
    # Print result in the required format
    print('__RESULT__:')
    print(result_id)
else:
    print('__RESULT__:')
    print('No data available')"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '#006Wt000007B5jWIAS', 'OwnerId': '005Wt000003NFB8IAO', 'CreatedDate': '2022-11-01T10:45:36.000+0000', 'CloseDate': '2023-04-28', 'ContractID__c': '800Wt00000DE97BIAT'}, {'Id': '006Wt000007B7OmIAK', 'OwnerId': '005Wt000003NBsIIAW', 'CreatedDate': '2020-03-10T09:22:30.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007B8RLIA0', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2022-11-15T10:32:45.000+0000', 'CloseDate': '2023-04-10', 'ContractID__c': '800Wt00000DE9aDIAT'}, {'Id': '006Wt000007BAfyIAG', 'OwnerId': '005Wt000003NJjNIAW', 'CreatedDate': '2022-11-02T11:23:48.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAjHIAW', 'OwnerId': '#005Wt000003NIfGIAW', 'CreatedDate': '2022-01-15T09:45:30.000+0000', 'CloseDate': '2023-04-11', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBAcIAO', 'OwnerId': '#005Wt000003NBp4IAG', 'CreatedDate': '2022-09-01T10:15:00.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BBH6IAO', 'OwnerId': '005Wt000003NJg9IAG', 'CreatedDate': '2022-09-14T14:32:54.000+0000', 'CloseDate': '2023-04-17', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDU9IAO', 'OwnerId': '005Wt000003NJjNIAW', 'CreatedDate': '2023-02-20T14:45:30.000+0000', 'CloseDate': '2023-04-30', 'ContractID__c': '800Wt00000DE0ryIAD'}, {'Id': '006Wt000007BDUAIA4', 'OwnerId': '#005Wt000003NJmbIAG', 'CreatedDate': '2022-11-09T10:30:25.000+0000', 'CloseDate': '2023-04-20', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHJGIA4', 'OwnerId': '005Wt000003NIiTIAW', 'CreatedDate': '2022-09-15T08:12:45.000+0000', 'CloseDate': '2023-04-01', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHvzIAG', 'OwnerId': '005Wt000003NIljIAG', 'CreatedDate': '2022-07-15T10:30:45.000+0000', 'CloseDate': '2023-04-12', 'ContractID__c': 'None'}], 'var_functions.query_db:5': [{'Id': '800Wt00000DE97BIAT', 'CompanySignedDate': '2023-05-16'}, {'Id': '800Wt00000DE9aDIAT', 'CompanySignedDate': '2023-02-28'}]}

exec(code, env_args)
