code = """import json
import pandas as pd
from datetime import datetime

# Load data
cases_path = locals()['var_function-call-7206768053077506601']
history_path = locals()['var_function-call-10648681579240081404']

with open(cases_path, 'r') as f:
    cases_data = json.load(f)

with open(history_path, 'r') as f:
    history_data = json.load(f)

def clean_id(x):
    if x and isinstance(x, str):
        return x.replace('#', '')
    return x

# Process Cases
cases = []
for c in cases_data:
    cases.append({
        'id': clean_id(c['id']),
        'ownerid': clean_id(c['ownerid']),
        'createddate': c['createddate'],
        'closeddate': c['closeddate']
    })
df_cases = pd.DataFrame(cases)
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'], errors='coerce')

# Process History
history = []
for h in history_data:
    history.append({
        'caseid': clean_id(h['caseid__c']),
        'oldvalue': clean_id(h['oldvalue__c']),
        'newvalue': clean_id(h['newvalue__c']),
        'createddate': h['createddate']
    })
df_history = pd.DataFrame(history)
df_history['createddate'] = pd.to_datetime(df_history['createddate'], errors='coerce')

# Define Window
start_date = pd.Timestamp('2023-05-02').tz_localize('UTC')
end_date = pd.Timestamp('2023-09-02 23:59:59').tz_localize('UTC')

# Normalize Timezones
if df_cases['createddate'].dt.tz is None:
    df_cases['createddate'] = df_cases['createddate'].dt.tz_localize('UTC')
if df_cases['closeddate'].dt.tz is None:
    df_cases['closeddate'] = df_cases['closeddate'].dt.tz_localize('UTC')
if df_history['createddate'].dt.tz is None:
    df_history['createddate'] = df_history['createddate'].dt.tz_localize('UTC')

# Identify Active Cases in Window
# created <= end AND (closed >= start OR closed is NaT)
active_cases_mask = (df_cases['createddate'] <= end_date) & \
                    ((df_cases['closeddate'] >= start_date) | (df_cases['closeddate'].isna()))
active_cases = df_cases[active_cases_mask].copy()
active_case_ids = set(active_cases['id'])

# Processed Count Logic
# Map Agent -> Set of CaseIDs they "owned" during the window intersection
# Timeline approach
relevant_history = df_history[df_history['caseid'].isin(active_case_ids)].sort_values(['caseid', 'createddate'])
agent_processed_count = {} 

for cid in active_case_ids:
    c_row = df_cases[df_cases['id'] == cid].iloc[0]
    c_create = c_row['createddate']
    c_close = c_row['closeddate'] if pd.notnull(c_row['closeddate']) else pd.Timestamp.max.tz_localize('UTC')
    
    current_owner = c_row['ownerid']
    current_start = c_create
    
    timeline = []
    c_hist = relevant_history[relevant_history['caseid'] == cid]
    
    for _, h_row in c_hist.iterrows():
        h_date = h_row['createddate']
        new_owner = h_row['newvalue']
        # If hist date is before creation (weird), skip? Or assume correction.
        # But generally hist is >= create.
        if h_date >= current_start:
            timeline.append((current_owner, current_start, h_date))
            current_owner = new_owner
            current_start = h_date
    
    timeline.append((current_owner, current_start, c_close))
    
    # Check intersection
    for owner, t_start, t_end in timeline:
        if owner:
            # Intersection of [t_start, t_end] with [start_date, end_date]
            overlap_start = max(t_start, start_date)
            overlap_end = min(t_end, end_date)
            
            if overlap_start < overlap_end:
                if owner not in agent_processed_count:
                    agent_processed_count[owner] = set()
                agent_processed_count[owner].add(cid)

# Handle Time Logic
# Closed in window, Unique Owners = 1
agent_handle_times = {}

# Closed in window
closed_in_window = df_cases[
    (df_cases['closeddate'] >= start_date) & 
    (df_cases['closeddate'] <= end_date)
].copy()

for _, c_row in closed_in_window.iterrows():
    cid = c_row['id']
    
    # Check transfers: Count unique owners in entire history (ever)
    # Because "cases that have been transferred" property is intrinsic to the case, not just the window.
    # If it was transferred in 2020, it's a "transferred case". Handle time logic excludes it.
    
    # Get all history for this case (not just active active ones, but we loaded all history)
    c_hist = df_history[df_history['caseid'] == cid]
    
    owners = set()
    if c_row['ownerid']: owners.add(c_row['ownerid'])
    for _, h in c_hist.iterrows():
        if h['newvalue'] and h['newvalue'] != 'None': owners.add(h['newvalue'])
        if h['oldvalue'] and h['oldvalue'] != 'None': owners.add(h['oldvalue'])
    
    if len(owners) == 1:
        # Not transferred
        owner = list(owners)[0]
        duration = (c_row['closeddate'] - c_row['createddate']).total_seconds()
        
        if owner not in agent_handle_times:
            agent_handle_times[owner] = []
        agent_handle_times[owner].append(duration)

# Final Selection
final_results = []
for agent, cases_set in agent_processed_count.items():
    processed_count = len(cases_set)
    if processed_count > 1:
        if agent in agent_handle_times:
            times = agent_handle_times[agent]
            if len(times) > 0:
                avg_time = sum(times) / len(times)
                final_results.append({
                    'agent': agent,
                    'processed': processed_count,
                    'avg_time': avg_time
                })

if final_results:
    final_results.sort(key=lambda x: x['avg_time'])
    print("__RESULT__:")
    print(json.dumps(final_results[0]['agent']))
else:
    # Fallback debug
    print("__RESULT__:")
    print(json.dumps("No qualified agent"))"""

env_args = {'var_function-call-18199340976651491628': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-9827286813105460724': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-745774768715260552': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-7014113440238423972': [{'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539tVIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539v7IAA', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T16:03:45.000+0000', 'field__c': 'Case Closed'}], 'var_function-call-6141072571166727096': [{'count': '7'}], 'var_function-call-17850988456605936473': [{'count': '153'}], 'var_function-call-10081475916434898076': [{'closeddate': '2023-12-02T16:45:51.000+0000'}, {'closeddate': '2023-11-02T14:10:33.000+0000'}, {'closeddate': '2023-10-16T15:22:17.000+0000'}, {'closeddate': '2023-10-15T14:23:52.000+0000'}, {'closeddate': '2023-10-05T16:02:30.000+0000'}, {'closeddate': '2023-10-02T14:45:22.000+0000'}, {'closeddate': '2023-10-02T09:32:45.000+0000'}, {'closeddate': '2023-09-30T16:03:45.000+0000'}, {'closeddate': '2023-09-26T12:20:45.000+0000'}, {'closeddate': '2023-09-22T08:43:27.000+0000'}, {'closeddate': '2023-09-18T09:53:18.000+0000'}, {'closeddate': '2023-09-16T21:27:33.000+0000'}, {'closeddate': '2023-09-08T16:25:49.000+0000'}, {'closeddate': '2023-09-07T16:45:30.000+0000'}, {'closeddate': '2023-08-15T14:54:02.000+0000'}, {'closeddate': '2023-07-01T19:41:08.000+0000'}, {'closeddate': '2023-06-30T19:03:08.000+0000'}, {'closeddate': '2023-06-03T15:21:34.000+0000'}, {'closeddate': '2023-06-02T13:35:12.000+0000'}, {'closeddate': '2023-05-10T14:59:42.000+0000'}], 'var_function-call-3011512126080988696': [{'count': '393'}], 'var_function-call-16300506009982063083': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10648681579240081404': 'file_storage/function-call-10648681579240081404.json', 'var_function-call-10145898340697273674': 'No agents met the criteria.', 'var_function-call-7206768053077506601': 'file_storage/function-call-7206768053077506601.json'}

exec(code, env_args)
