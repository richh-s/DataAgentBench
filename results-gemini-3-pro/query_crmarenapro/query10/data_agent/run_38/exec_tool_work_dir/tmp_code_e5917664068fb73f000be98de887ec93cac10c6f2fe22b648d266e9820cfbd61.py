code = """import pandas as pd
import json
import dateutil.parser

# Load data
data_path = locals()['var_function-call-11446974356465836571']
if isinstance(data_path, str) and data_path.endswith('.json'):
    with open(data_path, 'r') as f:
        data = json.load(f)
else:
    data = data_path

df = pd.DataFrame(data)

def clean_id(x):
    if pd.isna(x): return None
    x = str(x).strip()
    if x.startswith('#'):
        return x[1:]
    return x

df['case_id'] = df['case_id'].apply(clean_id)
df['current_owner_id'] = df['current_owner_id'].apply(clean_id)
df['history_owner_id'] = df['history_owner_id'].apply(clean_id)

# Dates
def parse_date(x):
    if not x or str(x).lower() == 'none':
        return pd.NaT
    try:
        return pd.to_datetime(x)
    except:
        return pd.NaT

df['createddate'] = df['createddate'].apply(parse_date)
df['closeddate'] = df['closeddate'].apply(parse_date)

# Group by case
case_groups = df.groupby('case_id')

agent_managed_cases = {} # agent_id -> set of case_ids
agent_durations = {} # agent_id -> list of durations

for case_id, group in case_groups:
    # Get all owners
    hist_owners = set(group['history_owner_id'].dropna().unique())
    curr_owner = group['current_owner_id'].iloc[0]
    
    all_owners = hist_owners.copy()
    if curr_owner:
        all_owners.add(curr_owner)
    
    # 1. Update Managed Counts
    # All cases in this DF are "Active in Period" (created before end, closed after start or open)
    for agent in all_owners:
        if agent not in agent_managed_cases:
            agent_managed_cases[agent] = set()
        agent_managed_cases[agent].add(case_id)

    # 2. Compute Handle Time (if applicable)
    # Check if closed in window
    closed_date = group['closeddate'].iloc[0]
    created_date = group['createddate'].iloc[0]
    
    in_window = False
    if pd.notna(closed_date):
        if pd.Timestamp('2023-05-02') <= closed_date <= pd.Timestamp('2023-09-02T23:59:59'):
            in_window = True
            
    if in_window:
        # Check transfer status
        # Count assignments
        # In SQL, we left joined. If no history, history_owner_id is NaN. Count is 0 (after dropna).
        # "There will be only ONE 'Owner Assignment' for non-transferred"
        # If count > 1 -> Transferred.
        # If count <= 1 -> Not Transferred.
        # But wait, if joined rows > 1, then multiple assignments.
        # Check number of rows in group where history_owner_id is not null?
        # Actually, SQL join rows = number of history entries.
        # Exception: If no history, 1 row with null history_owner_id.
        
        # Determine number of history entries
        history_entries = group['history_owner_id'].dropna().tolist()
        num_history = len(history_entries)
        
        is_transferred = False
        if num_history > 1:
            is_transferred = True
        
        if not is_transferred:
            if pd.notna(created_date) and pd.notna(closed_date):
                duration = (closed_date - created_date).total_seconds()
                
                # Identify the single owner
                # If num_history == 1, use that owner.
                # If num_history == 0, use current_owner.
                owner = None
                if num_history == 1:
                    owner = history_entries[0]
                elif num_history == 0:
                    owner = curr_owner
                
                if owner:
                    if owner not in agent_durations:
                        agent_durations[owner] = []
                    agent_durations[owner].append(duration)

# Compute averages
final_stats = []
for agent, durations in agent_durations.items():
    managed_count = len(agent_managed_cases.get(agent, []))
    if managed_count > 1:
        avg_time = sum(durations) / len(durations)
        final_stats.append({
            'agent_id': agent,
            'avg_handle_time': avg_time,
            'managed_count': managed_count
        })

final_stats.sort(key=lambda x: x['avg_handle_time'])

print("__RESULT__:")
print(json.dumps(final_stats))"""

env_args = {'var_function-call-7307833295138590340': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-16128561713154002520': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-16128561713154002567': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-16128561713154002614': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-16043054279467942764': [{'case_id': '#500Wt00000DDzscIAD', 'current_owner_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'history_owner_id': '005Wt000003NEtOIAW'}, {'case_id': '500Wt00000DDepmIAD', 'current_owner_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'history_owner_id': '005Wt000003NJufIAG'}, {'case_id': '500Wt00000DDzUPIA1', 'current_owner_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'history_owner_id': '005Wt000003NDqDIAW'}, {'case_id': '500Wt00000DDzuEIAT', 'current_owner_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'history_owner_id': '005Wt000003NJJaIAO'}, {'case_id': '500Wt00000DDyzpIAD', 'current_owner_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'history_owner_id': '005Wt000003NJGLIA4'}, {'case_id': '500Wt00000DDzsbIAD', 'current_owner_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'history_owner_id': '005Wt000003NJD9IAO'}, {'case_id': '#500Wt00000DE02HIAT', 'current_owner_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'history_owner_id': '005Wt000003NIddIAG'}], 'var_function-call-2059714518510132872': [], 'var_function-call-11348546479081194595': [{'count': '153'}], 'var_function-call-11348546479081195598': [{'count': '21'}], 'var_function-call-11446974356465836571': 'file_storage/function-call-11446974356465836571.json'}

exec(code, env_args)
