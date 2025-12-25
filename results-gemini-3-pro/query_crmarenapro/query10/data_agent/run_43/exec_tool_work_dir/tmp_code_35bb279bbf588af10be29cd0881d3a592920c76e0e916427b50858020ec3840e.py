code = """import json
import pandas as pd

cases_path = locals()['var_function-call-17249791054646370202']
history_path = locals()['var_function-call-10575199339099937077']

with open(cases_path, 'r') as f:
    cases_raw = json.load(f)

with open(history_path, 'r') as f:
    history_raw = json.load(f)

def clean_id(x):
    if not isinstance(x, str): return str(x)
    x = x.strip()
    if x.startswith('#'): return x[1:]
    return x

# 1. Process History
case_history_meta = {} # case_id -> {'count': int, 'agents': set}

for h in history_raw:
    cid = clean_id(h.get('caseid__c'))
    if cid not in case_history_meta:
        case_history_meta[cid] = {'count': 0, 'agents': set()}
    case_history_meta[cid]['count'] += 1
    val = clean_id(h.get('newvalue__c'))
    if val:
        case_history_meta[cid]['agents'].add(val)

# 2. Process Cases
processed_counts = {} # agent -> count
handle_times = {} # agent -> list of durations

# Window
today = pd.Timestamp('2023-09-02', tz='UTC') # inclusive? 09-02 end of day? 
# "In the past four months" usually [May 2, Sep 2].
start_date = pd.Timestamp('2023-05-02', tz='UTC')
end_date = pd.Timestamp('2023-09-03', tz='UTC') # Use < 09-03 for inclusive 09-02

for c in cases_raw:
    cid = clean_id(c.get('id'))
    oid = clean_id(c.get('ownerid'))
    created = c.get('createddate')
    closed = c.get('closeddate')
    
    if not created: continue
    created_dt = pd.to_datetime(created, utc=True)
    
    # Check Active in Window (Processed Filter)
    # Active if Created <= End AND (Closed >= Start or Closed is None)
    # Also ignore future cases (Created > Today)?
    # Prompt says "Today's date: 2023-09-02".
    # If case created 2023-09-22, it's in the future. Should not be counted?
    # Yes, normally analytics queries are relative to "Today".
    if created_dt >= end_date:
        continue # Future case
    
    is_closed = False
    closed_dt = None
    if closed and closed != 'None':
        closed_dt = pd.to_datetime(closed, utc=True)
        is_closed = True
    
    # Is Active?
    # Created < End is true.
    # Check Closed
    active = False
    if not is_closed:
        active = True # Open in window (since created < end)
    else:
        # Closed. Was it open during window?
        # It was open from Created to Closed.
        # Overlap with [Start, End]?
        # (Created < End) AND (Closed >= Start)
        if closed_dt >= start_date:
            active = True
    
    # Agents Involved
    involved_agents = set()
    assign_count = 0
    
    if cid in case_history_meta:
        involved_agents = case_history_meta[cid]['agents']
        assign_count = case_history_meta[cid]['count']
    
    involved_agents.add(oid)
    
    if active:
        for ag in involved_agents:
            processed_counts[ag] = processed_counts.get(ag, 0) + 1
            
    # Handle Time Calculation
    # Condition: Closed in Window AND Not Transferred (Count == 1)
    if is_closed:
        # Check closed in window [Start, End)
        if closed_dt >= start_date and closed_dt < end_date:
            if assign_count == 1: # Strict "Not Transferred"
                duration = (closed_dt - created_dt).total_seconds()
                if duration > 0:
                    # Assign to owner (should be single involved agent)
                    for ag in involved_agents:
                        if ag not in handle_times: handle_times[ag] = []
                        handle_times[ag].append(duration)

# 3. Calculate Results
candidates = []
for ag, count in processed_counts.items():
    if count > 1:
        times = handle_times.get(ag, [])
        if times:
            avg = sum(times) / len(times)
            candidates.append({'agent': ag, 'avg': avg, 'count': count})

candidates.sort(key=lambda x: x['avg'])

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-12130681138560027796': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12130681138560028065': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-13890973844187730133': [{'count': '165'}], 'var_function-call-10575199339099937418': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10575199339099937077': 'file_storage/function-call-10575199339099937077.json', 'var_function-call-1852491156045732706': None, 'var_function-call-15218986620377312517': {'total_cases_in_range': 7, 'cases_with_history': 7, 'sample_case_ids': ['500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzuEIAT', '500Wt00000DDzsbIAD', '500Wt00000DDepmIAD'], 'sample_hist_ids': ['500Wt00000DDPZ0IAP', '500Wt00000DDDtTIAX', '500Wt00000DDet1IAD', '500Wt00000DDzhJIAT', '500Wt00000DDyRvIAL']}, 'var_function-call-6272773224045968043': [{'count': '153'}], 'var_function-call-499108039320783181': {'candidates': [], 'debug_cases': [{'id': '500Wt00000DDepmIAD', 'count': 0, 'involved': ['005Wt000003NJufIAG']}, {'id': '500Wt00000DDyzpIAD', 'count': 0, 'involved': ['005Wt000003NJGLIA4']}, {'id': '500Wt00000DDzUPIA1', 'count': 0, 'involved': ['005Wt000003NDqDIAW']}, {'id': '500Wt00000DDzsbIAD', 'count': 0, 'involved': ['005Wt000003NJD9IAO']}, {'id': '500Wt00000DDzscIAD', 'count': 0, 'involved': ['005Wt000003NEtOIAW']}, {'id': '500Wt00000DDzuEIAT', 'count': 0, 'involved': ['005Wt000003NJJaIAO']}, {'id': '500Wt00000DE02HIAT', 'count': 0, 'involved': ['005Wt000003NIddIAG']}]}, 'var_function-call-3757333494456036275': [None], 'var_function-call-16292085721527687252': {'best': None, 'candidates': [], 'debug': [{'id': '500Wt00000DDepmIAD', 'count': 1, 'involved': ['005Wt000003NJufIAG']}, {'id': '500Wt00000DDyzpIAD', 'count': 1, 'involved': ['005Wt000003NJGLIA4']}, {'id': '500Wt00000DDzUPIA1', 'count': 1, 'involved': ['005Wt000003NDqDIAW']}, {'id': '500Wt00000DDzsbIAD', 'count': 1, 'involved': ['005Wt000003NJD9IAO']}, {'id': '500Wt00000DDzscIAD', 'count': 1, 'involved': ['005Wt000003NEtOIAW']}, {'id': '500Wt00000DDzuEIAT', 'count': 1, 'involved': ['005Wt000003NJJaIAO']}, {'id': '500Wt00000DE02HIAT', 'count': 1, 'involved': ['005Wt000003NIddIAG']}]}, 'var_function-call-17249791054646370202': 'file_storage/function-call-17249791054646370202.json'}

exec(code, env_args)
