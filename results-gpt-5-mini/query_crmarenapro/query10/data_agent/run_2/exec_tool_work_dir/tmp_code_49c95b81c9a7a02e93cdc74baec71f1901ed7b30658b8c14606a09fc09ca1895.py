code = """import pandas as pd
import json
from datetime import datetime

# Load inputs from storage variables
cases = pd.DataFrame(var_call_00JLXa2br1yJleNw2wf5btqq)
history_path = var_call_ozIi6EtBqJ2IzVNTTVqcBnaA

# Read full casehistory JSON from file path
with open(history_path, 'r', encoding='utf-8') as f:
    history = json.load(f)

hist = pd.DataFrame(history)

# Helper to clean IDs (remove leading # and strip whitespace)
def clean_id(x):
    if x is None:
        return None
    if not isinstance(x, str):
        return x
    s = x.strip()
    if s.startswith('#'):
        s = s.lstrip('#')
    if s == 'None' or s == '':
        return None
    return s

# Clean case ids and owner ids in cases
cases['id_clean'] = cases['id'].apply(clean_id)
cases['ownerid_clean'] = cases['ownerid'].apply(clean_id)

# Parse datetime
cases['createddate_dt'] = pd.to_datetime(cases['createddate'])
cases['closeddate_dt'] = pd.to_datetime(cases['closeddate'])

# Work only with cases closed in the 4-month window - they should already be, but ensure
start = pd.to_datetime('2023-05-02')
end = pd.to_datetime('2023-09-02')
cases = cases[(cases['closeddate_dt'] >= start) & (cases['closeddate_dt'] < end)].copy()

# Clean history ids
hist['caseid_clean'] = hist['caseid__c'].apply(clean_id)
hist['newvalue_clean'] = hist['newvalue__c'].apply(clean_id)

# Filter owner assignment records for these cases
owner_hist = hist[hist['field__c'] == 'Owner Assignment'].copy()
owner_hist = owner_hist[owner_hist['caseid_clean'].isin(cases['id_clean'])]

# For each case, count owner assignment events with a valid newvalue
owner_hist_valid = owner_hist[owner_hist['newvalue_clean'].notnull()]
assign_counts = owner_hist_valid.groupby('caseid_clean').size().reset_index(name='assign_count')

# Merge assign counts into cases
cases = cases.merge(assign_counts, left_on='id_clean', right_on='caseid_clean', how='left')
cases['assign_count'] = cases['assign_count'].fillna(0).astype(int)

# Mark transferred cases: assign_count > 1
cases['transferred'] = cases['assign_count'] > 1

# Compute handle time (in seconds) for non-transferred cases only
non_transferred = cases[~cases['transferred']].copy()
if not non_transferred.empty:
    non_transferred['handle_seconds'] = (non_transferred['closeddate_dt'] - non_transferred['createddate_dt']).dt.total_seconds()
else:
    non_transferred['handle_seconds'] = pd.Series(dtype=float)

# Compute assignment counts per agent among these closed cases (count distinct cases they were assigned to)
# Use owner_hist_valid mapping case -> agent (newvalue_clean). Count distinct caseids per agent
agent_case_counts = owner_hist_valid.groupby('newvalue_clean')['caseid_clean'].nunique().reset_index()
agent_case_counts.columns = ['agent_id', 'cases_assigned_count']

# Agents that processed more than one case
agents_gt1 = agent_case_counts[agent_case_counts['cases_assigned_count'] > 1].copy()

# For each agent, compute average handle time from non_transferred cases where case.ownerid_clean == agent
# Prepare mapping
nt = non_transferred[['id_clean', 'ownerid_clean', 'handle_seconds']].copy()
agent_handles = nt.groupby('ownerid_clean')['handle_seconds'].agg(['mean','count']).reset_index()
agent_handles.columns = ['agent_id','avg_handle_seconds','num_cases_counted']

# Join with agents_gt1 to filter only agents who processed >1 case
candidates = agents_gt1.merge(agent_handles, on='agent_id', how='left')
# Remove agents with no non-transferred cases (avg_handle_seconds NaN)
candidates = candidates[candidates['avg_handle_seconds'].notnull()]

# Find agent with lowest average handle time
result_agent = None
if not candidates.empty:
    best = candidates.sort_values(['avg_handle_seconds','agent_id']).iloc[0]
    result_agent = best['agent_id']

# Print result per required format as JSON-serializable string (null if None)
print("__RESULT__:")
print(json.dumps(result_agent))"""

env_args = {'var_call_SjKZAhYxbRI8P5qpJ0bLWQDp': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_ozIi6EtBqJ2IzVNTTVqcBnaA': 'file_storage/call_ozIi6EtBqJ2IzVNTTVqcBnaA.json', 'var_call_00JLXa2br1yJleNw2wf5btqq': [{'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}]}

exec(code, env_args)
