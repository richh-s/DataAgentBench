code = """import json
import datetime
from collections import defaultdict

# Access the full result from the previous query
full_result = var_functions.query_db:14

# If result is a string pointing to a JSON file, read it
if isinstance(full_result, str) and full_result.endswith('.json'):
    import os
    with open(full_result, 'r') as f:
        full_result = json.load(f)

# Check if we have multiple records or just one
print('Number of records:', len(full_result) if isinstance(full_result, list) else 'not a list')
print('Sample data:', full_result)

# Calculate turnaround days for each opportunity and average per agent
if isinstance(full_result, list) and len(full_result) > 0:
    agent_days = defaultdict(list)
    
    for row in full_result:
        owner_id = row.get('OwnerId')
        created_date = row.get('CreatedDate')
        company_signed_date = row.get('CompanySignedDate')
        
        # Parse dates
        try:
            if isinstance(created_date, str):
                # Remove timezone info for simplicity
                created_date = created_date.split('T')[0]
                created = datetime.datetime.strptime(created_date, '%Y-%m-%d').date()
            
            if isinstance(company_signed_date, str):
                signed = datetime.datetime.strptime(company_signed_date, '%Y-%m-%d').date()
            
            # Calculate days difference
            days_diff = (signed - created).days
            agent_days[owner_id].append(days_diff)
        except Exception as e:
            print(f'Error processing row: {e}')
    
    # Calculate average turnaround per agent
    agent_averages = {}
    for agent_id, days_list in agent_days.items():
        agent_averages[agent_id] = sum(days_list) / len(days_list)
    
    print('__RESULT__:')
    print(json.dumps(agent_averages))
else:
    print('__RESULT__:')
    print(json.dumps({}))"""

env_args = {'var_functions.query_db:0': [{'OwnerId': '005Wt000003NDEBIA4', 'CompanySignedDate': '2023-04-15', 'CreatedDate': '2022-06-15T10:20:30.000+0000'}], 'var_functions.query_db:2': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.query_db:5': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}], 'var_functions.list_db:6': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.execute_python:10': {'005Wt000003NDEBIA4': 304.0}, 'var_functions.execute_python:12': 'Need to query all opportunities closed in April 2023 to find the agent with quickest average turnaround', 'var_functions.query_db:14': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15'}]}

exec(code, env_args)
