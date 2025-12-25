code = """import json
import pandas as pd
from dateutil import parser
import numpy as np

# Load cases
cases = locals()['var_function-call-3457979809829173481']
# Load history
history_path = locals()['var_function-call-4118261784160134371']

with open(history_path, 'r') as f:
    history = json.load(f)

df_cases = pd.DataFrame(cases)
df_history = pd.DataFrame(history)

# Normalize IDs
def norm_id(x):
    if x and isinstance(x, str):
        return x.lstrip('#')
    return x

df_cases['id_norm'] = df_cases['id'].apply(norm_id)
df_cases['owner_norm'] = df_cases['ownerid'].apply(norm_id)
df_history['caseid_norm'] = df_history['caseid__c'].apply(norm_id)
df_history['newvalue_norm'] = df_history['newvalue__c'].apply(norm_id)

relevant_ids = set(df_cases['id_norm'])
df_hist_rel = df_history[df_history['caseid_norm'].isin(relevant_ids)]

# Agent Case Counts (Processing count)
agent_managed_cases = {} # agent_id -> set(case_ids)

for _, case in df_cases.iterrows():
    cid = case['id_norm']
    current_owner = case['owner_norm']
    
    # Owners from history
    hist_owners = df_hist_rel[df_hist_rel['caseid_norm'] == cid]['newvalue_norm'].unique()
    
    owners = set()
    if current_owner: owners.add(current_owner)
    owners.update(hist_owners)
    
    for o in owners:
        if o not in agent_managed_cases:
            agent_managed_cases[o] = set()
        agent_managed_cases[o].add(cid)

# Handle Times
agent_handle_times = {} # agent_id -> list of durations

window_start = pd.Timestamp('2023-05-02').replace(tzinfo=None)
window_end = pd.Timestamp('2023-09-02').replace(tzinfo=None)

for _, case in df_cases.iterrows():
    cid = case['id_norm']
    
    # Check if closed in window
    c_date_str = case['closeddate']
    if c_date_str == "None" or not c_date_str:
        continue
        
    try:
        closed = parser.parse(c_date_str).replace(tzinfo=None)
        created = parser.parse(case['createddate']).replace(tzinfo=None)
    except:
        continue
        
    if closed < window_start or closed > window_end:
        continue
        
    # Check transfer status
    # Count history records for this case
    case_hist_entries = df_hist_rel[df_hist_rel['caseid_norm'] == cid]
    # We are using 'Owner Assignment' records.
    # Count > 1 => Transferred.
    # Count <= 1 => Not Transferred.
    is_transferred = len(case_hist_entries) > 1
    
    if is_transferred:
        continue
        
    # Valid for handle time
    duration = (closed - created).total_seconds()
    
    # Assign to single owner
    # If 1 history record, use that owner. If 0, use current.
    target_owner = case['owner_norm']
    if len(case_hist_entries) == 1:
        target_owner = case_hist_entries.iloc[0]['newvalue_norm']
    
    if target_owner:
        if target_owner not in agent_handle_times:
            agent_handle_times[target_owner] = []
        agent_handle_times[target_owner].append(duration)

# Final calculation
candidates = []
for agent, cases_managed in agent_managed_cases.items():
    count = len(cases_managed)
    if count > 1:
        if agent in agent_handle_times:
            avg_time = np.mean(agent_handle_times[agent])
            candidates.append({
                "agent": agent,
                "count": count,
                "avg_time": avg_time
            })

if candidates:
    candidates.sort(key=lambda x: x['avg_time'])
    print("__RESULT__:")
    print(json.dumps(candidates[0]['agent']))
else:
    print("__RESULT__:")
    print(json.dumps("No matching agent"))"""

env_args = {'var_function-call-9241346808285847141': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-12556149855108314420': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_function-call-4118261784160134371': 'file_storage/function-call-4118261784160134371.json', 'var_function-call-6205398845989989636': 'No matching agent', 'var_function-call-4495172818801594668': 'debug_done', 'var_function-call-14953190459841128904': {'cases_count': 7, 'history_total': 165, 'relevant_history_count': 5, 'history_counts_sample': [['500Wt00000DDepmIAD', 1], ['500Wt00000DDyzpIAD', 1], ['500Wt00000DDzUPIA1', 1], ['500Wt00000DDzsbIAD', 1], ['500Wt00000DDzuEIAT', 1]], 'agents_gt_1': [], 'eligible_cases_count': 7, 'eligible_cases_sample': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '#500Wt00000DDzscIAD']}, 'var_function-call-3457979809829173481': [{'id': '#500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDNYoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPSZIA5', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDTxbIAH', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NIfFIAW'}, {'id': '500Wt00000DDU5iIAH', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000', 'ownerid': '#005Wt000003NDqEIAW'}, {'id': '500Wt00000DDYUGIA5', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000', 'ownerid': '#005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDZ27IAH', 'createddate': '2023-10-02T10:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJzVIAW'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '#500Wt00000DDfFcIAL', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000', 'ownerid': '005Wt000003NFKpIAO'}, {'id': '#500Wt00000DDfYwIAL', 'createddate': '2024-05-02T09:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIk5IAG'}, {'id': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJppIAG'}, {'id': '500Wt00000DDgLKIA1', 'createddate': '2023-11-03T11:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NHuUIAW'}, {'id': '500Wt00000DDnt6IAD', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DDsG2IAL', 'createddate': '2023-10-03T14:34:22.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NI90IAG'}, {'id': '#500Wt00000DDsG3IAL', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NI5mIAG'}, {'id': '500Wt00000DDxSdIAL', 'createddate': '2024-05-15T14:45:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ6gIAG'}, {'id': '#500Wt00000DDyuwIAD', 'createddate': '2023-10-16T09:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDz6FIAT', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDzRBIA1', 'createddate': '2023-09-20T10:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzW2IAL', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000', 'ownerid': '005Wt000003NIk7IAG'}, {'id': '500Wt00000DDzXdIAL', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJUrIAO'}, {'id': '#500Wt00000DDzZGIA1', 'createddate': '2023-09-06T11:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ8HIAW'}, {'id': '500Wt00000DDzZHIA1', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDze6IAD', 'createddate': '2023-10-20T10:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DDzivIAD', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzkXIAT', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NINVIA4'}, {'id': '500Wt00000DDznlIAD', 'createddate': '2023-09-04T14:20:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIwzIAG'}, {'id': '#500Wt00000DDzpNIAT', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000', 'ownerid': '005Wt000003NINVIA4'}, {'id': '500Wt00000DDzr0IAD', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJcvIAG'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDzz3IAD', 'createddate': '2024-05-02T09:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NFW6IAO'}, {'id': '500Wt00000DE00fIAD', 'createddate': '2023-09-05T10:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIAcIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}, {'id': '#500Wt00000DE03tIAD', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000', 'ownerid': '005Wt000003NHfzIAG'}, {'id': '500Wt00000DE078IAD', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000', 'ownerid': '005Wt000003NJTFIA4'}, {'id': '500Wt00000DE0BxIAL', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000', 'ownerid': '#005Wt000003NGwpIAG'}, {'id': '500Wt00000DE0ByIAL', 'createddate': '2024-05-05T10:15:30.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NGjuIAG'}, {'id': '500Wt00000DE0GnIAL', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000', 'ownerid': '#005Wt000003NF1SIAW'}, {'id': '500Wt00000DE0NGIA1', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000', 'ownerid': '#005Wt000003NHpeIAG'}]}

exec(code, env_args)
