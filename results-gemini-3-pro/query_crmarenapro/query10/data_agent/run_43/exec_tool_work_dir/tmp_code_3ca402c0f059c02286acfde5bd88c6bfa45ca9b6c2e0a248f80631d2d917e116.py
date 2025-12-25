code = """import json
import pandas as pd

cases_raw = locals()['var_function-call-10575199339099937418']
history_path = locals()['var_function-call-10575199339099937077']

with open(history_path, 'r') as f:
    history_raw = json.load(f)

def clean_id(x):
    if not isinstance(x, str): return str(x)
    x = x.strip()
    if x.startswith('#'): return x[1:]
    return x

# Process History
# Group by case_id
# Count "Owner Assignment" rows
# Collect involved agents
case_history_meta = {} # case_id -> {'count': int, 'agents': set}

for h in history_raw:
    cid = clean_id(h.get('caseid__c'))
    field = h.get('field__c')
    if field == 'Owner Assignment':
        if cid not in case_history_meta:
            case_history_meta[cid] = {'count': 0, 'agents': set()}
        case_history_meta[cid]['count'] += 1
        val = clean_id(h.get('newvalue__c'))
        if val:
            case_history_meta[cid]['agents'].add(val)

# Process Cases
agent_stats = {} # agent_id -> {'processed': 0, 'durations': []}

valid_cases_debug = []

for c in cases_raw:
    cid = clean_id(c.get('id'))
    oid = clean_id(c.get('ownerid'))
    created = c.get('createddate')
    closed = c.get('closeddate')
    
    if not (created and closed): continue
    
    # Date Filter
    closed_dt = pd.to_datetime(closed, utc=True)
    created_dt = pd.to_datetime(created, utc=True)
    
    # 2023-05-02 to 2023-09-02 (inclusive end?)
    # "In the past four months" usually [Start, End].
    # I'll use strictly < 2023-09-03 to include 09-02.
    if not (closed_dt >= pd.Timestamp('2023-05-02', tz='UTC') and closed_dt < pd.Timestamp('2023-09-03', tz='UTC')):
        continue
        
    # Get History Meta
    meta = case_history_meta.get(cid)
    
    involved_agents = set()
    assignment_count = 0
    
    if meta:
        involved_agents = meta['agents']
        assignment_count = meta['count']
    
    # Ensure current owner is in involved (sometimes history lags or is missing)
    involved_agents.add(oid)
    
    # If no history records found?
    # Policy says "there will be only ONE". So if 0 found, it violates policy description?
    # Or maybe "Case Creation" isn't "Owner Assignment".
    # If I see 0 "Owner Assignment" rows, is it count=1 (implicit) or count=0?
    # If I assume "ONE 'Owner Assignment'" is literal, then cases with 0 are problematic.
    # But checking the snippet:
    # Case `500Wt00000DDTEQIA5` -> Snippet has "Case Creation" but NO "Owner Assignment".
    # It has an owner `005Wt000003NJufIAG`. (From query 1? No, query 1 result doesn't show this ID in snippet).
    # Wait, the snippet of cases in previous turn:
    # `500Wt00000DDepmIAD` (Owner `005Wt000003NJufIAG`).
    # Check history for `500Wt00000DDepmIAD`:
    # In history snippet: `{"caseid__c": "500Wt00000DDepmIAD", "newvalue__c": "005Wt000003NJufIAG", "field__c": "Owner Assignment"}`.
    # Ah! So it IS there.
    # So valid cases SHOULD have entries.
    
    # Update Processed Count
    for ag in involved_agents:
        if ag not in agent_stats: agent_stats[ag] = {'processed': 0, 'durations': []}
        agent_stats[ag]['processed'] += 1
        
    # Handle Time Logic
    # "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    # So if count == 1: Calculate Duration. Assign to Owner.
    if assignment_count == 1:
        duration = (closed_dt - created_dt).total_seconds()
        # Assign to whom? The single owner.
        # Check if involved_agents has 1 item.
        # Ideally yes.
        # But involved_agents collects from history + current owner.
        # If history has 1 entry "Owner X", and current is "Owner X", set is {X}.
        for ag in involved_agents:
            agent_stats[ag]['durations'].append(duration)
            
    valid_cases_debug.append({
        'id': cid,
        'count': assignment_count,
        'involved': list(involved_agents)
    })

# Compute Results
final_list = []
for ag, stats in agent_stats.items():
    if stats['processed'] > 1:
        if stats['durations']:
            avg = sum(stats['durations']) / len(stats['durations'])
            final_list.append({'agent': ag, 'avg': avg, 'count': stats['processed']})

final_list.sort(key=lambda x: x['avg'])

print("__RESULT__:")
print(json.dumps({
    "candidates": final_list,
    "debug_cases": valid_cases_debug
}))"""

env_args = {'var_function-call-12130681138560027796': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12130681138560028065': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-13890973844187730133': [{'count': '165'}], 'var_function-call-10575199339099937418': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10575199339099937077': 'file_storage/function-call-10575199339099937077.json', 'var_function-call-1852491156045732706': None, 'var_function-call-15218986620377312517': {'total_cases_in_range': 7, 'cases_with_history': 7, 'sample_case_ids': ['500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzuEIAT', '500Wt00000DDzsbIAD', '500Wt00000DDepmIAD'], 'sample_hist_ids': ['500Wt00000DDPZ0IAP', '500Wt00000DDDtTIAX', '500Wt00000DDet1IAD', '500Wt00000DDzhJIAT', '500Wt00000DDyRvIAL']}, 'var_function-call-6272773224045968043': [{'count': '153'}]}

exec(code, env_args)
