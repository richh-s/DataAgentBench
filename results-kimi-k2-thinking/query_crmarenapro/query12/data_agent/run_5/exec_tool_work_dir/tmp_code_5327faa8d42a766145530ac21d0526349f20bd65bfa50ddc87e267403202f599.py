code = """import json
import datetime

# Access the query results from storage
results = locals()['var_functions.query_db:5']

# Calculate turnaround days for each opportunity
turnaround_data = []
for row in results:
    owner_id = row['OwnerId']
    created_date = row['CreatedDate']
    company_signed_date = row['CompanySignedDate']
    
    # Convert dates to datetime objects
    if isinstance(created_date, str):
        created = datetime.datetime.fromisoformat(created_date.replace('Z', '+00:00'))
    else:
        created = created_date
        
    if isinstance(company_signed_date, str):
        signed = datetime.datetime.fromisoformat(company_signed_date.replace('Z', '+00:00')) if 'T' in company_signed_date else datetime.datetime.strptime(company_signed_date, '%Y-%m-%d')
    else:
        signed = company_signed_date
    
    # Calculate days difference
    days_diff = (signed.date() - created.date()).days
    turnaround_data.append({'OwnerId': owner_id, 'Days': days_diff})

# Calculate average turnaround per agent
from collections import defaultdict
agent_totals = defaultdict(list)
for item in turnaround_data:
    agent_totals[item['OwnerId']].append(item['Days'])

agent_averages = {}
for agent_id, days_list in agent_totals.items():
    agent_averages[agent_id] = sum(days_list) / len(days_list)

print('__RESULT__:')
print(json.dumps(agent_averages))"""

env_args = {'var_functions.query_db:0': [{'OwnerId': '005Wt000003NDEBIA4', 'CompanySignedDate': '2023-04-15', 'CreatedDate': '2022-06-15T10:20:30.000+0000'}], 'var_functions.query_db:2': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:5': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.list_db:6': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem']}

exec(code, env_args)
