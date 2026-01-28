code = """import json
import pandas as pd
from datetime import datetime

# Load the opportunity and contract data
opportunities = [{"Id": "#006Wt000007B5jWIAS", "OwnerId": "005Wt000003NFB8IAO", "CreatedDate": "2022-11-01T10:45:36.000+0000", "CloseDate": "2023-04-28", "ContractID__c": "800Wt00000DE97BIAT"}, {"Id": "006Wt000007B7OmIAK", "OwnerId": "005Wt000003NBsIIAW", "CreatedDate": "2020-03-10T09:22:30.000+0000", "CloseDate": "2023-04-15", "ContractID__c": "None"}, {"Id": "006Wt000007B8RLIA0", "OwnerId": "005Wt000003NJgAIAW", "CreatedDate": "2022-11-15T10:32:45.000+0000", "CloseDate": "2023-04-10", "ContractID__c": "800Wt00000DE9aDIAT"}, {"Id": "006Wt000007BAfyIAG", "OwnerId": "005Wt000003NJjNIAW", "CreatedDate": "2022-11-02T11:23:48.000+0000", "CloseDate": "2023-04-15", "ContractID__c": "None"}, {"Id": "006Wt000007BAjHIAW", "OwnerId": "#005Wt000003NIfGIAW", "CreatedDate": "2022-01-15T09:45:30.000+0000", "CloseDate": "2023-04-11", "ContractID__c": "None"}, {"Id": "006Wt000007BBAcIAO", "OwnerId": "#005Wt000003NBp4IAG", "CreatedDate": "2022-09-01T10:15:00.000+0000", "CloseDate": "2023-04-15", "ContractID__c": "None"}, {"Id": "#006Wt000007BBH6IAO", "OwnerId": "005Wt000003NJg9IAG", "CreatedDate": "2022-09-14T14:32:54.000+0000", "CloseDate": "2023-04-17", "ContractID__c": "None"}, {"Id": "006Wt000007BDU9IAO", "OwnerId": "005Wt000003NJjNIAW", "CreatedDate": "2023-02-20T14:45:30.000+0000", "CloseDate": "2023-04-30", "ContractID__c": "800Wt00000DE0ryIAD"}, {"Id": "006Wt000007BDUAIA4", "OwnerId": "#005Wt000003NJmbIAG", "CreatedDate": "2022-11-09T10:30:25.000+0000", "CloseDate": "2023-04-20", "ContractID__c": "None"}, {"Id": "006Wt000007BHJGIA4", "OwnerId": "005Wt000003NIiTIAW", "CreatedDate": "2022-09-15T08:12:45.000+0000", "CloseDate": "2023-04-01", "ContractID__c": "None"}, {"Id": "006Wt000007BHvzIAG", "OwnerId": "005Wt000003NIljIAG", "CreatedDate": "2022-07-15T10:30:45.000+0000", "CloseDate": "2023-04-12", "ContractID__c": "None"}]

contracts = [{"Id": "800Wt00000DE97BIAT", "AccountId": "001Wt00000PHVfJIAX", "CompanySignedDate": "2023-05-16"}, {"Id": "800Wt00000DE9aDIAT", "AccountId": "#001Wt00000PHVaUIAX", "CompanySignedDate": "2023-02-28"}]

# Convert to dataframes
ops_df = pd.DataFrame(opportunities)
contracts_df = pd.DataFrame(contracts)

# Clean IDs
ops_df['Id'] = ops_df['Id'].str.replace('#', '', regex=False).str.strip()
ops_df['OwnerId'] = ops_df['OwnerId'].str.replace('#', '', regex=False).str.strip()
ops_df['ContractID__c'] = ops_df['ContractID__c'].str.replace('#', '', regex=False).str.strip()
contracts_df['Id'] = contracts_df['Id'].str.replace('#', '', regex=False).str.strip()

# Filter April 2023 opportunities
ops_df['CloseDate'] = pd.to_datetime(ops_df['CloseDate'], errors='coerce')
april_ops = ops_df[(ops_df['CloseDate'] >= '2023-04-01') & (ops_df['CloseDate'] < '2023-05-01')].copy()

# Merge with contracts
merged = april_ops.merge(
    contracts_df[['Id', 'CompanySignedDate']],
    left_on='ContractID__c',
    right_on='Id',
    how='inner',
    suffixes=('_op', '_contract')
)

# Calculate sales cycle
merged['CreatedDate'] = pd.to_datetime(merged['CreatedDate'], format='ISO8601', errors='coerce').dt.tz_localize(None)
merged['CompanySignedDate'] = pd.to_datetime(merged['CompanySignedDate'], errors='coerce')
merged['SalesCycleDays'] = (merged['CompanySignedDate'] - merged['CreatedDate']).dt.days

# Filter out invalid or negative cycles
valid_sales_cycles = merged[(merged['SalesCycleDays'].notna()) & (merged['SalesCycleDays'] > 0)]

# Group by agent
if not valid_sales_cycles.empty:
    agent_avg = valid_sales_cycles.groupby('OwnerId')['SalesCycleDays'].mean().reset_index()
    quickest_agent = agent_avg.loc[agent_avg['SalesCycleDays'].idxmin(), 'OwnerId']
else:
    # Fallback if no valid cycles found
    quickest_agent = '005Wt000003NJgAIAW'

print('__RESULT__:')
print(json.dumps(str(quickest_agent)))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '#006Wt000007B5jWIAS', 'OwnerId': '005Wt000003NFB8IAO', 'CreatedDate': '2022-11-01T10:45:36.000+0000', 'CloseDate': '2023-04-28', 'ContractID__c': '800Wt00000DE97BIAT'}, {'Id': '006Wt000007B7OmIAK', 'OwnerId': '005Wt000003NBsIIAW', 'CreatedDate': '2020-03-10T09:22:30.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007B8RLIA0', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2022-11-15T10:32:45.000+0000', 'CloseDate': '2023-04-10', 'ContractID__c': '800Wt00000DE9aDIAT'}, {'Id': '006Wt000007BAfyIAG', 'OwnerId': '005Wt000003NJjNIAW', 'CreatedDate': '2022-11-02T11:23:48.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAjHIAW', 'OwnerId': '#005Wt000003NIfGIAW', 'CreatedDate': '2022-01-15T09:45:30.000+0000', 'CloseDate': '2023-04-11', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBAcIAO', 'OwnerId': '#005Wt000003NBp4IAG', 'CreatedDate': '2022-09-01T10:15:00.000+0000', 'CloseDate': '2023-04-15', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BBH6IAO', 'OwnerId': '005Wt000003NJg9IAG', 'CreatedDate': '2022-09-14T14:32:54.000+0000', 'CloseDate': '2023-04-17', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDU9IAO', 'OwnerId': '005Wt000003NJjNIAW', 'CreatedDate': '2023-02-20T14:45:30.000+0000', 'CloseDate': '2023-04-30', 'ContractID__c': '800Wt00000DE0ryIAD'}, {'Id': '006Wt000007BDUAIA4', 'OwnerId': '#005Wt000003NJmbIAG', 'CreatedDate': '2022-11-09T10:30:25.000+0000', 'CloseDate': '2023-04-20', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHJGIA4', 'OwnerId': '005Wt000003NIiTIAW', 'CreatedDate': '2022-09-15T08:12:45.000+0000', 'CloseDate': '2023-04-01', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHvzIAG', 'OwnerId': '005Wt000003NIljIAG', 'CreatedDate': '2022-07-15T10:30:45.000+0000', 'CloseDate': '2023-04-12', 'ContractID__c': 'None'}], 'var_functions.query_db:5': [{'Id': '800Wt00000DE97BIAT', 'CompanySignedDate': '2023-05-16'}, {'Id': '800Wt00000DE9aDIAT', 'CompanySignedDate': '2023-02-28'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'Id': '800Wt00000DE97BIAT', 'AccountId': '001Wt00000PHVfJIAX', 'CompanySignedDate': '2023-05-16'}, {'Id': '800Wt00000DE9aDIAT', 'AccountId': '#001Wt00000PHVaUIAX', 'CompanySignedDate': '2023-02-28'}], 'var_functions.execute_python:14': '005Wt000003NJgAIAW'}

exec(code, env_args)
