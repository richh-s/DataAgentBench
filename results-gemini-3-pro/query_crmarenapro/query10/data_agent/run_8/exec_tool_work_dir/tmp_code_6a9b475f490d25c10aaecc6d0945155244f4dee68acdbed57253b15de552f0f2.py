code = """import json
import pandas as pd
from datetime import datetime

# Load data
cases = locals()['var_function-call-15813525106352124259']
history_path = locals()['var_function-call-1992848873889521844']

with open(history_path, 'r') as f:
    history = json.load(f)

# Helper to clean ID
def clean_id(x):
    if not isinstance(x, str):
        return x
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Clean Cases
cleaned_cases = []
for c in cases:
    c['id'] = clean_id(c['id'])
    c['ownerid'] = clean_id(c['ownerid'])
    cleaned_cases.append(c)

# Count Owner Assignments
owner_counts = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    owner_counts[cid] = owner_counts.get(cid, 0) + 1

# Group by Agent
agent_cases = {}
for c in cleaned_cases:
    agent = c['ownerid']
    if agent not in agent_cases:
        agent_cases[agent] = []
    agent_cases[agent].append(c)

# Calculate metrics
agent_metrics = []

for agent, cases_list in agent_cases.items():
    # Filter: processing more than one case
    # Assuming "processing" means closing > 1 case in the period
    if len(cases_list) <= 1:
        continue
    
    valid_durations = []
    for c in cases_list:
        cid = c['id']
        # Check if transferred
        # History tracks Owner Assignment.
        # If count > 1, transferred.
        # If count == 1, not transferred (original assignment).
        # If count == 0 (not in history), assume 1 (creation assignment might be implicit or missed). 
        # But data shows 'Owner Assignment' events.
        # Let's assume if it's not in history, it wasn't transferred? Or maybe data is incomplete?
        # Given the "165" count and list of cases, likely coverage is good.
        # If count > 1 -> exclude.
        
        count = owner_counts.get(cid, 0)
        # Wait, if count is 0, does it mean 1 assignment (creation)? Or data missing?
        # The prompt says: "For cases that have NOT been transferred ... only ONE 'Owner Assignment'... MORE THAN ONE..."
        # So I expect at least 1 for every case. If 0, maybe the "Creation" event isn't "Owner Assignment"?
        # But earlier distinct check showed "Case Creation" and "Owner Assignment".
        # Let's check if 'Case Creation' implies an owner assignment. Usually yes.
        # But the prompt specifically refers to 'Owner Assignment' count.
        # If count > 1, transferred.
        # If count <= 1, keep.
        
        if count > 1:
            continue
            
        # Parse dates
        # Format: "2023-07-01T10:30:00.000+0000"
        try:
            created = datetime.strptime(c['createddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
            closed = datetime.strptime(c['closeddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
        except ValueError:
            # try without microseconds if needed
            created = datetime.strptime(c['createddate'].split('.')[0] + "+0000", "%Y-%m-%dT%H:%M:%S%z")
            closed = datetime.strptime(c['closeddate'].split('.')[0] + "+0000", "%Y-%m-%dT%H:%M:%S%z")

        duration = (closed - created).total_seconds()
        valid_durations.append(duration)
    
    if len(valid_durations) > 0:
        avg_time = sum(valid_durations) / len(valid_durations)
        agent_metrics.append({'agent_id': agent, 'avg_time': avg_time, 'case_count': len(cases_list), 'valid_count': len(valid_durations)})

# Find lowest
if not agent_metrics:
    result = "No qualifying agents"
else:
    best_agent = min(agent_metrics, key=lambda x: x['avg_time'])
    result = best_agent['agent_id']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14838987602196373344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8892615390852284541': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-14093882633430532867': [{'count': '165'}], 'var_function-call-15813525106352124259': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-1992848873889521844': 'file_storage/function-call-1992848873889521844.json'}

exec(code, env_args)
