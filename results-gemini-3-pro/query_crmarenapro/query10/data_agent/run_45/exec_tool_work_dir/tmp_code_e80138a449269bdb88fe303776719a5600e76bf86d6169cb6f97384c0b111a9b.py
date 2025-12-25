code = """import json
import pandas as pd
from datetime import datetime

# Load cases
cases = locals()['var_function-call-10460115554179369151']

# Load history
history_path = locals()['var_function-call-10460115554179367206']
with open(history_path, 'r') as f:
    history = json.load(f)

# Helper to clean ID
def clean_id(oid):
    if oid and isinstance(oid, str):
        return oid.lstrip('#')
    return oid

# Process Cases
case_map = {} # id -> {created, closed, owner, is_transferred, handle_time, owners_set}
target_case_ids = set()

for c in cases:
    cid = clean_id(c['id'])
    target_case_ids.add(cid)
    
    # Parse dates
    # Format example: "2023-07-01T10:30:00.000+0000"
    # Using pandas to parse easily
    created = pd.to_datetime(c['createddate'])
    closed = pd.to_datetime(c['closeddate'])
    duration = (closed - created).total_seconds()
    
    case_map[cid] = {
        'created': created,
        'closed': closed,
        'duration': duration,
        'current_owner': clean_id(c['ownerid']),
        'owners': set()
    }

# Process History
# Filter for Owner Assignment
owner_assignments = [h for h in history if h['field__c'] == 'Owner Assignment']

# Group by case
history_map = {} # caseid -> list of assignments
for h in owner_assignments:
    cid = clean_id(h['caseid__c'])
    if cid not in history_map:
        history_map[cid] = []
    history_map[cid].append(h)

# Determine Transferred Status and Collect Owners for Target Cases
for cid in target_case_ids:
    assignments = history_map.get(cid, [])
    
    # Sort assignments by createddate just in case, though usually sorted or not needed for simple count
    # Count assignments
    # Rule: "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    count_assignments = len(assignments)
    
    is_transferred = False
    if count_assignments > 1:
        is_transferred = True
    elif count_assignments == 0:
        # No history? Assume not transferred if it exists in Case table?
        # Or maybe it's 1 assignment (creation) but not logged?
        # But description says "For cases that have NOT been transferred... there will be only ONE"
        # If 0, maybe data issue. But let's assume 1 (current owner).
        # Wait, if 0, we only know current owner.
        is_transferred = False # Assumption
    else:
        # == 1
        is_transferred = False
        
    case_map[cid]['is_transferred'] = is_transferred
    
    # Collect Owners
    # From history
    for h in assignments:
        if h.get('newvalue__c'):
            case_map[cid]['owners'].add(clean_id(h['newvalue__c']))
            
    # Also add current owner from Case table (should be in history, but just in case)
    case_map[cid]['owners'].add(case_map[cid]['current_owner'])

# Calculate Agent Stats
agent_stats = {} # agent_id -> {'processed_count': 0, 'durations': []}

# We need to iterate over all Target Cases and attribute them to agents
for cid, info in case_map.items():
    # For count: attribute to ALL owners
    for owner in info['owners']:
        if owner not in agent_stats:
            agent_stats[owner] = {'processed_count': 0, 'durations': []}
        agent_stats[owner]['processed_count'] += 1
        
    # For handle time: attribute ONLY to owner IF not transferred
    if not info['is_transferred']:
        # Who is the owner?
        # If not transferred, there is only 1 owner.
        # It should be in info['owners'] (size 1) and info['current_owner']
        owner = info['current_owner']
        if owner in agent_stats:
            agent_stats[owner]['durations'].append(info['duration'])

# Filter and Find Min
results = []
for agent, stats in agent_stats.items():
    if stats['processed_count'] > 1:
        if len(stats['durations']) > 0:
            avg_time = sum(stats['durations']) / len(stats['durations'])
            results.append({
                'agent': agent,
                'avg_time': avg_time,
                'count': stats['processed_count'],
                'durations': stats['durations'] # for debug
            })

# Sort by avg_time
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13068910769840781709': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-1417980459216219882': [{'count': '7'}], 'var_function-call-1417980459216218149': [{'count': '165'}], 'var_function-call-10460115554179369151': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-10460115554179367206': 'file_storage/function-call-10460115554179367206.json'}

exec(code, env_args)
