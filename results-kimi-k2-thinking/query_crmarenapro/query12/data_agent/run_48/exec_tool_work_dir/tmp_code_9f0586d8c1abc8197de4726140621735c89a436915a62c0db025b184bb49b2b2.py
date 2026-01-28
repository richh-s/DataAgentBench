code = """import json
from datetime import datetime

# Get the data
key = 'var_functions.query_db:20'
results = locals()[key]

# If results is a string (file path), read it
if isinstance(results, str) and '.json' in results:
    with open(results, 'r') as f:
        results = json.load(f)

# Debug print
print('Number of opportunities:', len(results))

# Process each opportunity to calculate turnaround time
agent_turnarounds = {}

for opp in results:
    agent_id = opp['AgentId']
    created_str = opp['CreatedDate']
    signed_str = opp['CompanySignedDate']
    
    # Parse created date (ISO format with timezone)
    created_date = datetime.fromisoformat(created_str.replace('Z', '+00:00'))
    
    # Parse signed date (YYYY-MM-DD format)
    signed_date = datetime.strptime(signed_str, '%Y-%m-%d')
    signed_date = signed_date.replace(tzinfo=created_date.tzinfo)  # Add timezone info
    
    # Calculate days between created and signed
    turnaround_days = (signed_date - created_date).days
    
    # Debug print
    print(f"Agent: {agent_id}, Created: {created_date.date()}, Signed: {signed_date.date()}, Days: {turnaround_days}")
    
    # Add to agent's list
    if agent_id not in agent_turnarounds:
        agent_turnarounds[agent_id] = []
    agent_turnarounds[agent_id].append(turnaround_days)

# Calculate average turnaround for each agent
agent_averages = {}
for agent_id, turnarounds in agent_turnarounds.items():
    avg = sum(turnarounds) / len(turnarounds)
    agent_averages[agent_id] = avg
    print(f"Agent {agent_id}: average {avg} days over {len(turnarounds)} opportunities")

# Find agent with minimum average turnaround
if agent_averages:
    quickest_agent = min(agent_averages, key=agent_averages.get)
    result = quickest_agent
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:12': [{'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:14': [{'OpportunityId': '006Wt000007BI41IAG', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:16': [{'OpportunityId': '006Wt000007BDApIAO', 'AgentId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'AgentId': '005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.query_db:18': [{'total_opps': '2'}], 'var_functions.query_db:20': [{'OpportunityId': '006Wt000007BHPhIAO', 'AgentId': '005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}, {'OpportunityId': '006Wt000007BDApIAO', 'AgentId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}]}

exec(code, env_args)
