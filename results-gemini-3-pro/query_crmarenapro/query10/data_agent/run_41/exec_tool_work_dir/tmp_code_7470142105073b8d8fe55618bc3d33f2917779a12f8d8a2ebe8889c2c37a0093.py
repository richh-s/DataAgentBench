code = """import json
import pandas as pd
from datetime import datetime

# Load data
cases_data = locals()['var_function-call-16300506009982063083']
history_path = locals()['var_function-call-10648681579240081404']

with open(history_path, 'r') as f:
    history_data = json.load(f)

# Clean IDs
def clean_id(x):
    if x and isinstance(x, str):
        return x.replace('#', '')
    return x

cases = []
for c in cases_data:
    cases.append({
        'id': clean_id(c['id']),
        'ownerid': clean_id(c['ownerid']),
        'createddate': c['createddate'],
        'closeddate': c['closeddate']
    })

history = []
for h in history_data:
    history.append({
        'caseid': clean_id(h['caseid__c']),
        'oldvalue': clean_id(h['oldvalue__c']),
        'newvalue': clean_id(h['newvalue__c'])
    })

# Convert to DF for easier handling
df_cases = pd.DataFrame(cases)
df_history = pd.DataFrame(history)

# Parse dates
# Format: "2023-07-01T19:41:08.000+0000"
# Python isoformat might handle it, or use pd.to_datetime
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Filter cases by date window
# Past 4 months: 2023-05-02 to 2023-09-02 (inclusive)
start_date = pd.Timestamp('2023-05-02').tz_localize('UTC')
end_date = pd.Timestamp('2023-09-02 23:59:59').tz_localize('UTC')

# Ensure naive dates are handled (though sample shows +0000)
if df_cases['createddate'].dt.tz is None:
    df_cases['createddate'] = df_cases['createddate'].dt.tz_localize('UTC')
if df_cases['closeddate'].dt.tz is None:
    df_cases['closeddate'] = df_cases['closeddate'].dt.tz_localize('UTC')

filtered_cases = df_cases[
    (df_cases['closeddate'] >= start_date) & 
    (df_cases['closeddate'] <= end_date)
].copy()

# Calculate Handle Time (in seconds)
filtered_cases['handle_time'] = (filtered_cases['closeddate'] - filtered_cases['createddate']).dt.total_seconds()

# Analyze per agent
agent_cases = {} # Set of case IDs per agent
agent_solo_times = {} # List of handle times for solo cases

for _, case in filtered_cases.iterrows():
    case_id = case['id']
    
    # Get history for this case
    case_hist = df_history[df_history['caseid'] == case_id]
    
    # Determine owners involved
    involved_agents = set()
    
    # From history
    for _, row in case_hist.iterrows():
        if row['newvalue'] and row['newvalue'] != 'None':
            involved_agents.add(row['newvalue'])
        if row['oldvalue'] and row['oldvalue'] != 'None':
            involved_agents.add(row['oldvalue'])
            
    # Also add current owner from Case table (should be in history, but just in case)
    if case['ownerid']:
        involved_agents.add(case['ownerid'])
        
    # Update agent_cases count
    for agent in involved_agents:
        if agent not in agent_cases:
            agent_cases[agent] = set()
        agent_cases[agent].add(case_id)
        
    # Check if transferred
    # Transferred if history count > 1 (assuming "Owner Assignment" records)
    # The history loaded IS filtered by field__c='Owner Assignment'
    # Wait, check if history list is empty?
    # If empty, it means 1 assignment (creation) but maybe not logged in this table?
    # Earlier I saw "Case Creation" logged separately.
    # But I fetched records with field__c='Owner Assignment'.
    # If a case has 0 records in this filtered history:
    #   Then it likely has just the initial owner.
    #   Is it possible to have 0 records?
    #   Let's check the earlier sample. Case '500Wt00000DDNYoIAP' had 1 'Owner Assignment'.
    #   So 1 record = Not Transferred. >1 records = Transferred.
    #   What if 0? Maybe data issue or different logic.
    #   I will assume count <= 1 means Not Transferred.
    
    is_transferred = len(case_hist) > 1
    
    if not is_transferred:
        # Assign handle time to the owner
        # Which owner? The one in Case table or the one in history? Should be same.
        owner = case['ownerid']
        if owner:
            if owner not in agent_solo_times:
                agent_solo_times[owner] = []
            agent_solo_times[owner].append(case['handle_time'])

# Compute metrics
results = []
for agent, cases_set in agent_cases.items():
    processed_count = len(cases_set)
    
    if processed_count > 1:
        # Check if agent has solo times
        if agent in agent_solo_times and len(agent_solo_times[agent]) > 0:
            avg_time = sum(agent_solo_times[agent]) / len(agent_solo_times[agent])
            results.append({
                'agent_id': agent,
                'avg_time': avg_time,
                'processed_count': processed_count,
                'solo_count': len(agent_solo_times[agent])
            })

# Find lowest
if results:
    # Sort by avg_time
    results.sort(key=lambda x: x['avg_time'])
    best_agent = results[0]['agent_id']
    final_output = results
else:
    best_agent = None
    final_output = "No agents met the criteria."

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-18199340976651491628': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9827286813105460724': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-745774768715260552': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-7014113440238423972': [{'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539tVIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539v7IAA', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T16:03:45.000+0000', 'field__c': 'Case Closed'}], 'var_function-call-6141072571166727096': [{'count': '7'}], 'var_function-call-17850988456605936473': [{'count': '153'}], 'var_function-call-10081475916434898076': [{'closeddate': '2023-12-02T16:45:51.000+0000'}, {'closeddate': '2023-11-02T14:10:33.000+0000'}, {'closeddate': '2023-10-16T15:22:17.000+0000'}, {'closeddate': '2023-10-15T14:23:52.000+0000'}, {'closeddate': '2023-10-05T16:02:30.000+0000'}, {'closeddate': '2023-10-02T14:45:22.000+0000'}, {'closeddate': '2023-10-02T09:32:45.000+0000'}, {'closeddate': '2023-09-30T16:03:45.000+0000'}, {'closeddate': '2023-09-26T12:20:45.000+0000'}, {'closeddate': '2023-09-22T08:43:27.000+0000'}, {'closeddate': '2023-09-18T09:53:18.000+0000'}, {'closeddate': '2023-09-16T21:27:33.000+0000'}, {'closeddate': '2023-09-08T16:25:49.000+0000'}, {'closeddate': '2023-09-07T16:45:30.000+0000'}, {'closeddate': '2023-08-15T14:54:02.000+0000'}, {'closeddate': '2023-07-01T19:41:08.000+0000'}, {'closeddate': '2023-06-30T19:03:08.000+0000'}, {'closeddate': '2023-06-03T15:21:34.000+0000'}, {'closeddate': '2023-06-02T13:35:12.000+0000'}, {'closeddate': '2023-05-10T14:59:42.000+0000'}], 'var_function-call-3011512126080988696': [{'count': '393'}], 'var_function-call-16300506009982063083': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10648681579240081404': 'file_storage/function-call-10648681579240081404.json'}

exec(code, env_args)
