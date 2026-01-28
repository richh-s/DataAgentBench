code = """import json
import pandas as pd
from datetime import datetime

# Load the data
cases = [
  {"id": "500Wt00000DDepmIAD", "ownerid": "005Wt000003NJufIAG", "createddate": "2023-07-01T10:30:00.000+0000", "closeddate": "2023-07-01T19:41:08.000+0000"},
  {"id": "500Wt00000DDyzpIAD", "ownerid": "005Wt000003NJGLIA4", "createddate": "2023-08-15T14:30:00.000+0000", "closeddate": "2023-08-15T14:54:02.000+0000"},
  {"id": "500Wt00000DDzUPIA1", "ownerid": "005Wt000003NDqDIAW", "createddate": "2023-05-10T14:45:00.000+0000", "closeddate": "2023-05-10T14:59:42.000+0000"},
  {"id": "500Wt00000DDzsbIAD", "ownerid": "005Wt000003NJD9IAO", "createddate": "2023-06-30T13:03:00.000+0000", "closeddate": "2023-06-30T19:03:08.000+0000"},
  {"id": "#500Wt00000DDzscIAD", "ownerid": "005Wt000003NEtOIAW", "createddate": "2023-05-02T23:55:00.000+0000", "closeddate": "2023-05-03T00:11:47.000+0000"},
  {"id": "500Wt00000DDzuEIAT", "ownerid": "005Wt000003NJJaIAO", "createddate": "2023-06-02T09:30:00.000+0000", "closeddate": "2023-06-02T13:35:12.000+0000"},
  {"id": "#500Wt00000DE02HIAT", "ownerid": "005Wt000003NIddIAG", "createddate": "2023-06-03T14:45:00.000+0000", "closeddate": "2023-06-03T15:21:34.000+0000"}
]

assignment_counts = [
  {"caseid__c": "500Wt00000DDzZHIA1", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDzr0IAD", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDflsIAD", "assignment_count": "2"},
  {"caseid__c": "500Wt00000DDzuEIAT", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDzkXIAT", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDzUPIA1", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDyzpIAD", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDzXdIAL", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDzsbIAD", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDTxbIAH", "assignment_count": "1"},
  {"caseid__c": "500Wt00000DDepmIAD", "assignment_count": "1"}
]

# Filter out transferred cases (assignment_count > 1)
transferred_case_ids = {ac['caseid__c'] for ac in assignment_counts if int(ac['assignment_count']) > 1}

# Get only non-transferred cases
non_transferred_cases = []
for case in cases:
    case_id = case['id']
    # Remove leading # if present
    if case_id.startswith('#'):
        case_id = case_id[1:]
    if case_id not in transferred_case_ids:
        non_transferred_cases.append(case)

# Calculate handle time for each case and aggregate by agent
agent_cases = {}
for case in non_transferred_cases:
    ownerid = case['ownerid']
    created = datetime.fromisoformat(case['createddate'].replace('Z', '+00:00'))
    closed = datetime.fromisoformat(case['closeddate'].replace('Z', '+00:00'))
    handle_time_hours = (closed - created).total_seconds() / 3600.0
    
    if ownerid not in agent_cases:
        agent_cases[ownerid] = []
    agent_cases[ownerid].append(handle_time_hours)

# Filter agents with more than 1 case and calculate average handle time
agent_stats = []
for ownerid, handle_times in agent_cases.items():
    if len(handle_times) > 1:
        avg_handle_time = sum(handle_times) / len(handle_times)
        agent_stats.append({
            'ownerid': ownerid,
            'case_count': len(handle_times),
            'avg_handle_time_hours': avg_handle_time
        })

# Sort by average handle time
agent_stats.sort(key=lambda x: x['avg_handle_time_hours'])

# Get the agent with the lowest average handle time
result = agent_stats[0]['ownerid'] if agent_stats else None

# Print in the required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:6': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_functions.query_db:8': [{'caseid__c': '500Wt00000DDzZHIA1', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzr0IAD', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDflsIAD', 'assignment_count': '2'}, {'caseid__c': '500Wt00000DDzuEIAT', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzkXIAT', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzUPIA1', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDyzpIAD', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzXdIAL', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzsbIAD', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDTxbIAH', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDepmIAD', 'assignment_count': '1'}], 'var_functions.query_db:10': [{'case_count': '7'}], 'var_functions.query_db:14': [], 'var_functions.query_db:16': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_functions.query_db:18': [{'caseid__c': '500Wt00000DDzZHIA1', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzr0IAD', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDflsIAD', 'assignment_count': '2'}, {'caseid__c': '500Wt00000DDzuEIAT', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzkXIAT', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzUPIA1', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDyzpIAD', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzXdIAL', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDzsbIAD', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDTxbIAH', 'assignment_count': '1'}, {'caseid__c': '500Wt00000DDepmIAD', 'assignment_count': '1'}]}

exec(code, env_args)
