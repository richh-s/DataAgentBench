code = """import json
import pandas as pd
from datetime import datetime
import os

# Read the query result - use forward slashes to avoid unicode escape issues
file_path = "C:/Users/sarah/AppData/Local/Temp/tmpkro5h4s5.json"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error reading file: {e}")
    # Try to get the data from the variable directly if file access fails
    try:
        data = locals().get('var_functions.query_db:10', [])
    except:
        data = []

if not data:
    # If still no data, try reading a preview
    preview = locals().get('preview_var_functions.query_db:10', '')
    if preview and preview.startswith('['):
        try:
            data = json.loads(preview[:10000])
        except:
            data = []

print(f"Loaded {len(data)} records")

if len(data) > 0:
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Clean and parse dates
    df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')
    df['closeddate'] = pd.to_datetime(df['closeddate'], errors='coerce')
    df['history_createddate'] = pd.to_datetime(df['history_createddate'], errors='coerce')
    
    # Remove records with invalid dates
    valid_cases = df.dropna(subset=['createddate', 'closeddate'])
    
    if len(valid_cases) > 0:
        # Compute handle time in hours
        valid_cases = valid_cases.copy()
        valid_cases['handle_time_hours'] = (valid_cases['closeddate'] - valid_cases['createddate']).dt.total_seconds() / 3600
        
        # Identify cases with transfers
        owner_assignments = valid_cases[valid_cases['field__c'] == 'Owner Assignment']
        assignment_counts = owner_assignments.groupby('id').size().reset_index(name='assignment_count')
        
        # Merge with cases
        cases_with_count = valid_cases.merge(assignment_counts, on='id', how='left')
        cases_with_count['assignment_count'] = cases_with_count['assignment_count'].fillna(0)
        
        # Filter for non-transferred cases (exactly 1 owner assignment)
        non_transferred_cases = cases_with_count[cases_with_count['assignment_count'] == 1]
        
        print(f"Total valid cases: {len(valid_cases['id'].unique())}")
        print(f"Non-transferred cases: {len(non_transferred_cases['id'].unique())}")
        
        # Get unique cases with handle times
        unique_cases = non_transferred_cases.drop_duplicates(subset=['id'])
        
        # Group by owner to calculate statistics
        owner_stats = unique_cases.groupby('ownerid').agg({
            'handle_time_hours': ['count', 'mean']
        }).round(2)
        
        # Flatten column names
        owner_stats.columns = ['case_count', 'avg_handle_time_hours']
        owner_stats = owner_stats.reset_index()
        
        # Filter agents with more than 1 case
        agents_multiple_cases = owner_stats[owner_stats['case_count'] > 1]
        
        print(f"Agent count (filtered): {len(agents_multiple_cases)}")
        
        # Find agent with lowest average handle time
        if not agents_multiple_cases.empty:
            best_agent_idx = agents_multiple_cases['avg_handle_time_hours'].idxmin()
            best_agent = agents_multiple_cases.loc[best_agent_idx]
            
            result = {
                'agent_id': best_agent['ownerid'],
                'avg_handle_time_hours': float(best_agent['avg_handle_time_hours']),
                'case_count': int(best_agent['case_count'])
            }
            
            print(f"Best agent: {result}")
            
            # Print results in required format
            print("__RESULT__:")
            print(result['agent_id'])
        else:
            print("No agents with more than one case found")
            print("__RESULT__:")
            print("")
    else:
        print("No valid cases with dates found")
        print("__RESULT__:")
        print("")
else:
    print("No data loaded")
    print("__RESULT__:")
    print("")"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}, {'id': '500Wt00000DDPSZIA5', 'priority': 'Medium', 'subject': 'Slow Reply from Support Team', 'description': "The delay in obtaining a prompt response from the TechPulse support team is causing frustration and hindering our team's efficiency.", 'status': 'Closed', 'contactid': '003Wt00000JqqVtIAJ', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '#001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'priority': 'Low', 'subject': 'Scaling Difficulties ', 'description': 'We are struggling to effectively scale the AI DesignShift solution, affecting our operational expansion, and we require assistance.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqv0zIAB', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000078xAFIAY', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGdzxIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '500Wt00000DDPsOIAX', 'priority': 'Medium', 'subject': 'EcoPCB Data Integration Error', 'description': 'I am facing issues integrating EcoPCB Creator with third-party applications, which is causing disruptions in project workflows.', 'status': 'Working', 'contactid': '003Wt00000JqyEtIAJ', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000079ATyIAM', 'issueid__c': 'a03Wt00000JqzKcIAJ', 'accountid': '001Wt00000PHRF9IAP', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDPsPIAX', 'priority': 'Medium', 'subject': 'Customization Issue', 'description': "I find it difficult to adapt the AI Cirku-Tech platform to my company's very specialized circuit design requirements despite the customization features available.", 'status': 'Closed', 'contactid': '003Wt00000Jqy0PIAR', 'createddate': '2023-04-05T17:51:00.000+0000', 'closeddate': '2023-04-06T11:30:54.000+0000', 'orderitemid__c': '802Wt00000794bXIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '#001Wt00000PGHsyIAH', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDQRsIAP', 'priority': 'Medium', 'subject': 'Scalability Issue', 'description': "I am facing challenges in scaling the OptiPower Manager to meet my organization's growing demands, hindering our expansion efforts.", 'status': 'Closed', 'contactid': '#003Wt00000Jqwg6IAB', 'createddate': '2023-03-08T06:49:00.000+0000', 'closeddate': '2023-03-08T07:07:30.000+0000', 'orderitemid__c': '802Wt00000796yFIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PGzM9IAL', 'ownerid': '#005Wt000003NFKoIAO'}], 'var_functions.query_db:6': [{'total_rows': '393'}], 'var_functions.query_db:8': [{'ownerid': '005Wt000003NIvNIAW'}, {'ownerid': '005Wt000003NIc3IAG'}, {'ownerid': '#005Wt000003NF1SIAW'}, {'ownerid': '005Wt000003NIAcIAO'}, {'ownerid': '#005Wt000003NFr4IAG'}, {'ownerid': '005Wt000003NIYnIAO'}, {'ownerid': '#005Wt000003NI90IAG'}, {'ownerid': '005Wt000003NJ6fIAG'}, {'ownerid': '005Wt000003NIDqIAO'}, {'ownerid': '005Wt000003NFKpIAO'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
