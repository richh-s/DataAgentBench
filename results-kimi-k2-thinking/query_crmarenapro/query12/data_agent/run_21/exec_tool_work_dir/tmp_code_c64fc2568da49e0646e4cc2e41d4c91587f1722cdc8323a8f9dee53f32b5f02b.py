code = """import json

# Read the data from the previous query
result_data = locals().get('var_functions.query_db:2', [])

# Calculate average days per agent
from collections import defaultdict
agent_days = defaultdict(list)

for record in result_data:
    agent_id = record.get('OwnerId')
    days_to_close = record.get('days_to_close')
    if agent_id and days_to_close:
        # Convert string to int if needed
        if isinstance(days_to_close, str):
            try:
                days_to_close = int(days_to_close)
            except:
                continue
        agent_days[agent_id].append(days_to_close)

# Calculate average for each agent
agent_averages = {}
for agent_id, days_list in agent_days.items():
    if days_list:
        agent_averages[agent_id] = sum(days_list) / len(days_list)

# Find agent with minimum average
if agent_averages:
    min_avg_agent = min(agent_averages, key=agent_averages.get)
    result = min_avg_agent
else:
    result = None

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:2': [{'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2022-06-15T10:20:30.000+0000', 'CompanySignedDate': '2023-04-15', 'days_to_close': '304'}]}

exec(code, env_args)
