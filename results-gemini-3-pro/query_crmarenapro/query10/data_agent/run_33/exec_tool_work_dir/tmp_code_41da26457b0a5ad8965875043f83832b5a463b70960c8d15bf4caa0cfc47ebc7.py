code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-8714509910446930341'], 'r') as f:
    cases_raw = json.load(f)
with open(locals()['var_function-call-12405440511442738773'], 'r') as f:
    hist_raw = json.load(f)

df_cases = pd.DataFrame(cases_raw)
df_hist = pd.DataFrame(hist_raw)

def clean_id(x):
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

df_cases['id_clean'] = df_cases['id'].apply(clean_id)
df_cases['owner_clean'] = df_cases['ownerid'].apply(clean_id)
df_hist['caseid_clean'] = df_hist['caseid__c'].apply(clean_id)
df_hist['newval_clean'] = df_hist['newvalue__c'].apply(clean_id)

start_date = pd.Timestamp("2023-05-02", tz="UTC")
end_date = pd.Timestamp("2023-09-02", tz="UTC")
end_date_inclusive = end_date + pd.Timedelta(days=1)

df_cases['closeddate_dt'] = pd.to_datetime(df_cases['closeddate'], errors='coerce')
df_cases['createddate_dt'] = pd.to_datetime(df_cases['createddate'], errors='coerce')

# Active Cases in window
# Created before end of window
# Closed after start of window OR Open
active_cases = df_cases[
    (df_cases['createddate_dt'] < end_date_inclusive) &
    ( (df_cases['closeddate_dt'] >= start_date) | (df_cases['closeddate_dt'].isna()) )
]

# Closed Cases in window (for Handle Time)
closed_cases = df_cases[
    (df_cases['closeddate_dt'] >= start_date) & 
    (df_cases['closeddate_dt'] < end_date_inclusive)
]

# Map History
hist_groups = df_hist.groupby('caseid_clean')

# Count Processed (Active)
processed_counts = {}
for idx, row in active_cases.iterrows():
    case_id = row['id_clean']
    current_owner = row['owner_clean']
    
    owners = set()
    if case_id in hist_groups.groups:
        owners.update(hist_groups.get_group(case_id)['newval_clean'].unique())
    if current_owner:
        owners.add(current_owner)
    
    for o in owners:
        processed_counts[o] = processed_counts.get(o, 0) + 1

# Calculate Handle Time (Closed)
agent_handle_times = {}

for idx, row in closed_cases.iterrows():
    case_id = row['id_clean']
    current_owner = row['owner_clean']
    
    owners = set()
    if case_id in hist_groups.groups:
        owners.update(hist_groups.get_group(case_id)['newval_clean'].unique())
    if current_owner:
        owners.add(current_owner)
    
    # Check Single Owner
    if len(owners) == 1:
        owner = list(owners)[0]
        duration = (row['closeddate_dt'] - row['createddate_dt']).total_seconds()
        
        if owner not in agent_handle_times:
            agent_handle_times[owner] = []
        agent_handle_times[owner].append(duration)

# Combine
candidates = []
for agent, count in processed_counts.items():
    if count > 1:
        if agent in agent_handle_times:
            times = agent_handle_times[agent]
            avg_time = sum(times) / len(times)
            candidates.append({
                "agent": agent,
                "avg_time": avg_time,
                "count": count
            })

if not candidates:
    print("__RESULT__:")
    print(json.dumps("No candidates"))
else:
    best = min(candidates, key=lambda x: x['avg_time'])
    print("__RESULT__:")
    print(json.dumps(best['agent']))"""

env_args = {'var_function-call-2226308914537843042': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-18198891999226845478': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-1173095882525426615': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-8714509910446930341': 'file_storage/function-call-8714509910446930341.json', 'var_function-call-12526052071437487588': 75, 'var_function-call-12405440511442738773': 'file_storage/function-call-12405440511442738773.json', 'var_function-call-6352173754959738164': 'No matching agents', 'var_function-call-4585494441108598850': {'total_cases': 75, 'relevant_cases': 7, 'hist_records': 165, 'sample_case_ids': ['500Wt00000DDNYoIAP', '500Wt00000DDPIsIAP', '500Wt00000DDPM6IAP', '500Wt00000DDPSZIA5', '500Wt00000DDPsPIAX'], 'sample_hist_case_ids': ['500Wt00000DDzpNIAT', '500Wt00000DDfHCIA1', '500Wt00000DDZ0VIAX', '500Wt00000DDQoUIAX', '500Wt00000DDzm9IAD'], 'sample_relevant_case_dates': ['2023-07-01T19:41:08.000+0000', '2023-08-15T14:54:02.000+0000', '2023-05-10T14:59:42.000+0000', '2023-06-30T19:03:08.000+0000', '2023-05-03T00:11:47.000+0000']}, 'var_function-call-64151291801392956': {'debug_cases': [{'case_id': '500Wt00000DDepmIAD', 'owners': ['005Wt000003NJufIAG'], 'owner_count': 1}, {'case_id': '500Wt00000DDyzpIAD', 'owners': ['005Wt000003NJGLIA4'], 'owner_count': 1}, {'case_id': '500Wt00000DDzUPIA1', 'owners': ['005Wt000003NDqDIAW'], 'owner_count': 1}, {'case_id': '500Wt00000DDzsbIAD', 'owners': ['005Wt000003NJD9IAO'], 'owner_count': 1}, {'case_id': '500Wt00000DDzscIAD', 'owners': ['005Wt000003NEtOIAW'], 'owner_count': 1}, {'case_id': '500Wt00000DDzuEIAT', 'owners': ['005Wt000003NJJaIAO'], 'owner_count': 1}, {'case_id': '500Wt00000DE02HIAT', 'owners': ['005Wt000003NIddIAG'], 'owner_count': 1}], 'processed_counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}}}

exec(code, env_args)
