code = """import json
import datetime
from collections import defaultdict

# Get the query result
result = var_functions.query_db:28

print('Records found:', len(result))
print('Sample data:', result[:1])

# Calculate turnaround days for each record
turnaround_times = []
for record in result:
    created_str = record['CreatedDate']
    signed_str = record['CompanySignedDate']
    
    # Parse dates
    if 'T' in created_str:
        created_date = datetime.datetime.fromisoformat(created_str.replace('Z', '+00:00')).date()
    else:
        created_date = datetime.datetime.strptime(created_str, '%Y-%m-%d').date()
    
    signed_date = datetime.datetime.strptime(signed_str, '%Y-%m-%d').date()
    
    # Calculate days difference
    days_diff = (signed_date - created_date).days
    turnaround_times.append({
        'OwnerId': record['OwnerId'],
        'Days': days_diff
    })

# Group by agent and calculate average
agent_days = defaultdict(list)
for item in turnaround_times:
    agent_days[item['OwnerId']].append(item['Days'])

agent_averages = {}
for agent, days in agent_days.items():
    agent_averages[agent] = sum(days) / len(days)

# Find agent with minimum average turnaround
quickest_agent = min(agent_averages, key=agent_averages.get) if agent_averages else None

print('__RESULT__:')
print(json.dumps(quickest_agent))"""

env_args = {'var_functions.query_db:0': [{'OwnerId': '005Wt000003NDEBIA4', 'CompanySignedDate': '2023-04-15', 'CreatedDate': '2022-06-15T10:20:30.000+0000'}], 'var_functions.query_db:2': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:5': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.list_db:6': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.execute_python:10': {'005Wt000003NDEBIA4': 304.0}, 'var_functions.execute_python:12': 'Need to query all opportunities closed in April 2023 to find the agent with quickest average turnaround', 'var_functions.query_db:14': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:20': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15', 'OpportunityId': '006Wt000007BI41IAG', 'ContractId': '800Wt00000DE9FGIA1'}], 'var_functions.query_db:26': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15', 'AccountId': '001Wt00000PFrk1IAD'}], 'var_functions.query_db:28': [{'Id': '800Wt00000DE9FGIA1', 'CompanySignedDate': '2023-04-15', 'OpportunityId': '006Wt000007BI41IAG', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000'}], 'var_functions.query_db:30': [{'contract_count': '1'}]}

exec(code, env_args)
