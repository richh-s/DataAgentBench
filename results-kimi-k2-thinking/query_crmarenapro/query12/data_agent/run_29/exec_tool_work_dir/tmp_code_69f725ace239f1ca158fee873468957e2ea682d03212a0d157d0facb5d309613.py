code = """import json
import pandas as pd

# Read the query result
data = locals()['var_functions.query_db:16']

if data:
    df = pd.DataFrame(data)
    
    # Clean up OwnerId by removing leading # if present
    df['OwnerId_Clean'] = df['OwnerId'].str.lstrip('#')
    
    # Convert dates to datetime objects, handling timezone info
    df['CreatedDate_DT'] = pd.to_datetime(df['CreatedDate']).dt.tz_localize(None)  # Remove timezone
    df['SignedDate_DT'] = pd.to_datetime(df['CompanySignedDate']).dt.tz_localize(None)  # Already no timezone
    
    # Calculate turnaround days
    df['TurnaroundDays'] = (df['SignedDate_DT'] - df['CreatedDate_DT']).dt.days
    
    # Group by OwnerId and calculate average turnaround
    avg_turnaround = df.groupby('OwnerId_Clean')['TurnaroundDays'].mean().sort_values()
    
    print('__RESULT__:')
    print(json.dumps({'top_agent': avg_turnaround.index[0]}))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No data found'}))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-09-05T11:32:46.000+0000'}, {'Id': '006Wt000007Aw3WIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIc1IAG', 'CreatedDate': '2024-04-05T12:15:30.000+0000'}, {'Id': '006Wt000007Aw3XIAS', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJZhIAO', 'CreatedDate': '2021-02-10T14:23:45.000+0000'}, {'Id': '006Wt000007Aya9IAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDJ0IAO', 'CreatedDate': '2023-08-11T09:30:00.000+0000'}, {'Id': '006Wt000007AyaAIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2022-07-20T14:13:45.000+0000'}, {'Id': '006Wt000007AyaBIAS', 'ContractID__c': '800Wt00000DE9DdIAL', 'OwnerId': '005Wt000003NErnIAG', 'CreatedDate': '2023-08-14T10:30:00.000+0000'}, {'Id': '#006Wt000007AyaCIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NEdJIAW', 'CreatedDate': '2020-12-18T14:35:47.000+0000'}, {'Id': '#006Wt000007AyaDIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIybIAG', 'CreatedDate': '2021-05-13T10:30:45.000+0000'}, {'Id': '006Wt000007Ayi2IAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2021-03-02T10:45:30.000+0000'}, {'Id': '006Wt000007AywiIAC', 'ContractID__c': '800Wt00000DE45uIAD', 'OwnerId': '005Wt000003NBsIIAW', 'CreatedDate': '2021-11-05T10:15:30.000+0000'}], 'var_functions.query_db:6': [{'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:8': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:10': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:14': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractId': '#800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:16': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.list_db:18': ['User', 'Account', 'Contact']}

exec(code, env_args)
