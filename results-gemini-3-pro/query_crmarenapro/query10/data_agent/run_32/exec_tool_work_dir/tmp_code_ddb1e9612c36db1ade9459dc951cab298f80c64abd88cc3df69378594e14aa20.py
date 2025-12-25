code = """import json
import pandas as pd
from datetime import datetime

cases_data = locals()['var_function-call-3515426018230989725']
history_path = locals()['var_function-call-724238365973199859']
with open(history_path, 'r') as f:
    history_data = json.load(f)

df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

relevant_case_ids = set(df_cases['id'].unique())
df_history_filtered = df_history[df_history['caseid__c'].isin(relevant_case_ids)].copy()

debug_info = {}
debug_info['num_cases'] = len(df_cases)
debug_info['num_history_filtered'] = len(df_history_filtered)
debug_info['case_ids'] = list(relevant_case_ids)

agent_managed = {}
# Init with current owner
for _, row in df_cases.iterrows():
    c_id = row['id']
    owner = row['ownerid']
    if owner not in agent_managed: agent_managed[owner] = set()
    agent_managed[owner].add(c_id)

# Add history
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

debug_info['agent_managed_counts'] = {k: len(v) for k, v in agent_managed.items()}

# Check Handle Times
agent_handle_times = {} # AgentID -> List of durations
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")

for _, row in df_cases.iterrows():
    owner = row['ownerid']
    c_created = parse_date(row['createddate'])
    c_closed = parse_date(row['closeddate'])
    duration = (c_closed - c_created).total_seconds()
    
    if owner not in agent_handle_times:
        agent_handle_times[owner] = []
    agent_handle_times[owner].append(duration)

debug_info['agent_closers'] = list(agent_handle_times.keys())
debug_info['multi_managed_agents'] = [k for k, v in agent_managed.items() if len(v) > 1]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-13710148199737365862': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-3515426018230989725': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-12924332762788559106': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-554246957191354409': [{'count': '7'}], 'var_function-call-724238365973199859': 'file_storage/function-call-724238365973199859.json', 'var_function-call-4325308466962925836': [], 'var_function-call-2501105650080026199': 'debug done'}

exec(code, env_args)
