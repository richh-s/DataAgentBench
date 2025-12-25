code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-4741343475108631162'], 'r') as f:
    history = json.load(f)

with open(locals()['var_function-call-1467132616485381509'], 'r') as f:
    cases = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        if i.startswith('#'):
            return i[1:]
        return i
    return None

def parse_date(d):
    if not d: return None
    # Format: 2023-09-07T16:30:00.000+0000
    # Python 3.11+ handles standard ISO with Z or offset, but simple split might be safer/faster given constraints
    try:
        return datetime.strptime(d[:19], "%Y-%m-%dT%H:%M:%S")
    except:
        return None

START_DATE = datetime(2022, 4, 10)
END_DATE = datetime(2023, 4, 10)

handled_agents = set()
transfer_counts = {}

# Process Cases for Handled Set
for c in cases:
    oid = clean_id(c.get('ownerid'))
    if not oid or not oid.startswith('005'): continue
    
    cd = parse_date(c.get('createddate'))
    cld = parse_date(c.get('closeddate'))
    
    # Check if case was open/active during window
    # Created before End AND (Not closed OR Closed after Start)
    if cd and cd <= END_DATE:
        if not cld or cld >= START_DATE:
            handled_agents.add(oid)

# Process History
for h in history:
    if h.get('field__c') != 'Owner Assignment': continue
    
    old_val = clean_id(h.get('oldvalue__c'))
    new_val = clean_id(h.get('newvalue__c'))
    date = parse_date(h.get('createddate'))
    
    if not date: continue
    
    # Metric: Transfer Counts in Window
    # Transfer from old_val to new_val
    if START_DATE <= date <= END_DATE:
        if old_val and old_val.startswith('005'):
            transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1
        
        # Add to handled set (Active in window)
        if old_val and old_val.startswith('005'):
            handled_agents.add(old_val)
        if new_val and new_val.startswith('005'):
            handled_agents.add(new_val)
            
    # If date > END_DATE, the old_val agent held it before date. 
    # Did they hold it in window? Most likely yes if they just transferred it. 
    if date > END_DATE:
        if old_val and old_val.startswith('005'):
            handled_agents.add(old_val)

# Prepare candidates
candidates = []
for agent in handled_agents:
    count = transfer_counts.get(agent, 0)
    candidates.append({'id': agent, 'count': count})

# Find min
candidates.sort(key=lambda x: x['count'])

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-5260945133747048414': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4004111035141208110': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-4741343475108631162': 'file_storage/function-call-4741343475108631162.json', 'var_function-call-1467132616485381509': 'file_storage/function-call-1467132616485381509.json'}

exec(code, env_args)
