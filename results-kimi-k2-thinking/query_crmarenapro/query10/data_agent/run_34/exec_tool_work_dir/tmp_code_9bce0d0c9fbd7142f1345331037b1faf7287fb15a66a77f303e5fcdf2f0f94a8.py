code = """import json
from datetime import datetime

# Load case data
cases = locals()['var_functions.query_db:8']
if isinstance(cases, str):
    with open(cases, 'r') as f:
        cases = json.load(f)

# Load owner assignment data
owner_history = locals()['var_functions.query_db:18']
if isinstance(owner_history, str):
    with open(owner_history, 'r') as f:
        owner_history = json.load(f)

print('Cases:', len(cases))
print('Owner history records:', len(owner_history))

# Build map of case ID to handle time (minutes)
handle_times = {}
for case in cases:
    cid = case['id'].replace('#', '')
    created = case['createddate']
    closed = case['closeddate']
    
    # Parse dates
    created_dt = datetime.strptime(created, '%Y-%m-%dT%H:%M:%S.%f%z')
    closed_dt = datetime.strptime(closed, '%Y-%m-%dT%H:%M:%S.%f%z')
    
    # Calculate minutes
    minutes = (closed_dt - created_dt).total_seconds() / 60
    handle_times[cid] = {'minutes': minutes, 'owner': case['ownerid']}

print('Case handle times:', {k: (v['minutes'], v['owner']) for k, v in list(handle_times.items())[:3]})

# Build owner assignment counts per case
case_owner_counts = {}
for rec in owner_history:
    cid = rec['caseid__c'].replace('#', '')
    if cid not in case_owner_counts:
        case_owner_counts[cid] = 0
    case_owner_counts[cid] += 1

print('Case owner assignment counts:', case_owner_counts)
print('All cases have single owner assignment:', all(c == 1 for c in case_owner_counts.values()))

# Group by owner and calculate metrics
owner_stats = {}
for cid, info in handle_times.items():
    owner = info['owner']
    minutes = info['minutes']
    
    if owner not in owner_stats:
        owner_stats[owner] = {'cases': 0, 'total_minutes': 0}
    
    owner_stats[owner]['cases'] += 1
    owner_stats[owner]['total_minutes'] += minutes

print('Owner stats:', owner_stats)

# Calculate average handle times and filter for agents with > 1 case
eligible_owners = {}
for owner, stats in owner_stats.items():
    if stats['cases'] > 1:
        eligible_owners[owner] = stats['total_minutes'] / stats['cases']

print('Eligible owners (>1 case):', eligible_owners)

# Find agent with lowest average handle time
if eligible_owners:
    best_agent = min(eligible_owners, key=eligible_owners.get)
    print('Best agent:', best_agent)
    result = {'agent_id': best_agent}
else:
    print('No eligible agents found')
    result = {'agent_id': None, 'message': 'No agents with more than one case'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:4': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.execute_python:10': {'case_ids': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'case_id_tuple': "('500Wt00000DDepmIAD','500Wt00000DDyzpIAD','500Wt00000DDzUPIA1','500Wt00000DDzsbIAD','500Wt00000DDzscIAD','500Wt00000DDzuEIAT','500Wt00000DE02HIAT')"}, 'var_functions.query_db:12': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.execute_python:16': {'in_clause': "('500Wt00000DDepmIAD','500Wt00000DDyzpIAD','500Wt00000DDzUPIA1','500Wt00000DDzsbIAD','500Wt00000DDzscIAD','500Wt00000DDzuEIAT','500Wt00000DE02HIAT')", 'case_ids': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT']}, 'var_functions.query_db:18': [{'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}]}

exec(code, env_args)
