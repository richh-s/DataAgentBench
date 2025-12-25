code = """import json
import pandas as pd

# Load Active Cases
active_cases_raw = locals()['var_function-call-825315341004275369']
# Load History
history_path = locals()['var_function-call-10460115554179367206']
with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(oid):
    if oid and isinstance(oid, str):
        return oid.lstrip('#')
    return oid

# 1. Process Active Cases
# We need to know:
# - Who owned it (for qualification count)
# - Is it closed in window? (for AHT)
# - Is it transferred? (for AHT)
# - Duration (for AHT)

active_case_map = {}
for c in active_cases_raw:
    cid = clean_id(c['id'])
    
    # Check if closed in window
    # Filter: closeddate >= '2023-05-02' AND closeddate <= '2023-09-02'
    # The query `createddate <= '2023-09-02' AND (closeddate >= '2023-05-02' OR closeddate IS NULL)`
    # includes cases closed after 2023-09-02? No, `closeddate >= ...` is unbounded upper.
    # But `createddate <= ...` bounds creation.
    # Handle Time needs closed cases within the "past four months".
    # Assume closeddate must be <= 2023-09-02 for the AHT calculation.
    
    is_closed_in_window = False
    duration = None
    
    if c['closeddate'] and c['closeddate'] != 'None':
        closed = pd.to_datetime(c['closeddate'])
        if closed <= pd.Timestamp('2023-09-02', tz='UTC') and closed >= pd.Timestamp('2023-05-02', tz='UTC'):
            is_closed_in_window = True
            created = pd.to_datetime(c['createddate'])
            duration = (closed - created).total_seconds()
            
    active_case_map[cid] = {
        'owners': set(),
        'current_owner': clean_id(c['ownerid']),
        'is_closed_in_window': is_closed_in_window,
        'duration': duration,
        'assignments': 0
    }

# 2. Map History to Cases
owner_assignments = [h for h in history if h['field__c'] == 'Owner Assignment']
history_map = {}
for h in owner_assignments:
    cid = clean_id(h['caseid__c'])
    if cid not in history_map:
        history_map[cid] = []
    history_map[cid].append(h)

# 3. Determine Owners and Transfer Status
for cid, info in active_case_map.items():
    assignments = history_map.get(cid, [])
    info['assignments'] = len(assignments)
    
    # Owners from history
    for h in assignments:
        if h.get('newvalue__c'):
            info['owners'].add(clean_id(h['newvalue__c']))
            
    # Always add current owner (fallback or consistency)
    info['owners'].add(info['current_owner'])
    
    # Transfer Status
    # Rule: "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    # If assignments == 1 -> Non-Transferred.
    # If assignments == 0 -> Assume Non-Transferred (Only current owner known).
    # If assignments > 1 -> Transferred.
    
    if info['assignments'] > 1:
        info['is_transferred'] = True
    else:
        info['is_transferred'] = False

# 4. Aggregate by Agent
agent_stats = {}

for cid, info in active_case_map.items():
    # For Qualification: All owners of this Active Case get +1 count
    for owner in info['owners']:
        if owner not in agent_stats:
            agent_stats[owner] = {'case_count': 0, 'durations': []}
        agent_stats[owner]['case_count'] += 1
        
    # For AHT: Only attribute to owner if Closed in Window AND Non-Transferred
    if info['is_closed_in_window'] and not info['is_transferred']:
        # Single owner
        owner = info['current_owner']
        # Double check owner is in stats (it should be from loop above)
        if owner in agent_stats:
            agent_stats[owner]['durations'].append(info['duration'])

# 5. Filter and Find Min
qualified_agents = []
for agent, stats in agent_stats.items():
    if stats['case_count'] > 1:
        # Check if they have measurable handle time
        if len(stats['durations']) > 0:
            avg = sum(stats['durations']) / len(stats['durations'])
            qualified_agents.append({
                'agent': agent,
                'avg_time': avg,
                'count': stats['case_count']
            })

qualified_agents.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(qualified_agents))"""

env_args = {'var_function-call-13068910769840781709': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-1417980459216219882': [{'count': '7'}], 'var_function-call-1417980459216218149': [{'count': '165'}], 'var_function-call-10460115554179369151': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-10460115554179367206': 'file_storage/function-call-10460115554179367206.json', 'var_function-call-10832968714057640408': [], 'var_function-call-15123414602789126229': {'500Wt00000DDepmIAD': {'owners': ['005Wt000003NJufIAG'], 'assignments': 1, 'current': '005Wt000003NJufIAG'}, '500Wt00000DDyzpIAD': {'owners': ['005Wt000003NJGLIA4'], 'assignments': 1, 'current': '005Wt000003NJGLIA4'}, '500Wt00000DDzUPIA1': {'owners': ['005Wt000003NDqDIAW'], 'assignments': 1, 'current': '005Wt000003NDqDIAW'}, '500Wt00000DDzsbIAD': {'owners': ['005Wt000003NJD9IAO'], 'assignments': 1, 'current': '005Wt000003NJD9IAO'}, '500Wt00000DDzscIAD': {'owners': ['005Wt000003NEtOIAW'], 'assignments': 1, 'current': '005Wt000003NEtOIAW'}, '500Wt00000DDzuEIAT': {'owners': ['005Wt000003NJJaIAO'], 'assignments': 1, 'current': '005Wt000003NJJaIAO'}, '500Wt00000DE02HIAT': {'owners': ['005Wt000003NIddIAG'], 'assignments': 1, 'current': '005Wt000003NIddIAG'}}, 'var_function-call-825315341004275369': 'file_storage/function-call-825315341004275369.json'}

exec(code, env_args)
