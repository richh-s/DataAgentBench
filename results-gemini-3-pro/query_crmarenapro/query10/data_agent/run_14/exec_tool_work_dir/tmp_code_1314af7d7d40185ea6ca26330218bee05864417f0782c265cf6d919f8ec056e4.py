code = """import json
import pandas as pd

# Load All Cases
cases_path = locals()['var_function-call-8934662887018848188']
with open(cases_path, 'r') as f:
    cases_data = json.load(f)
df_cases = pd.DataFrame(cases_data)

# Clean
df_cases['id'] = df_cases['id'].astype(str).str.strip().str.lstrip('#')
df_cases['ownerid'] = df_cases['ownerid'].astype(str).str.strip()
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'], errors='coerce')

# Define Window
start_dt = pd.Timestamp('2023-05-02 00:00:00').tz_localize('UTC')
end_dt = pd.Timestamp('2023-09-02 23:59:59').tz_localize('UTC')

# Filter Active Cases
def is_active(row):
    created = row['createddate']
    closed = row['closeddate']
    if created > end_dt: return False
    if pd.isna(closed): return True
    if closed < start_dt: return False
    return True

df_cases['active'] = df_cases.apply(is_active, axis=1)
active_cases_ids = set(df_cases[df_cases['active']]['id'])

# Load History
history_path = locals()['var_function-call-5130305458207948578']
with open(history_path, 'r') as f:
    history_data = json.load(f)
df_history = pd.DataFrame(history_data)
if not df_history.empty:
    df_history['caseid__c'] = df_history['caseid__c'].astype(str).str.strip().str.lstrip('#')

# Build Managed Map (Only for active cases)
agent_managed_count = {} 
# From History
if not df_history.empty:
    for _, row in df_history.iterrows():
        cid = row['caseid__c']
        if cid in active_cases_ids:
            old = row['oldvalue__c']
            new = row['newvalue__c']
            if old and str(old).lower() != 'none':
                agent_managed_count.setdefault(str(old).strip(), set()).add(cid)
            if new and str(new).lower() != 'none':
                agent_managed_count.setdefault(str(new).strip(), set()).add(cid)

# From Current Owners
for _, row in df_cases.iterrows():
    if row['active']:
        cid = row['id']
        owner = row['ownerid']
        if owner and str(owner).lower() != 'none':
            agent_managed_count.setdefault(str(owner).strip(), set()).add(cid)

# Candidates
candidates = [a for a, cases in agent_managed_count.items() if len(cases) > 1]

# Calculate Handle Time (Closed in Window)
closed_in_window = df_cases[(df_cases['closeddate'] >= start_dt) & (df_cases['closeddate'] <= end_dt)]

results = []
for agent in candidates:
    agent_cases = closed_in_window[closed_in_window['ownerid'] == agent]
    if agent_cases.empty:
        continue
    durations = (agent_cases['closeddate'] - agent_cases['createddate']).dt.total_seconds()
    avg_time = durations.mean()
    results.append({'agent': agent, 'avg_time': avg_time})

# Result
print("__RESULT__:")
if results:
    best = min(results, key=lambda x: x['avg_time'])
    print(json.dumps(best['agent']))
else:
    print(json.dumps("No Agent Found"))"""

env_args = {'var_function-call-7739635252061129344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2025312579826353346': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-16971736032208043209': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-5130305458207948578': 'file_storage/function-call-5130305458207948578.json', 'var_function-call-14067261926836533561': [], 'var_function-call-13229871005830536108': 'Done', 'var_function-call-608620150156589308': [{'count': '153'}], 'var_function-call-8934662887018848188': 'file_storage/function-call-8934662887018848188.json'}

exec(code, env_args)
