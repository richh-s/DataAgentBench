code = """import json
import pandas as pd
from dateutil import parser
from datetime import datetime, timezone

cases = locals()['var_function-call-10023071106298998827']
history_path = locals()['var_function-call-784307763129056357']

with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(i):
    if isinstance(i, str) and i.startswith('#'):
        return i[1:]
    return i

# Build History Maps
case_owners = {} 
case_assignment_counts = {}

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
agent_counts = {} # All participation in the 69 cases
agent_durations = {} # Only valid closed cases

window_start = parser.parse("2023-05-02T00:00:00+0000")
window_end = parser.parse("2023-09-02T23:59:59+0000")

for c in cases:
    cid = clean_id(c.get('id'))
    current_owner = clean_id(c.get('ownerid'))
    
    created_str = c.get('createddate')
    closed_str = c.get('closeddate')
    
    # 1. Update Participation Counts
    participants = set()
    if cid in case_owners:
        participants = case_owners[cid].copy()
    if current_owner:
        participants.add(current_owner)
    
    for p in participants:
        if p not in agent_counts:
            agent_counts[p] = set()
        agent_counts[p].add(cid)
        
    # 2. Update Handle Time (Closed in Window, Non-Transferred)
    if closed_str and closed_str != "None":
        closed = parser.parse(closed_str)
        created = parser.parse(created_str)
        
        if closed >= window_start and closed <= window_end:
             assign_count = case_assignment_counts.get(cid, 0)
             if assign_count <= 1: # Non-transferred
                 duration = (closed - created).total_seconds()
                 if current_owner:
                     if current_owner not in agent_durations:
                         agent_durations[current_owner] = []
                     agent_durations[current_owner].append(duration)

# Find Winner
min_avg = float('inf')
winner = None
results = []

for agent, case_set in agent_counts.items():
    count = len(case_set)
    if count > 1: # Processed > 1 case
        if agent in agent_durations and len(agent_durations[agent]) > 0:
            avg_time = sum(agent_durations[agent]) / len(agent_durations[agent])
            results.append({'agent': agent, 'avg': avg_time, 'count': count})
            if avg_time < min_avg:
                min_avg = avg_time
                winner = agent

print("__RESULT__:")
print(json.dumps(winner))"""

env_args = {'var_function-call-3169947919775588018': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11094665114348091594': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}], 'var_function-call-12419991242502265436': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-3036060008762067892': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-784307763129056357': 'file_storage/function-call-784307763129056357.json', 'var_function-call-12722181617071459268': None, 'var_function-call-8561298200741821859': {'debug': {'total_cases': 7, 'cases_with_history': 7, 'transferred_cases': 0, 'non_transferred_cases': 7, 'agents_with_counts': 7, 'agents_with_durations': 7}, 'top_results': []}, 'var_function-call-10023071106298998827': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDDtTIAX', 'ownerid': '#005Wt000003NJWTIA4', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPZ0IAP', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPsOIAX', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDQoUIAX', 'ownerid': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDRB2IAP', 'ownerid': '005Wt000003NFhOIAW', 'createddate': '2021-01-10T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDRW0IAP', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2021-06-03T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDTEQIA5', 'ownerid': '005Wt000003NJ9tIAG', 'createddate': '2022-03-02T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDTHfIAP', 'ownerid': '#005Wt000003NJeXIAW', 'createddate': '2021-10-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzRCIA1', 'ownerid': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYipIAH', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2022-03-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYpGIAX', 'ownerid': '005Wt000003NJLBIA4', 'createddate': '2021-03-31T11:41:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZ0VIAX', 'ownerid': '#005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZ5LIAX', 'ownerid': '005Wt000003NHfyIAG', 'createddate': '2021-11-11T12:13:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZJuIAP', 'ownerid': '#005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZtLIAX', 'ownerid': '#005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDeoCIAT', 'ownerid': '#005Wt000003NIYnIAO', 'createddate': '2020-07-01T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDfHCIA1', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDfYxIAL', 'ownerid': '005Wt000003NJcvIAG', 'createddate': '2022-04-01T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDfvXIAT', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2021-03-24T18:04:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDnt7IAD', 'ownerid': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDsG4IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2020-11-05T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsKtIAL', 'ownerid': '#005Wt000003NJQ1IAO', 'createddate': '2021-08-24T13:25:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDt7GIAT', 'ownerid': '#005Wt000003NDu7IAG', 'createddate': '2021-11-01T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDt7HIAT', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2021-02-01T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxScIAL', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxduIAD', 'ownerid': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDxkMIAT', 'ownerid': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDydCIAT', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2021-05-24T04:08:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDyznIAD', 'ownerid': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzB4IAL', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzEIIA1', 'ownerid': '005Wt000003NInJIAW', 'createddate': '2021-06-02T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzJ8IAL', 'ownerid': '#005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzMLIA1', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '#500Wt00000DDzUQIA1', 'ownerid': '#005Wt000003NH3GIAW', 'createddate': '2022-03-04T11:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzW3IAL', 'ownerid': '#005Wt000003NIfHIAW', 'createddate': '2021-11-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzXeIAL', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDze5IAD', 'ownerid': '005Wt000003NHpeIAG', 'createddate': '2021-10-22T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzm9IAD', 'ownerid': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzmBIAT', 'ownerid': '#005Wt000003NIDqIAO', 'createddate': '2022-01-28T02:41:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzmCIAT', 'ownerid': '005Wt000003NIXBIA4', 'createddate': '2021-09-10T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzqzIAD', 'ownerid': '#005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr2IAD', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-01-10T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzvqIAD', 'ownerid': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzxRIAT', 'ownerid': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE00gIAD', 'ownerid': '005Wt000003NJWTIA4', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE00hIAD', 'ownerid': '005Wt000003NBcAIAW', 'createddate': '2021-11-15T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '500Wt00000DE05VIAT', 'ownerid': '005Wt000003NI2XIAW', 'createddate': '2021-01-03T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE079IAD', 'ownerid': '005Wt000003NJoDIAW', 'createddate': '2021-07-05T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE07AIAT', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2021-11-02T09:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0ALIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2021-09-17T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0K1IAL', 'ownerid': '#005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0WvIAL', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2021-07-07T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0a9IAD', 'ownerid': '005Wt000003NHGAIA4', 'createddate': '2021-06-16T08:30:00.000+0000', 'closeddate': 'None'}]}

exec(code, env_args)
