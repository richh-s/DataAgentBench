code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Get the file path from storage
file_path = locals()['var_functions.query_db:6']

# Read case history data
with open(file_path, 'r') as f:
    case_history_data = json.load(f)

# Load cases data from earlier query
cases_data = [
    {"id": "#500Wt00000DDDfwIAH", "priority": "Medium", "subject": "Feature Update Notifications Lack", "description": "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", "status": "Waiting on Customer", "contactid": "003Wt00000JqxKSIAZ", "createddate": "2023-07-02T11:00:00.000+0000", "closeddate": "None", "orderitemid__c": "802Wt00000797r4IAA", "issueid__c": "a03Wt00000JqzSfIAJ", "accountid": "001Wt00000PFttwIAD", "ownerid": "005Wt000003NJ0DIAW"},
    {"id": "500Wt00000DDDtTIAX", "priority": "Medium", "subject": "Missing Feature Update Alerts", "description": "I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.", "status": "Waiting on Customer   ", "contactid": "003Wt00000Jqp3WIAR", "createddate": "2020-12-29T08:36:00.000+0000", "closeddate": "None", "orderitemid__c": "802Wt00000798aDIAQ", "issueid__c": "a03Wt00000JqzSfIAJ", "accountid": "001Wt00000PHVkAIAX", "ownerid": "#005Wt000003NJWTIA4"},
    {"id": "500Wt00000DDNYoIAP", "priority": "Medium", "subject": "Delayed Support Response ", "description": "I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.", "status": "Closed", "contactid": "#003Wt00000JqqVtIAJ", "createddate": "2023-09-30T11:30:00.000+0000", "closeddate": "2023-09-30T16:03:45.000+0000", "orderitemid__c": "802Wt00000792tiIAA", "issueid__c": "a03Wt00000JqtOtIAJ", "accountid": "001Wt00000PGZZoIAP", "ownerid": "005Wt000003NIc3IAG"},
    {"id": "500Wt00000DDPIsIAP", "priority": "Medium", "subject": "AI Feature Malfunction", "description": "Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.", "status": "Closed ", "contactid": "003Wt00000JqlkjIAB", "createddate": "2022-08-05T14:30:00.000+0000", "closeddate": "2022-08-05T14:39:32.000+0000", "orderitemid__c": "802Wt00000797r3IAA", "issueid__c": "a03Wt00000JqxVjIAJ", "accountid": "#001Wt00000PGRnYIAX", "ownerid": "#005Wt000003NEzqIAG"},
    {"id": "500Wt00000DDPM6IAP", "priority": "High", "subject": "Access Issues with Training Module", "description": "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", "status": "Closed", "contactid": "#003Wt00000Jqv14IAB", "createddate": "2020-09-01T10:30:00.000+0000", "closeddate": "2020-09-01T14:08:55.000+0000", "orderitemid__c": "802Wt00000797r5IAA", "issueid__c": "a03Wt00000JqvNUIAZ", "accountid": "001Wt00000PGzSaIAL", "ownerid": "005Wt000003NISLIA4"}
]

# Convert to DataFrames
hist_df = pd.DataFrame(case_history_data)
cases_df = pd.DataFrame(cases_data)

# Clean the data
# Remove leading # from ID-like fields
for col in ['caseid__c', 'newvalue__c', 'oldvalue__c']:
    if col in hist_df.columns:
        hist_df[col] = hist_df[col].str.lstrip('#')

for col in ['id', 'ownerid', 'contactid', 'accountid']:
    if col in cases_df.columns:
        cases_df[col] = cases_df[col].str.lstrip('#')

# Remove trailing whitespace
cases_df['status'] = cases_df['status'].str.rstrip()

# Count owner assignments per case to detect transfers
assignments_per_case = hist_df[hist_df['field__c'] == 'Owner Assignment'].groupby('caseid__c').size().reset_index(name='assignment_count')

# Identify cases with transfers (more than 1 assignment)
cases_with_transfers = assignments_per_case[assignments_per_case['assignment_count'] > 1]['caseid__c'].tolist()

print('__RESULT__:')
print(json.dumps(f"Found {len(cases_with_transfers)} cases with transfers out of {len(assignments_per_case)} total cases with assignments", ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:5': [{'count': '43'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': 'Loaded 165 case history records, cleaned'}

exec(code, env_args)
