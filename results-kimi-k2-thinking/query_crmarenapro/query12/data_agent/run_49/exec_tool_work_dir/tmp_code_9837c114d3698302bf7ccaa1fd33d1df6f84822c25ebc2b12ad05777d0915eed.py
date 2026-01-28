code = """import json
import datetime

# Retrieve the stored results
results = locals()['var_functions.query_db:2']

# Parse the data and calculate turnaround days
for record in results:
    # Parse dates
    created_date = datetime.datetime.fromisoformat(record['CreatedDate'].replace('Z', '+00:00'))
    company_signed_date = datetime.datetime.fromisoformat(record['CompanySignedDate'] + 'T00:00:00+00:00')
    
    # Calculate turnaround days
    turnaround_days = (company_signed_date - created_date).days
    record['turnaround_days'] = turnaround_days

# Group by OwnerId and calculate average turnaround
from collections import defaultdict

agent_turnarounds = defaultdict(list)
for record in results:
    owner_id = record['OwnerId']
    # Clean up potential corruption (leading #)
    if owner_id.startswith('#'):
        owner_id = owner_id[1:]
    agent_turnarounds[owner_id].append(record['turnaround_days'])

# Calculate averages
agent_averages = {}
for owner_id, days_list in agent_turnarounds.items():
    agent_averages[owner_id] = sum(days_list) / len(days_list)

# Find agent with minimum average turnaround
min_avg_agent = min(agent_averages, key=agent_averages.get)

print('__RESULT__:')
print(json.dumps(min_avg_agent))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13', 'OpportunityId': '006Wt000007BDApIAO', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'OwnerId': '005Wt000003NISMIA4'}, {'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30', 'OpportunityId': '006Wt000007BHPhIAO', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'OwnerId': '#005Wt000003NEa3IAG'}]}

exec(code, env_args)
