code = """import pandas as pd
import json

# Load data
cases_file = locals()['var_function-call-3141734985280865475']
history_file = locals()['var_function-call-5340587037609171017']

with open(cases_file, 'r') as f:
    cases_data = json.load(f)

with open(history_file, 'r') as f:
    history_data = json.load(f)

cases_df = pd.DataFrame(cases_data)
history_df = pd.DataFrame(history_data)

# Cleaning
def clean_id(x):
    if pd.isna(x) or str(x) == 'None': return None
    x = str(x).strip()
    if x.startswith('#'): x = x[1:]
    return x

if not cases_df.empty:
    cases_df['id'] = cases_df['id'].apply(clean_id)
    cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
    # Handle "None" strings by coercing
    cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], errors='coerce')
    cases_df['createddate'] = pd.to_datetime(cases_df['createddate'], errors='coerce')

if not history_df.empty:
    history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
    history_df['oldvalue__c'] = history_df['oldvalue__c'].apply(clean_id)
    history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

# 1. Build Agent Processed Counts (All Cases)
agent_processed_counts = {}
history_owners = {}

if not history_df.empty:
    for _, row in history_df.iterrows():
        cid = row['caseid__c']
        if cid not in history_owners: history_owners[cid] = set()
        if row['oldvalue__c']: history_owners[cid].add(row['oldvalue__c'])
        if row['newvalue__c']: history_owners[cid].add(row['newvalue__c'])

if not cases_df.empty:
    for _, row in cases_df.iterrows():
        cid = row['id']
        processors = set()
        if row['ownerid']: processors.add(row['ownerid'])
        if cid in history_owners: processors.update(history_owners[cid])
        
        for ag in processors:
            agent_processed_counts[ag] = agent_processed_counts.get(ag, 0) + 1

# 2. Build Handle Times (Windowed)
start_date = pd.Timestamp('2023-05-02', tz='UTC')
end_date = pd.Timestamp('2023-09-02', tz='UTC')

# Fix TZ
if not cases_df.empty:
    if cases_df['closeddate'].dt.tz is None:
        cases_df['closeddate'] = cases_df['closeddate'].dt.tz_localize('UTC')
    else:
        cases_df['closeddate'] = cases_df['closeddate'].dt.tz_convert('UTC')
        
    if cases_df['createddate'].dt.tz is None:
        cases_df['createddate'] = cases_df['createddate'].dt.tz_localize('UTC')
    else:
        cases_df['createddate'] = cases_df['createddate'].dt.tz_convert('UTC')

closed_cases_window = cases_df[
    (cases_df['closeddate'] >= start_date) & 
    (cases_df['closeddate'] <= end_date)
]

agent_handle_times = {}
for _, row in closed_cases_window.iterrows():
    ag = row['ownerid']
    # Calculate duration (closed - created)
    # Ensure both are not NaT
    if pd.notna(row['closeddate']) and pd.notna(row['createddate']):
        duration = (row['closeddate'] - row['createddate']).total_seconds()
        
        if ag:
            if ag not in agent_handle_times: agent_handle_times[ag] = []
            agent_handle_times[ag].append(duration)

# 3. Combine and Filter
results = []
for agent, times in agent_handle_times.items():
    p_count = agent_processed_counts.get(agent, 0)
    if p_count > 1:
        avg = sum(times) / len(times)
        results.append({'AgentId': agent, 'AvgTime': avg, 'Count': p_count})

results_df = pd.DataFrame(results)
if not results_df.empty:
    best = results_df.sort_values('AvgTime').iloc[0]
    final_answer = best['AgentId']
    debug_info = results_df.sort_values('AvgTime').head(5).to_dict(orient='records')
else:
    final_answer = "No eligible agents found"
    debug_info = []

print("__RESULT__:")
print(json.dumps({
    "final_answer": final_answer,
    "debug_info": debug_info
}))"""

env_args = {'var_function-call-5914537462471561066': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14753310501971979415': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10623675109369733718': [], 'var_function-call-6935807388844192585': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-5340587037609171017': 'file_storage/function-call-5340587037609171017.json', 'var_function-call-9706460253253253793': {'final_answer': 'No eligible agents found', 'debug_info': []}, 'var_function-call-3536005288999288306': {'closed_cases_count': 7, 'closed_cases_ids': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'case_owners': {'500Wt00000DDepmIAD': ['005Wt000003NJufIAG'], '500Wt00000DDyzpIAD': ['005Wt000003NJGLIA4'], '500Wt00000DDzUPIA1': ['005Wt000003NDqDIAW'], '500Wt00000DDzsbIAD': ['005Wt000003NJD9IAO'], '500Wt00000DDzscIAD': ['005Wt000003NEtOIAW'], '500Wt00000DDzuEIAT': ['005Wt000003NJJaIAO'], '500Wt00000DE02HIAT': ['005Wt000003NIddIAG']}, 'agent_counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}}, 'var_function-call-3141734985280865475': 'file_storage/function-call-3141734985280865475.json'}

exec(code, env_args)
