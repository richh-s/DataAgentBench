code = """import json
from datetime import datetime

# Load cases
cases = locals()['var_function-call-17551838553651043930']
# cases is a list of dicts

# Load history
history_path = locals()['var_function-call-11261257856447075564']
with open(history_path, 'r') as f:
    history = json.load(f)

# Helper to clean ID
def clean_id(i):
    if i and isinstance(i, str):
        return i.strip().lstrip('#')
    return i

# Prepare data
case_map = {}
for c in cases:
    cid = clean_id(c['id'])
    # Parse dates
    # Format: 2023-07-01T10:30:00.000+0000
    # We need handle time in some unit. Seconds is fine.
    # Python 3.12 datetime.fromisoformat handles basic ISO. +0000 might need handling if not supported directly.
    # strptime "%Y-%m-%dT%H:%M:%S.%f%z"
    try:
        created = datetime.strptime(c['createddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
        closed = datetime.strptime(c['closeddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
        duration = (closed - created).total_seconds()
    except Exception as e:
        duration = 0 # Should not happen based on data
        print(f"Date parse error: {e}")
        
    case_map[cid] = {
        'id': cid,
        'ownerid': clean_id(c['ownerid']),
        'duration': duration,
        'history_entries': []
    }

# Process history
# history contains only 'Owner Assignment' rows
for h in history:
    cid = clean_id(h['caseid__c'])
    if cid in case_map:
        case_map[cid]['history_entries'].append(h)

# Analyze
agent_stats = {} # agent_id -> {'managed_cases': set(), 'valid_handle_times': []}

for cid, data in case_map.items():
    entries = data['history_entries']
    
    # Identify owners
    # Owners are the 'newvalue__c' in the assignment history.
    # Also ensure the current 'ownerid' is accounted for (it should be the last newvalue).
    owners = set()
    for e in entries:
        owners.add(clean_id(e['newvalue__c']))
    
    # If no history, fallback to Case.ownerid
    if not entries:
        owners.add(data['ownerid'])
        is_transferred = False
    else:
        # Rule: Only ONE 'Owner Assignment' -> Not transferred.
        # > 1 -> Transferred.
        if len(entries) > 1:
            is_transferred = True
        else:
            is_transferred = False
            
    # Update Agent Stats
    for owner in owners:
        if owner not in agent_stats:
            agent_stats[owner] = {'managed_cases': set(), 'valid_handle_times': []}
        agent_stats[owner]['managed_cases'].add(cid)
    
    # Assign Handle Time
    if not is_transferred:
        # Assign to the single owner.
        # If entries exist, it's the newvalue of the single entry.
        # If no entries, it's Case.ownerid.
        if entries:
            final_owner = clean_id(entries[0]['newvalue__c'])
        else:
            final_owner = data['ownerid']
            
        if final_owner not in agent_stats:
            agent_stats[final_owner] = {'managed_cases': set(), 'valid_handle_times': []}
        
        agent_stats[final_owner]['valid_handle_times'].append(data['duration'])

# Calculate Averages and Find Lowest
eligible_agents = []
for agent, stats in agent_stats.items():
    if len(stats['managed_cases']) > 1:
        if stats['valid_handle_times']:
            avg_time = sum(stats['valid_handle_times']) / len(stats['valid_handle_times'])
            eligible_agents.append({
                'id': agent,
                'avg_time': avg_time,
                'managed_count': len(stats['managed_cases'])
            })

# Sort
eligible_agents.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(eligible_agents))"""

env_args = {'var_function-call-16084396659173659689': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17551838553651043930': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-17551838553651042327': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-17551838553651040724': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11261257856447075564': 'file_storage/function-call-11261257856447075564.json'}

exec(code, env_args)
