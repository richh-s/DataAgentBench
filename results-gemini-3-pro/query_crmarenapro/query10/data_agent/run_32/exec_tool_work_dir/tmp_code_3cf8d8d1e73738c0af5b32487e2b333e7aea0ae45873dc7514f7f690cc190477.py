code = """import json
import pandas as pd
from datetime import datetime

# Load cases
cases_data = locals()['var_function-call-3515426018230989725']
history_path = locals()['var_function-call-724238365973199859']
with open(history_path, 'r') as f:
    history_data = json.load(f)

df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

relevant_case_ids = set(df_cases['id'].unique())
df_history_filtered = df_history[df_history['caseid__c'].isin(relevant_case_ids)].copy()

print(f"Total Cases: {len(df_cases)}")
print(f"Total History Records: {len(df_history)}")
print(f"Filtered History Records: {len(df_history_filtered)}")

agent_managed = {}
for _, row in df_cases.iterrows():
    c_id = row['id']
    owner = row['ownerid']
    if owner not in agent_managed: agent_managed[owner] = set()
    agent_managed[owner].add(c_id)

for _, row in df_history_filtered.iterrows():
    c_id = row['caseid__c']
    new_owner = row['newvalue__c']
    old_owner = row['oldvalue__c']
    if new_owner and new_owner != 'None':
        if new_owner not in agent_managed: agent_managed[new_owner] = set()
        agent_managed[new_owner].add(c_id)
    if old_owner and old_owner != 'None':
        if old_owner not in agent_managed: agent_managed[old_owner] = set()
        agent_managed[old_owner].add(c_id)

print("Agent Managed Counts:")
for k, v in agent_managed.items():
    print(f"{k}: {len(v)}")

# Check handle times attribution
agent_closers = df_cases['ownerid'].value_counts()
print("Closers (from Case table):")
print(agent_closers)

print("__RESULT__:")
print(json.dumps("debug done"))"""

env_args = {'var_function-call-13710148199737365862': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-3515426018230989725': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-12924332762788559106': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-554246957191354409': [{'count': '7'}], 'var_function-call-724238365973199859': 'file_storage/function-call-724238365973199859.json', 'var_function-call-4325308466962925836': []}

exec(code, env_args)
