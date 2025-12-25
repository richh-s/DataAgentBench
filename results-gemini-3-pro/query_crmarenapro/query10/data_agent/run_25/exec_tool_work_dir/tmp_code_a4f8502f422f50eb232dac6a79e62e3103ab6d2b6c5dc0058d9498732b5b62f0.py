code = """import pandas as pd
import json

# Load data
cases_data = locals()['var_function-call-4469204960662346704']
history_file = locals()['var_function-call-670256500848698491']

with open(history_file, 'r') as f:
    history_data = json.load(f)

df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

# Cleaning
def clean_id(x):
    if pd.isna(x) or x == 'None':
        return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

df_cases['id'] = df_cases['id'].apply(clean_id)
df_cases['ownerid'] = df_cases['ownerid'].apply(clean_id)
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

df_history['caseid__c'] = df_history['caseid__c'].apply(clean_id)
df_history['oldvalue__c'] = df_history['oldvalue__c'].apply(clean_id)
df_history['newvalue__c'] = df_history['newvalue__c'].apply(clean_id)

# Define Window
start_date = pd.Timestamp('2023-05-02').tz_localize('UTC')
end_date = pd.Timestamp('2023-09-02').tz_localize('UTC')

# 1. Determine "Processors" for each case in df_cases
# We use all fetched cases to determine the "processing count".
case_processors = {}

# Init with current owner
for _, row in df_cases.iterrows():
    cid = row['id']
    oid = row['ownerid']
    if cid not in case_processors:
        case_processors[cid] = set()
    if oid:
        case_processors[cid].add(oid)

# Add from history
relevant_case_ids = set(df_cases['id'].unique())
df_history_rel = df_history[df_history['caseid__c'].isin(relevant_case_ids)]

for _, row in df_history_rel.iterrows():
    cid = row['caseid__c']
    old_v = row['oldvalue__c']
    new_v = row['newvalue__c']
    
    if cid in case_processors:
        if old_v:
            case_processors[cid].add(old_v)
        if new_v:
            case_processors[cid].add(new_v)

# Count cases processed per agent
agent_case_counts = {}
for cid, agents in case_processors.items():
    for agent in agents:
        agent_case_counts[agent] = agent_case_counts.get(agent, 0) + 1

# 2. Calculate Handle Time Stats
# Only for cases CLOSED in the window
mask_closed = (df_cases['closeddate'] >= start_date) & (df_cases['closeddate'] <= end_date)
df_closed = df_cases[mask_closed].copy()

df_closed['handle_time'] = (df_closed['closeddate'] - df_closed['createddate']).dt.total_seconds()

agent_handle_times = {} # list of times

for _, row in df_closed.iterrows():
    agent = row['ownerid']
    time = row['handle_time']
    if agent:
        if agent not in agent_handle_times:
            agent_handle_times[agent] = []
        agent_handle_times[agent].append(time)

# 3. Combine
results = []
for agent, times in agent_handle_times.items():
    count = agent_case_counts.get(agent, 0)
    # Filter: processing > 1 case
    if count > 1:
        avg_time = sum(times) / len(times)
        results.append({
            'agent_id': agent,
            'avg_time': avg_time,
            'processed_count': count,
            'closed_count': len(times)
        })

results_df = pd.DataFrame(results).sort_values(by='avg_time')

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-9776892701324455047': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10958570626037852530': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10769889240167148629': [{'count': '153'}], 'var_function-call-1350100862477643396': [{'min': '2020-07-05T09:51:05.000+0000', 'max': '2023-12-02T16:45:51.000+0000'}], 'var_function-call-10171662404576225263': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-670256500848698491': 'file_storage/function-call-670256500848698491.json', 'var_function-call-9782903921279051320': {'case_processors': {'500Wt00000DDepmIAD': ['005Wt000003NJufIAG'], '500Wt00000DDyzpIAD': ['005Wt000003NJGLIA4'], '500Wt00000DDzUPIA1': ['005Wt000003NDqDIAW'], '500Wt00000DDzsbIAD': ['005Wt000003NJD9IAO'], '500Wt00000DDzscIAD': ['005Wt000003NEtOIAW'], '500Wt00000DDzuEIAT': ['005Wt000003NJJaIAO'], '500Wt00000DE02HIAT': ['005Wt000003NIddIAG']}, 'agent_case_counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}, 'agent_handle_times_count': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}, 'results': []}, 'var_function-call-4469204960662346704': [{'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW', 'createddate': '2023-10-02T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG', 'createddate': '2024-05-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW', 'createddate': '2023-11-03T11:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG', 'createddate': '2023-10-03T14:34:22.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2024-05-15T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-10-16T09:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-20T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-09-06T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-20T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2023-09-04T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2024-05-02T09:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO', 'createddate': '2023-09-05T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG', 'createddate': '2024-05-05T10:15:30.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}]}

exec(code, env_args)
