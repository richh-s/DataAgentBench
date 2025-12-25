code = """import json

# Load previous results
cases = locals()['var_function-call-8542522144959194876']
history_7 = locals()['var_function-call-1841919419859699863']

# 1. Identify Owners of closed cases and Calculate Handle Time
# Also check for transfers for these cases (we already saw none, but good to be robust)
case_transfers = {} # caseid -> count of assignments
for h in history_7:
    cid = h['caseid__c']
    case_transfers[cid] = case_transfers.get(cid, 0) + 1

# Eligible cases for AHT (Not transferred)
# And map Owner -> list of Handle Times
agent_handle_times = {} # AgentId -> [times]
# Also keep track of Case IDs closed by agent (for Count)
agent_closed_cases = {} # AgentId -> set(caseids)

from datetime import datetime

for c in cases:
    cid = c['id']
    if cid.startswith('#'): cid = cid[1:]
    
    # Check transfer
    # If not in history, maybe 0 assignments? (Impossible if created). 
    # But we saw all had 1 assignment.
    # If count > 1, transferred.
    if case_transfers.get(cid, 0) > 1:
        continue # Exclude from AHT
        
    owner = c['ownerid']
    created = datetime.strptime(c['createddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
    closed = datetime.strptime(c['closeddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
    duration = (closed - created).total_seconds()
    
    if owner not in agent_handle_times:
        agent_handle_times[owner] = []
        agent_closed_cases[owner] = set()
    
    agent_handle_times[owner].append(duration)
    agent_closed_cases[owner].add(cid)

candidate_agents = list(agent_handle_times.keys())

print("__RESULT__:")
print(json.dumps(candidate_agents))"""

env_args = {'var_function-call-5822339402360875576': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-8542522144959196223': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-8542522144959194876': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-1841919419859699863': [{'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
