code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-1518981953904716875'], 'r') as f:
    cases = json.load(f)
with open(locals()['var_function-call-4271949275430875243'], 'r') as f:
    history = json.load(f)

# Convert to DataFrame
df_cases = pd.DataFrame(cases)
df_history = pd.DataFrame(history)

# Filter cases closed in the past 4 months (2023-05-02 to 2023-09-02)
# Parse dates
def parse_date(d):
    if not d: return None
    # Handle potentially different formats or timezone
    try:
        return datetime.strptime(d.split('.')[0], "%Y-%m-%dT%H:%M:%S")
    except:
        return None

start_date = datetime(2023, 5, 2)
end_date = datetime(2023, 9, 2, 23, 59, 59)

valid_cases = []
for c in cases:
    closed = parse_date(c.get('closeddate'))
    created = parse_date(c.get('createddate'))
    if closed and start_date <= closed <= end_date:
        # Calculate handle time in seconds
        ht = (closed - created).total_seconds()
        c['handle_time_seconds'] = ht
        valid_cases.append(c)

print(f"Found {len(valid_cases)} cases closed in the window.")

# Process history to identify owners per case
case_owners = {} # case_id -> set of owners

# Initialize with current owners for all valid cases (as fallback or base)
for c in valid_cases:
    case_owners[c['id']] = set()
    if c.get('ownerid'):
        case_owners[c['id']].add(c['ownerid'])

# Add from history
# We need to consider ALL history for these cases to determine if they were transferred
# So filter history for only the valid case IDs
valid_case_ids = set(c['id'] for c in valid_cases)

# history might contain cases not in valid_cases, that's fine
# But we only care about valid_cases
for h in history:
    cid = h.get('caseid__c')
    if cid in valid_case_ids:
        # Add newvalue (owner)
        owner = h.get('newvalue__c')
        if owner:
            case_owners[cid].add(owner)
        # Also oldvalue if it's an owner? 
        # Usually oldvalue="None" for creation, or previous owner ID.
        old = h.get('oldvalue__c')
        if old and old != "None":
            case_owners[cid].add(old)

# Agent Stats
agent_processed_count = {} # agent_id -> count
agent_ht_sum = {} # agent_id -> sum seconds
agent_ht_count = {} # agent_id -> count of cases contributing to HT

for c in valid_cases:
    cid = c['id']
    owners = case_owners[cid]
    
    # Update processed count
    for agent in owners:
        agent_processed_count[agent] = agent_processed_count.get(agent, 0) + 1
    
    # Update Handle Time
    # Only if NOT transferred (count of owners == 1)
    if len(owners) == 1:
        # The single owner gets the HT
        agent = list(owners)[0]
        agent_ht_sum[agent] = agent_ht_sum.get(agent, 0.0) + c['handle_time_seconds']
        agent_ht_count[agent] = agent_ht_count.get(agent, 0) + 1
    else:
        # Transferred case. No HT computed.
        pass

# Calculate results
results = []
for agent, count in agent_processed_count.items():
    if count > 1: # Filter: processing more than one case
        if agent in agent_ht_count and agent_ht_count[agent] > 0:
            avg_ht = agent_ht_sum[agent] / agent_ht_count[agent]
            results.append({
                'agent_id': agent,
                'avg_handle_time': avg_ht,
                'processed_count': count,
                'ht_count': agent_ht_count[agent]
            })

# Find lowest
if results:
    results.sort(key=lambda x: x['avg_handle_time'])
    best_agent = results[0]
    print("__RESULT__:")
    print(json.dumps(best_agent['agent_id']))
else:
    print("__RESULT__:")
    print(json.dumps("No eligible agents found"))"""

env_args = {'var_function-call-7690210003021158341': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-16457674010664790620': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-4576443792012588565': [], 'var_function-call-17953215166236416196': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-8952938976537607787': [{'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1048852573031136957': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-7026344890111544585': [{'min': '2020-07-05T09:51:05.000+0000', 'max': '2023-12-02T16:45:51.000+0000'}], 'var_function-call-1518981953904716875': 'file_storage/function-call-1518981953904716875.json', 'var_function-call-4271949275430875243': 'file_storage/function-call-4271949275430875243.json'}

exec(code, env_args)
