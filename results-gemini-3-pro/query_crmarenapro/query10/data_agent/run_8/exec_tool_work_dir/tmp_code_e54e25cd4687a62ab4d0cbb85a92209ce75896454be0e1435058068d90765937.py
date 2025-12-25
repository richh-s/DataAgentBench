code = """import json
import pandas as pd
from datetime import datetime

# Load data
cases = locals()['var_function-call-15813525106352124259']
history_path = locals()['var_function-call-1992848873889521844']
total_counts_raw = locals()['var_function-call-17157627302662119840']

with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(x):
    if not isinstance(x, str):
        return x
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Process Total Counts
agent_total_counts = {}
for entry in total_counts_raw:
    aid = clean_id(entry['ownerid'])
    count = int(entry['total_cases'])
    agent_total_counts[aid] = agent_total_counts.get(aid, 0) + count

# Process History Counts
owner_counts = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    owner_counts[cid] = owner_counts.get(cid, 0) + 1

# Process Cases
agent_durations = {}

for c in cases:
    cid = clean_id(c['id'])
    aid = clean_id(c['ownerid'])
    
    # Check if transferred
    # Count owner assignment events
    # If not in history, assume 1? (Or 0? 0 means no record, maybe not transferred? But earlier analysis said 165 records and 7 cases matches sample).
    # All sampled cases had history.
    
    cnt = owner_counts.get(cid, 0)
    if cnt > 1:
        # Transferred, exclude from handle time
        continue
    
    # Calculate duration
    try:
        created = datetime.strptime(c['createddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
        closed = datetime.strptime(c['closeddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        created = datetime.strptime(c['createddate'].split('.')[0] + "+0000", "%Y-%m-%dT%H:%M:%S%z")
        closed = datetime.strptime(c['closeddate'].split('.')[0] + "+0000", "%Y-%m-%dT%H:%M:%S%z")
    
    duration = (closed - created).total_seconds()
    
    if aid not in agent_durations:
        agent_durations[aid] = []
    agent_durations[aid].append(duration)

# Calculate Averages and Filter
results = []
for agent, durations in agent_durations.items():
    # Filter: processing more than one case (Total Count > 1)
    total_processed = agent_total_counts.get(agent, 0)
    
    if total_processed <= 1:
        continue
        
    avg_time = sum(durations) / len(durations)
    results.append({'agent': agent, 'avg_time': avg_time})

# Find best
if not results:
    final_result = "No qualifying agents"
else:
    best = min(results, key=lambda x: x['avg_time'])
    final_result = best['agent']

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-14838987602196373344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8892615390852284541': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-14093882633430532867': [{'count': '165'}], 'var_function-call-15813525106352124259': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-1992848873889521844': 'file_storage/function-call-1992848873889521844.json', 'var_function-call-6551131518112016470': 'No qualifying agents', 'var_function-call-3479205796434553846': 'Done', 'var_function-call-13496426400625874618': {'agent_counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}, 'owner_counts_sample': {'500Wt00000DDzpNIAT': 1, '500Wt00000DDfHCIA1': 1, '500Wt00000DDZ0VIAX': 1, '500Wt00000DDQoUIAX': 1, '500Wt00000DDzm9IAD': 1}, 'agent_details': []}, 'var_function-call-17157627302662119840': [{'ownerid': '005Wt000003NIvNIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NIc3IAG', 'total_cases': '2'}, {'ownerid': '#005Wt000003NF1SIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NIAcIAO', 'total_cases': '1'}, {'ownerid': '#005Wt000003NFr4IAG', 'total_cases': '2'}, {'ownerid': '005Wt000003NIYnIAO', 'total_cases': '2'}, {'ownerid': '#005Wt000003NI90IAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NJ6fIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NIDqIAO', 'total_cases': '1'}, {'ownerid': '005Wt000003NFKpIAO', 'total_cases': '2'}, {'ownerid': '#005Wt000003NH3GIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NHuUIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NJrRIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NJ6gIAG', 'total_cases': '2'}, {'ownerid': '005Wt000003NIVZIA4', 'total_cases': '2'}, {'ownerid': '#005Wt000003NEzqIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NDu7IAG', 'total_cases': '2'}, {'ownerid': '005Wt000003NInJIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NHpeIAG', 'total_cases': '2'}, {'ownerid': '005Wt000003NJD9IAO', 'total_cases': '2'}, {'ownerid': '005Wt000003NJ3RIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NHsrIAG', 'total_cases': '2'}, {'ownerid': '#005Wt000003NJbJIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NJcvIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NJhlIAG', 'total_cases': '4'}, {'ownerid': '005Wt000003NJTFIA4', 'total_cases': '2'}, {'ownerid': '#005Wt000003NJeXIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NFhOIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NDu7IAG', 'total_cases': '1'}, {'ownerid': '#005Wt000003NJ0DIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NIXBIA4', 'total_cases': '2'}, {'ownerid': '005Wt000003NJLBIA4', 'total_cases': '2'}, {'ownerid': '005Wt000003NH3GIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NEtOIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NFKoIAO', 'total_cases': '2'}, {'ownerid': '005Wt000003NFW6IAO', 'total_cases': '2'}, {'ownerid': '005Wt000003NI5mIAG', 'total_cases': '3'}, {'ownerid': '#005Wt000003NBcAIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NGjuIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NGjuIAG', 'total_cases': '1'}, {'ownerid': '#005Wt000003NINVIA4', 'total_cases': '1'}, {'ownerid': '005Wt000003NJcwIAG', 'total_cases': '1'}, {'ownerid': '#005Wt000003NJhlIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NDJ1IAO', 'total_cases': '1'}, {'ownerid': '005Wt000003NJcvIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NEtOIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NJGLIA4', 'total_cases': '2'}, {'ownerid': '005Wt000003NIwzIAG', 'total_cases': '2'}, {'ownerid': '005Wt000003NJzVIAW', 'total_cases': '2'}, {'ownerid': '#005Wt000003NIfHIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NFKoIAO', 'total_cases': '2'}, {'ownerid': '005Wt000003NJWTIA4', 'total_cases': '1'}, {'ownerid': '005Wt000003NEGhIAO', 'total_cases': '1'}, {'ownerid': '005Wt000003NIliIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NBcAIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NIaQIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NGwpIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NDXZIA4', 'total_cases': '1'}, {'ownerid': '005Wt000003NJufIAG', 'total_cases': '2'}, {'ownerid': '005Wt000003NDqDIAW', 'total_cases': '3'}, {'ownerid': '#005Wt000003NDqEIAW', 'total_cases': '2'}, {'ownerid': '005Wt000003NBykIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NJoDIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NIfFIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NJ9tIAG', 'total_cases': '2'}, {'ownerid': '005Wt000003NHfzIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NI2XIAW', 'total_cases': '2'}, {'ownerid': '005Wt000003NIc2IAG', 'total_cases': '1'}, {'ownerid': '#005Wt000003NIYnIAO', 'total_cases': '1'}, {'ownerid': '005Wt000003NEdKIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NIvNIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NJeXIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NIk5IAG', 'total_cases': '2'}, {'ownerid': '#005Wt000003NJEjIAO', 'total_cases': '2'}, {'ownerid': '#005Wt000003NJWTIA4', 'total_cases': '1'}, {'ownerid': '005Wt000003NJ0DIAW', 'total_cases': '3'}, {'ownerid': '005Wt000003NJ8HIAW', 'total_cases': '4'}, {'ownerid': '005Wt000003NJppIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NHuUIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NInLIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NJUrIAO', 'total_cases': '1'}, {'ownerid': '#005Wt000003NIDqIAO', 'total_cases': '1'}, {'ownerid': '005Wt000003NJJaIAO', 'total_cases': '4'}, {'ownerid': '005Wt000003NJbJIAW', 'total_cases': '2'}, {'ownerid': '005Wt000003NDsUIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NINVIA4', 'total_cases': '3'}, {'ownerid': '005Wt000003NHfyIAG', 'total_cases': '1'}, {'ownerid': '005Wt000003NHGAIA4', 'total_cases': '2'}, {'ownerid': '005Wt000003NIddIAG', 'total_cases': '4'}, {'ownerid': '005Wt000003NIk7IAG', 'total_cases': '4'}, {'ownerid': '005Wt000003NIfFIAW', 'total_cases': '1'}, {'ownerid': '#005Wt000003NEGhIAO', 'total_cases': '1'}, {'ownerid': '005Wt000003NJ6gIAG', 'total_cases': '4'}, {'ownerid': '005Wt000003NDqFIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NItlIAG', 'total_cases': '1'}, {'ownerid': '#005Wt000003NHpeIAG', 'total_cases': '1'}, {'ownerid': '#005Wt000003NJoDIAW', 'total_cases': '1'}, {'ownerid': '005Wt000003NISLIA4', 'total_cases': '2'}, {'ownerid': '#005Wt000003NJQ1IAO', 'total_cases': '1'}]}

exec(code, env_args)
