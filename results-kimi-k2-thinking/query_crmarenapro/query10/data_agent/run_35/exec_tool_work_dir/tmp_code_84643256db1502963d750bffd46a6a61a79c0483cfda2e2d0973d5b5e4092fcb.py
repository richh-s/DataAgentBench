code = """import json
import pandas as pd
from datetime import datetime

# Load the full data from the file
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean the data - remove leading #
df['id'] = df['id'].astype(str).str.replace('^#', '', regex=True)
df['ownerid'] = df['ownerid'].astype(str).str.replace('^#', '', regex=True)
df['caseid__c'] = df['caseid__c'].astype(str).str.replace('^#', '', regex=True)

# Convert dates
df['createddate'] = pd.to_datetime(df['createddate'])
df['closeddate'] = pd.to_datetime(df['closeddate'])

# Define the cutoff date (past 4 months from 2023-09-02 so >= 2023-05-01)
cutoff_date = pd.Timestamp('2023-05-01')

# Filter for relevant period
df_filtered = df[df['closeddate'] >= cutoff_date].copy()

# Group by caseid to count owner assignments per case
case_assignment_counts = df_filtered.groupby('id').agg({
    'field__c': lambda x: (x == 'Owner Assignment').sum()
}).rename(columns={'field__c': 'assignment_count'}).reset_index()

# Identify cases that were NOT transferred (only one owner assignment)
non_transferred_cases = case_assignment_counts[case_assignment_counts['assignment_count'] == 1]['id'].tolist()

# Filter the original data for non-transferred cases only
df_non_transferred = df_filtered[df_filtered['id'].isin(non_transferred_cases)].copy()

# For each case, get the createddate and closeddate
case_times = df_non_transferred.groupby('id').agg({
    'createddate': 'min',
    'closeddate': 'max',
    'ownerid': 'first'
}).reset_index()

# Calculate handle time in hours for each case
case_times['handle_time_hours'] = (case_times['closeddate'] - case_times['createddate']).dt.total_seconds() / 3600

# Group by agent to calculate average handle time and case count
agent_stats = case_times.groupby('ownerid').agg({
    'handle_time_hours': 'mean',
    'id': 'count'
}).rename(columns={'id': 'case_count'}).reset_index()

# Filter agents who processed more than one case
agents_multiple_cases = agent_stats[agent_stats['case_count'] > 1].copy()

# Find the agent with the lowest average handle time
if not agents_multiple_cases.empty:
    min_idx = agents_multiple_cases['handle_time_hours'].idxmin()
    best_agent = agents_multiple_cases.loc[min_idx]
    result = best_agent['ownerid']
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_functions.query_db:5': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
