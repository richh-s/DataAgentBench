code = """import json
import pandas as pd

# Load data
cases_file = locals()['var_function-call-10647056009092713491']
history_file = locals()['var_function-call-16697359687568498881']

with open(cases_file, 'r') as f:
    cases_data = json.load(f)

with open(history_file, 'r') as f:
    history_data = json.load(f)

df_case = pd.DataFrame(cases_data)
df_hist = pd.DataFrame(history_data)

# Cleaning
def clean_id(x):
    if pd.isna(x): return x
    x = str(x).strip()
    if x.startswith('#'): return x[1:]
    return x

df_case['id'] = df_case['id'].apply(clean_id)
df_case['ownerid'] = df_case['ownerid'].apply(clean_id)
df_hist['caseid__c'] = df_hist['caseid__c'].apply(clean_id)
df_hist['newvalue__c'] = df_hist['newvalue__c'].apply(clean_id)

# Dates
# Handle "None" strings if present
df_case['createddate'] = pd.to_datetime(df_case['createddate'], errors='coerce')
df_case['closeddate'] = pd.to_datetime(df_case['closeddate'], errors='coerce')

start_window = pd.Timestamp('2023-05-02').tz_localize('UTC')
end_window = pd.Timestamp('2023-09-02').tz_localize('UTC') + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

# Map Case -> List of Agents (Ever)
case_agents = {}
# Initialize with current owner
for _, row in df_case.iterrows():
    cid = row['id']
    oid = row['ownerid']
    if pd.notna(oid):
        if cid not in case_agents: case_agents[cid] = set()
        case_agents[cid].add(oid)

# Add history owners
# We must use ALL history, not just window-filtered history, to identify "Processed" agents correctly.
for _, row in df_hist.iterrows():
    cid = row['caseid__c']
    nv = row['newvalue__c']
    if pd.notna(nv):
        if cid in case_agents: # Only if case exists in DB
            case_agents[cid].add(nv)

# Determine Transferred Status (for Handle Time calculation)
# Count distinct agents per case? Or count history lines?
# Prompt: "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
# Let's use history lines count.
assignment_counts = df_hist[df_hist['field__c'] == 'Owner Assignment'].groupby('caseid__c').size()
# Map
case_is_transferred = {}
for cid in df_case['id']:
    count = assignment_counts.get(cid, 0)
    # If count > 1 -> Transferred
    # If count <= 1 -> Not Transferred (0 or 1)
    if count > 1:
        case_is_transferred[cid] = True
    else:
        case_is_transferred[cid] = False

# 1. Calculate Processed Count (Active in Window)
agent_processed_count = {}

for _, row in df_case.iterrows():
    cid = row['id']
    created = row['createddate']
    closed = row['closeddate']
    
    # Check Active in Window
    # Active if Created <= EndWindow AND (Closed >= StartWindow OR Closed is NaT)
    is_active = False
    if pd.notna(created) and created <= end_window:
        if pd.isna(closed) or closed >= start_window:
            is_active = True
            
    if is_active:
        # Add to agents
        agents = case_agents.get(cid, set())
        for agent in agents:
            agent_processed_count[agent] = agent_processed_count.get(agent, 0) + 1

# 2. Calculate Handle Time (Closed in Window, Not Transferred)
agent_durations = {} # {agent: [seconds, ...]}

for _, row in df_case.iterrows():
    cid = row['id']
    closed = row['closeddate']
    created = row['createddate']
    
    # Check Closed in Window
    if pd.notna(closed) and closed >= start_window and closed <= end_window:
        # Check Not Transferred
        if not case_is_transferred.get(cid, False):
            # Calculate Duration
            duration = (closed - created).total_seconds()
            owner = row['ownerid']
            
            if owner not in agent_durations:
                agent_durations[owner] = []
            agent_durations[owner].append(duration)

# 3. Filter and Find Min
results = []
for agent, count in agent_processed_count.items():
    if count > 1:
        # Check if agent has handle time stats
        if agent in agent_durations and len(agent_durations[agent]) > 0:
            avg = sum(agent_durations[agent]) / len(agent_durations[agent])
            results.append({
                'agent': agent,
                'avg_seconds': avg,
                'count_processed': count,
                'count_scored': len(agent_durations[agent])
            })

results.sort(key=lambda x: x['avg_seconds'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-9368097647540502280': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_function-call-9368097647540500261': [], 'var_function-call-11179191046412315998': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-16697359687568502204': [{'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}], 'var_function-call-16697359687568498881': 'file_storage/function-call-16697359687568498881.json', 'var_function-call-13683469007934532295': [], 'var_function-call-10511093459739645858': {'total_cases_in_db': 21, 'cases_in_window': 7, 'sample_case_ids': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD'], 'history_records': 165, 'history_sample_ids': ['500Wt00000DDzpNIAT', '500Wt00000DDfHCIA1', '500Wt00000DDZ0VIAX', '500Wt00000DDQoUIAX', '500Wt00000DDzm9IAD']}, 'var_function-call-16181121753062401402': {'cases': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'closeddate_str': '2023-07-01'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'closeddate_str': '2023-08-15'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'closeddate_str': '2023-05-10'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'closeddate_str': '2023-06-30'}, {'id': '500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'closeddate_str': '2023-05-03'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'closeddate_str': '2023-06-02'}, {'id': '500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'closeddate_str': '2023-06-03'}], 'history': [{'caseid__c': '500Wt00000DDzscIAD', 'newvalue__c': '005Wt000003NEtOIAW'}, {'caseid__c': '500Wt00000DDepmIAD', 'newvalue__c': '005Wt000003NJufIAG'}, {'caseid__c': '500Wt00000DDzUPIA1', 'newvalue__c': '005Wt000003NDqDIAW'}, {'caseid__c': '500Wt00000DDzuEIAT', 'newvalue__c': '005Wt000003NJJaIAO'}, {'caseid__c': '500Wt00000DDyzpIAD', 'newvalue__c': '005Wt000003NJGLIA4'}, {'caseid__c': '500Wt00000DDzsbIAD', 'newvalue__c': '005Wt000003NJD9IAO'}, {'caseid__c': '500Wt00000DE02HIAT', 'newvalue__c': '005Wt000003NIddIAG'}]}, 'var_function-call-5374195175318566352': [{'count': '153'}], 'var_function-call-5374195175318568031': [{'count': '21'}], 'var_function-call-10647056009092713491': 'file_storage/function-call-10647056009092713491.json'}

exec(code, env_args)
