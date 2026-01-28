code = """import json

# Load the query result
result = var_functions.query_db:10

# Load and inspect some data from the large file
file_path = var_functions.query_db:8

# Read the full data
with open(file_path, 'r') as f:
    all_transfers = json.load(f)

# Debug: Check agents with 0 transfers
# Let's find agents who received cases but didn't transfer any away

from collections import defaultdict

# Count all transfers FROM agents
transfers_from = defaultdict(int)
# Count cases handled BY agents (received)
cases_received = defaultdict(int)

for record in all_transfers:
    created_date = record.get('createddate', '')
    # Filter for last 4 quarters: 2022-04-01 to 2023-03-31
    if '2022-04-01' <= created_date < '2023-04-01':
        oldvalue = record.get('oldvalue__c', 'None')
        newvalue = record.get('newvalue__c', 'None')
        
        # Count transfers FROM agent (if not initial assignment)
        if oldvalue != 'None':
            transfers_from[oldvalue] += 1
        
        # Count cases received by agent
        if newvalue != 'None':
            cases_received[newvalue] += 1

# Find agents who handled cases (>0) and find those with fewest transfers
eligible_agents = []
for agent, cases in cases_received.items():
    if cases > 0:
        transfers = transfers_from.get(agent, 0)
        eligible_agents.append((agent, transfers, cases))

# Sort by transfer count, then by cases handled
seligible_agents_sorted = sorted(eligible_agents, key=lambda x: (x[1], -x[2]))

print('Top 10 agents with fewest transfers:')
for agent, transfers, cases in eligible_agents_sorted[:10]:
    print(f'Agent: {agent}, Transfers: {transfers}, Cases: {cases}')

print(f'\nTotal eligible agents: {len(eligible_agents_sorted)}')

if eligible_agents_sorted:
    agent_id, transfers, cases = eligible_agents_sorted[0]
    print(f'\nAgent with fewest transfers:')
    print(f'Agent ID: {agent_id}')
    print(f'Transfer count: {transfers}')
    print(f'Cases handled: {cases}')

print('__RESULT__:')
print(agent_id if eligible_agents_sorted else 'No agents found')"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'agent_id': '005Wt000003NIliIAG', 'transfer_count': '1'}]}

exec(code, env_args)
