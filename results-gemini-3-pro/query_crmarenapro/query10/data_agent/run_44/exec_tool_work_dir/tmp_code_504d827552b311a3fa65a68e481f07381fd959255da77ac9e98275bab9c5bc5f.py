code = """import json
from collections import defaultdict

# Load data
cases = locals()['var_function-call-9379197308370690660']
history_path = locals()['var_function-call-6841357651747039383']
with open(history_path, 'r') as f:
    history = json.load(f)

# Helper to clean IDs
def clean_id(id_str):
    if not id_str: return None
    if id_str.startswith('#'):
        return id_str[1:]
    return id_str

# Index history by caseid
history_by_case = defaultdict(list)
for h in history:
    cid = clean_id(h.get('caseid__c'))
    if cid:
        history_by_case[cid].append(h)

agent_processed_counts = defaultdict(int)
agent_durations = defaultdict(list)

# Process each closed case
from datetime import datetime

for c in cases:
    cid = clean_id(c['id'])
    # Parse dates
    # Format: 2023-07-01T10:30:00.000+0000
    fmt = "%Y-%m-%dT%H:%M:%S.%f%z" 
    # Python 3.12 handles %z with +0000 but might need fix if colon missing in offset.
    # The sample shows +0000. datetime.strptime supports this.
    try:
        created_dt = datetime.strptime(c['createddate'], fmt)
        closed_dt = datetime.strptime(c['closeddate'], fmt)
    except ValueError:
        # Try without microseconds if fails or adjust format
        # Sample: 2023-07-01T19:41:08.000+0000
        # It matches.
        continue

    duration_seconds = (closed_dt - created_dt).total_seconds()
    
    # Get history
    h_list = history_by_case.get(cid, [])
    
    # Filter for 'Owner Assignment'
    owner_assignments = [h for h in h_list if h.get('field__c') == 'Owner Assignment']
    
    # Identify agents involved
    agents_involved = set()
    
    # From history
    for oa in owner_assignments:
        old = clean_id(oa.get('oldvalue__c'))
        new = clean_id(oa.get('newvalue__c'))
        if old and old != 'None': agents_involved.add(old)
        if new and new != 'None': agents_involved.add(new)
        
    # From current case owner
    final_owner = clean_id(c['ownerid'])
    if final_owner:
        agents_involved.add(final_owner)
        
    # Increment counts
    for agent in agents_involved:
        agent_processed_counts[agent] += 1
        
    # Handle Time Logic
    # "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    # "For those that have been transferred... MORE THAN ONE"
    # "When computing handle time, we do not compute... for cases that have been transferred"
    
    # Check number of assignments
    # If 0 assignments in history, but we have a final owner, assume 1 (Initial).
    # If 1 assignment in history (old=None, new=X), not transferred.
    # If > 1 assignments, transferred.
    
    num_assignments = len(owner_assignments)
    
    # Note: Sometimes history might be missing initial assignment if it's old?
    # But for these cases created in 2023, history should be there.
    # Case 1 in result: created 2023-07-01.
    
    if num_assignments <= 1:
        # Not transferred (or 0 found, assumed 1).
        # Assign duration to final owner
        if final_owner:
            agent_durations[final_owner].append(duration_seconds)
    else:
        # Transferred. Do not compute handle time.
        pass

# Calculate Averages and Filter
results = []
for agent, count in agent_processed_counts.items():
    if count > 1:
        # Eligible
        durs = agent_durations.get(agent, [])
        if durs:
            avg_time = sum(durs) / len(durs)
            results.append({
                "agent_id": agent,
                "processed_count": count,
                "avg_handle_time": avg_time,
                "num_measured_cases": len(durs)
            })

# Find lowest
if results:
    sorted_results = sorted(results, key=lambda x: x['avg_handle_time'])
    print("__RESULT__:")
    print(json.dumps(sorted_results))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-16935417607994828587': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11268043920336260726': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-9379197308370690660': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-6841357651747039383': 'file_storage/function-call-6841357651747039383.json'}

exec(code, env_args)
