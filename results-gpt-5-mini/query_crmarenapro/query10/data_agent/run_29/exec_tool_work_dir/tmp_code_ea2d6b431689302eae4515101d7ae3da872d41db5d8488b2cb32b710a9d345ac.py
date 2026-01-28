code = """import json
import pandas as pd
from datetime import datetime, timezone

# Load variables from storage
casehistory_path = var_call_MTNrM9wTFodWcZfgzDV5mUR8  # file path for large result
cases_list = var_call_G8tonwqeibXgpiCyC3IqMrEZ

# Read casehistory JSON file
with open(casehistory_path, 'r') as f:
    casehistory = json.load(f)

# Create DataFrames
ch = pd.DataFrame(casehistory)
cases = pd.DataFrame(cases_list)

# Helper clean functions
def clean_id(x):
    if x is None:
        return None
    x = str(x).strip()
    if x == 'None' or x == '':
        return None
    # remove leading hashes
    return x.lstrip('#').strip()

# Clean case ids and agent ids in casehistory
if not ch.empty:
    ch['caseid__c'] = ch['caseid__c'].map(clean_id)
    ch['newvalue__c'] = ch['newvalue__c'].map(clean_id)
    ch['oldvalue__c'] = ch['oldvalue__c'].map(clean_id)
    ch['field__c'] = ch['field__c'].astype(str).str.strip()
else:
    ch = pd.DataFrame(columns=['caseid__c','newvalue__c','oldvalue__c','field__c','createddate'])

# Clean cases
if not cases.empty:
    cases['id'] = cases['id'].map(clean_id)
    # normalize date strings and convert to datetime or None
    def parse_dt(x):
        if x is None:
            return None
        s = str(x).strip()
        if s == '' or s == 'None' or s.lower() == 'none':
            return None
        # many timestamps like 2023-07-02T11:00:00.000+0000
        try:
            # Remove fractional seconds beyond microseconds if present
            # pandas can parse ISO with timezone offset
            return pd.to_datetime(s)
        except Exception:
            try:
                return pd.to_datetime(s.split('.')[0])
            except Exception:
                return None

    cases['created_dt'] = cases['createddate'].map(parse_dt)
    cases['closed_dt'] = cases['closeddate'].map(parse_dt)
    cases['ownerid'] = cases['ownerid'].map(clean_id)
else:
    cases = pd.DataFrame(columns=['id','created_dt','closed_dt','ownerid'])

# Define period: last four months from 2023-09-02 => start 2023-05-02 00:00:00, end 2023-09-02 23:59:59
start = pd.to_datetime('2023-05-02T00:00:00')
end = pd.to_datetime('2023-09-02T23:59:59')

# Filter closed cases within period
cases_closed = cases[(cases['closed_dt'].notnull()) & (cases['closed_dt'] >= start) & (cases['closed_dt'] <= end)].copy()

# Build owner assignment events from casehistory where field contains 'owner'
ch_owner = ch[ch['field__c'].str.lower().str.contains('owner', na=False)].copy()

# Only consider casehistory entries for cases in closed period
ch_owner = ch_owner[ch_owner['caseid__c'].isin(cases_closed['id'])]

# Count owner assignment events per case
owner_assign_counts = ch_owner.groupby('caseid__c').size().to_frame('owner_assignments')

# Non-transferred cases: owner_assignments <=1 (including 0)
cases_closed = cases_closed.merge(owner_assign_counts, how='left', left_on='id', right_on='caseid__c')
cases_closed['owner_assignments'] = cases_closed['owner_assignments'].fillna(0).astype(int)
non_transferred = cases_closed[cases_closed['owner_assignments'] <= 1].copy()

# Compute handle time seconds for non-transferred cases
non_transferred['handle_seconds'] = (non_transferred['closed_dt'] - non_transferred['created_dt']).dt.total_seconds()
# Drop cases with missing datetimes or negative
non_transferred = non_transferred[non_transferred['handle_seconds'].notnull()]
non_transferred = non_transferred[non_transferred['handle_seconds'] >= 0]

# For processed counts per agent: union of casehistory newvalue agents and case ownerid for closed cases (per policy applies to both initial and transferred)
# Build mapping agent -> set(case ids)
from collections import defaultdict
agent_cases = defaultdict(set)

# Add ownerid from cases_closed
for _, row in cases_closed.iterrows():
    aid = row['ownerid']
    cid = row['id']
    if aid:
        agent_cases[aid].add(cid)

# Add newvalue agents from casehistory owner events (for closed cases)
for _, row in ch_owner.iterrows():
    aid = row['newvalue__c']
    cid = row['caseid__c']
    if aid and cid:
        agent_cases[aid].add(cid)

# Compute processed_count per agent
agent_counts = {aid: len(cset) for aid, cset in agent_cases.items()}

# Filter agents processed more than one case
agents_gt1 = {aid:cnt for aid,cnt in agent_counts.items() if cnt > 1}

# Compute avg handle time per agent using non_transferred cases and agent = case.ownerid
avg_ht = non_transferred.groupby('ownerid')['handle_seconds'].mean().to_dict()

# Find agents present in both sets
candidates = []
for aid in agents_gt1:
    if aid in avg_ht:
        candidates.append((aid, avg_ht[aid]))

# Find min avg
result_agent = None
if candidates:
    candidates.sort(key=lambda x: x[1])
    result_agent = candidates[0][0]

# Prepare output as JSON string (or empty string if none)
out = json.dumps(result_agent if result_agent is not None else "")
print("__RESULT__:")
print(out)"""

env_args = {'var_call_coI1PWUMvMm3JDLNncoRnp2a': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_x66HXGKuFEaINz6BLeUcWu3Z': [], 'var_call_veofjhMrdYeXGjMnGEZ76E9B': [], 'var_call_G8tonwqeibXgpiCyC3IqMrEZ': [{'id': '#500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ0DIAW', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJWTIA4', 'status': 'Waiting on Customer   '}, {'id': '500Wt00000DDNYoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'ownerid': '005Wt000003NIc3IAG', 'status': 'Closed'}, {'id': '500Wt00000DDPIsIAP', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'ownerid': '#005Wt000003NEzqIAG', 'status': 'Closed '}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'ownerid': '005Wt000003NISLIA4', 'status': 'Closed'}, {'id': '500Wt00000DDPSZIA5', 'createddate': '2023-10-02T14:15:00.000+0000', 'closeddate': '2023-10-02T14:45:22.000+0000', 'ownerid': '005Wt000003NJhlIAG', 'status': 'Closed'}, {'id': '500Wt00000DDPZ0IAP', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJD9IAO', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDPsOIAX', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIk7IAG', 'status': 'Working'}, {'id': '500Wt00000DDPsPIAX', 'createddate': '2023-04-05T17:51:00.000+0000', 'closeddate': '2023-04-06T11:30:54.000+0000', 'ownerid': '005Wt000003NJ8HIAW', 'status': 'Closed'}, {'id': '500Wt00000DDQRsIAP', 'createddate': '2023-03-08T06:49:00.000+0000', 'closeddate': '2023-03-08T07:07:30.000+0000', 'ownerid': '#005Wt000003NFKoIAO', 'status': 'Closed'}, {'id': '500Wt00000DDQoUIAX', 'createddate': '2021-09-15T10:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJcwIAG', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NFhOIAW', 'status': 'Waiting on Customer  '}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'closeddate': '2020-09-05T18:15:21.000+0000', 'ownerid': '005Wt000003NItlIAG', 'status': 'Closed'}, {'id': '500Wt00000DDRW0IAP', 'createddate': '2021-06-03T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NFKpIAO', 'status': 'Working'}, {'id': '#500Wt00000DDTEQIA5', 'createddate': '2022-03-02T10:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJ9tIAG', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDTERIA5', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000', 'ownerid': '005Wt000003NIk5IAG', 'status': 'Closed'}, {'id': '500Wt00000DDTHfIAP', 'createddate': '2021-10-05T14:45:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJeXIAW', 'status': 'Working'}, {'id': '500Wt00000DDTxbIAH', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NIfFIAW', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDU5iIAH', 'createddate': '2023-10-15T09:15:47.000+0000', 'closeddate': '2023-10-15T14:23:52.000+0000', 'ownerid': '#005Wt000003NDqEIAW', 'status': 'Closed'}, {'id': '500Wt00000DDYUGIA5', 'createddate': '2023-10-02T09:15:00.000+0000', 'closeddate': '2023-10-02T09:32:45.000+0000', 'ownerid': '#005Wt000003NJ6gIAG', 'status': 'Closed'}, {'id': '#500Wt00000DDYdwIAH', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000', 'ownerid': '#005Wt000003NJbJIAW', 'status': 'Closed'}, {'id': '500Wt00000DDzRCIA1', 'createddate': '2021-09-20T15:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NHuUIAW', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDYipIAH', 'createddate': '2022-03-15T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJLBIA4', 'status': 'Waiting on Customer  '}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJLBIA4', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDYpHIAX', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000', 'ownerid': '005Wt000003NJ6gIAG', 'status': 'Closed'}, {'id': '500Wt00000DDZ0VIAX', 'createddate': '2021-10-15T13:46:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NEtOIAW', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDZ27IAH', 'createddate': '2023-10-02T10:15:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJzVIAW', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDZ5LIAX', 'createddate': '2021-11-11T12:13:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NHfyIAG', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDZJuIAP', 'createddate': '2023-01-18T14:45:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NJoDIAW', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'closeddate': '2020-07-05T09:51:05.000+0000', 'ownerid': '#005Wt000003NJ6gIAG', 'status': 'Closed'}, {'id': '#500Wt00000DDZtKIAX', 'createddate': '2023-01-04T08:47:00.000+0000', 'closeddate': '2023-01-04T12:19:08.000+0000', 'ownerid': '005Wt000003NINVIA4', 'status': 'Closed'}, {'id': '500Wt00000DDZtLIAX', 'createddate': '2022-05-15T14:00:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NGjuIAG', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NIYnIAO', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG', 'status': 'Closed'}, {'id': '#500Wt00000DDet1IAD', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000', 'ownerid': '005Wt000003NH3GIAW', 'status': 'Closed'}, {'id': '#500Wt00000DDfFcIAL', 'createddate': '2023-09-22T08:28:00.000+0000', 'closeddate': '2023-09-22T08:43:27.000+0000', 'ownerid': '005Wt000003NFKpIAO', 'status': 'Closed'}, {'id': '500Wt00000DDfHCIA1', 'createddate': '2021-07-23T11:00:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIXBIA4', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDfYwIAL', 'createddate': '2024-05-02T09:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NIk5IAG', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDfYxIAL', 'createddate': '2022-04-01T10:30:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJcvIAG', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDflsIAD', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NJppIAG', 'status': 'Waiting on Customer'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'closeddate': 'None', 'ownerid': '005Wt000003NFW6IAO', 'status': 'Waiting on Customer'}, {'id': '500Wt00000DDfx8IAD', 'createddate': '2023-01-03T10:15:00.000+0000', 'closeddate': '2023-01-03T18:45:59.000+0000', 'ownerid': '005Wt000003NJhlIAG', 'status': 'Closed'}, {'id': '500Wt00000DDg1yIAD', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000', 'ownerid': '005Wt000003NJbJIAW', 'status': 'Closed'}, {'id': '500Wt00000DDg1zIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000', 'ownerid': '005Wt000003NJrRIAW', 'status': 'Closed'}, {'id': '500Wt00000DDg20IAD', 'createddate': '2022-12-01T10:00:00.000+0000', 'closeddate': '2022-12-01T14:48:57.000+0000', 'ownerid': '005Wt000003NIvNIAW', 'status': 'Closed'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'closeddate': '2021-03-05T16:11:47.000+0000', 'ownerid': '#005Wt000003NJ0DIAW', 'status': 'Closed '}, {'id': '500Wt00000DDg8RIAT', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000', 'ownerid': '005Wt000003NEGhIAO', 'status': 'Closed'}, {'id': '500Wt00000DDgLKIA1', 'createddate': '2023-11-03T11:30:00.000+0000', 'closeddate': 'None', 'ownerid': '#005Wt000003NHuUIAW', 'status': 'Working  '}, {'id': '500Wt00000DDgLLIA1', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000', 'ownerid': '005Wt000003NDqFIAW', 'status': 'Closed'}, {'id': '500Wt00000DDnt6IAD', 'createddate': '2023-10-16T09:00:00.000+0000', 'closeddate': '2023-10-16T15:22:17.000+0000', 'ownerid': '005Wt000003NIddIAG', 'status': 'Closed'}], 'var_call_MTNrM9wTFodWcZfgzDV5mUR8': 'file_storage/call_MTNrM9wTFodWcZfgzDV5mUR8.json'}

exec(code, env_args)
