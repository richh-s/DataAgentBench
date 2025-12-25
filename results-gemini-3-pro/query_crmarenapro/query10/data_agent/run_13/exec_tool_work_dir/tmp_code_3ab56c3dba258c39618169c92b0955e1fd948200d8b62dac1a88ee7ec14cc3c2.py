code = """import json
import pandas as pd
from datetime import datetime, timezone

# Load cases
cases_file = locals()['var_function-call-682345438020800525']
with open(cases_file, 'r') as f:
    cases_data = json.load(f)

# Load history
history_file = locals()['var_function-call-4362075390909810117']
with open(history_file, 'r') as f:
    history_data = json.load(f)

# Dates
# Window: 2023-05-02 to 2023-09-02
start_date = pd.Timestamp("2023-05-02", tz="UTC")
end_date = pd.Timestamp("2023-09-02", tz="UTC")
# Note: Data dates have timezone info (+0000). pd.to_datetime handles it.
# We should ensure start/end are timezone aware.

def clean_id(i):
    if not i or str(i).lower() == 'none':
        return None
    return str(i).strip().lstrip('#')

def parse_date(d):
    if not d or str(d).lower() == 'none':
        return None
    try:
        dt = pd.to_datetime(d)
        if dt.tzinfo is None:
            dt = dt.tz_localize('UTC')
        return dt
    except:
        return None

# Process Cases
# We need to map case_id to its involved agents.
# First, identify active cases and closed cases.
active_cases = [] # IDs
closed_cases = [] # (ID, Owner, Duration)

# Also create a map of case_id -> final_owner for all cases, to help history processing
case_final_owners = {}

for c in cases_data:
    cid = clean_id(c['id'])
    if not cid: continue
    
    owner = clean_id(c['ownerid'])
    created = parse_date(c['createddate'])
    closed = parse_date(c['closeddate'])
    
    case_final_owners[cid] = owner
    
    if not created: continue # Should have created date
    
    # Check Active in Window
    # Created <= End Date AND (Closed is None OR Closed >= Start Date)
    is_active = False
    if created <= end_date:
        if closed is None:
            is_active = True
        elif closed >= start_date:
            is_active = True
    
    if is_active:
        active_cases.append(cid)
    
    # Check Closed in Window (for handle time)
    # Closed between Start and End
    if closed and closed >= start_date and closed <= end_date:
        duration = (closed - created).total_seconds()
        closed_cases.append({
            'id': cid,
            'owner': owner,
            'duration': duration
        })

# Map case_id -> set of agents
# Initialize with final owner for all active cases (we only care about active cases for "processed" count)
# Actually, if an agent processed a case that is NOT active in the window, does it count?
# "Processing more than one case" - implies in the period.
# I will restrict "processed count" to cases active in the window.
case_agents = {cid: set() for cid in active_cases}

# Add final owners
for cid in active_cases:
    owner = case_final_owners.get(cid)
    if owner:
        case_agents[cid].add(owner)

# Add history owners
active_cases_set = set(active_cases)
for h in history_data:
    hcid = clean_id(h['caseid__c'])
    if hcid in active_cases_set:
        old = clean_id(h['oldvalue__c'])
        new = clean_id(h['newvalue__c'])
        if old: case_agents[hcid].add(old)
        if new: case_agents[hcid].add(new)

# Aggregate Stats
agent_stats = {}

# 1. Processed Count
for cid, agents in case_agents.items():
    for agent in agents:
        if agent not in agent_stats:
            agent_stats[agent] = {'processed_count': 0, 'total_time': 0.0, 'closed_count': 0}
        agent_stats[agent]['processed_count'] += 1

# 2. Handle Time (from closed_cases)
for c in closed_cases:
    owner = c['owner']
    # Owner might not be in stats if they weren't in active_cases involved list?
    # If case is closed in window, it IS active in window. So it should be there.
    if owner:
        if owner not in agent_stats:
             agent_stats[owner] = {'processed_count': 0, 'total_time': 0.0, 'closed_count': 0}
        
        agent_stats[owner]['total_time'] += c['duration']
        agent_stats[owner]['closed_count'] += 1

# Filter and Find Lowest
results = []
for agent, stats in agent_stats.items():
    if stats['processed_count'] > 1 and stats['closed_count'] > 0:
        avg = stats['total_time'] / stats['closed_count']
        results.append({
            'agent': agent,
            'avg_time': avg,
            'processed': stats['processed_count'],
            'closed': stats['closed_count']
        })

results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13889925607589652212': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-4362075390909812662': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-4362075390909810117': 'file_storage/function-call-4362075390909810117.json', 'var_function-call-11505706217797150176': [], 'var_function-call-5544576152632122422': [{'count': '153'}], 'var_function-call-682345438020800525': 'file_storage/function-call-682345438020800525.json'}

exec(code, env_args)
