code = """import json
from datetime import datetime

cases_path = locals()['var_function-call-9420257839074769044']
history_path = locals()['var_function-call-11261257856447075564']

with open(cases_path, 'r') as f:
    cases = json.load(f)
with open(history_path, 'r') as f:
    history = json.load(f)

# Config
START_DATE = datetime(2023, 5, 2)
END_DATE = datetime(2023, 9, 2)

def parse_dt(s):
    if not s or s == "None":
        return None
    try:
        return datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f%z").replace(tzinfo=None) # Remove tz for simple comparison
    except:
        return None

def clean_id(i):
    if i and isinstance(i, str):
        return i.strip().lstrip('#')
    return i

# Map History to Case
case_history = {} # cid -> list of entries
for h in history:
    cid = clean_id(h['caseid__c'])
    if cid not in case_history:
        case_history[cid] = []
    case_history[cid].append(h)

agent_stats = {} # agent_id -> {'managed_count': 0, 'handle_times': []}

for c in cases:
    cid = clean_id(c['id'])
    created = parse_dt(c['createddate'])
    closed = parse_dt(c['closeddate'])
    
    # Filter out future cases (created after today)
    if created and created > END_DATE:
        continue
        
    # Check "Processed" Status (Active in Window)
    # Active if created <= END and (closed >= START or closed is None or closed > END)
    # Logic: It overlaps with [START, END]
    # Interval [Created, Closed (or INF)]. Overlap with [START, END]?
    # Yes if Created <= END and (Closed is None or Closed >= START)
    
    is_processed = False
    if created and created <= END_DATE:
        if closed is None or closed >= START_DATE:
             is_processed = True
             
    if not is_processed:
        continue
        
    # Determine Owners
    owners = set()
    entries = case_history.get(cid, [])
    # If history, owners are newvalue__c
    for e in entries:
        owners.add(clean_id(e['newvalue__c']))
    
    # Fallback to Case.ownerid if no history (or ensure current owner is in list)
    current_owner = clean_id(c['ownerid'])
    owners.add(current_owner)
    
    # Update Managed Count
    for o in owners:
        if o not in agent_stats: agent_stats[o] = {'managed_count': 0, 'handle_times': []}
        agent_stats[o]['managed_count'] += 1
        
    # Check Metric Eligibility
    # Closed in Window
    if closed and closed >= START_DATE and closed <= END_DATE:
        # Check Transferred
        # Rule: Only ONE 'Owner Assignment' -> Not Transferred.
        # But I must check the 'Owner Assignment' entries specifically.
        # The history list passed here contains only 'Owner Assignment' (from previous SQL).
        # So len(entries) checks number of assignments.
        # However, entries might include duplicates? The previous snippet showed unique events.
        # I'll trust len(entries).
        # If len(entries) > 1 -> Transferred.
        # If len(entries) <= 1 -> Not Transferred. (1 usually means creation assignment or single assignment).
        # Actually, if 0 entries in history, it means no recorded assignment change. Just the initial owner? 
        # Assume Not Transferred if <= 1.
        
        is_transferred = len(entries) > 1
        
        if not is_transferred:
            duration = (closed - created).total_seconds()
            
            # Assign to Final Owner
            # If history, take last newvalue? Or just use c['ownerid'] which should be current.
            # Use c['ownerid'].
            final_owner = current_owner
            
            if final_owner not in agent_stats:
                 agent_stats[final_owner] = {'managed_count': 0, 'handle_times': []}
            
            agent_stats[final_owner]['handle_times'].append(duration)

# Calculate results
results = []
for agent, stats in agent_stats.items():
    if stats['managed_count'] > 1:
        if stats['handle_times']:
            avg = sum(stats['handle_times']) / len(stats['handle_times'])
            results.append({'id': agent, 'avg': avg, 'count': stats['managed_count']})

results.sort(key=lambda x: x['avg'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16084396659173659689': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17551838553651043930': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-17551838553651042327': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-17551838553651040724': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11261257856447075564': 'file_storage/function-call-11261257856447075564.json', 'var_function-call-3253871082083541322': [], 'var_function-call-1002297143353410861': [{'count': '21'}], 'var_function-call-1002297143353410410': [{'closeddate': '2023-12-02T16:45:51.000+0000'}, {'closeddate': '2023-11-02T14:10:33.000+0000'}, {'closeddate': '2023-10-16T15:22:17.000+0000'}, {'closeddate': '2023-10-15T14:23:52.000+0000'}, {'closeddate': '2023-10-05T16:02:30.000+0000'}], 'var_function-call-1002297143353409959': {'500Wt00000DDzscIAD': ['005Wt000003NEtOIAW'], '500Wt00000DDepmIAD': ['005Wt000003NJufIAG'], '500Wt00000DDzUPIA1': ['005Wt000003NDqDIAW'], '500Wt00000DDzuEIAT': ['005Wt000003NJJaIAO'], '500Wt00000DDyzpIAD': ['005Wt000003NJGLIA4'], '500Wt00000DDzsbIAD': ['005Wt000003NJD9IAO'], '500Wt00000DE02HIAT': ['005Wt000003NIddIAG']}, 'var_function-call-3157752014415146853': [{'count': '153'}], 'var_function-call-9420257839074769044': 'file_storage/function-call-9420257839074769044.json'}

exec(code, env_args)
