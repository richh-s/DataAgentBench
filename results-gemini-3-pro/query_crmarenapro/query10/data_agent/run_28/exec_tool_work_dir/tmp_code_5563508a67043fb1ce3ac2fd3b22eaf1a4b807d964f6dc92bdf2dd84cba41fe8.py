code = """import json
import pandas as pd
from datetime import datetime

# Load cases
cases_list = locals()['var_function-call-5909842420318969754']

# Load history from file
with open(locals()['var_function-call-11308014558138915622'], 'r') as f:
    history_list = json.load(f)

# Helper to clean IDs
def clean_id(x):
    if not isinstance(x, str):
        return x
    x = x.strip()
    if x.startswith('#'):
        return x[1:]
    return x

# Process History
# Group by caseid__c
case_owners = {} # case_id -> list of owners (newvalue__c)

for h in history_list:
    cid = clean_id(h.get('caseid__c'))
    oid = clean_id(h.get('newvalue__c'))
    
    if cid and oid:
        if cid not in case_owners:
            case_owners[cid] = []
        case_owners[cid].append(oid)

# Process Cases
agent_stats = {} # agent_id -> {'managed_count': 0, 'handle_times': []}

for c in cases_list:
    cid = clean_id(c.get('id'))
    created_str = c.get('createddate')
    closed_str = c.get('closeddate')
    
    if not cid or not created_str or not closed_str:
        continue
        
    # Calculate duration
    try:
        # Format: 2023-07-01T10:30:00.000+0000
        # Python 3.11+ supports %z, usually. Or use pd.to_datetime
        # Let's use pd.to_datetime for robustness
        created_dt = pd.to_datetime(created_str)
        closed_dt = pd.to_datetime(closed_str)
        duration = (closed_dt - created_dt).total_seconds()
    except Exception as e:
        continue
        
    owners = case_owners.get(cid, [])
    
    # Logic based on hint: 
    # Single Owner: len(owners) == 1 (or 0 if inconsistent, fall back to ownerid)
    # Transferred: len(owners) > 1
    
    is_transferred = False
    
    if len(owners) > 1:
        is_transferred = True
        unique_owners = set(owners)
    elif len(owners) == 1:
        unique_owners = set(owners)
    else:
        # No history found. Contradicts hint?
        # Fallback: assume single owner from Case table
        oid = clean_id(c.get('ownerid'))
        unique_owners = {oid} if oid else set()
        
    for agent in unique_owners:
        if agent not in agent_stats:
            agent_stats[agent] = {'managed_count': 0, 'handle_times': []}
        
        agent_stats[agent]['managed_count'] += 1
        
        if not is_transferred:
            # Only count handle time if not transferred
            agent_stats[agent]['handle_times'].append(duration)

# Calculate Average
results = []
for agent, stats in agent_stats.items():
    if stats['managed_count'] > 1:
        times = stats['handle_times']
        if len(times) > 0:
            avg_time = sum(times) / len(times)
            results.append({'agent_id': agent, 'avg_time': avg_time, 'count': stats['managed_count'], 'valid_cases': len(times)})

# Find lowest
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9305866664193886812': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5909842420318969754': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10922903359105958166': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-11308014558138915622': 'file_storage/function-call-11308014558138915622.json'}

exec(code, env_args)
