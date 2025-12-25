code = """import pandas as pd
import json

data = locals()['var_function-call-16043054279467942764']
if isinstance(data, str) and data.endswith('.json'):
    with open(data, 'r') as f:
        data = json.load(f)

df = pd.DataFrame(data)

def clean_id(x):
    if pd.isna(x): return None
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

df['case_id'] = df['case_id'].apply(clean_id)
df['history_owner_id'] = df['history_owner_id'].apply(clean_id)

# Stats
unique_cases = df['case_id'].nunique()
print(f"Total unique cases: {unique_cases}")

case_groups = df.groupby('case_id')
assignment_counts = case_groups['history_owner_id'].count()
print("Assignment counts stats:")
print(assignment_counts.value_counts().to_dict())

# Check how many agents would have > 1 case
agent_counts = {}
for case_id, group in case_groups:
    owners = set(group['history_owner_id'].dropna().unique())
    owners.add(clean_id(group['current_owner_id'].iloc[0]))
    for o in owners:
        if o:
            agent_counts[o] = agent_counts.get(o, 0) + 1

print("Agent managed case counts:")
# Print first 10
print(dict(list(agent_counts.items())[:10]))

agents_gt_1 = [a for a, c in agent_counts.items() if c > 1]
print(f"Agents with > 1 cases: {len(agents_gt_1)}")

# Re-run logic briefly
valid_durations = 0
for case_id, group in case_groups:
    num = group['history_owner_id'].count()
    if num <= 1:
        valid_durations += 1

print(f"Cases considered non-transferred (<=1 assignment): {valid_durations}")

print("__RESULT__:")
print("DEBUG_DONE")"""

env_args = {'var_function-call-7307833295138590340': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-16128561713154002520': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-16128561713154002567': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-16128561713154002614': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-16043054279467942764': [{'case_id': '#500Wt00000DDzscIAD', 'current_owner_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'history_owner_id': '005Wt000003NEtOIAW'}, {'case_id': '500Wt00000DDepmIAD', 'current_owner_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'history_owner_id': '005Wt000003NJufIAG'}, {'case_id': '500Wt00000DDzUPIA1', 'current_owner_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'history_owner_id': '005Wt000003NDqDIAW'}, {'case_id': '500Wt00000DDzuEIAT', 'current_owner_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'history_owner_id': '005Wt000003NJJaIAO'}, {'case_id': '500Wt00000DDyzpIAD', 'current_owner_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'history_owner_id': '005Wt000003NJGLIA4'}, {'case_id': '500Wt00000DDzsbIAD', 'current_owner_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'history_owner_id': '005Wt000003NJD9IAO'}, {'case_id': '#500Wt00000DE02HIAT', 'current_owner_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'history_owner_id': '005Wt000003NIddIAG'}], 'var_function-call-2059714518510132872': []}

exec(code, env_args)
