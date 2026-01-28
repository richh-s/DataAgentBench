code = """import json
from datetime import datetime

data_key = 'var_functions.query_db:14'
if data_key in locals():
    sales_data = locals()[data_key]
else:
    sales_data = []

# Calculate turnaround days for each opportunity
opportunities_with_turnaround = []

for opp in sales_data:
    created_date = datetime.strptime(opp['CreatedDate'][:10], '%Y-%m-%d')
    signed_date = datetime.strptime(opp['CompanySignedDate'], '%Y-%m-%d')
    turnaround_days = (signed_date - created_date).days
    
    opportunities_with_turnaround.append({
        'OwnerId': opp['OwnerId'],
        'turnaround_days': turnaround_days
    })

# Calculate average turnaround per owner
owner_stats = {}
if opportunities_with_turnaround:
    for opp in opportunities_with_turnaround:
        owner_id = opp['OwnerId']
        if owner_id not in owner_stats:
            owner_stats[owner_id] = []
        owner_stats[owner_id].append(opp['turnaround_days'])

    # Calculate average turnaround for each owner
    average_turnarounds = {}
    for owner_id, days_list in owner_stats.items():
        average_turnarounds[owner_id] = sum(days_list) / len(days_list)

    # Sort by average turnaround (ascending) to find the quickest
    sorted_owners = sorted(average_turnarounds.items(), key=lambda x: x[1])

    # Get the agent with the quickest turnaround
    quickest_agent_id = sorted_owners[0][0]
else:
    quickest_agent_id = "No data found"

print('__RESULT__:')
print(quickest_agent_id)"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '006Wt000007AvVeIAK', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007Aw3WIAS', 'OwnerId': '005Wt000003NIc1IAG', 'CreatedDate': '2024-04-05T12:15:30.000+0000', 'CloseDate': '2024-06-15', 'ContractID__c': 'None'}, {'Id': '006Wt000007Aw3XIAS', 'OwnerId': '#005Wt000003NJZhIAO', 'CreatedDate': '2021-02-10T14:23:45.000+0000', 'CloseDate': '2021-05-30', 'ContractID__c': 'None'}, {'Id': '006Wt000007Aya9IAC', 'OwnerId': '005Wt000003NDJ0IAO', 'CreatedDate': '2023-08-11T09:30:00.000+0000', 'CloseDate': '2023-11-30', 'ContractID__c': 'None'}, {'Id': '006Wt000007AyaAIAS', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2022-07-20T14:13:45.000+0000', 'CloseDate': '2023-11-15', 'ContractID__c': 'None'}], 'var_functions.query_db:5': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'CustomerSignedDate': '2024-04-15', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'CustomerSignedDate': '2023-07-01', 'CompanySignedDate': '2023-07-02'}], 'var_functions.query_db:6': [{'OwnerId': '005Wt000003NJgAIAW', 'OpportunityId': '#006Wt000007BChmIAG', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13', 'ContractId': '#800Wt00000DE9FFIA1'}, {'OwnerId': '005Wt000003NISMIA4', 'OpportunityId': '006Wt000007BDApIAO', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13', 'ContractId': '800Wt00000DE8sgIAD'}, {'OwnerId': '#005Wt000003NEa3IAG', 'OpportunityId': '006Wt000007BHPhIAO', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30', 'ContractId': '800Wt00000DE9ryIAD'}], 'var_functions.query_db:8': [{'OwnerId': '005Wt000003NJgAIAW', 'OpportunityId': '#006Wt000007BChmIAG', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'OpportunityId': '006Wt000007BDApIAO', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'OpportunityId': '006Wt000007BHPhIAO', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:14': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'CompanySignedDate': '2023-06-13'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
