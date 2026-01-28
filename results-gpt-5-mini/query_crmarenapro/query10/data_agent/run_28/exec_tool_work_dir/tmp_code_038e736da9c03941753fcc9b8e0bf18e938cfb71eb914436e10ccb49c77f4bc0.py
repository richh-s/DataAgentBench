code = """import json
import pandas as pd

# Load full closed cases data from file
with open(var_call_toPz4JrmcYl5Qqv8Edzu61wk, 'r') as f:
    cases = json.load(f)

df_cases = pd.DataFrame(cases)
# Normalize 'None' strings to None
for col in ['createddate', 'closeddate', 'ownerid', 'id']:
    if col in df_cases.columns:
        df_cases[col] = df_cases[col].replace('None', None)

# parse datetimes with UTC
df_cases['created_dt'] = pd.to_datetime(df_cases['createddate'], errors='coerce', utc=True)
df_cases['closed_dt'] = pd.to_datetime(df_cases['closeddate'], errors='coerce', utc=True)

start = pd.Timestamp('2023-05-02', tz='UTC')
end = pd.Timestamp('2023-09-02', tz='UTC')
# filter closed in period
df_closed = df_cases[df_cases['closed_dt'].notna() & (df_cases['closed_dt'] >= start) & (df_cases['closed_dt'] <= end)].copy()

# Load casehistory rows fetched earlier
df_hist = pd.DataFrame(var_call_N8XGPfnzxupWUgJwIq9Aenln)
if not df_hist.empty:
    df_hist['caseid__c'] = df_hist['caseid__c'].astype(str)
    df_hist['field__c'] = df_hist['field__c'].astype(str)
    df_hist['newvalue__c'] = df_hist['newvalue__c'].replace('None', None)
else:
    df_hist = pd.DataFrame(columns=['caseid__c','field__c','newvalue__c'])

# helper: normalize ids (strip whitespace)
def norm(x):
    if pd.isna(x):
        return None
    return str(x).strip()

df_closed['id_norm'] = df_closed['id'].apply(norm)
df_closed['owner_norm'] = df_closed['ownerid'].apply(norm)

# Determine owner assignment counts per case
owner_counts = {}
owner_assignment_newvals = {}  # caseid -> list of newvalue owners
for caseid in df_closed['id_norm'].tolist():
    rows = df_hist[(df_hist['caseid__c'].apply(lambda x: norm(x)) == caseid) & (df_hist['field__c'].str.contains('Owner', na=False))]
    cnt = len(rows)
    owner_counts[caseid] = cnt
    newvals = [norm(v) for v in rows['newvalue__c'].tolist() if v not in (None, 'None')]
    owner_assignment_newvals[caseid] = newvals

# Build processed cases per agent
processed_cases = {}  # agent -> set(caseid)
for _, row in df_closed.iterrows():
    cid = row['id_norm']
    owner = row['owner_norm']
    # include case.ownerid
    if owner:
        processed_cases.setdefault(owner, set()).add(cid)
    # include any owner assignment newvalue owners
    for nv in owner_assignment_newvals.get(cid, []):
        if nv:
            processed_cases.setdefault(nv, set()).add(cid)

# Compute per-agent handle times for non-transferred cases
agent_handle_times = {}  # agent -> list of seconds
for _, row in df_closed.iterrows():
    cid = row['id_norm']
    owner = row['owner_norm']
    if owner is None:
        continue
    cnt = owner_counts.get(cid, 0)
    # non-transferred cases are those with <=1 owner assignment
    if cnt <= 1:
        if pd.isna(row['created_dt']) or pd.isna(row['closed_dt']):
            continue
        seconds = (row['closed_dt'] - row['created_dt']).total_seconds()
        # only consider if non-negative
        if seconds < 0:
            continue
        agent_handle_times.setdefault(owner, []).append(seconds)

# Prepare results: filter agents with processed >1 and have handle times
candidates = []
for agent, caseset in processed_cases.items():
    if len(caseset) > 1 and agent in agent_handle_times and len(agent_handle_times[agent])>0:
        avg = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
        candidates.append((agent, avg))

# find agent with lowest avg
result_agent = None
if candidates:
    candidates.sort(key=lambda x: x[1])
    result_agent = candidates[0][0]

print("__RESULT__:")
print(json.dumps(result_agent))"""

env_args = {'var_call_8Uvrwqbrji5jX8dMW9bFvXfE': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_NZIO1A2y6kvhSn65Rc3dFZUg': [], 'var_call_rvHjP8lERP1rK9mZIzMHCzOb': [{'id': '500Wt00000DDxSdIAL', 'ownerid': '005Wt000003NJ6gIAG', 'createddate': '2024-05-15T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0ByIAL', 'ownerid': '005Wt000003NGjuIAG', 'createddate': '2024-05-05T10:15:30.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDfYwIAL', 'ownerid': '005Wt000003NIk5IAG', 'createddate': '2024-05-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzz3IAD', 'ownerid': '005Wt000003NFW6IAO', 'createddate': '2024-05-02T09:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE03tIAD', 'ownerid': '005Wt000003NHfzIAG', 'createddate': '2023-12-02T11:30:00.000+0000', 'closeddate': '2023-12-02T16:45:51.000+0000'}, {'id': '500Wt00000DDgLKIA1', 'ownerid': '#005Wt000003NHuUIAW', 'createddate': '2023-11-03T11:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0BxIAL', 'ownerid': '#005Wt000003NGwpIAG', 'createddate': '2023-11-02T10:00:00.000+0000', 'closeddate': '2023-11-02T14:10:33.000+0000'}, {'id': '500Wt00000DDze6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-20T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDyuwIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-10-16T09:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDnt6IAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000'}, {'id': '500Wt00000DDU5iIAH', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000'}, {'id': '500Wt00000DDzW2IAL', 'ownerid': '005Wt000003NIk7IAG', 'createddate': '2023-10-05T09:45:00.000+0000', 'closeddate': '2023-10-05T16:02:30.000+0000'}, {'id': '#500Wt00000DDsG2IAL', 'ownerid': '#005Wt000003NI90IAG', 'createddate': '2023-10-03T14:34:22.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPSZIA5', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000'}, {'id': '#500Wt00000DDZ27IAH', 'ownerid': '005Wt000003NJzVIAW', 'createddate': '2023-10-02T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYUGIA5', 'ownerid': '#005Wt000003NJ6gIAG', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000'}, {'id': '500Wt00000DDNYoIAP', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000'}, {'id': '500Wt00000DE0NGIA1', 'ownerid': '#005Wt000003NHpeIAG', 'createddate': '2023-09-25T10:30:00.000+0000', 'closeddate': '2023-09-26T12:20:45.000+0000'}, {'id': '#500Wt00000DDfFcIAL', 'ownerid': '005Wt000003NFKpIAO', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000'}, {'id': '500Wt00000DDzRBIA1', 'ownerid': '005Wt000003NIc3IAG', 'createddate': '2023-09-20T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0GnIAL', 'ownerid': '#005Wt000003NF1SIAW', 'createddate': '2023-09-18T09:45:00.000+0000', 'closeddate': '2023-09-18T09:53:18.000+0000'}, {'id': '500Wt00000DE078IAD', 'ownerid': '005Wt000003NJTFIA4', 'createddate': '2023-09-16T15:30:00.000+0000', 'closeddate': '2023-09-16T21:27:33.000+0000'}, {'id': '#500Wt00000DDzpNIAT', 'ownerid': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'closeddate': '2023-09-07T16:45:30.000+0000'}, {'id': '#500Wt00000DDzZGIA1', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-09-06T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE00fIAD', 'ownerid': '005Wt000003NIAcIAO', 'createddate': '2023-09-05T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDznlIAD', 'ownerid': '005Wt000003NIwzIAG', 'createddate': '2023-09-04T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDz6FIAT', 'ownerid': '005Wt000003NJhlIAG', 'createddate': '2023-09-03T10:15:00.000+0000', 'closeddate': '2023-09-08T16:25:49.000+0000'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzMMIA1', 'ownerid': '#005Wt000003NDqEIAW', 'createddate': '2023-04-15T09:30:00.000+0000', 'closeddate': '2023-04-15T15:30:16.000+0000'}, {'id': '#500Wt00000DDzvpIAD', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-04-10T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPsPIAX', 'ownerid': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000', 'closeddate': '2023-04-06T11:30:54.000+0000'}, {'id': '#500Wt00000DE0VJIA1', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0FDIA1', 'ownerid': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000', 'closeddate': '2023-03-23T08:12:40.000+0000'}, {'id': '500Wt00000DDyRvIAL', 'ownerid': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzPZIA1', 'ownerid': '#005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000', 'closeddate': '2023-03-18T09:27:15.000+0000'}], 'var_call_toPz4JrmcYl5Qqv8Edzu61wk': 'file_storage/call_toPz4JrmcYl5Qqv8Edzu61wk.json', 'var_call_VLC4nNKd12bPdMfuqe2uG4Yu': ['#500Wt00000DDzscIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzuEIAT', '#500Wt00000DE02HIAT', '500Wt00000DDzsbIAD', '500Wt00000DDepmIAD', '500Wt00000DDyzpIAD'], 'var_call_N8XGPfnzxupWUgJwIq9Aenln': [{'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000534aXIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537LSIAY', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:59:42.000+0000', 'field__c': 'Case Closed'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537TXIAY', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000537a0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:54:02.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537wXIAQ', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt000005390gIAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt000005395XIAQ', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539ALIAY', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-02T13:35:12.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000539LfIAI', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-07-01T19:41:08.000+0000', 'field__c': 'Case Closed'}]}

exec(code, env_args)
