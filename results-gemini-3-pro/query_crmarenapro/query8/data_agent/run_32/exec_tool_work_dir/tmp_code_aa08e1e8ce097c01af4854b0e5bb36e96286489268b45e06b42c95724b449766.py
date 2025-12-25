code = """import json
from datetime import datetime

# Load the case history
file_path = locals()['var_function-call-12358601199876924892']
with open(file_path, 'r') as f:
    history = json.load(f)

# Define date range
start_date = datetime(2022, 4, 1)
end_date = datetime(2023, 3, 31)

def parse_date(date_str):
    # Format: 2023-09-07T16:30:00.000+0000
    # Python 3.12 handles ISO format with %z, but the +0000 might need handling if not standard
    # Simple workaround: split by T and take date part, or use fromisoformat
    try:
        # 2023-09-07T16:30:00.000+0000
        # Removing timezone for simple comparison or handling it
        dt = datetime.strptime(date_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
        return dt
    except Exception as e:
        return None

# Filter rows in date range
filtered_rows = []
for row in history:
    d = parse_date(row['createddate'])
    if d and start_date <= d <= end_date:
        filtered_rows.append(row)

# Identify Handled Agents (newvalue__c in filtered rows)
# and calculate Transfer Counts (oldvalue__c in filtered rows)
# We only care about agents who appear as newvalue__c (or implicitly handling?)
# "Among those who handled more than 0 cases" -> Must have been assigned a case in the period?
# Or handled a case that was assigned earlier?
# The provided definition of Handled implies "Assigned". 
# "this filter applies to both the first agent that the case was first assigned to and the agent that the case was transferred to"
# This implies Handled = Assigned.
# So I will collect all agents who were ASSIGNED a case in the period.

handled_agents = set()
transfer_counts = {}

for row in filtered_rows:
    new_owner = row.get('newvalue__c')
    old_owner = row.get('oldvalue__c')
    
    # Clean IDs
    if new_owner and new_owner != 'None':
        new_owner = new_owner.strip()
        handled_agents.add(new_owner)
    
    if old_owner and old_owner != 'None':
        old_owner = old_owner.strip()
        # Count transfers FROM old_owner
        transfer_counts[old_owner] = transfer_counts.get(old_owner, 0) + 1

# Now, we consider only agents in handled_agents.
# Their transfer count is 0 if not in transfer_counts.

results = []
for agent in handled_agents:
    count = transfer_counts.get(agent, 0)
    results.append({'agent_id': agent, 'transfers': count})

# Find min
if results:
    min_transfers = min(r['transfers'] for r in results)
    candidates = [r['agent_id'] for r in results if r['transfers'] == min_transfers]
else:
    candidates = []
    min_transfers = -1

print("__RESULT__:")
print(json.dumps({'min_transfers': min_transfers, 'candidates': candidates, 'count_candidates': len(candidates)}))"""

env_args = {'var_function-call-2420836909563224927': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5384257016623672216': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-12044959519315846892': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-12358601199876924892': 'file_storage/function-call-12358601199876924892.json'}

exec(code, env_args)
