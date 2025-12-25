code = """import pandas as pd
import json

# Load data
cases_data = locals()['var_function-call-14753310501971979415']
history_file = locals()['var_function-call-5340587037609171017']

with open(history_file, 'r') as f:
    history_data = json.load(f)

cases_df = pd.DataFrame(cases_data)
history_df = pd.DataFrame(history_data)

def clean_id(x):
    if pd.isna(x) or x == 'None': return None
    x = str(x).strip()
    if x.startswith('#'): x = x[1:]
    return x

cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
history_df['oldvalue__c'] = history_df['oldvalue__c'].apply(clean_id)
history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

# Filter logic (simplified)
start_date = pd.Timestamp('2023-05-02', tz='UTC')
end_date = pd.Timestamp('2023-09-02', tz='UTC')
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])
if cases_df['closeddate'].dt.tz is None:
    cases_df['closeddate'] = cases_df['closeddate'].dt.tz_localize('UTC')
else:
    cases_df['closeddate'] = cases_df['closeddate'].dt.tz_convert('UTC')

closed_cases = cases_df[
    (cases_df['closeddate'] >= start_date) & 
    (cases_df['closeddate'] <= end_date)
]

print("__RESULT__:")
debug_output = {}
debug_output['closed_cases_count'] = len(closed_cases)
debug_output['closed_cases_ids'] = closed_cases['id'].tolist()

# Owners per case
case_owners = {}
for cid in closed_cases['id']:
    owners = set()
    # Current
    curr = closed_cases[closed_cases['id'] == cid]['ownerid'].iloc[0]
    owners.add(curr)
    # History
    hist = history_df[history_df['caseid__c'] == cid]
    for _, row in hist.iterrows():
        if row['oldvalue__c']: owners.add(row['oldvalue__c'])
        if row['newvalue__c']: owners.add(row['newvalue__c'])
    case_owners[cid] = list(owners)

debug_output['case_owners'] = case_owners

# Agent Counts
agent_counts = {}
for cid, owners in case_owners.items():
    for ag in owners:
        agent_counts[ag] = agent_counts.get(ag, 0) + 1

debug_output['agent_counts'] = agent_counts

print(json.dumps(debug_output))"""

env_args = {'var_function-call-5914537462471561066': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14753310501971979415': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10623675109369733718': [], 'var_function-call-6935807388844192585': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-5340587037609171017': 'file_storage/function-call-5340587037609171017.json', 'var_function-call-9706460253253253793': {'final_answer': 'No eligible agents found', 'debug_info': []}}

exec(code, env_args)
