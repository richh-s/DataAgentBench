code = """import json
import pandas as pd
from dateutil import parser

cases = locals()['var_function-call-3036060008762067892']
history_path = locals()['var_function-call-784307763129056357']

with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(i):
    if isinstance(i, str) and i.startswith('#'):
        return i[1:]
    return i

# Build History Maps
case_owners = {} # CaseID -> Set of Owners
case_assignment_counts = {} # CaseID -> Int

for h in history:
    cid = clean_id(h.get('caseid__c'))
    new_owner = clean_id(h.get('newvalue__c'))
    
    if cid:
        if cid not in case_owners:
            case_owners[cid] = set()
        if new_owner:
            case_owners[cid].add(new_owner)
        
        case_assignment_counts[cid] = case_assignment_counts.get(cid, 0) + 1

# Process Cases
agent_counts = {} # AgentID -> Set of CaseIDs
agent_durations = {} # AgentID -> List of durations (seconds)

for c in cases:
    cid = clean_id(c.get('id'))
    current_owner = clean_id(c.get('ownerid'))
    
    created_str = c.get('createddate')
    closed_str = c.get('closeddate')
    
    if not created_str or not closed_str:
        continue
        
    created = parser.parse(created_str)
    closed = parser.parse(closed_str)
    duration = (closed - created).total_seconds()
    
    # Track Participation
    participants = set()
    if cid in case_owners:
        participants = case_owners[cid].copy()
    if current_owner:
        participants.add(current_owner)
    
    for p in participants:
        if p not in agent_counts:
            agent_counts[p] = set()
        agent_counts[p].add(cid)
        
    # Track Handle Time (Non-Transferred Only)
    assign_count = case_assignment_counts.get(cid, 0)
    
    # If assign_count > 1, it's transferred.
    if assign_count <= 1:
        if current_owner:
            if current_owner not in agent_durations:
                agent_durations[current_owner] = []
            agent_durations[current_owner].append(duration)

# Determine Winner
min_avg = float('inf')
winner = None
results = []

for agent, case_set in agent_counts.items():
    count = len(case_set)
    if count > 1:
        if agent in agent_durations and len(agent_durations[agent]) > 0:
            avg_time = sum(agent_durations[agent]) / len(agent_durations[agent])
            results.append({'agent': agent, 'avg': avg_time, 'count': count})
            if avg_time < min_avg:
                min_avg = avg_time
                winner = agent

print("__RESULT__:")
print(json.dumps(winner))"""

env_args = {'var_function-call-3169947919775588018': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11094665114348091594': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}], 'var_function-call-12419991242502265436': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-3036060008762067892': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-784307763129056357': 'file_storage/function-call-784307763129056357.json'}

exec(code, env_args)
