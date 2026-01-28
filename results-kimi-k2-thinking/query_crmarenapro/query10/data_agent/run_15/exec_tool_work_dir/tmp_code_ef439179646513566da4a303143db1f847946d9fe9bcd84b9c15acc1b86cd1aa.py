code = """import json
import pandas as pd

# Load both datasets
cases = locals().get('var_functions.query_db:28', [])
history = locals().get('var_functions.query_db:8', [])

print('Cases count: ' + str(len(cases)))
print('History count: ' + str(len(history)))

# Process cases
clean_cases = []
for case in cases:
    clean_cases.append({
        'id': case['id'].lstrip('#'),
        'ownerid': case['ownerid'].lstrip('#'),
        'createddate': pd.to_datetime(case['createddate']),
        'closeddate': pd.to_datetime(case['closeddate'])
    })

cases_df = pd.DataFrame(clean_cases)
cases_df['handle_time'] = (cases_df['closeddate'] - cases_df['createddate']).dt.total_seconds() / 3600

# Process history - clean values
for hist in history:
    hist['caseid__c'] = hist['caseid__c'].lstrip('#')
    hist['newvalue__c'] = hist['newvalue__c'].lstrip('#')

history_df = pd.DataFrame(history)

# Get cases with only one owner assignment (not transferred)
case_assignments = history_df.groupby('caseid__c').size().reset_index(name='assignment_count')
single_assignment_cases = case_assignments[case_assignments['assignment_count'] == 1]['caseid__c'].tolist()

print('Single assignment cases: ' + str(len(single_assignment_cases)))
print('Case IDs with single assignment: ' + str(single_assignment_cases))

# Filter to only non-transferred cases
non_transferred = cases_df[cases_df['id'].isin(single_assignment_cases)]
print('Non-transferred cases: ' + str(len(non_transferred)))

if not non_transferred.empty:
    # Get the original agent from history for these cases
    initial_assignments = history_df[history_df['caseid__c'].isin(single_assignment_cases)]
    initial_assignments = initial_assignments.sort_values('createddate').groupby('caseid__c').first().reset_index()
    
    # Merge to get agent info
    merged = non_transferred.merge(initial_assignments[['caseid__c', 'newvalue__c']], left_on='id', right_on='caseid__c', how='left')
    merged['agent_id'] = merged['newvalue__c'].fillna(merged['ownerid'])
    
    print('Merged data count: ' + str(len(merged)))
    print('Agent counts: ' + str(merged.groupby('agent_id').size().to_dict()))
    
    # Count cases per agent
    agent_case_counts = merged.groupby('agent_id').size().reset_index(name='case_count')
    multiple_case_agents = agent_case_counts[agent_case_counts['case_count'] > 1]['agent_id'].tolist()
    
    print('Agents with multiple cases: ' + str(multiple_case_agents))
    
    if multiple_case_agents:
        # Calculate average handle time
        filtered = merged[merged['agent_id'].isin(multiple_case_agents)]
        avg_times = filtered.groupby('agent_id')['handle_time'].mean().reset_index()
        avg_times.columns = ['agent_id', 'avg_handle_time']
        avg_times = avg_times.sort_values('avg_handle_time')
        
        lowest_agent = avg_times.iloc[0]['agent_id']
        print('Lowest agent: ' + lowest_agent)
        print('__RESULT__:')
        print(json.dumps(lowest_agent))
    else:
        print('__RESULT__:')
        print(json.dumps(None))
else:
    print('__RESULT__:')
    print(json.dumps(None))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_functions.query_db:8': [{'id': 'a04Wt00000538O1IAI', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T11:30:02.000+0000'}, {'id': 'a04Wt00000538O3IAI', 'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'id': 'a04Wt00000538mAIAQ', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'id': 'a04Wt00000538FtIAI', 'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'field__c': 'Owner Assignment', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'id': '#a04Wt00000537zlIAA', 'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'id': 'a04Wt00000536Z5IAI', 'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'id': 'a04Wt00000538pNIAQ', 'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'id': 'a04Wt00000538hKIAQ', 'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'field__c': 'Owner Assignment', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'id': 'a04Wt00000537ZzIAI', 'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'field__c': 'Owner Assignment', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'field__c': 'Owner Assignment', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'field__c': 'Owner Assignment', 'createddate': '2023-06-03T14:45:00.000+0000'}], 'var_functions.execute_python:12': None, 'var_functions.execute_python:14': None, 'var_functions.list_db:16': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:18': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_functions.execute_python:22': None, 'var_functions.query_db:24': [{'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}], 'var_functions.execute_python:26': None, 'var_functions.query_db:28': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_functions.execute_python:30': None}

exec(code, env_args)
