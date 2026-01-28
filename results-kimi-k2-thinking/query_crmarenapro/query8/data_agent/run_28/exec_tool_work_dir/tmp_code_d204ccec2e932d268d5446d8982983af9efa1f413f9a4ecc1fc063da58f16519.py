code = """import json
import pandas as pd

# Get the case history data from storage
casehistory_raw = locals()['var_functions.query_db:5']

# Check if it's a file path or direct data
if isinstance(casehistory_raw, str) and casehistory_raw.endswith('.json'):
    with open(casehistory_raw, 'r') as f:
        casehistory_data = json.load(f)
else:
    casehistory_data = casehistory_raw

# Filter for Owner Assignment records (which indicate transfers)
owner_assignments = [r for r in casehistory_data if r.get('field__c') == 'Owner Assignment']

# Get the agent IDs from newvalue__c field
transfer_data = []
for record in owner_assignments:
    agent_id = record.get('newvalue__c')
    if agent_id and agent_id != 'None':
        # Clean up IDs that might have leading #
        if agent_id.startswith('#'):
            agent_id = agent_id[1:]
        transfer_data.append({
            'agent_id': agent_id,
            'case_id': record.get('caseid__c'),
            'date': record.get('createddate')
        })

# Create DataFrame
df = pd.DataFrame(transfer_data)

print('__RESULT__:')
print(json.dumps({
    'total_records': len(casehistory_data),
    'owner_assignment_records': len(owner_assignments),
    'transfer_records': len(transfer_data),
    'sample_transfers': transfer_data[:5]
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
