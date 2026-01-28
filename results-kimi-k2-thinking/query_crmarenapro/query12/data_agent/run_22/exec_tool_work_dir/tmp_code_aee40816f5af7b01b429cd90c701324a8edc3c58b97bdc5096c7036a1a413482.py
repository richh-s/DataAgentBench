code = """import json
from datetime import datetime

# Get the query results from storage
query_results = locals()['var_functions.query_db:2']

# Process each opportunity to calculate turnaround days
agent_turnarounds = {}

for record in query_results:
    owner_id = record['OwnerId']
    created_date_str = record['CreatedDate']
    company_signed_date_str = record['CompanySignedDate']
    
    # Parse dates
    try:
        # Handle ISO format with timezone
        created_date = datetime.fromisoformat(created_date_str.replace('Z', '+00:00'))
        company_signed_date = datetime.strptime(company_signed_date_str, '%Y-%m-%d')
        
        # Calculate turnaround in days
        turnaround_days = (company_signed_date - created_date).days
        
        # Add to agent's list of turnarounds
        if owner_id not in agent_turnarounds:
            agent_turnarounds[owner_id] = []
        agent_turnarounds[owner_id].append(turnaround_days)
        
    except Exception as e:
        print(f"Error processing record: {e}")

# Calculate average turnaround for each agent
agent_averages = {}
for owner_id, turnarounds in agent_turnarounds.items():
    agent_averages[owner_id] = sum(turnarounds) / len(turnarounds)

# Find agent with quickest average turnaround
quickest_agent = min(agent_averages, key=agent_averages.get)

result = quickest_agent

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}]}

exec(code, env_args)
