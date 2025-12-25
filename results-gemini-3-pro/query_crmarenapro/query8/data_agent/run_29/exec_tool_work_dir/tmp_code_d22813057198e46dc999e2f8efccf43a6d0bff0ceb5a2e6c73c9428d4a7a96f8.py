code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-8126399227036074897'], 'r') as f:
    data = json.load(f)

# Define date range
start_date = datetime(2022, 4, 1)
end_date = datetime(2023, 3, 31)

def clean_id(val):
    if not val or val == 'None':
        return None
    val = str(val).strip()
    if val.startswith('#'):
        return val[1:]
    return val

handled_agents = set()
transfer_counts = {}

# Process records
filtered_records = []
for r in data:
    # Check field
    if r.get('field__c') != 'Owner Assignment':
        continue
    
    # Check date
    c_date_str = r.get('createddate')
    # Format: "2023-09-07T16:30:00.000+0000"
    # Python isoformat might handle it, or strptime
    try:
        # Simple parse for YYYY-MM-DD
        dt = datetime.strptime(c_date_str[:10], "%Y-%m-%d")
        if not (start_date <= dt <= end_date):
            continue
    except:
        continue

    filtered_records.append(r)

    # Clean IDs
    old_val = clean_id(r.get('oldvalue__c'))
    new_val = clean_id(r.get('newvalue__c'))

    # Update population
    if old_val:
        handled_agents.add(old_val)
    if new_val:
        handled_agents.add(new_val)

# Initialize counts
for agent in handled_agents:
    transfer_counts[agent] = 0

# Count transfers
for r in filtered_records:
    old_val = clean_id(r.get('oldvalue__c'))
    if old_val:
        if old_val in transfer_counts:
            transfer_counts[old_val] += 1
        else:
            # Should be in handled_agents if logic holds, but safe add
            transfer_counts[old_val] = 1

# Find min
min_transfers = float('inf')
min_agent = None

sorted_agents = sorted(transfer_counts.items(), key=lambda x: (x[1], x[0]))

print("__RESULT__:")
print(json.dumps(sorted_agents))"""

env_args = {'var_function-call-3552046821111797620': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-16132431978656463409': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-2215454728334574223': [{'count': '393'}], 'var_function-call-8126399227036074897': 'file_storage/function-call-8126399227036074897.json'}

exec(code, env_args)
