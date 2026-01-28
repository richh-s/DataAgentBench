code = """import json
import re
from datetime import datetime

# Get the query results
opportunities = locals()['var_functions.query_db:2']

# Clean and process the data
valid_opportunities = []

for opp in opportunities:
    # Skip records with None/Null contract data
    if opp['ContractID__c'] == 'None' or opp['CompanySignedDate'] == 'None':
        continue
    
    # Clean OwnerId (remove leading # if present)
    owner_id = opp['OwnerId']
    if owner_id.startswith('#'):
        owner_id = owner_id[1:]
    
    # Parse dates
    try:
        created_date = datetime.fromisoformat(opp['CreatedDate'].replace('Z', '+00:00'))
        # CompanySignedDate appears to be in YYYY-MM-DD format
        signed_date = datetime.strptime(opp['CompanySignedDate'], '%Y-%m-%d')
        signed_date = signed_date.replace(tzinfo=created_date.tzinfo)  # Add timezone info
        
        # Calculate turnaround days
        turnaround_days = (signed_date - created_date).days
        
        valid_opportunities.append({
            'OpportunityId': opp['OpportunityId'],
            'OwnerId': owner_id,
            'CreatedDate': opp['CreatedDate'],
            'CompanySignedDate': opp['CompanySignedDate'],
            'TurnaroundDays': turnaround_days
        })
    except Exception as e:
        continue

# Group by OwnerId and calculate average turnaround
from collections import defaultdict

owner_stats = defaultdict(list)
for opp in valid_opportunities:
    owner_stats[opp['OwnerId']].append(opp['TurnaroundDays'])

# Calculate average turnaround for each owner
owner_averages = {}
for owner_id, turnarounds in owner_stats.items():
    avg_turnaround = sum(turnarounds) / len(turnarounds)
    owner_averages[owner_id] = {
        'average_turnaround': avg_turnarounds,
        'opportunity_count': len(turnarounds)
    }

# Find owner with quickest average turnaround
if owner_averages:
    quickest_owner = min(owner_averages.keys(), key=lambda x: owner_averages[x]['average_turnaround'])
    result = quickest_owner
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}, {'OpportunityId': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}, {'OpportunityId': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'ContractID__c': 'None', 'CompanySignedDate': 'None'}]}

exec(code, env_args)
