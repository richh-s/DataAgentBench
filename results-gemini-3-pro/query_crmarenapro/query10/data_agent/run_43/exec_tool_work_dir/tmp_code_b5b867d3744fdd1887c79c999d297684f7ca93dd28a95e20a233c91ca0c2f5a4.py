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
case_history_meta = {} # case_id -> {'count': int, 'agents': set}

for h in history_raw:
    cid = clean_id(h.get('caseid__c'))
    # All rows are Owner Assignment
    if cid not in case_history_meta:
        case_history_meta[cid] = {'count': 0, 'agents': set()}
    case_history_meta[cid]['count'] += 1
    val = clean_id(h.get('newvalue__c'))
    if val:
        case_history_meta[cid]['agents'].add(val)

# Process Cases
agent_stats = {} # agent_id -> {'processed': 0, 'durations': []}
debug_list = []

for c in cases_raw:
    cid = clean_id(c.get('id'))
    oid = clean_id(c.get('ownerid'))
    created = c.get('createddate')
    closed = c.get('closeddate')
    
    if not (created and closed): continue
    
    closed_dt = pd.to_datetime(closed, utc=True)
    created_dt = pd.to_datetime(created, utc=True)
    
    # Strict Date Filter
    # Cases closed in past 4 months
    start = pd.Timestamp('2023-05-02', tz='UTC')
    end = pd.Timestamp('2023-09-03', tz='UTC')
    if not (closed_dt >= start and closed_dt < end):
        continue
        
    meta = case_history_meta.get(cid)
    
    involved_agents = set()
    assignment_count = 0
    
    if meta:
        involved_agents = meta['agents']
        assignment_count = meta['count']
    
    involved_agents.add(oid)
    
    # Stats
    for ag in involved_agents:
        if ag not in agent_stats: agent_stats[ag] = {'processed': 0, 'durations': []}
        agent_stats[ag]['processed'] += 1
        
    # Handle Time
    # "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    # If assignment_count == 1: valid.
    # If assignment_count == 0? (Should not happen if policy holds and data is clean).
    # If it happens, let's log it.
    
    if assignment_count == 1:
        duration = (closed_dt - created_dt).total_seconds()
        # Assign to the single owner
        # If involved_agents has > 1 (e.g. history says X, ownerid says Y?), then data issue.
        # But normally {X}.
        for ag in involved_agents:
            agent_stats[ag]['durations'].append(duration)
            
    debug_list.append({'id': cid, 'count': assignment_count, 'involved': list(involved_agents)})

# Result
candidates = []
for ag, stats in agent_stats.items():
    if stats['processed'] > 1:
        if stats['durations']:
            avg = sum(stats['durations']) / len(stats['durations'])
            candidates.append({'agent': ag, 'avg': avg})
        else:
            # processed > 1 but no valid handle time cases (all transferred)
            # Should we ignore? "lowest average handle time".
            # If no handle time, can't compare.
            pass

candidates.sort(key=lambda x: x['avg'])

print("__RESULT__:")
print(json.dumps({
    "best": candidates[0]['agent'] if candidates else None,
    "candidates": candidates,
    "debug": debug_list
}))"""

env_args = {'var_function-call-12130681138560027796': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12130681138560028065': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-13890973844187730133': [{'count': '165'}], 'var_function-call-10575199339099937418': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10575199339099937077': 'file_storage/function-call-10575199339099937077.json', 'var_function-call-1852491156045732706': None, 'var_function-call-15218986620377312517': {'total_cases_in_range': 7, 'cases_with_history': 7, 'sample_case_ids': ['500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzuEIAT', '500Wt00000DDzsbIAD', '500Wt00000DDepmIAD'], 'sample_hist_ids': ['500Wt00000DDPZ0IAP', '500Wt00000DDDtTIAX', '500Wt00000DDet1IAD', '500Wt00000DDzhJIAT', '500Wt00000DDyRvIAL']}, 'var_function-call-6272773224045968043': [{'count': '153'}], 'var_function-call-499108039320783181': {'candidates': [], 'debug_cases': [{'id': '500Wt00000DDepmIAD', 'count': 0, 'involved': ['005Wt000003NJufIAG']}, {'id': '500Wt00000DDyzpIAD', 'count': 0, 'involved': ['005Wt000003NJGLIA4']}, {'id': '500Wt00000DDzUPIA1', 'count': 0, 'involved': ['005Wt000003NDqDIAW']}, {'id': '500Wt00000DDzsbIAD', 'count': 0, 'involved': ['005Wt000003NJD9IAO']}, {'id': '500Wt00000DDzscIAD', 'count': 0, 'involved': ['005Wt000003NEtOIAW']}, {'id': '500Wt00000DDzuEIAT', 'count': 0, 'involved': ['005Wt000003NJJaIAO']}, {'id': '500Wt00000DE02HIAT', 'count': 0, 'involved': ['005Wt000003NIddIAG']}]}, 'var_function-call-3757333494456036275': [None]}

exec(code, env_args)
