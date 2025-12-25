code = """import json
import pandas as pd

# Load data
cases = locals()['var_function-call-6235709102432108974']
history_path = locals()['var_function-call-5446965614530322862']

with open(history_path, 'r') as f:
    history = json.load(f)

# Helper to clean IDs
def clean_id(x):
    if not x: return x
    return str(x).replace('#', '').strip()

# Prepare Case Data
# Filter cases to ensure strictly within window (already filtered by SQL roughly)
# SQL: closeddate >= '2023-05-02' AND closeddate < '2023-09-03'
# This covers 2023-09-02 fully.
# We trust the SQL result for the set of cases.

# Build Case Map
case_map = {}
for c in cases:
    cid = clean_id(c['id'])
    # Parse dates
    # format: 2023-07-01T10:30:00.000+0000
    try:
        created = pd.to_datetime(c['createddate'])
        closed = pd.to_datetime(c['closeddate'])
        duration = (closed - created).total_seconds()
    except:
        duration = 0 # Should not happen based on data
    
    case_map[cid] = {
        'owner': clean_id(c['ownerid']),
        'duration': duration,
        'history_count': 0,
        'owners': set()
    }

# Process History
for h in history:
    cid = clean_id(h['caseid__c'])
    if cid in case_map:
        case_map[cid]['history_count'] += 1
        new_owner = clean_id(h['newvalue__c'])
        if new_owner:
            case_map[cid]['owners'].add(new_owner)
        old_owner = clean_id(h['oldvalue__c'])
        if old_owner and old_owner != 'None':
            case_map[cid]['owners'].add(old_owner)

# Fallback: If no history found for a case, assume single owner from Case table
for cid, cdata in case_map.items():
    if cdata['history_count'] == 0:
        cdata['history_count'] = 1
        cdata['owners'].add(cdata['owner'])
    # Ensure current owner is in owners set (it should be)
    cdata['owners'].add(cdata['owner'])

# Calculate Metrics per Agent
agent_metrics = {} # {agent_id: {'processed_count': 0, 'durations': []}}

# 1. Calculate Processed Count
# Iterate all cases in window
for cid, cdata in case_map.items():
    for agent in cdata['owners']:
        if agent not in agent_metrics:
            agent_metrics[agent] = {'processed_count': 0, 'durations': []}
        agent_metrics[agent]['processed_count'] += 1

# 2. Calculate Handle Time
# Only for Single Owner cases (history_count == 1)
# Assign to the single owner
for cid, cdata in case_map.items():
    if cdata['history_count'] == 1:
        agent = cdata['owner']
        if agent in agent_metrics:
            agent_metrics[agent]['durations'].append(cdata['duration'])

# Filter and Find Best
eligible_agents = []
for agent, metrics in agent_metrics.items():
    if metrics['processed_count'] > 1 and len(metrics['durations']) > 0:
        avg_time = sum(metrics['durations']) / len(metrics['durations'])
        eligible_agents.append({
            'agent': agent,
            'avg_time': avg_time,
            'processed': metrics['processed_count']
        })

# Sort by avg_time ascending
eligible_agents.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(eligible_agents))"""

env_args = {'var_function-call-25694081247760875': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12242375876057293113': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-4426529604873226006': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-10682198703271803977': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-14247413615305265901': [{'count': '7'}], 'var_function-call-6235709102432108974': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-5446965614530322862': 'file_storage/function-call-5446965614530322862.json'}

exec(code, env_args)
