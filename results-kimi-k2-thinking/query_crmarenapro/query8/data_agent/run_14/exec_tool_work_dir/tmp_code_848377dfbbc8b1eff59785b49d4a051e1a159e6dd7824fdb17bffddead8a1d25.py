code = """import json
import pandas as pd
from datetime import datetime

# Read the casehistory data from file
file_path = "file_storage/functions.query_db:5.json"

with open(file_path, 'r') as f:
    casehistory_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(casehistory_data)

# Remove leading # from ids if present
df['id'] = df['id'].str.lstrip('#')
df['caseid__c'] = df['caseid__c'].str.lstrip('#')
df['oldvalue__c'] = df['oldvalue__c'].str.lstrip('#')
df['newvalue__c'] = df['newvalue__c'].str.lstrip('#')

# Filter for date range (last 4 quarters from 2023-04-10)
start_date = '2022-04-10'
end_date = '2023-04-10'

# Convert createddate to datetime
df['createddate'] = pd.to_datetime(df['createddate'])
df_filtered = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]

# Filter for Owner Assignment events
df_owner_assignments = df_filtered[df_filtered['field__c'] == 'Owner Assignment'].copy()

# Count transfers per agent
# A transfer happens when oldvalue__c is not 'None' (meaning agent is transferring out)
transfer_counts = df_owner_assignments[df_owner_assignments['oldvalue__c'] != 'None']['oldvalue__c'].value_counts()

# Get agents who handled more than 0 cases in the date period
case_counts = df_owner_assignments['newvalue__c'].value_counts()
valid_agents = case_counts[case_counts > 0].index

# Filter transfer counts to only include valid agents
filtered_transfer_counts = transfer_counts[transfer_counts.index.isin(valid_agents)]

print('__RESULT__:')
print(json.dumps({
    'total_casehistory_records': len(df),
    'filtered_date_records': len(df_filtered),
    'owner_assignment_records': len(df_owner_assignments),
    'agents_with_cases': len(valid_agents),
    'transfer_counts_sample': dict(filtered_transfer_counts.head()) if len(filtered_transfer_counts) > 0 else {}
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:10': {'file_path': 'file_storage/functions.query_db:5.json'}}

exec(code, env_args)
