code = """import pandas as pd
import json

# Load previous results
cases_data = locals()['var_function-call-4442720613570255940']
history_file = locals()['var_function-call-4132599317159768779']

cases = pd.DataFrame(cases_data)
with open(history_file) as f:
    history = pd.DataFrame(json.load(f))

def clean_id(x):
    if x is None: return None
    s = str(x).strip()
    if s.startswith('#'): s = s[1:]
    if s == 'None': return None
    return s

cases['id'] = cases['id'].apply(clean_id)
cases['ownerid'] = cases['ownerid'].apply(clean_id)
history['caseid__c'] = history['caseid__c'].apply(clean_id)
history['oldvalue__c'] = history['oldvalue__c'].apply(clean_id)
history['newvalue__c'] = history['newvalue__c'].apply(clean_id)

relevant_case_ids = set(cases['id'].unique())
history = history[history['caseid__c'].isin(relevant_case_ids)]
grouped_history = history.groupby('caseid__c')

agent_case_counts = {}
agent_handle_times = {}

for idx, row in cases.iterrows():
    case_id = row['id']
    current_owner = row['ownerid']
    owners = {current_owner}
    is_transferred = False
    
    if case_id in grouped_history.groups:
        hist_entries = grouped_history.get_group(case_id)
        if len(hist_entries) > 1:
            is_transferred = True
        for _, h_row in hist_entries.iterrows():
            if h_row['oldvalue__c']: owners.add(h_row['oldvalue__c'])
            if h_row['newvalue__c']: owners.add(h_row['newvalue__c'])
            
    for agent in owners:
        agent_case_counts[agent] = agent_case_counts.get(agent, 0) + 1
        
    if not is_transferred:
        created = pd.to_datetime(row['createddate'])
        closed = pd.to_datetime(row['closeddate'])
        duration = (closed - created).total_seconds()
        if current_owner not in agent_handle_times: agent_handle_times[current_owner] = []
        agent_handle_times[current_owner].append(duration)

debug_info = {
    "num_cases": len(cases),
    "sample_case_counts": list(agent_case_counts.items())[:10],
    "sample_handle_times_keys": list(agent_handle_times.keys())[:10],
    "max_count": max(agent_case_counts.values()) if agent_case_counts else 0,
    "agents_with_stats": len(agent_handle_times)
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1717150342863390368': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8867289235392817470': [{'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG'}, {'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW'}, {'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None'}, {'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None'}], 'var_function-call-4442720613570255940': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-4132599317159768779': 'file_storage/function-call-4132599317159768779.json', 'var_function-call-9563550674464290533': None}

exec(code, env_args)
