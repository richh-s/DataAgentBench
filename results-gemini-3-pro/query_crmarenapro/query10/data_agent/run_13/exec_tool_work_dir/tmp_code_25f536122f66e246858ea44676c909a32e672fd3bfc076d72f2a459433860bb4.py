code = """import json
import pandas as pd
from datetime import datetime

# Load cases
cases_data = locals()['var_function-call-4362075390909812662']
# Load history
history_file = locals()['var_function-call-4362075390909810117']
with open(history_file, 'r') as f:
    history_data = json.load(f)

# Helper to clean IDs
def clean_id(i):
    if not i:
        return ""
    return str(i).strip().lstrip('#')

# Parse dates
def parse_date(d):
    # Format: 2023-07-01T10:30:00.000+0000
    # Python 3.11+ supports fromisoformat for this, but safer to use strptime or simple parsing
    # The timezone part +0000 might need handling.
    # We can use pd.to_datetime
    return pd.to_datetime(d)

# Process Cases
cases = []
target_case_ids = set()
for c in cases_data:
    cid = clean_id(c['id'])
    target_case_ids.add(cid)
    
    # Calculate duration
    created = parse_date(c['createddate'])
    closed = parse_date(c['closeddate'])
    duration = (closed - created).total_seconds() # in seconds
    
    cases.append({
        'clean_id': cid,
        'final_owner': clean_id(c['ownerid']),
        'duration': duration,
        'raw': c
    })

# Process History
# Map case_id -> set of involved agents
case_agents = {cid: set() for cid in target_case_ids}

# Initialize with final owner (they are involved)
for c in cases:
    case_agents[c['clean_id']].add(c['final_owner'])

# Go through history
for h in history_data:
    hcid = clean_id(h['caseid__c'])
    if hcid in target_case_ids:
        old = clean_id(h['oldvalue__c'])
        new = clean_id(h['newvalue__c'])
        # If value is 'None' or empty, ignore? 
        # Actually 'None' string might be present.
        if old and old.lower() != 'none':
            case_agents[hcid].add(old)
        if new and new.lower() != 'none':
            case_agents[hcid].add(new)

# Calculate metrics per agent
agent_stats = {} 
# structure: {agent_id: {'processed_cases': set(), 'owned_closed_cases': 0, 'total_handle_time': 0.0}}

# 1. Populate processed cases
for cid, agents in case_agents.items():
    for agent in agents:
        if agent not in agent_stats:
            agent_stats[agent] = {'processed_cases': set(), 'owned_closed_cases': 0, 'total_handle_time': 0.0}
        agent_stats[agent]['processed_cases'].add(cid)

# 2. Populate handle time stats (only for final owner)
for c in cases:
    owner = c['final_owner']
    if owner not in agent_stats:
        # Should be there from step 1, but just in case
        agent_stats[owner] = {'processed_cases': set(), 'owned_closed_cases': 0, 'total_handle_time': 0.0}
        agent_stats[owner]['processed_cases'].add(c['clean_id'])
    
    agent_stats[owner]['owned_closed_cases'] += 1
    agent_stats[owner]['total_handle_time'] += c['duration']

# Filter and find lowest average
eligible_agents = []

for agent, stats in agent_stats.items():
    processed_count = len(stats['processed_cases'])
    if processed_count > 1:
        if stats['owned_closed_cases'] > 0:
            avg_time = stats['total_handle_time'] / stats['owned_closed_cases']
            eligible_agents.append({
                'agent_id': agent,
                'avg_time': avg_time,
                'processed': processed_count,
                'owned': stats['owned_closed_cases']
            })

# Sort by avg_time
eligible_agents.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(eligible_agents))"""

env_args = {'var_function-call-13889925607589652212': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-4362075390909812662': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-4362075390909810117': 'file_storage/function-call-4362075390909810117.json'}

exec(code, env_args)
