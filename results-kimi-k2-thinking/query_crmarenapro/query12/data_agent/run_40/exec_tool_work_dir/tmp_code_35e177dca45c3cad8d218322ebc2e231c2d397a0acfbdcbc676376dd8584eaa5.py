code = """import json
import datetime
from collections import defaultdict

# Access the query result from the previous call
opportunities = locals()['var_functions.query_db:6']

# Calculate turnaround days for each opportunity
turnaround_data = []

for opp in opportunities:
    try:
        # Parse created date (includes timestamp)
        created_date_str = opp['CreatedDate']
        if 'T' in created_date_str:
            created_date = datetime.datetime.fromisoformat(created_date_str.replace('Z', '+00:00')).date()
        else:
            created_date = datetime.datetime.strptime(created_date_str, '%Y-%m-%d').date()
        
        # Parse company signed date (date only)
        company_signed_date_str = opp['CompanySignedDate']
        if isinstance(company_signed_date_str, str):
            company_signed_date = datetime.datetime.strptime(company_signed_date_str, '%Y-%m-%d').date()
        else:
            company_signed_date = company_signed_date_str
        
        # Calculate turnaround days
        turnaround_days = (company_signed_date - created_date).days
        
        turnaround_data.append({
            'OpportunityId': opp['OpportunityId'],
            'OwnerId': opp['OwnerId'],
            'TurnaroundDays': turnaround_days
        })
        
    except Exception as e:
        print("Error processing opportunity: " + str(e))

# Group by OwnerId and calculate average turnaround
agent_turnarounds = defaultdict(list)
for data in turnaround_data:
    agent_turnarounds[data['OwnerId']].append(data['TurnaroundDays'])

# Calculate average turnaround for each agent
agent_averages = {}
for owner_id, turnarounds in agent_turnarounds.items():
    avg_turnaround = sum(turnarounds) / len(turnarounds)
    agent_averages[owner_id] = avg_turnaround

# Find agent with minimum average turnaround
if agent_averages:
    quickest_agent = min(agent_averages, key=agent_averages.get)
    result = quickest_agent
else:
    result = None

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}], 'var_functions.execute_python:5': None, 'var_functions.query_db:6': [{'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
