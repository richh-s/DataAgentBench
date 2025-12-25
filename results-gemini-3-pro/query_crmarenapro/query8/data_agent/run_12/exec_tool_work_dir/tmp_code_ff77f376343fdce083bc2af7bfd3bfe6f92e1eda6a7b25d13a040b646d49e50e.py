code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-8139464499209271755'], 'r') as f:
    history = json.load(f)

# Helper to clean ID
def clean_id(val):
    if val and isinstance(val, str):
        if val.startswith('#'):
            return val[1:]
        return val
    return val

# Filter for Owner Assignment
assignments = [r for r in history if r.get('field__c') == 'Owner Assignment']

# Define window
start_date = pd.Timestamp('2022-04-10', tz='UTC')
end_date = pd.Timestamp('2023-04-10', tz='UTC')

# Containers
handled_counts_window = {}
transfer_counts_window = {}
all_agents = set()

for r in assignments:
    # Parse date
    # Format: 2022-03-02T10:15:00.000+0000
    try:
        dt = pd.to_datetime(r['createddate'])
    except:
        continue
    
    in_window = (dt >= start_date) and (dt <= end_date)
    
    new_agent = clean_id(r.get('newvalue__c'))
    old_agent = clean_id(r.get('oldvalue__c'))
    
    # Ignore 'None'
    if new_agent == 'None': new_agent = None
    if old_agent == 'None': old_agent = None

    if new_agent:
        all_agents.add(new_agent)
        if in_window:
            handled_counts_window[new_agent] = handled_counts_window.get(new_agent, 0) + 1
            
    if old_agent:
        all_agents.add(old_agent)
        if in_window:
            transfer_counts_window[old_agent] = transfer_counts_window.get(old_agent, 0) + 1

# Candidates: Handled > 0 in window
candidates = [a for a in handled_counts_window if handled_counts_window[a] > 0]

# If no candidates in window, maybe "handled > 0" refers to ever?
# Let's check candidates count.
print("Candidates in window:", len(candidates))

# Find min transfer count for candidates
results = []
for agent in candidates:
    tc = transfer_counts_window.get(agent, 0)
    results.append({'agent': agent, 'transfers': tc, 'handled': handled_counts_window[agent]})

# Sort by transfers (asc)
results.sort(key=lambda x: x['transfers'])

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-12268255451877300690': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15607863566886824677': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-3973721063512414452': [{'count': '39'}], 'var_function-call-15089162678779735596': [{'count': '393'}], 'var_function-call-8139464499209271755': 'file_storage/function-call-8139464499209271755.json'}

exec(code, env_args)
