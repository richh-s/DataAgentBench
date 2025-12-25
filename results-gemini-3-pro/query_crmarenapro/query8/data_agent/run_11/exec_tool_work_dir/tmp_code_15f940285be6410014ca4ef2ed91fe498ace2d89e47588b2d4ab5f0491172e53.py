code = """import json
from datetime import datetime

# Load data
file_path = locals()['var_function-call-15840550546839219915']
with open(file_path, 'r') as f:
    history_data = json.load(f)

# Define period
# Last 4 quarters from 2023-04-10
# Q1 2023: Jan-Mar
# Q4 2022: Oct-Dec
# Q3 2022: Jul-Sep
# Q2 2022: Apr-Jun
# Range: 2022-04-01 to 2023-03-31 inclusive
start_date = datetime(2022, 4, 1)
end_date = datetime(2023, 3, 31, 23, 59, 59)

handled_agents = set()
transfer_counts = {}

# Helper to clean ID
def clean_id(val):
    if not val or val == 'None':
        return None
    val = val.strip()
    if val.startswith('#'):
        val = val[1:]
    if len(val) < 5: # Minimal check
        return None
    return val

# Parse date helper
# Format: "2023-09-07T16:30:00.000+0000"
# Simple parsing
def parse_date(date_str):
    try:
        # 2023-09-07T16:30:00.000+0000
        # Removing timezone for simple comparison or handling it
        # +0000 is UTC.
        # We can ignore timezone if we assume all data is UTC or consistent
        dt_str = date_str.split('+')[0]
        # 2023-09-07T16:30:00.000
        # Truncate millis if needed or parse
        return datetime.strptime(dt_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
    except Exception as e:
        return None

count_in_period = 0

for record in history_data:
    d_str = record.get('createddate')
    dt = parse_date(d_str)
    
    if dt and start_date <= dt <= end_date:
        count_in_period += 1
        
        old_val = clean_id(record.get('oldvalue__c'))
        new_val = clean_id(record.get('newvalue__c'))
        
        # Track Handled (Assigned To)
        if new_val:
            handled_agents.add(new_val)
            
        # Track Transfers (From old_val)
        # Only if old_val is a valid agent (not None)
        # Assuming oldvalue__c is the agent ID
        if old_val:
            transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1

# Filter: Among those who handled > 0 cases
# Means agent must be in handled_agents
candidates = []
for agent in handled_agents:
    t_count = transfer_counts.get(agent, 0)
    candidates.append((agent, t_count))

# Find min
if candidates:
    # Sort by count (asc)
    candidates.sort(key=lambda x: x[1])
    min_count = candidates[0][1]
    # Get all with min_count
    best_agents = [c[0] for c in candidates if c[1] == min_count]
    result = {"min_count": min_count, "agents": best_agents, "total_candidates": len(candidates)}
else:
    result = {"min_count": None, "agents": []}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3045517057883522603': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5940713645896962222': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-2920167374087173322': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-6188298989589663829': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15840550546839219915': 'file_storage/function-call-15840550546839219915.json'}

exec(code, env_args)
