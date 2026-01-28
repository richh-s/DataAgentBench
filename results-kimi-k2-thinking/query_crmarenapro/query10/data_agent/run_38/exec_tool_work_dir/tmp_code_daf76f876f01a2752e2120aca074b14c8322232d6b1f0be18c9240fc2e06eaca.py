code = """import json
import pandas as pd

# Read the file path from storage
file_path = locals()['var_functions.query_db:6']

# Read the case history data
with open(file_path, 'r') as f:
    case_history = json.load(f)

# Convert to DataFrame
df_history = pd.DataFrame(case_history)

# Parse dates
df_history['createddate'] = pd.to_datetime(df_history['createddate'])

# Filter date range: from 2023-05-02 to 2023-09-02 (past 4 months from 2023-09-02)
start_date = '2023-05-02'
end_date = '2023-09-02'
mask = (df_history['createddate'] >= start_date) & (df_history['createddate'] <= end_date)
df_filtered = df_history[mask].copy()

# Count assignments per caseid to identify cases with multiple assignments
# (which means they have been transferred)
case_assignments = df_filtered.groupby('caseid__c').size().reset_index(name='assignment_count')

# Identify cases with multiple assignments (transferred cases)
transferred_cases = case_assignments[case_assignments['assignment_count'] > 1]['caseid__c'].tolist()

# Count cases per agent that were NOT transferred
# For each agent, count unique case IDs where that case appears only once in the filtered data
non_transferred_cases = case_assignments[case_assignments['assignment_count'] == 1]['caseid__c'].tolist()

# Filter df_filtered to only include non-transferred cases
df_non_transferred = df_filtered[df_filtered['caseid__c'].isin(non_transferred_cases)]

# Count total cases per agent from non-transferred cases (newvalue__c = agent_id)
agent_cases = df_non_transferred.groupby('newvalue__c').agg({
    'caseid__c': 'nunique'
}).reset_index()

agent_cases.columns = ['agent_id', 'case_count']

# Filter agents with more than 1 case
agent_cases_filtered = agent_cases[agent_cases['case_count'] > 1]

print(f"Found {len(agent_cases_filtered)} agents with more than 1 non-transferred case")
print("Agents meeting criteria:")
print(agent_cases_filtered)

# Now get the actual case data to calculate handle time
print("Calculating handle times...")

result = {
    "agent_count": len(agent_cases_filtered),
    "agent_ids": agent_cases_filtered['agent_id'].tolist() if len(agent_cases_filtered) > 0 else []
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDTxbIAH', 'priority': 'High', 'subject': 'Security Compliance Clarification  ', 'description': "I am struggling to comprehend and comply with TechPulse Solutions' evolving security compliance standards.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqu47IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt0000079ATxIAM', 'issueid__c': 'a03Wt00000JqzPSIAZ', 'accountid': '001Wt00000PHVqdIAH', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDepmIAD', 'priority': 'Medium', 'subject': 'Update Alerts Missing', 'description': "I am not receiving consistent notifications about feature updates, which causes us to miss out on the CloudLink Designer's full capabilities.", 'status': 'Closed', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'orderitemid__c': '802Wt000007906kIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDflsIAD', 'priority': 'Medium', 'subject': 'Lag in AI Cirku-Tech', 'description': "The latency issues with the AI Cirku-Tech platform are causing disruptions when deployed within my organization's existing systems.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqwxpIAB', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798S9IAI', 'issueid__c': 'a03Wt00000JqzR3IAJ', 'accountid': '001Wt00000PGaNjIAL', 'ownerid': '005Wt000003NJppIAG'}, {'id': '#500Wt00000DDsG3IAL', 'priority': 'Medium', 'subject': 'Feature Update Alerts Missing', 'description': "I am not receiving notifications about new feature updates for DevVision IDE, which is leading to missed opportunities to fully utilize the software's capabilities.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqwGHIAZ', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000795izIAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PGeJIIA1', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDyzpIAD', 'priority': 'High', 'subject': 'Tailoring Problem', 'description': 'The AI Cirku-Tech tool is not flexible enough for specific customizations required by our unique projects.', 'status': 'Closed', 'contactid': '#003Wt00000Jqt79IAB', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'orderitemid__c': '802Wt00000798NMIAY', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PHViZIAX', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'priority': 'Medium', 'subject': 'AI Features Unreliable', 'description': 'The AI functionalities of the CollabCircuit Hub are not consistently working, leading to decreased productivity and dissatisfaction among our team members.', 'status': 'Closed', 'contactid': '003Wt00000Jquw2IAB', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'orderitemid__c': '802Wt00000797CjIAI', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '001Wt00000PHVfJIAX', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzXdIAL', 'priority': 'High', 'subject': 'Inconsistent AI Performance   ', 'description': 'We continue to face issues with the AI-powered features of CollabCircuit Hub not performing reliably, which negatively impacts our workflow and user experience.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jquw2IAB', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797CjIAI', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PHVfJIAX', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '500Wt00000DDzZHIA1', 'priority': 'Medium', 'subject': 'Need More Customization Options', 'description': 'I find it difficult to adapt the QuantumPCB Modeler to our unique industry requirements, as it lacks sufficient customizability options.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxM1IAJ', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798qLIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '001Wt00000PGaHIIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzivIAD', 'priority': 'High', 'subject': 'Workflow Integration Lag  ', 'description': 'I am experiencing significant delays when trying to integrate the AI Cirku-Tech solution into my current HR workflows.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqwxpIAB', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798S9IAI', 'issueid__c': 'a03Wt00000JqzR3IAJ', 'accountid': '#001Wt00000PGaNjIAL', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'priority': 'High', 'subject': 'Delay in Workflow Integration', 'description': "I'm encountering frequent workflow integration lags which are hindering my department's process efficiency.", 'status': 'Waiting on Customer', 'contactid': '#003Wt00000JqwxpIAB', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798S9IAI', 'issueid__c': 'a03Wt00000JqzR3IAJ', 'accountid': '001Wt00000PGaNjIAL', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDzr0IAD', 'priority': 'Medium', 'subject': 'Customization Issue', 'description': 'I am finding it difficult to customize the AI Cirku-Tech platform to meet our niche industry needs despite the available options.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000Jqt79IAB', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798NMIAY', 'issueid__c': 'a03Wt00000JqmX6IAJ', 'accountid': '#001Wt00000PHViZIAX', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzsbIAD', 'priority': 'High', 'subject': 'Scalability Problem', 'description': 'I am encountering difficulties in scaling TechPulse solutions to meet the increasing demands of our enterprise which is impacting our expansion efforts.', 'status': 'Closed', 'contactid': '003Wt00000JqviSIAR', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '#001Wt00000PGovMIAT', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'priority': 'High', 'subject': 'Scaling Issues with OptiPower', 'description': 'I face challenges in scaling the OptiPower Manager to accommodate increasing demands for our projects.', 'status': 'Closed', 'contactid': '#003Wt00000JqxfNIAR', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'orderitemid__c': '802Wt00000796qDIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB', 'accountid': '001Wt00000PFsmcIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'priority': 'High', 'subject': 'Installation Issues', 'description': 'I am experiencing persistent errors during installation that prevent me from setting up the PulseSim Pro software.', 'status': 'Closed', 'contactid': '003Wt00000JqqEAIAZ', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'orderitemid__c': '802Wt00000799UfIAI', 'issueid__c': 'a03Wt00000JqhItIAJ', 'accountid': '001Wt00000PGcpMIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'priority': 'Medium', 'subject': 'Setup Error', 'description': 'The initial installation process for PulseSim Pro constantly fails, which is blocking my workflow.', 'status': 'Closed', 'contactid': '#003Wt00000JqqEAIAZ', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'orderitemid__c': '802Wt00000799UfIAI', 'issueid__c': 'a03Wt00000JqhItIAJ', 'accountid': '001Wt00000PGcpMIAT', 'ownerid': '005Wt000003NIddIAG'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
