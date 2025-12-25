code = """import json
import pandas as pd
from datetime import datetime

# Load Case Data
cases_list = locals()['var_function-call-13868011625856397802']
df_cases = pd.DataFrame(cases_list)

# Load History Data
history_file = locals()['var_function-call-17706431306088359284']
with open(history_file, 'r') as f:
    history_list = json.load(f)
df_history = pd.DataFrame(history_list)

# Clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#')
    return x

df_cases['id'] = df_cases['id'].apply(clean_id)
df_cases['ownerid'] = df_cases['ownerid'].apply(clean_id)
df_history['caseid__c'] = df_history['caseid__c'].apply(clean_id)
df_history['newvalue__c'] = df_history['newvalue__c'].apply(clean_id)
df_history['oldvalue__c'] = df_history['oldvalue__c'].apply(clean_id)

# Dates
today = pd.Timestamp('2023-09-02').tz_localize('UTC')
four_months_ago = today - pd.DateOffset(months=4)

df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_history['createddate'] = pd.to_datetime(df_history['createddate'])

# Filter Cases Closed in Window
mask_closed = (df_cases['closeddate'] >= four_months_ago) & (df_cases['closeddate'] <= today)
closed_cases_df = df_cases[mask_closed].copy()

# Calculate Handle Time (seconds)
closed_cases_df['handle_time'] = (closed_cases_df['closeddate'] - closed_cases_df['createddate']).dt.total_seconds()

# Identify Transfers (Count in history)
# Note: df_history only contains 'Owner Assignment' records
transfer_counts = df_history['caseid__c'].value_counts()
transferred_case_ids = set(transfer_counts[transfer_counts > 1].index)

# Metric Cases (Single Owner)
metric_cases = closed_cases_df[~closed_cases_df['id'].isin(transferred_case_ids)]
metric_cases = metric_cases[metric_cases['ownerid'].str.startswith('005')]

agent_handle_times = metric_cases.groupby('ownerid')['handle_time'].mean()

# Processed Count
agent_cases = set()

# 1. Closed cases owners
for _, row in closed_cases_df.iterrows():
    if str(row['ownerid']).startswith('005'):
        agent_cases.add((row['ownerid'], row['id']))

# 2. History participants in window
mask_hist_window = (df_history['createddate'] >= four_months_ago) & (df_history['createddate'] <= today)
hist_window = df_history[mask_hist_window]

for _, row in hist_window.iterrows():
    case_id = row['caseid__c']
    new_owner = row['newvalue__c']
    old_owner = row['oldvalue__c']
    
    if str(new_owner).startswith('005'):
        agent_cases.add((new_owner, case_id))
    if str(old_owner).startswith('005'):
        agent_cases.add((old_owner, case_id))

processed_counts = {}
for agent, case in agent_cases:
    processed_counts[agent] = processed_counts.get(agent, 0) + 1

valid_agents = [agent for agent, count in processed_counts.items() if count > 1]

# Find lowest handle time
best_agent = None
min_ht = float('inf')

for agent in valid_agents:
    if agent in agent_handle_times:
        ht = agent_handle_times[agent]
        if ht < min_ht:
            min_ht = ht
            best_agent = agent

print("__RESULT__:")
print(json.dumps(best_agent))"""

env_args = {'var_function-call-17344133026750884577': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-13868011625856397802': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000', 'status': 'Closed '}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000', 'status': 'Closed  '}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000', 'status': 'Closed'}], 'var_function-call-3390573772000670217': [], 'var_function-call-11498057912472810426': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-5565142978560353871': [{'caseid__c': '500Wt00000DDzpNIAT', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000'}, {'caseid__c': '500Wt00000DDfHCIA1', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDZ0VIAX', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000'}, {'caseid__c': '500Wt00000DDQoUIAX', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzm9IAD', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000'}], 'var_function-call-17706431306088359284': 'file_storage/function-call-17706431306088359284.json'}

exec(code, env_args)
