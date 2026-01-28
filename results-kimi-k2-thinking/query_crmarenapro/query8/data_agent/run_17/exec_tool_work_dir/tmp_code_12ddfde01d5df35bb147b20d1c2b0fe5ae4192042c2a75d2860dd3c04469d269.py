code = """import json
from collections import defaultdict

# Get the file path from storage using locals()
result_file = locals()['var_functions.query_db:8']

# Read the full data
with open(result_file, 'r') as f:
    all_transfers = json.load(f)

# Count transfers FROM agents and cases received BY agents
transfers_from = defaultdict(int)
cases_received = defaultdict(int)

for record in all_transfers:
    created_date = record.get('createddate', '')
    if created_date >= '2022-04-01' and created_date < '2023-04-01':
        oldvalue = record.get('oldvalue__c', 'None')
        newvalue = record.get('newvalue__c', 'None')
        
        if oldvalue != 'None':
            transfers_from[oldvalue] += 1
        
        if newvalue != 'None':
            cases_received[newvalue] += 1

# Find agents with cases handled > 0 and minimum transfers
eligible_agents = []
for agent in cases_received:
    cases = cases_received[agent]
    if cases > 0:
        transfers = transfers_from.get(agent, 0)
        eligible_agents.append((agent, transfers, cases))

eligible_agents.sort(key=lambda x: (x[1], -x[2]))

agent_id = eligible_agents[0][0] if eligible_agents else 'No agents found'
print('__RESULT__:')
print(agent_id)"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'agent_id': '005Wt000003NIliIAG', 'transfer_count': '1'}]}

exec(code, env_args)
