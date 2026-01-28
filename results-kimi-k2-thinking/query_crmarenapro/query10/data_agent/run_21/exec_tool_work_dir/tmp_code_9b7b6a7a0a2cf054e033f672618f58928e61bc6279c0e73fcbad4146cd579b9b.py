code = """import json
import pandas as pd
from collections import defaultdict

# Load data
cases = locals()['var_functions.query_db:22']  # Closed cases
history = locals()['var_functions.query_db:8']  # Case history

# Create DataFrames
df_cases = pd.DataFrame(cases)
df_history = pd.DataFrame(history)

# Clean IDs (remove # prefix)
def clean_id(id_val):
    if isinstance(id_val, str) and id_val.startswith('#'):
        return id_val[1:]
    return id_val

df_cases['id'] = df_cases['id'].apply(clean_id)
df_cases['ownerid'] = df_cases['ownerid'].apply(clean_id)

df_history['caseid__c'] = df_history['caseid__c'].apply(clean_id)
df_history['oldvalue__c'] = df_history['oldvalue__c'].apply(clean_id)
df_history['newvalue__c'] = df_history['newvalue__c'].apply(clean_id)

# Parse dates
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Get owner assignment history
owner_assignments = df_history[df_history['field__c'] == 'Owner Assignment'].copy()
owner_assignments['createddate'] = pd.to_datetime(owner_assignments['createddate'])

# Identify transferred cases
transferred_cases = set()
case_owner_count = defaultdict(int)

case_ids = df_cases['id'].tolist()
for case_id in case_ids:
    assignments = owner_assignments[owner_assignments['caseid__c'] == case_id]
    case_owner_count[case_id] = len(assignments)
    if len(assignments) > 1:
        transferred_cases.add(case_id)
    elif len(assignments) == 1 and assignments.iloc[0]['oldvalue__c'] != 'None':
        transferred_cases.add(case_id)

# Debug: Show case owner counts
print('Case owner assignment counts:')
for case_id in case_ids:
    count = case_owner_count[case_id]
    is_transferred = case_id in transferred_cases
    print(f'{case_id}: {count} assignments, transferred: {is_transferred}')

# Calculate handle times for non-transferred cases
agent_cases = defaultdict(list)

for idx, case in df_cases.iterrows():
    case_id = case['id']
    
    if case_id in transferred_cases:
        print(f'Skipping transferred case: {case_id}')
        continue
    
    # Get the owner from case history (more reliable)
    assignments = owner_assignments[owner_assignments['caseid__c'] == case_id]
    if len(assignments) > 0:
        agent_id = assignments.iloc[0]['newvalue__c']
    else:
        agent_id = case['ownerid']
    
    # Calculate handle time in hours
    handle_time = (case['closeddate'] - case['createddate']).total_seconds() / 3600
    agent_cases[agent_id].append(handle_time)
    print(f'Case {case_id}: Agent {agent_id}, Handle time: {handle_time:.2f} hours')

# Calculate average handle time per agent
agent_stats = []
for agent_id, handle_times in agent_cases.items():
    if len(handle_times) > 1:  # Only agents with more than one case
        avg_time = sum(handle_times) / len(handle_times)
        agent_stats.append({
            'agent_id': agent_id,
            'case_count': len(handle_times),
            'avg_handle_time': avg_time,
            'handle_times': handle_times
        })
        print(f'Agent {agent_id}: {len(handle_times)} cases, Avg: {avg_time:.2f} hours')

# Find agent with lowest average
if agent_stats:
    best_agent = min(agent_stats, key=lambda x: x['avg_handle_time'])
    result = best_agent['agent_id']
    print(f'Best agent: {result} with avg {best_agent["avg_handle_time"]:.2f} hours')
else:
    result = 'No agent found'
    print('No agent with multiple non-transferred cases found')

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_functions.query_db:2': [], 'var_functions.list_db:5': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:6': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:8': [{'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW'}, {'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Case Creation', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-07-01T10:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Creation', 'createddate': '2023-07-01T10:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Closed', 'createddate': '2023-07-01T19:41:08.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T09:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Case Creation', 'createddate': '2023-06-12T09:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T10:00:06.000+0000', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Creation', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Closed', 'createddate': '2023-08-15T14:54:02.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'createddate': '2023-05-10T14:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Creation', 'createddate': '2023-05-10T14:45:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Closed', 'createddate': '2023-05-10T14:59:42.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Owner Assignment', 'createddate': '2023-06-22T11:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Case Creation', 'createddate': '2023-06-22T11:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Case Creation', 'createddate': '2023-07-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Case Creation', 'createddate': '2023-06-19T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Owner Assignment', 'createddate': '2023-06-19T14:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Case Creation', 'createddate': '2023-08-01T10:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Owner Assignment', 'createddate': '2023-08-01T10:00:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'createddate': '2023-06-30T13:03:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Creation', 'createddate': '2023-06-30T13:03:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'createddate': '2023-06-30T19:03:08.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'createddate': '2023-06-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Creation', 'createddate': '2023-06-02T09:30:00.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Closed', 'createddate': '2023-06-02T13:35:12.000+0000', 'oldvalue__c': 'None', 'newvalue__c': 'None'}], 'var_functions.query_db:10': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_functions.execute_python:14': 'No agent found with multiple cases', 'var_functions.execute_python:20': 'No agent found', 'var_functions.query_db:22': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}]}

exec(code, env_args)
