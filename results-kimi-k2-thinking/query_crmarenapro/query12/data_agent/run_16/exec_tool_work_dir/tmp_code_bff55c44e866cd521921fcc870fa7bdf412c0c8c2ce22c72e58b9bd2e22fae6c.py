code = """import json
from datetime import datetime

# Get opportunities and contracts
topps = locals()['var_functions.query_db:26']
contracts = locals()['var_functions.query_db:24']

# Parse dates
for opp in topps:
    opp['CreatedDate'] = opp['CreatedDate'][:10]

# Create contract lookup
cont_lookup = {c['Id']: c['CompanySignedDate'] for c in contracts}

# Join and calculate days
agent_turnarounds = {}

for opp in topps:
    contract_id = opp['ContractID__c']
    if contract_id in cont_lookup:
        created = datetime.strptime(opp['CreatedDate'], '%Y-%m-%d')
        company_signed = datetime.strptime(cont_lookup[contract_id], '%Y-%m-%d')
        days = (company_signed - created).days
        
        # Normalize owner ID (strip # and whitespace)
        owner_id = opp['OwnerId'].replace('#', '').strip()
        
        if owner_id not in agent_turnarounds:
            agent_turnarounds[owner_id] = []
        agent_turnarounds[owner_id].append(days)

# Calculate averages
agent_averages = {}
for owner, times in agent_turnarounds.items():
    agent_averages[owner] = sum(times) / len(times)

print('__RESULT__:')
print(json.dumps({
    'agent_averages': agent_averages,
    'agent_turnarounds': agent_turnarounds
}))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '#006Wt000007B1klIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000'}, {'Id': '006Wt000007B49NIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000'}, {'Id': '006Wt000007B62sIAC', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000'}, {'Id': '006Wt000007B6itIAC', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000'}, {'Id': '#006Wt000007B7tQIAS', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000'}, {'Id': '#006Wt000007B7yJIAS', 'ContractID__c': 'None', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000'}, {'Id': '006Wt000007B8CqIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000'}, {'Id': '#006Wt000007B8FyIAK', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000'}, {'Id': '#006Wt000007BA3JIAW', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000'}, {'Id': '006Wt000007BABLIA4', 'ContractID__c': 'None', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000'}], 'var_functions.query_db:5': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16'}, {'Id': '800Wt00000DD0SaIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CustomerSignedDate': '2021-09-28', 'CompanySignedDate': '2021-09-28'}, {'Id': '#800Wt00000DD0SbIAL', 'AccountId': '001Wt00000PGXrLIAX', 'CustomerSignedDate': '2023-07-11', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDDuRIAX', 'AccountId': '001Wt00000PGYgxIAH', 'CustomerSignedDate': '2024-04-15', 'CompanySignedDate': '2024-04-16'}, {'Id': '800Wt00000DDNFUIA5', 'AccountId': '#001Wt00000PGeJIIA1', 'CustomerSignedDate': '2023-07-01', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDNFVIA5', 'AccountId': '#001Wt00000PGoAaIAL', 'CustomerSignedDate': '2021-06-25', 'CompanySignedDate': '2021-06-26'}, {'Id': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CustomerSignedDate': '2022-09-01', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDPXRIA5', 'AccountId': '001Wt00000PHRTeIAP', 'CustomerSignedDate': '2022-04-20', 'CompanySignedDate': '2022-04-22'}, {'Id': '800Wt00000DDPXSIA5', 'AccountId': '001Wt00000PGeJIIA1', 'CustomerSignedDate': '2023-02-20', 'CompanySignedDate': '2023-02-25'}, {'Id': '800Wt00000DDPXTIA5', 'AccountId': '001Wt00000PHVnNIAX', 'CustomerSignedDate': '2023-10-12', 'CompanySignedDate': '2023-10-13'}], 'var_functions.query_db:6': [{'ContractID__c': '800Wt00000DE8sgIAD'}, {'ContractID__c': '800Wt00000DE9ryIAD'}, {'ContractID__c': '800Wt00000DE9FFIA1'}], 'var_functions.query_db:12': [{'OwnerId': '005Wt000003NISMIA4', 'ContractID__c': '800Wt00000DE8sgIAD', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'ContractID__c': '800Wt00000DE9ryIAD', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:14': [{'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:16': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD'}], 'var_functions.execute_python:18': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD'}], 'var_functions.query_db:20': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'Id': '#800Wt00000DD0SbIAL', 'CompanySignedDate': '2023-07-12'}, {'Id': '800Wt00000DDNFUIA5', 'CompanySignedDate': '2023-07-02'}, {'Id': '800Wt00000DDPXTIA5', 'CompanySignedDate': '2023-10-13'}, {'Id': '#800Wt00000DDeUqIAL', 'CompanySignedDate': '2023-09-25'}, {'Id': '#800Wt00000DDfKSIA1', 'CompanySignedDate': '2023-08-24'}, {'Id': '#800Wt00000DDfKTIA1', 'CompanySignedDate': '2023-06-21'}, {'Id': '800Wt00000DDg3bIAD', 'CompanySignedDate': '2023-07-25'}, {'Id': '800Wt00000DDt5fIAD', 'CompanySignedDate': '2023-08-23'}, {'Id': '800Wt00000DDt8uIAD', 'CompanySignedDate': '2023-12-20'}, {'Id': '800Wt00000DDtNUIA1', 'CompanySignedDate': '2023-05-30'}, {'Id': '800Wt00000DDxHMIA1', 'CompanySignedDate': '2023-09-13'}, {'Id': '800Wt00000DDxZ5IAL', 'CompanySignedDate': '2023-06-22'}, {'Id': '800Wt00000DDyKWIA1', 'CompanySignedDate': '2023-10-06'}, {'Id': '800Wt00000DDyuzIAD', 'CompanySignedDate': '2023-10-18'}, {'Id': '800Wt00000DE0n7IAD', 'CompanySignedDate': '2023-10-31'}, {'Id': '#800Wt00000DE0ryIAD', 'CompanySignedDate': '2023-05-12'}, {'Id': '#800Wt00000DE0s0IAD', 'CompanySignedDate': '2023-12-06'}, {'Id': '800Wt00000DE1JKIA1', 'CompanySignedDate': '2023-10-06'}, {'Id': '800Wt00000DE3kwIAD', 'CompanySignedDate': '2023-11-11'}, {'Id': '800Wt00000DE4NgIAL', 'CompanySignedDate': '2023-11-26'}, {'Id': '800Wt00000DE4YwIAL', 'CompanySignedDate': '2023-11-27'}, {'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE90kIAD', 'CompanySignedDate': '2023-10-15'}, {'Id': '800Wt00000DE97BIAT', 'CompanySignedDate': '2023-05-16'}, {'Id': '800Wt00000DE97DIAT', 'CompanySignedDate': '2023-09-15'}, {'Id': '800Wt00000DE9C2IAL', 'CompanySignedDate': '2023-07-19'}, {'Id': '800Wt00000DE9DdIAL', 'CompanySignedDate': '2023-11-23'}, {'Id': '#800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13'}, {'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15'}, {'Id': '800Wt00000DE9OvIAL', 'CompanySignedDate': '2023-08-29'}, {'Id': '800Wt00000DE9QXIA1', 'CompanySignedDate': '2023-08-23'}, {'Id': '800Wt00000DE9S9IAL', 'CompanySignedDate': '2023-10-16'}, {'Id': '800Wt00000DE9VNIA1', 'CompanySignedDate': '2023-06-21'}, {'Id': '800Wt00000DE9bpIAD', 'CompanySignedDate': '2023-08-29'}, {'Id': '#800Wt00000DE9dSIAT', 'CompanySignedDate': '2023-10-20'}, {'Id': '#800Wt00000DE9jtIAD', 'CompanySignedDate': '2023-12-21'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:26': [{'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1'}, {'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD'}, {'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD'}]}

exec(code, env_args)
