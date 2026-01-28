code = """import json
from collections import defaultdict

# Load the query result
result_file = var_functions.query_db:8

# Read the full data
with open(result_file, 'r') as f:
    all_transfers = json.load(f)

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
for agent in cases_received:
    cases = cases_received[agent]
    if cases > 0:
        transfers = transfers_from.get(agent, 0)
        eligible_agents.append((agent, transfers, cases))

# Sort by transfer count ascending, then by cases handled descending
eligible_agents.sort(key=lambda x: (x[1], -x[2]))

if eligible_agents:
    agent_id = eligible_agents[0][0]
    transfers = eligible_agents[0][1]
    cases = eligible_agents[0][2]
    print('Agent ID with fewest transfers:', agent_id)
    print('Transfer count:', transfers)
    print('Cases handled:', cases)
    
    print('__RESULT__:')
    print(agent_id)
else:
    print('__RESULT__:')
    print('No agents found')"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'agent_id': '005Wt000003NIliIAG', 'transfer_count': '1'}]}

exec(code, env_args)
