code = """import json
import pandas as pd
from datetime import datetime

# Load data
cases = locals()['var_function-call-15813525106352124259']
history_path = locals()['var_function-call-1992848873889521844']

with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(x):
    if not isinstance(x, str):
        return x
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Debug stats
print("Total Cases:", len(cases))
print("Total History Entries:", len(history))

# Check ID cleaning
cleaned_cases = []
for c in cases:
    c['id'] = clean_id(c['id'])
    c['ownerid'] = clean_id(c['ownerid'])
    cleaned_cases.append(c)

owner_counts = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    owner_counts[cid] = owner_counts.get(cid, 0) + 1

# Check overlap
case_ids = set(c['id'] for c in cleaned_cases)
hist_ids = set(owner_counts.keys())
overlap = case_ids.intersection(hist_ids)
print("Cases with History:", len(overlap))
print("Sample Owner Counts:", list(owner_counts.items())[:5])

# Agent stats
agent_counts = {}
for c in cleaned_cases:
    aid = c['ownerid']
    agent_counts[aid] = agent_counts.get(aid, 0) + 1

print("Agent Case Counts:", agent_counts)

# Check why no qualifying agents
# Loop again and print decision
metrics = []
for agent, count in agent_counts.items():
    if count <= 1:
        continue
    
    # Process this agent
    agent_case_list = [c for c in cleaned_cases if c['ownerid'] == agent]
    valid_durations = []
    
    for c in agent_case_list:
        cid = c['id']
        oc = owner_counts.get(cid, 0)
        
        # Logic check
        # If oc > 1 => Transferred
        # If oc <= 1 => Not Transferred
        if oc > 1:
            continue
            
        valid_durations.append(1) # Just count valid cases for now
    
    metrics.append({'agent': agent, 'total': count, 'valid': len(valid_durations)})

print("Agent Metrics:", metrics)

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-14838987602196373344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8892615390852284541': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-14093882633430532867': [{'count': '165'}], 'var_function-call-15813525106352124259': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-1992848873889521844': 'file_storage/function-call-1992848873889521844.json', 'var_function-call-6551131518112016470': 'No qualifying agents'}

exec(code, env_args)
