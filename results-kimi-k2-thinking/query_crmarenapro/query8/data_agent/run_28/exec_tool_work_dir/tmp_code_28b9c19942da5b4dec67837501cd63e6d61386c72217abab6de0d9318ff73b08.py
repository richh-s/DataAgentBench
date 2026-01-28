code = """import json
import pandas as pd
from datetime import datetime

# Get the case history data from storage
casehistory_raw = locals()['var_functions.query_db:5']

# Check if it's a file path or direct data
if isinstance(casehistory_raw, str) and casehistory_raw.endswith('.json'):
    with open(casehistory_raw, 'r') as f:
        casehistory_data = json.load(f)
else:
    casehistory_data = casehistory_raw

# Define the date range for last 4 quarters (Q2 2022 to Q1 2023)
# Start: 2022-04-01, End: 2023-03-31
start_date = datetime.strptime('2022-04-01', '%Y-%m-%d')
end_date = datetime.strptime('2023-03-31', '%Y-%m-%d')

# Parse dates and filter records within the last 4 quarters
filtered_records = []
for record in casehistory_data:
    date_str = record.get('createddate', '').split('T')[0]
    if date_str:
        try:
            record_date = datetime.strptime(date_str, '%Y-%m-%d')
            if start_date <= record_date <= end_date:
                filtered_records.append(record)
        except:
            pass

# Get all owner assignments in the date range
owner_assignments = [r for r in filtered_records if r.get('field__c') == 'Owner Assignment']

# Create a mapping of which agents handled which cases
agent_cases = {}
case_owners = {}  # Track all owners for each case sorted by date

# Create list of all assignments with dates for proper ordering
assignments_with_dates = []
for record in owner_assignments:
    case_id = record.get('caseid__c')
    agent_id = record.get('newvalue__c')
    date_str = record.get('createddate', '')
    
    if agent_id and agent_id != 'None' and case_id:
        # Clean up IDs
        if agent_id.startswith('#'):
            agent_id = agent_id[1:]
            
        assignments_with_dates.append({
            'case_id': case_id,
            'agent_id': agent_id,
            'date': date_str
        })
        
        # Track cases handled by each agent
        if agent_id not in agent_cases:
            agent_cases[agent_id] = set()
        agent_cases[agent_id].add(case_id)

# Sort assignments by date for each case to get proper transfer order
from collections import defaultdict
assignments_by_case = defaultdict(list)
for assign in assignments_with_dates:
    assignments_by_case[assign['case_id']].append(assign)

# Sort each case's assignments by date
for case_id in assignments_by_case:
    assignments_by_case[case_id].sort(key=lambda x: x['date'])

case_owners = {}
for case_id, assignments in assignments_by_case.items():
    case_owners[case_id] = [assign['agent_id'] for assign in assignments]

# Calculate transfer counts: a transfer happens when a case has multiple owners
# The agent who HAD the case before the transfer is the one who transferred it
transfer_counts = {}

for case_id, owners in case_owners.items():
    if len(owners) > 1:  # Case was transferred
        # For each transfer, the previous owner transferred to the next owner
        for i in range(len(owners) - 1):
            from_agent = owners[i]
            
            if from_agent not in transfer_counts:
                transfer_counts[from_agent] = 0
            transfer_counts[from_agent] += 1

# Ensure all agents with cases are in the transfer_counts dict
for agent_id in agent_cases.keys():
    if agent_id not in transfer_counts:
        transfer_counts[agent_id] = 0

# Only consider agents who handled more than 0 cases
eligible_agents = {}
for agent_id, cases in agent_cases.items():
    if len(cases) > 0:
        eligible_agents[agent_id] = {
            'case_count': len(cases),
            'transfer_count': transfer_counts.get(agent_id, 0)
        }

# Find the agent(s) with the minimum transfer count
min_transfer_count = min([info['transfer_count'] for info in eligible_agents.values()])
agents_with_min_transfers = [
    agent_id for agent_id, info in eligible_agents.items() 
    if info['transfer_count'] == min_transfer_count
]

# If multiple agents have the same minimum transfer count, return the first one
result_agent_id = agents_with_min_transfers[0] if agents_with_min_transfers else None

print('__RESULT__:')
print(json.dumps({
    'result_agent_id': result_agent_id,
    'min_transfer_count': min_transfer_count,
    'total_eligible_agents': len(eligible_agents),
    'agents_with_min_transfers': agents_with_min_transfers
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'total_records': 393, 'owner_assignment_records': 165, 'transfer_records': 165, 'sample_transfers': [{'agent_id': '005Wt000003NINVIA4', 'case_id': '500Wt00000DDzpNIAT', 'date': '2023-09-07T16:30:00.000+0000'}, {'agent_id': '005Wt000003NIXBIA4', 'case_id': '500Wt00000DDfHCIA1', 'date': '2021-07-23T11:00:00.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'case_id': '500Wt00000DDZ0VIAX', 'date': '2021-10-15T13:46:00.000+0000'}, {'agent_id': '005Wt000003NJcwIAG', 'case_id': '500Wt00000DDQoUIAX', 'date': '2021-09-15T10:00:00.000+0000'}, {'agent_id': '005Wt000003NJ3RIAW', 'case_id': '500Wt00000DDzm9IAD', 'date': '2022-03-03T10:00:00.000+0000'}]}, 'var_functions.execute_python:14': {'agents_with_cases': 32, 'total_transfers': 1, 'sample_agents': [['005Wt000003NJcvIAG', 1], ['005Wt000003NIliIAG', 2], ['005Wt000003NDqFIAW', 1], ['005Wt000003NEzqIAG', 1], ['005Wt000003NEGhIAO', 1], ['005Wt000003NJ6gIAG', 1], ['005Wt000003NIVZIA4', 1], ['005Wt000003NBcAIAW', 1], ['005Wt000003NHsrIAG', 2], ['005Wt000003NFr4IAG', 1]], 'sample_transfers': [['005Wt000003NIliIAG', 1], ['005Wt000003NJcvIAG', 0], ['005Wt000003NDqFIAW', 0], ['005Wt000003NEzqIAG', 0], ['005Wt000003NEGhIAO', 0], ['005Wt000003NJ6gIAG', 0], ['005Wt000003NIVZIA4', 0], ['005Wt000003NBcAIAW', 0], ['005Wt000003NHsrIAG', 0], ['005Wt000003NFr4IAG', 0]]}}

exec(code, env_args)
