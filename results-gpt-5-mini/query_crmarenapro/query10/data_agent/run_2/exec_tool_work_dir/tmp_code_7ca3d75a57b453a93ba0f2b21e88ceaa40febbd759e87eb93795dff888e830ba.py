code = """import pandas as pd
import json

# Re-examine data to ensure we didn't miss agents: print intermediates
cases = pd.DataFrame(var_call_00JLXa2br1yJleNw2wf5btqq)
with open(var_call_ozIi6EtBqJ2IzVNTTVqcBnaA,'r',encoding='utf-8') as f:
    history = json.load(f)
hist = pd.DataFrame(history)

# Cleaning function
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

cases['id_clean'] = cases['id'].apply(clean_id)
cases['ownerid_clean'] = cases['ownerid'].apply(clean_id)
cases['createddate_dt'] = pd.to_datetime(cases['createddate']).dt.tz_convert(None)
cases['closeddate_dt'] = pd.to_datetime(cases['closeddate']).dt.tz_convert(None)

start = pd.to_datetime('2023-05-02')
end = pd.to_datetime('2023-09-02')

cases = cases[(cases['closeddate_dt'] >= start) & (cases['closeddate_dt'] < end)].copy()

hist['caseid_clean'] = hist['caseid__c'].apply(clean_id)
hist['newvalue_clean'] = hist['newvalue__c'].apply(clean_id)
owner_hist = hist[hist['field__c'] == 'Owner Assignment'].copy()
owner_hist = owner_hist[owner_hist['caseid_clean'].isin(cases['id_clean'])]
owner_hist_valid = owner_hist[owner_hist['newvalue_clean'].notnull()]

# compute assign_counts per case
assign_counts = owner_hist_valid.groupby('caseid_clean').size().reset_index(name='assign_count')
cases = cases.merge(assign_counts, left_on='id_clean', right_on='caseid_clean', how='left')
cases['assign_count'] = cases['assign_count'].fillna(0).astype(int)

# count owner assignments per agent
agent_case_counts = owner_hist_valid.groupby('newvalue_clean')['caseid_clean'].nunique().reset_index()
agent_case_counts.columns = ['agent_id', 'cases_assigned_count']

# non-transferred cases
cases['transferred'] = cases['assign_count'] > 1
non_transferred = cases[~cases['transferred']].copy()
non_transferred['handle_seconds'] = (non_transferred['closeddate_dt'] - non_transferred['createddate_dt']).dt.total_seconds()

# agent handles
nt = non_transferred[['id_clean','ownerid_clean','handle_seconds']]
agent_handles = nt.groupby('ownerid_clean')['handle_seconds'].agg(['mean','count']).reset_index()
agent_handles.columns = ['agent_id','avg_handle_seconds','num_cases_counted']

candidates = agent_case_counts.merge(agent_handles, on='agent_id', how='left')

# Convert dataframes to serializable forms: only keep relevant small summaries
out = {
    'agent_case_counts': agent_case_counts.to_dict(orient='records'),
    'agent_handles': agent_handles.fillna('').to_dict(orient='records'),
    'candidates': candidates.fillna('').to_dict(orient='records')
}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_SjKZAhYxbRI8P5qpJ0bLWQDp': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_ozIi6EtBqJ2IzVNTTVqcBnaA': 'file_storage/call_ozIi6EtBqJ2IzVNTTVqcBnaA.json', 'var_call_00JLXa2br1yJleNw2wf5btqq': [{'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}], 'var_call_zbNMK0pn6SatY84oRhuK151z': None}

exec(code, env_args)
