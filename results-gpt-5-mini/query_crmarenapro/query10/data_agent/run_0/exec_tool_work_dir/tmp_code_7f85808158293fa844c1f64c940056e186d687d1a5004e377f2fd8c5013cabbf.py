code = """import json
import pandas as pd
from datetime import datetime

# Load data from storage variables
# var_call_TN1EmJFYPjTCmYImBdXrOOC5 is a file path to the full casehistory__c query result
with open(var_call_TN1EmJFYPjTCmYImBdXrOOC5, 'r') as f:
    casehistory = json.load(f)

# var_call_4XbLbXXuvsctV4XxcG9zm3KM is the list of cases closed in the period
cases_closed = var_call_4XbLbXXuvsctV4XxcG9zm3KM

# Convert to DataFrames
ch_df = pd.DataFrame(casehistory)
cases_df = pd.DataFrame(cases_closed)

# Normalize whitespace and possible leading # in ids for comparisons
ch_df['caseid__c'] = ch_df['caseid__c'].astype(str).str.strip()
ch_df['field__c'] = ch_df['field__c'].astype(str).str.strip()
ch_df['newvalue__c'] = ch_df['newvalue__c'].astype(str).str.strip()

cases_df['id'] = cases_df['id'].astype(str).str.strip()
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'], utc=True)
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], utc=True)

# Get closed case ids
closed_case_ids = set(cases_df['id'].tolist())

# Filter case history to owner assignments for these cases
owner_ch = ch_df[(ch_df['field__c'] == 'Owner Assignment') & (ch_df['caseid__c'].isin(closed_case_ids))].copy()

# Count owner assignments per case
owner_counts = owner_ch.groupby('caseid__c').size().to_dict()  # caseid -> count

# Build mapping case -> single owner (for non-transferred cases)
single_owner_per_case = {}
for cid, cnt in owner_counts.items():
    if cnt == 1:
        # get the owner id
        owner_row = owner_ch[owner_ch['caseid__c'] == cid].iloc[0]
        owner_id = owner_row['newvalue__c']
        single_owner_per_case[cid] = owner_id

# Compute handle time (in seconds) for each closed case
cases_df['handle_seconds'] = (cases_df['closeddate'] - cases_df['createddate']).dt.total_seconds()
case_handle_time = cases_df.set_index('id')['handle_seconds'].to_dict()

# For each non-transferred case, attribute handle time to the owner
owner_handle_times = {}  # owner_id -> list of handle_seconds (only from non-transferred cases)
for cid, owner in single_owner_per_case.items():
    # Skip if owner is null-like
    if owner in [None, 'None', '', 'nan']:
        continue
    # Clean potential leading # in owner id
    owner_clean = owner.strip()
    if owner_clean.startswith('#'):
        owner_clean = owner_clean[1:]
    # Get handle seconds for case
    if cid in case_handle_time:
        owner_handle_times.setdefault(owner_clean, []).append(case_handle_time[cid])

# Now compute for eligibility: agents who processed (appeared as owner in any owner assignment) more than one case
# We count unique case ids per agent across the closed cases
agent_case_sets = {}
for _, row in owner_ch.iterrows():
    agent = row['newvalue__c'].strip()
    if agent.startswith('#'):
        agent = agent[1:]
    cid = row['caseid__c']
    agent_case_sets.setdefault(agent, set()).add(cid)

# Compute counts
agent_counts = {agent: len(cases) for agent, cases in agent_case_sets.items()}

# Eligible agents: count > 1
eligible_agents = {agent for agent, cnt in agent_counts.items() if cnt > 1}

# For eligible agents, compute average handle time from owner_handle_times
import math
avg_handle = {}
for agent in eligible_agents:
    times = owner_handle_times.get(agent, [])
    # Only consider if there is at least one non-transferred case to compute average
    if len(times) > 0:
        avg = sum(times) / len(times)
        avg_handle[agent] = avg

# If no eligible agent has computable average, return None
if not avg_handle:
    result = None
else:
    # Find agent with lowest average handle time. In case of tie, pick lexicographically smallest id
    min_avg = min(avg_handle.values())
    candidates = [a for a,v in avg_handle.items() if abs(v - min_avg) < 1e-6]
    chosen = sorted(candidates)[0]
    result = chosen

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ro9NZi3Jj73gEiMgPc36DgTQ': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_TN1EmJFYPjTCmYImBdXrOOC5': 'file_storage/call_TN1EmJFYPjTCmYImBdXrOOC5.json', 'var_call_4XbLbXXuvsctV4XxcG9zm3KM': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
