code = """import pandas as pd
import json

# Get filenames from storage
cases_file = locals()['var_function-call-13506550345692657605']
history_file = locals()['var_function-call-304691642357648652']

# Load data
with open(cases_file, 'r') as f:
    cases_data = json.load(f)
with open(history_file, 'r') as f:
    history_data = json.load(f)

cases = pd.DataFrame(cases_data)
history = pd.DataFrame(history_data)

# Helper to clean IDs
def clean_id(x):
    if pd.isna(x): return x
    x = str(x).strip()
    if x.startswith('#'): return x[1:]
    return x

cases['id'] = cases['id'].apply(clean_id)
cases['ownerid'] = cases['ownerid'].apply(clean_id)
if not history.empty:
    history['caseid__c'] = history['caseid__c'].apply(clean_id)
    history['newvalue__c'] = history['newvalue__c'].apply(clean_id)

# Date Parsing
cases['createddate'] = pd.to_datetime(cases['createddate'], errors='coerce')
cases['closeddate'] = pd.to_datetime(cases['closeddate'], errors='coerce')

# Define Window
# "Past four months" from 2023-09-02
# 2023-05-02 to 2023-09-02 (inclusive)
end_date = pd.Timestamp('2023-09-02 23:59:59', tz='UTC')
start_date = pd.Timestamp('2023-05-02 00:00:00', tz='UTC')

# Filter Closed Cases in Window
window_cases = cases[
    (cases['closeddate'] >= start_date) & 
    (cases['closeddate'] <= end_date)
].copy()

# List of target case IDs
target_case_ids = set(window_cases['id'])

# Filter History for these cases
target_history = history[history['caseid__c'].isin(target_case_ids)]

# Identify Single vs Multi Owner
owner_counts = target_history.groupby('caseid__c').size()
single_owner_ids = set(owner_counts[owner_counts == 1].index)
# multi_owner_ids = set(owner_counts[owner_counts > 1].index)

ids_with_history = set(target_history['caseid__c'])
ids_without_history = target_case_ids - ids_with_history
single_owner_ids.update(ids_without_history)

# Calculate Agent Case Counts (Processing Count)
agent_counts = {}

# From history
for _, row in target_history.iterrows():
    agent = row['newvalue__c']
    if pd.isna(agent): continue
    if agent not in agent_counts: agent_counts[agent] = set()
    agent_counts[agent].add(row['caseid__c'])

# From cases without history
for _, row in window_cases[window_cases['id'].isin(ids_without_history)].iterrows():
    agent = row['ownerid']
    if pd.isna(agent): continue
    if agent not in agent_counts: agent_counts[agent] = set()
    agent_counts[agent].add(row['id'])

# Calculate Handle Time for Single Owner Cases
agent_ht_sums = {}
agent_ht_counts = {}

for _, row in window_cases.iterrows():
    cid = row['id']
    if cid in single_owner_ids:
        agent = row['ownerid']
        if pd.isna(agent): continue
        
        ht = (row['closeddate'] - row['createddate']).total_seconds()
        
        if agent not in agent_ht_sums:
            agent_ht_sums[agent] = 0.0
            agent_ht_counts[agent] = 0
        agent_ht_sums[agent] += ht
        agent_ht_counts[agent] += 1

# Compute Averages and Find Best
results = []
for agent, case_set in agent_counts.items():
    if len(case_set) > 1: # Processed > 1 case
        if agent in agent_ht_sums:
            avg_ht = agent_ht_sums[agent] / agent_ht_counts[agent]
            results.append({
                'agent': agent,
                'avg_ht': avg_ht,
                'count_processed': len(case_set),
                'count_ht_cases': agent_ht_counts[agent]
            })

results_df = pd.DataFrame(results).sort_values('avg_ht')

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-82796130940059613': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11405178363707483728': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_function-call-12757248016520783316': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-10431209380168234962': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-661934745513348312': [{'id': 'a04Wt000005322SIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539tVIAQ', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T11:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539v7IAA', 'caseid__c': '500Wt00000DDNYoIAP', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-30T16:03:45.000+0000', 'field__c': 'Case Closed'}], 'var_function-call-8082838188678180397': [{'count': '75'}], 'var_function-call-3161303279279784545': [{'count': '393'}], 'var_function-call-13506550345692657605': 'file_storage/function-call-13506550345692657605.json', 'var_function-call-304691642357648652': 'file_storage/function-call-304691642357648652.json'}

exec(code, env_args)
