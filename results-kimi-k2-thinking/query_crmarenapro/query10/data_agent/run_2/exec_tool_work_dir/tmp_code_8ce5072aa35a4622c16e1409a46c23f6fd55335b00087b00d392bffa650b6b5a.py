code = """import json
from datetime import datetime

# Load the data
cases_data = locals()['var_functions.query_db:10']
history_data = locals()['var_functions.query_db:12']

if isinstance(cases_data, str) and cases_data.endswith('.json'):
    with open(cases_data, 'r') as f:
        cases = json.load(f)
else:
    cases = cases_data

if isinstance(history_data, str) and history_data.endswith('.json'):
    with open(history_data, 'r') as f:
        casehistory = json.load(f)
else:
    casehistory = history_data

# Filter for owner assignment records
owner_assignments = [h for h in casehistory if h['field__c'] == 'Owner Assignment']

# Create a mapping of case ID to count of owner assignments
case_owner_counts = {}
for assignment in owner_assignments:
    case_id = assignment['caseid__c']
    case_owner_counts[case_id] = case_owner_counts.get(case_id, 0) + 1

# Analyze each case
results = []
for case in cases:
    case_id = case['id'].lstrip('#') if case['id'] else None
    owner_id = case['ownerid'].lstrip('#') if case['ownerid'] else None
    created_date = case['createddate']
    closed_date = case['closeddate']
    
    # Get owner assignment count
    owner_count = case_owner_counts.get(case_id, 0)
    
    # Check if case was transferred (more than 1 owner assignment)
    was_transferred = owner_count > 1
    
    # Calculate handle time only for non-transferred cases
    handle_time = None
    if not was_transferred and closed_date and closed_date != 'None':
        try:
            created = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
            closed = datetime.fromisoformat(closed_date.replace('Z', '+00:00'))
            handle_time = (closed - created).total_seconds() / 3600  # in hours
        except:
            pass
    
    results.append({
        'case_id': case_id,
        'owner_id': owner_id,
        'created_date': created_date,
        'closed_date': closed_date,
        'owner_assignments': owner_count,
        'was_transferred': was_transferred,
        'handle_time_hours': handle_time
    })

# Group by agent and calculate statistics
agent_stats = {}
for result in results:
    owner_id = result['owner_id']
    if not owner_id:
        continue
        
    if owner_id not in agent_stats:
        agent_stats[owner_id] = {
            'case_count': 0,
            'handle_times': []
        }
    
    agent_stats[owner_id]['case_count'] += 1
    if result['handle_time_hours'] is not None:
        agent_stats[owner_id]['handle_times'].append(result['handle_time_hours'])

# Calculate average handle time for agents with more than 1 case
agent_averages = {}
for agent_id, stats in agent_stats.items():
    if stats['case_count'] > 1 and stats['handle_times']:
        avg_handle_time = sum(stats['handle_times']) / len(stats['handle_times'])
        agent_averages[agent_id] = {
            'average_handle_time_hours': avg_handle_time,
            'case_count': stats['case_count'],
            'closed_cases': len(stats['handle_times'])
        }

# Sort by average handle time
sorted_agents = sorted(agent_averages.items(), key=lambda x: x[1]['average_handle_time_hours'])

print("__RESULT__:")
print(json.dumps({
    "agent_count": len(agent_averages),
    "top_agents": sorted_agents[:5],
    "all_agents": agent_averages
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_functions.query_db:5': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:6': [{'count': '153'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDTxbIAH', 'priority': 'High', 'subject': 'Security Compliance Clarification  ', 'description': "I am struggling to comprehend and comply with TechPulse Solutions' evolving security compliance standards.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqu47IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000079ATxIAM', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'accountid': '001Wt00000PHVqdIAH', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDepmIAD', 'priority': 'Medium', 'subject': 'Update Alerts Missing', 'description': "I am not receiving consistent notifications about feature updates, which causes us to miss out on the CloudLink Designer's full capabilities.", 'status': 'Closed', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'orderitemid__c': '802Wt000007906kIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDflsIAD', 'priority': 'Medium', 'subject': 'Lag in AI Cirku-Tech', 'description': "The latency issues with the AI Cirku-Tech platform are causing disruptions when deployed within my organization's existing systems.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqwxpIAB', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798S9IAI', 'issueid__c': 'a03Wt00000JqzR3IAJ', 'accountid': '001Wt00000PGaNjIAL', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDsG3IAL', 'priority': 'Medium', 'subject': 'Feature Update Alerts Missing', 'description': "I am not receiving notifications about new feature updates for DevVision IDE, which is leading to missed opportunities to fully utilize the software's capabilities.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqwGHIAZ', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000795izIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PGeJIIA1', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyzpIAD', 'priority': 'High', 'subject': 'Tailoring Problem', 'description': 'The AI Cirku-Tech tool is not flexible enough for specific customizations required by our unique projects.', 'status': 'Closed', 'contactid': '#003Wt00000Jqt79IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'orderitemid__c': '802Wt00000798NMIAY', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PHViZIAX', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'priority': 'Medium', 'subject': 'AI Features Unreliable', 'description': 'The AI functionalities of the CollabCircuit Hub are not consistently working, leading to decreased productivity and dissatisfaction among our team members.', 'status': 'Closed', 'contactid': '003Wt00000Jquw2IAB', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'orderitemid__c': '802Wt00000797CjIAI', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '001Wt00000PHVfJIAX', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzXdIAL', 'priority': 'High', 'subject': 'Inconsistent AI Performance   ', 'description': 'We continue to face issues with the AI-powered features of CollabCircuit Hub not performing reliably, which negatively impacts our workflow and user experience.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jquw2IAB', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797CjIAI', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PHVfJIAX', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '500Wt00000DDzZHIA1', 'priority': 'Medium', 'subject': 'Need More Customization Options', 'description': 'I find it difficult to adapt the QuantumPCB Modeler to our unique industry requirements, as it lacks sufficient customizability options.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxM1IAJ', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798qLIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PGaHIIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzivIAD', 'priority': 'High', 'subject': 'Workflow Integration Lag  ', 'description': 'I am experiencing significant delays when trying to integrate the AI Cirku-Tech solution into my current HR workflows.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqwxpIAB', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798S9IAI', 'issueid__c': 'a03Wt00000JqzR3IAJ', 'accountid': '#001Wt00000PGaNjIAL', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'priority': 'High', 'subject': 'Delay in Workflow Integration', 'description': "I'm encountering frequent workflow integration lags which are hindering my department's process efficiency.", 'status': 'Waiting on Customer', 'contactid': '#003Wt00000JqwxpIAB', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798S9IAI', 'issueid__c': 'a03Wt00000JqzR3IAJ', 'accountid': '001Wt00000PGaNjIAL', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzr0IAD', 'priority': 'Medium', 'subject': 'Customization Issue', 'description': 'I am finding it difficult to customize the AI Cirku-Tech platform to meet our niche industry needs despite the available options.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqt79IAB', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798NMIAY', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '#001Wt00000PHViZIAX', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzsbIAD', 'priority': 'High', 'subject': 'Scalability Problem', 'description': 'I am encountering difficulties in scaling TechPulse solutions to meet the increasing demands of our enterprise which is impacting our expansion efforts.', 'status': 'Closed', 'contactid': '003Wt00000JqviSIAR', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '#001Wt00000PGovMIAT', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'priority': 'High', 'subject': 'Scaling Issues with OptiPower', 'description': 'I face challenges in scaling the OptiPower Manager to accommodate increasing demands for our projects.', 'status': 'Closed', 'contactid': '#003Wt00000JqxfNIAR', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'orderitemid__c': '802Wt00000796qDIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PFsmcIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'priority': 'High', 'subject': 'Installation Issues', 'description': 'I am experiencing persistent errors during installation that prevent me from setting up the PulseSim Pro software.', 'status': 'Closed', 'contactid': '003Wt00000JqqEAIAZ', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'orderitemid__c': '802Wt00000799UfIAI', 'issueid__c': 'a03Wt00000JqhItIAJ', 'accountid': '001Wt00000PGcpMIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'priority': 'Medium', 'subject': 'Setup Error', 'description': 'The initial installation process for PulseSim Pro constantly fails, which is blocking my workflow.', 'status': 'Closed', 'contactid': '#003Wt00000JqqEAIAZ', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'orderitemid__c': '802Wt00000799UfIAI', 'issueid__c': 'a03Wt00000JqhItIAJ', 'accountid': '001Wt00000PGcpMIAT', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'case_count': 16, 'history_count': 393, 'sample_cases': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDTxbIAH', 'priority': 'High', 'subject': 'Security Compliance Clarification  ', 'description': "I am struggling to comprehend and comply with TechPulse Solutions' evolving security compliance standards.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqu47IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000079ATxIAM', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'accountid': '001Wt00000PHVqdIAH', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDepmIAD', 'priority': 'Medium', 'subject': 'Update Alerts Missing', 'description': "I am not receiving consistent notifications about feature updates, which causes us to miss out on the CloudLink Designer's full capabilities.", 'status': 'Closed', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'orderitemid__c': '802Wt000007906kIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJufIAG'}], 'sample_history': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}]}}

exec(code, env_args)
