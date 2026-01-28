code = """import json
import datetime

# Retrieve the data from storage
assignments_data = locals()['var_functions.query_db:10']
cases_data = locals()['var_functions.query_db:6']

# Clean ID fields by removing trailing whitespace and # prefix
def clean_id(id_value):
    if id_value is None:
        return None
    id_str = str(id_value).strip()
    if id_str.startswith('#'):
        id_str = id_str[1:]
    return id_str

# Process assignments data
assignments_by_case = {}
for assignment in assignments_data:
    case_id = clean_id(assignment['caseid__c'])
    owner_id = clean_id(assignment['newvalue__c'])
    
    if case_id not in assignments_by_case:
        assignments_by_case[case_id] = []
    assignments_by_case[case_id].append({
        'owner_id': owner_id,
        'assignment_date': assignment['assignment_date']
    })

# Identify non-transferred cases (only one owner assignment)
non_transferred_cases = []
for case_id, assignments in assignments_by_case.items():
    if len(assignments) == 1:  # Only one assignment means no transfer
        non_transferred_cases.append({
            'case_id': case_id,
            'owner_id': assignments[0]['owner_id']
        })

print(f"Found {len(non_transferred_cases)} non-transferred cases")
for c in non_transferred_cases[:5]:
    print(f"  {c}")

# Process cases data to get handle times
cases_dict = {}
for case_data in cases_data:
    case_id = clean_id(case_data['id'])
    owner_id = clean_id(case_data['ownerid'])
    createddate = case_data['createddate']
    closeddate = case_data['closeddate']
    
    cases_dict[case_id] = {
        'owner_id': owner_id,
        'createddate': createddate,
        'closeddate': closeddate
    }

print(f"\nTotal cases in data: {len(cases_dict)}")

# Find agents who handled more than one case in the non-transferred set
agent_cases = {}
for case_info in non_transferred_cases:
    case_id = case_info['case_id']
    owner_id = case_info['owner_id']
    
    if owner_id not in agent_cases:
        agent_cases[owner_id] = []
    agent_cases[owner_id].append(case_id)

# Filter agents with more than one case
agents_with_multiple_cases = {agent: cases for agent, cases in agent_cases.items() if len(cases) > 1}

print(f"\nAgents with more than one case: {len(agents_with_multiple_cases)}")
for agent, case_list in agents_with_multiple_cases.items():
    print(f"  Agent {agent}: {len(case_list)} cases")

# Calculate handle times for each agent
agent_handle_times = {}
for agent_id, case_ids in agents_with_multiple_cases.items():
    handle_times = []
    
    for case_id in case_ids:
        if case_id in cases_dict:
            case_data = cases_dict[case_id]
            closed = case_data['closeddate']
            
            # Only calculate handle time for closed cases
            if closed and closed != 'None':
                handle_times.append({
                    'case_id': case_id,
                    'createddate': case_data['createddate'],
                    'closeddate': closed
                })
    
    # Only include agents with at least one closed case
    if handle_times:
        agent_handle_times[agent_id] = handle_times

# Calculate average handle times
from datetime import datetime

def parse_datetime(dt_str):
    """Parse datetime string to datetime object"""
    if not dt_str or dt_str == 'None':
        return None
    
    # Handle different formats
    dt_str = str(dt_str)
    if '.' in dt_str:
        dt_str = dt_str.split('.')[0]
    
    try:
        return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except:
        return None

agent_avg_handle_time = {}
for agent_id, case_list in agent_handle_times.items():
    total_seconds = 0
    valid_cases = 0
    
    for case_info in case_list:
        created = parse_datetime(case_info['createddate'])
        closed = parse_datetime(case_info['closeddate'])
        
        if created and closed:
            handle_seconds = (closed - created).total_seconds()
            total_seconds += handle_seconds
            valid_cases += 1
    
    if valid_cases > 0:
        avg_seconds = total_seconds / valid_cases
        avg_hours = avg_seconds / 3600
        agent_avg_handle_time[agent_id] = {
            'avg_hours': avg_hours,
            'case_count': valid_cases,
            'avg_seconds': avg_seconds
        }

print(f"\nAgents with calculable handle times: {len(agent_avg_handle_time)}")
for agent, data in agent_avg_handle_time.items():
    print(f"  Agent {agent}: {data['avg_hours']:.2f} hours avg, {data['case_count']} cases")

# Sort by average handle time and get the lowest
if agent_avg_handle_time:
    sorted_agents = sorted(agent_avg_handle_time.items(), key=lambda x: x[1]['avg_hours'])
    print("\nRanking by lowest avg handle time:")
    for i, (agent, data) in enumerate(sorted_agents[:5]):
        print(f"  {i+1}. Agent {agent}: {data['avg_hours']:.2f} hours")
    
    lowest_agent = sorted_agents[0][0]
    print(f"\nAgent with lowest avg handle time: {lowest_agent}")
    
    result = json.dumps(lowest_agent)
    print('__RESULT__:')
    print(result)
else:
    print('__RESULT__:')
    print(json.dumps("No agents found with multiple cases and calculable handle times"))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': [{'id': 'a04Wt00000538O1IAI', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538O3IAI', 'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538mAIAQ', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538FtIAI', 'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537zlIAA', 'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000536Z5IAI', 'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538pNIAQ', 'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538hKIAQ', 'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537ZzIAI', 'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:6': [{'id': '#500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ0DIAW', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDTxbIAH', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NIfFIAW', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG', 'status': 'Closed'}, {'id': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJppIAG', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDsG3IAL', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NI5mIAG', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW', 'status': 'Closed'}, {'id': '500Wt00000DDzXdIAL', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJUrIAO', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzZHIA1', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDzivIAD', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzkXIAT', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NINVIA4', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzr0IAD', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJcvIAG', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG', 'status': 'Closed'}], 'var_functions.query_db:8': [{'caseid__c': '500Wt00000DDepmIAD', 'owner_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'owner_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'owner_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'owner_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'owner_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}], 'var_functions.query_db:10': [{'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'assignment_date': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'assignment_date': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'assignment_date': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'assignment_date': '2023-06-12T10:00:06.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'assignment_date': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'assignment_date': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'assignment_date': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'assignment_date': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'assignment_date': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'assignment_date': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'assignment_date': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'assignment_date': '2023-06-02T09:30:00.000+0000'}], 'var_functions.query_db:12': [{'caseid__c': '500Wt00000DDTxbIAH', 'history_date': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW'}, {'caseid__c': '500Wt00000DDepmIAD', 'history_date': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG'}, {'caseid__c': '500Wt00000DDflsIAD', 'history_date': '2023-06-12T09:45:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW'}, {'caseid__c': '500Wt00000DDflsIAD', 'history_date': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG'}, {'caseid__c': '500Wt00000DDyzpIAD', 'history_date': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4'}, {'caseid__c': '500Wt00000DDzUPIA1', 'history_date': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzXdIAL', 'history_date': '2023-06-22T11:00:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO'}, {'caseid__c': '500Wt00000DDzZHIA1', 'history_date': '2023-07-02T09:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzkXIAT', 'history_date': '2023-06-19T14:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'caseid__c': '500Wt00000DDzr0IAD', 'history_date': '2023-08-01T10:00:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG'}, {'caseid__c': '500Wt00000DDzsbIAD', 'history_date': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO'}, {'caseid__c': '500Wt00000DDzuEIAT', 'history_date': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO'}]}

exec(code, env_args)
