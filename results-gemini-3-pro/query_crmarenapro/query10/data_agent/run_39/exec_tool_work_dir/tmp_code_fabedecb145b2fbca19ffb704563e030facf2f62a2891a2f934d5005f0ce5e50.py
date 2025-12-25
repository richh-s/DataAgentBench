code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-16862357102522627028'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-8693146939927682377'], 'r') as f:
    history_data = json.load(f)

# Helper to clean IDs
def clean_id(x):
    if x and isinstance(x, str):
        return x.strip().lstrip('#')
    return x

# Prepare Cases DataFrame
df_cases = pd.DataFrame(cases_data)
df_cases['id'] = df_cases['id'].apply(clean_id)
df_cases['ownerid'] = df_cases['ownerid'].apply(clean_id)
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'], errors='coerce')

# Prepare History DataFrame
df_history = pd.DataFrame(history_data)
# Note: field__c is not in columns because it wasn't selected, but rows are filtered by it.
df_history['caseid__c'] = df_history['caseid__c'].apply(clean_id)
df_history['newvalue__c'] = df_history['newvalue__c'].apply(clean_id)

# Define Date Window
end_date = pd.Timestamp('2023-09-02').tz_localize('UTC')
start_date = end_date - pd.DateOffset(months=4) # 2023-05-02

# 1. Identify "Active" cases for "Processing Count"
mask_active = (df_cases['createddate'] <= end_date) & (
    (df_cases['closeddate'] >= start_date) | (df_cases['closeddate'].isna())
)
active_case_ids = set(df_cases[mask_active]['id'])

# 2. Map Active Cases to Agents (Owners)
agent_cases = {} 

# From Current Owner (Case table)
for _, row in df_cases[mask_active].iterrows():
    aid = row['ownerid']
    cid = row['id']
    if aid not in agent_cases: agent_cases[aid] = set()
    agent_cases[aid].add(cid)

# From History (Transfers/Assignments) for Active Cases
active_history = df_history[df_history['caseid__c'].isin(active_case_ids)]
for _, row in active_history.iterrows():
    aid = row['newvalue__c']
    cid = row['caseid__c']
    if aid not in agent_cases: agent_cases[aid] = set()
    agent_cases[aid].add(cid)

# 3. Calculate Handle Time for "Closed" cases in Window
mask_closed_in_window = (df_cases['closeddate'] >= start_date) & (df_cases['closeddate'] <= end_date)
df_closed = df_cases[mask_closed_in_window].copy()

# Duration
df_closed['handle_time'] = (df_closed['closeddate'] - df_closed['createddate']).dt.total_seconds()

# Group by Final Owner
agent_handle_stats = {} 
for _, row in df_closed.iterrows():
    aid = row['ownerid']
    time = row['handle_time']
    if aid not in agent_handle_stats: agent_handle_stats[aid] = []
    agent_handle_stats[aid].append(time)

# 4. Filter and Find Lowest
results = []
for agent, times in agent_handle_stats.items():
    # Filter: Processing > 1 case
    processed_count = len(agent_cases.get(agent, set()))
    
    if processed_count > 1:
        avg_time = sum(times) / len(times)
        results.append({
            'agent': agent,
            'avg_time': avg_time,
            'processed_count': processed_count
        })

results_df = pd.DataFrame(results)
if not results_df.empty:
    results_df = results_df.sort_values('avg_time')
    # Print top 5 for debugging (sanity check)
    # print(results_df.head(5).to_dict(orient='records'))
    best_agent = results_df.iloc[0]['agent']
    print('__RESULT__:')
    print(json.dumps(best_agent))
else:
    print('__RESULT__:')
    print(json.dumps("No matching agent"))"""

env_args = {'var_function-call-5761545501581564423': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2520864252183331026': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-17138908491164010984': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-16862357102522627028': 'file_storage/function-call-16862357102522627028.json', 'var_function-call-8693146939927682377': 'file_storage/function-call-8693146939927682377.json'}

exec(code, env_args)
