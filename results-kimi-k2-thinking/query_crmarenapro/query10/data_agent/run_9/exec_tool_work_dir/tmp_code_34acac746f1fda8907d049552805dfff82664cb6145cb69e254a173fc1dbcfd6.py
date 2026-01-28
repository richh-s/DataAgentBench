code = """import json
import pandas as pd
from datetime import datetime

# Get the cases data from the previous query
cases_data = locals()['var_functions.query_db:18']

# Get the owner assignments data from the previous query
assignments_data = locals()['var_functions.query_db:20']

print(f"Total cases: {len(cases_data)}")
print(f"Total owner assignments: {len(assignments_data)}")

# Convert to DataFrames
df_cases = pd.DataFrame(cases_data)
df_assignments = pd.DataFrame(assignments_data)

# Clean owner IDs - remove leading #
df_cases['ownerid_clean'] = df_cases['ownerid'].str.replace('^#', '', regex=True)

# Parse dates
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Compute handle time in hours
df_cases['handle_time_hours'] = (df_cases['closeddate'] - df_cases['createddate']).dt.total_seconds() / 3600

# Count owner assignments per case
assignment_counts = df_assignments.groupby('caseid__c').size().reset_index(name='assignment_count')

# Merge cases with assignment counts
df_merged = df_cases.merge(assignment_counts, left_on='id', right_on='caseid__c', how='left')

# Fill NaN assignment counts with 0
df_merged['assignment_count'] = df_merged['assignment_count'].fillna(0)

print(f"\nCases with assignment counts:")
print(df_merged[['id', 'ownerid_clean', 'assignment_count', 'handle_time_hours']].head())

# Filter for non-transferred cases (exactly 1 owner assignment)
non_transferred_cases = df_merged[df_merged['assignment_count'] == 1]

print(f"\nNon-transferred cases: {len(non_transferred_cases)}")
print(f"Total cases: {len(df_merged)}")

if len(non_transferred_cases) > 0:
    # Group by owner to calculate statistics
    owner_stats = non_transferred_cases.groupby('ownerid_clean').agg({
        'handle_time_hours': ['count', 'mean']
    }).round(2)
    
    # Flatten column names
    owner_stats.columns = ['case_count', 'avg_handle_time_hours']
    owner_stats = owner_stats.reset_index()
    
    print(f"\nAll agents with non-transferred cases:")
    print(owner_stats.to_string())
    
    # Filter agents with more than 1 case
    agents_multiple_cases = owner_stats[owner_stats['case_count'] > 1]
    
    print(f"\nAgents with > 1 case:")
    print(agents_multiple_cases.to_string())
    
    # Find agent with lowest average handle time
    if not agents_multiple_cases.empty:
        best_agent_idx = agents_multiple_cases['avg_handle_time_hours'].idxmin()
        best_agent = agents_multiple_cases.loc[best_agent_idx]
        
        print(f"\nBest agent: {best_agent['ownerid_clean']}")
        print(f"Average handle time: {best_agent['avg_handle_time_hours']} hours")
        print(f"Case count: {best_agent['case_count']}")
        
        # Return the agent ID
        print("__RESULT__:")
        print(best_agent['ownerid_clean'])
    else:
        print("No agents with more than one non-transferred case found")
        print("__RESULT__:")
        print("")
else:
    print("No non-transferred cases found")
    print("__RESULT__:")
    print("")"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDPSZIA5', 'priority': 'Medium', 'subject': 'Slow Reply from Support Team', 'description': "The delay in obtaining a prompt response from the TechPulse support team is causing frustration and hindering our team's efficiency.", 'status': 'Closed', 'contactid': '003Wt00000JqqVtIAJ', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '#001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'priority': 'Low', 'subject': 'Scaling Difficulties ', 'description': 'We are struggling to effectively scale the AI DesignShift solution, affecting our operational expansion, and we require assistance.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqv0zIAB', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000078xAFIAY', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGdzxIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '500Wt00000DDPsOIAX', 'priority': 'Medium', 'subject': 'EcoPCB Data Integration Error', 'description': 'I am facing issues integrating EcoPCB Creator with third-party applications, which is causing disruptions in project workflows.', 'status': 'Working', 'contactid': '003Wt00000JqyEtIAJ', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000079ATyIAM', 'issueid__c': 'a03Wt00000JqzKcIAJ', 'accountid': '001Wt00000PHRF9IAP', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDPsPIAX', 'priority': 'Medium', 'subject': 'Customization Issue', 'description': "I find it difficult to adapt the AI Cirku-Tech platform to my company's very specialized circuit design requirements despite the customization features available.", 'status': 'Closed', 'contactid': '003Wt00000Jqy0PIAR', 'createddate': '2023-04-05T17:51:00.000+0000', 'closeddate': '2023-04-06T11:30:54.000+0000', 'orderitemid__c': '802Wt00000794bXIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '#001Wt00000PGHsyIAH', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDQRsIAP', 'priority': 'Medium', 'subject': 'Scalability Issue', 'description': "I am facing challenges in scaling the OptiPower Manager to meet my organization's growing demands, hindering our expansion efforts.", 'status': 'Closed', 'contactid': '#003Wt00000Jqwg6IAB', 'createddate': '2023-03-08T06:49:00.000+0000', 'closeddate': '2023-03-08T07:07:30.000+0000', 'orderitemid__c': '802Wt00000796yFIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGzM9IAL', 'ownerid': '#005Wt000003NFKoIAO'}], 'var_functions.query_db:6': [{'total_rows': '393'}], 'var_functions.query_db:8': [{'ownerid': '005Wt000003NIvNIAW'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '#005Wt000003NF1SIAW'}, {'ownerid': '005Wt000003NIAcIAO'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '#005Wt000003NI90IAG'}, {'ownerid': '005Wt000003NJ6fIAG'}, {'ownerid': '005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NFKpIAO'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_functions.query_db:20': [{'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005322UIAQ', 'caseid__c': '500Wt00000DE0NGIA1', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000533xqIAA', 'caseid__c': '500Wt00000DDz6FIAT', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000534aYIAQ', 'caseid__c': '500Wt00000DDzW2IAL', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000535ulIAA', 'caseid__c': '500Wt00000DDYUGIA5', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000536cIIAQ', 'caseid__c': '500Wt00000DDU5iIAH', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537TYIAY', 'caseid__c': '500Wt00000DE0BxIAL', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538NzIAI', 'caseid__c': '500Wt00000DDz6FIAT', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt000005395ZIAQ', 'caseid__c': '500Wt00000DDnt6IAD', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539S5IAI', 'caseid__c': '500Wt00000DE078IAD', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539VJIAY', 'caseid__c': '500Wt00000DE0GnIAL', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539yLIAQ', 'caseid__c': '500Wt00000DDPSZIA5', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
