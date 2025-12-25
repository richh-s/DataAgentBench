code = """import json
from datetime import datetime

# Load the data
with open(locals()['var_function-call-12020941486477026334'], 'r') as f:
    history = json.load(f)

# Define the window
start_date = datetime(2022, 4, 10)
end_date = datetime(2023, 4, 10)

transfer_counts = {}
population = set()

for entry in history:
    # Check if this is an owner assignment (it should be due to query filter)
    # Parse date
    # Date format: "2023-09-07T16:30:00.000+0000"
    # We can handle the timezone or just ignore if consistent. +0000 is UTC.
    dt_str = entry['createddate']
    # Removing +0000 for simple parsing or using strptime
    # Python 3.12 has fromisoformat but might struggle with +0000 without colon in older versions, but let's try strict format
    # Simpler: just take the YYYY-MM-DD part and compare if we don't care about time precision for the boundary?
    # Actually, precise comparison is better.
    # Convert "2023-09-07T16:30:00.000+0000" to datetime
    # We can strip the +0000 and treat as UTC naive for comparison if we define start/end as naive.
    dt_naive_str = dt_str.split('+')[0]
    dt = datetime.strptime(dt_naive_str, "%Y-m-%dT%H:%M:%S.%f")
    
    # Add to population (anyone involved in an assignment handles a case)
    if entry['newvalue__c'] and entry['newvalue__c'] != 'None':
        population.add(entry['newvalue__c'])
    if entry['oldvalue__c'] and entry['oldvalue__c'] != 'None':
        population.add(entry['oldvalue__c'])
        
    # Check for transfer in window
    if start_date <= dt <= end_date:
        if entry['oldvalue__c'] and entry['oldvalue__c'] != 'None':
            # This is a transfer FROM oldvalue__c
            agent_id = entry['oldvalue__c']
            transfer_counts[agent_id] = transfer_counts.get(agent_id, 0) + 1

# Calculate counts for population
results = []
for agent_id in population:
    count = transfer_counts.get(agent_id, 0)
    results.append({'id': agent_id, 'count': count})

# Find min
if not results:
    min_val = 0
    min_agents = []
else:
    min_val = min(r['count'] for r in results)
    min_agents = [r['id'] for r in results if r['count'] == min_val]

print("__RESULT__:")
print(json.dumps({'min_val': min_val, 'min_agents': min_agents, 'total_pop': len(population)}))"""

env_args = {'var_function-call-10037541303498214618': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10863993742589604424': [{'field__c': 'Case Creation', 'cnt': '153'}, {'field__c': 'Case Closed', 'cnt': '75'}, {'field__c': 'Owner Assignment', 'cnt': '165'}], 'var_function-call-14618880228806568354': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-12020941486477026334': 'file_storage/function-call-12020941486477026334.json'}

exec(code, env_args)
