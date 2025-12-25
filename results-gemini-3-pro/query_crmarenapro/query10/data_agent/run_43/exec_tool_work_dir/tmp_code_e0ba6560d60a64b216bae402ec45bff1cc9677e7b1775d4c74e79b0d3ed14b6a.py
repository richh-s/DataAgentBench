code = """import json
import pandas as pd
from datetime import datetime

# Load data
cases_raw = locals()['var_function-call-10575199339099937418']
history_path = locals()['var_function-call-10575199339099937077']

with open(history_path, 'r') as f:
    history_raw = json.load(f)

# Helper to clean IDs
def clean_id(x):
    if not isinstance(x, str):
        return str(x)
    x = x.strip()
    if x.startswith('#'):
        return x[1:]
    return x

# Prepare Cases
cases = []
for c in cases_raw:
    cid = clean_id(c.get('id'))
    oid = clean_id(c.get('ownerid'))
    created = c.get('createddate')
    closed = c.get('closeddate')
    
    if created and closed:
        cases.append({
            'id': cid,
            'ownerid': oid,
            'created': created,
            'closed': closed
        })

df_cases = pd.DataFrame(cases)
df_cases['closed_dt'] = pd.to_datetime(df_cases['closed'], utc=True)
df_cases['created_dt'] = pd.to_datetime(df_cases['created'], utc=True)

# Filter by date range: 2023-05-02 to 2023-09-02
start_date = pd.Timestamp('2023-05-02', tz='UTC')
end_date = pd.Timestamp('2023-09-03', tz='UTC') # Exclusive of 09-03 means inclusive of 09-02
# "Past four months" from 2023-09-02 is 2023-05-02.

df_cases = df_cases[(df_cases['closed_dt'] >= start_date) & (df_cases['closed_dt'] < end_date)]

# Prepare History
# Filter history for field 'Owner Assignment' (already done in query but good to be safe if reused)
# Clean IDs
history_map = {} # case_id -> list of agent_ids
history_counts = {} # case_id -> count of assignments

for h in history_raw:
    cid = clean_id(h.get('caseid__c'))
    agent_id = clean_id(h.get('newvalue__c'))
    
    if cid not in history_map:
        history_map[cid] = []
        history_counts[cid] = 0
    
    if agent_id:
        history_map[cid].append(agent_id)
    history_counts[cid] += 1

# Process
agent_case_counts = {} # agent_id -> count of processed cases
agent_handle_times = {} # agent_id -> list of durations in seconds

for idx, row in df_cases.iterrows():
    cid = row['id']
    
    # Get agents involved
    # If case not in history, fallback to current owner and count=1?
    # Policy: "For cases that have NOT been transferred... there will be only ONE 'Owner Assignment'"
    # If missing from history, it might be data incompleteness. 
    # But I must follow the data I have.
    # If no history, I'll assume 1 assignment (the current owner) if that seems reasonable?
    # Or strict: if not in history, I don't know the assignments.
    # Given "corruption", relying on `ownerid` + history is safer.
    
    involved_agents = set()
    assignment_count = 0
    
    if cid in history_map:
        involved_agents.update(history_map[cid])
        assignment_count = history_counts[cid]
    else:
        # Fallback: assume the current owner is the only one
        # This handles cases where "Owner Assignment" event wasn't captured or query limited
        # But my query captured ALL 'Owner Assignment' events.
        # If a case exists but no assignment record, maybe it was created and never assigned? (Unlikely if closed)
        # Or maybe "Case Creation" sets the owner but doesn't log "Owner Assignment"?
        # Let's check the snippet. Case `500Wt00000DDTEQIA5` has "Case Creation" but no "Owner Assignment".
        # It has `ownerid`. 
        # I will assume: If no "Owner Assignment" record, count = 1 (Original Owner).
        # If there are records, use them.
        involved_agents.add(row['ownerid'])
        assignment_count = max(assignment_count, 1) # If 0 history, count as 1.

    # Update Processed Counts
    for ag in involved_agents:
        agent_case_counts[ag] = agent_case_counts.get(ag, 0) + 1
        
    # Handle Time Calculation
    # Only if assignment_count == 1
    # Who gets the credit? The single agent.
    if assignment_count == 1:
        # Calculate duration
        duration = (row['closed_dt'] - row['created_dt']).total_seconds()
        if duration < 0: continue # Sanity check
        
        # The agent is the one in involved_agents (should be size 1)
        # If size > 1 but count == 1? (Data inconsistency).
        # Just iterate involved_agents
        for ag in involved_agents:
            if ag not in agent_handle_times:
                agent_handle_times[ag] = []
            agent_handle_times[ag].append(duration)

# Calculate Stats
results = []
for agent, count in agent_case_counts.items():
    if count > 1:
        times = agent_handle_times.get(agent, [])
        if times:
            avg_time = sum(times) / len(times)
            results.append({
                'agent': agent,
                'avg_time': avg_time,
                'case_count': count
            })

# Sort by avg_time
results.sort(key=lambda x: x['avg_time'])

if results:
    best_agent = results[0]['agent']
else:
    best_agent = None

print("__RESULT__:")
print(json.dumps(best_agent))"""

env_args = {'var_function-call-12130681138560027796': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12130681138560028065': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-13890973844187730133': [{'count': '165'}], 'var_function-call-10575199339099937418': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10575199339099937077': 'file_storage/function-call-10575199339099937077.json'}

exec(code, env_args)
