code = """import json
from datetime import datetime

# Let's analyze the data more carefully
cases = [
    {"id": "500Wt00000DDepmIAD", "createddate": "2023-07-01T10:30:00.000+0000", "closeddate": "2023-07-01T19:41:08.000+0000", "ownerid": "005Wt000003NJufIAG"},
    {"id": "500Wt00000DDyzpIAD", "createddate": "2023-08-15T14:30:00.000+0000", "closeddate": "2023-08-15T14:54:02.000+0000", "ownerid": "005Wt000003NJGLIA4"},
    {"id": "500Wt00000DDzUPIA1", "createddate": "2023-05-10T14:45:00.000+0000", "closeddate": "2023-05-10T14:59:42.000+0000", "ownerid": "005Wt000003NDqDIAW"},
    {"id": "500Wt00000DDzsbIAD", "createddate": "2023-06-30T13:03:00.000+0000", "closeddate": "2023-06-30T19:03:08.000+0000", "ownerid": "005Wt000003NJD9IAO"},
    {"id": "#500Wt00000DDzscIAD", "createddate": "2023-05-02T23:55:00.000+0000", "closeddate": "2023-05-03T00:11:47.000+0000", "ownerid": "005Wt000003NEtOIAW"},
    {"id": "500Wt00000DDzuEIAT", "createddate": "2023-06-02T09:30:00.000+0000", "closeddate": "2023-06-02T13:35:12.000+0000", "ownerid": "005Wt000003NJJaIAO"},
    {"id": "#500Wt00000DE02HIAT", "createddate": "2023-06-03T14:45:00.000+0000", "closeddate": "2023-06-03T15:21:34.000+0000", "ownerid": "005Wt000003NIddIAG"}
]

owner_assignments = [
    {"caseid__c": "500Wt00000DDepmIAD", "field__c": "Owner Assignment", "newvalue__c": "005Wt000003NJufIAG", "createddate": "2023-07-01T10:30:00.000+0000"},
    {"caseid__c": "500Wt00000DDzUPIA1", "field__c": "Owner Assignment", "newvalue__c": "005Wt000003NDqDIAW", "createddate": "2023-05-10T14:45:00.000+0000"},
    {"caseid__c": "500Wt00000DDzuEIAT", "field__c": "Owner Assignment", "newvalue__c": "005Wt000003NJJaIAO", "createddate": "2023-06-02T09:30:00.000+0000"},
    {"caseid__c": "500Wt00000DDyzpIAD", "field__c": "Owner Assignment", "newvalue__c": "005Wt000003NJGLIA4", "createddate": "2023-08-15T14:30:00.000+0000"},
    {"caseid__c": "500Wt00000DDzsbIAD", "field__c": "Owner Assignment", "newvalue__c": "005Wt000003NJD9IAO", "createddate": "2023-06-30T13:03:00.000+0000"}
]

# Count number of owner assignments per case
case_assignment_counts = {}
for assignment in owner_assignments:
    case_id = assignment['caseid__c']
    case_assignment_counts[case_id] = case_assignment_counts.get(case_id, 0) + 1

print("Case assignment counts:")
print(json.dumps(case_assignment_counts, indent=2))

# Check which cases have assignment records
case_ids = [case['id'] for case in cases]
print("\nCase IDs from cases query:")
print(json.dumps(case_ids, indent=2))

# Filter to cases with exactly one owner assignment (not transferred)
non_transferred_cases = []
handle_times = []
agent_case_counts = {}
agent_handle_times = {}

for case in cases:
    case_id = case['id']
    assignment_count = case_assignment_counts.get(case_id, 0)
    
    print(f"Case {case_id}: {assignment_count} assignments")
    
    # We only count cases with exactly one owner assignment as non-transferred
    if assignment_count == 1:
        # Check that the owner in case matches the owner in assignment
        matching_assignment = [a for a in owner_assignments if a['caseid__c'] == case_id][0]
        if matching_assignment['newvalue__c'] == case['ownerid']:
            non_transferred_cases.append(case)
            created = datetime.fromisoformat(case['createddate'].replace('Z', '+00:00'))
            closed = datetime.fromisoformat(case['closeddate'].replace('Z', '+00:00'))
            handle_time = (closed - created).total_seconds() / 3600  # in hours
            handle_times.append(handle_time)
            
            agent_id = case['ownerid']
            agent_case_counts[agent_id] = agent_case_counts.get(agent_id, 0) + 1
            if agent_id not in agent_handle_times:
                agent_handle_times[agent_id] = []
            agent_handle_times[agent_id].append(handle_time)

print(f"\nFound {len(non_transferred_cases)} non-transferred cases")
print(f"Agent case counts: {json.dumps(agent_case_counts)}")

# Calculate average handle time for agents with more than 1 case
agents_with_multiple_cases = {}
for agent_id, case_count in agent_case_counts.items():
    if case_count > 1:
        avg_handle_time = sum(agent_handle_times[agent_id]) / len(agent_handle_times[agent_id])
        agents_with_multiple_cases[agent_id] = {
            'case_count': case_count,
            'avg_handle_time_hours': avg_handle_time,
            'avg_handle_time_minutes': avg_handle_time * 60
        }

print(f"\nAgents with >1 case:")
print(json.dumps(agents_with_multiple_cases, indent=2))

if agents_with_multiple_cases:
    best_agent = min(agents_with_multiple_cases.items(), key=lambda x: x[1]['avg_handle_time_hours'])
    print(f"\nBest agent: {best_agent[0]} with avg handle time {best_agent[1]['avg_handle_time_minutes']:.2f} minutes")
else:
    print("No agents with more than 1 case found")"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:14': [{'table_name': 'Case'}, {'table_name': 'knowledge__kav'}, {'table_name': 'issue__c'}, {'table_name': 'casehistory__c'}, {'table_name': 'emailmessage'}, {'table_name': 'livechattranscript'}], 'var_functions.query_db:16': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.execute_python:18': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.query_db:20': [{'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}]}

exec(code, env_args)
