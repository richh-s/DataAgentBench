code = """import json
from datetime import datetime

# Get the data from the previous query
results = var_functions.query_db:5

# Process each opportunity
agent_turnarounds = {}

for opp in results:
    # Clean the OwnerId (remove leading # if present)
    owner_id = opp['OwnerId']
    if owner_id.startswith('#'):
        owner_id = owner_id[1:]
    
    # Parse dates
    created_date = datetime.fromisoformat(opp['CreatedDate'].replace('Z', '+00:00'))
    signed_date = datetime.strptime(opp['CompanySignedDate'], '%Y-%m-%d')
    
    # Calculate days between created and signed
    turnaround_days = (signed_date - created_date).days
    
    # Add to agent's list
    if owner_id not in agent_turnarounds:
        agent_turnarounds[owner_id] = []
    agent_turnarounds[owner_id].append(turnaround_days)

# Calculate average turnaround for each agent
agent_averages = {}
for agent_id, turnarounds in agent_turnarounds.items():
    agent_averages[agent_id] = sum(turnarounds) / len(turnarounds)

# Find agent with minimum average turnaround
quickest_agent = min(agent_averages, key=agent_averages.get)

print('__RESULT__:')
print(json.dumps(quickest_agent))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
