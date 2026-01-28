code = """import pandas as pd
import json
# load datasets from storage
cases_all = pd.DataFrame(var_call_H2Wr4WIMxClnradGLfNypGHE)
casehist = pd.DataFrame(var_call_wOuwzhuv9XGCfIRHd4HdeKeK)
# normalize ids (strip leading # if present) to join reliably
def clean_id(x):
    if pd.isna(x):
        return x
    s = str(x).strip()
    if s.startswith('#'):
        return s[1:]
    return s

cases_all['id_clean'] = cases_all['id'].apply(clean_id)
cases_all['ownerid_clean'] = cases_all['ownerid'].apply(clean_id)
casehist['caseid_clean'] = casehist['caseid__c'].apply(clean_id)
casehist['newvalue_clean'] = casehist['newvalue__c'].apply(clean_id)
casehist['oldvalue_clean'] = casehist['oldvalue__c'].apply(lambda x: clean_id(x) if x not in (None,'None') else None)

# Count processed per agent: any owner assignment where newvalue is agent in casehistory within window OR the final owner in cases table
# Build list of (agent, caseid) from casehistory newvalue and from cases final owner
ch_pairs = casehist[['caseid_clean','newvalue_clean']].dropna().rename(columns={'caseid_clean':'case_id','newvalue_clean':'agent_id'})
cases_pairs = cases_all[['id_clean','ownerid_clean']].rename(columns={'id_clean':'case_id','ownerid_clean':'agent_id'})
all_pairs = pd.concat([ch_pairs, cases_pairs], ignore_index=True).drop_duplicates()
# compute processed counts per agent
processed_counts = all_pairs.groupby('agent_id').size().reset_index(name='processed_count')

# Now compute handle time per agent but excluding transferred cases
# To know if a case was transferred: count owner assignments in casehistory for that case >1
owner_assign_counts = casehist.groupby('caseid_clean').size().reset_index(name='owner_assignments')

# Merge with cases
cases_all['caseid_clean'] = cases_all['id'].apply(clean_id)
cases = cases_all.merge(owner_assign_counts, left_on='caseid_clean', right_on='caseid_clean', how='left')
cases['owner_assignments'] = cases['owner_assignments'].fillna(0).astype(int)
# transferred if owner_assignments > 1
cases['transferred'] = cases['owner_assignments'] > 1
# compute handle_seconds
cases['createddate'] = pd.to_datetime(cases['createddate'], utc=True)
cases['closeddate'] = pd.to_datetime(cases['closeddate'], utc=True)
cases['handle_seconds'] = (cases['closeddate'] - cases['createddate']).dt.total_seconds()
# For handle time, only include cases where transferred==False
handle = cases[~cases['transferred']][['caseid_clean','ownerid_clean','handle_seconds']].rename(columns={'caseid_clean':'case_id','ownerid_clean':'agent_id'})
# Now compute average handle time per agent for agents who processed more than one case (processed_counts>1)
# Merge processed_counts into handle
agent_stats = handle.groupby('agent_id').agg(avg_handle_seconds=('handle_seconds','mean'), handled_cases=('case_id','count')).reset_index()
agent_stats = agent_stats.merge(processed_counts, on='agent_id', how='left')
agent_stats['processed_count'] = agent_stats['processed_count'].fillna(0).astype(int)
# Filter agents with processed_count > 1
candidates = agent_stats[agent_stats['processed_count']>1].copy()
# Find agent with lowest average handle time
if candidates.empty:
    result = None
else:
    best = candidates.loc[candidates['avg_handle_seconds'].idxmin()]
    result = best['agent_id']

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4gUeumy2BYO99JCjZbmbBl02': [{'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'owner_assignment_count': '0'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'owner_assignment_count': '0'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'owner_assignment_count': '1'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'owner_assignment_count': '1'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'owner_assignment_count': '1'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'owner_assignment_count': '1'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'owner_assignment_count': '1'}], 'var_call_H2Wr4WIMxClnradGLfNypGHE': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_NSFZAv1nKhLyfiAkgRRsUBgk': [{'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'owner_change_count': '0'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'owner_change_count': '0'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'owner_change_count': '1'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'owner_change_count': '1'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'owner_change_count': '1'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'owner_change_count': '1'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'owner_change_count': '1'}], 'var_call_28rJolefy42rnLu87eIRuCvl': 'READY', 'var_call_wOuwzhuv9XGCfIRHd4HdeKeK': [{'caseid__c': '500Wt00000DDzscIAD', 'newvalue__c': '005Wt000003NEtOIAW', 'oldvalue__c': 'None', 'createddate': '2023-05-02T23:55:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzZHIA1', 'newvalue__c': '005Wt000003NDqDIAW', 'oldvalue__c': 'None', 'createddate': '2023-07-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDepmIAD', 'newvalue__c': '005Wt000003NJufIAG', 'oldvalue__c': 'None', 'createddate': '2023-07-01T10:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDflsIAD', 'newvalue__c': '005Wt000003NJppIAG', 'oldvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzr0IAD', 'newvalue__c': '005Wt000003NJcvIAG', 'oldvalue__c': 'None', 'createddate': '2023-08-01T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzUPIA1', 'newvalue__c': '005Wt000003NDqDIAW', 'oldvalue__c': 'None', 'createddate': '2023-05-10T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzXdIAL', 'newvalue__c': '005Wt000003NJUrIAO', 'oldvalue__c': 'None', 'createddate': '2023-06-22T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDsG3IAL', 'newvalue__c': '005Wt000003NI5mIAG', 'oldvalue__c': 'None', 'createddate': '2023-08-10T14:20:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDDfwIAH', 'newvalue__c': '005Wt000003NH3GIAW', 'oldvalue__c': 'None', 'createddate': '2023-07-02T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDTxbIAH', 'newvalue__c': '005Wt000003NIfFIAW', 'oldvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzkXIAT', 'newvalue__c': '005Wt000003NINVIA4', 'oldvalue__c': 'None', 'createddate': '2023-06-19T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzuEIAT', 'newvalue__c': '005Wt000003NJJaIAO', 'oldvalue__c': 'None', 'createddate': '2023-06-02T09:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDflsIAD', 'newvalue__c': '005Wt000003NF1SIAW', 'oldvalue__c': 'None', 'createddate': '2023-06-12T09:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzivIAD', 'newvalue__c': '005Wt000003NDqDIAW', 'oldvalue__c': 'None', 'createddate': '2023-06-05T11:15:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDyzpIAD', 'newvalue__c': '005Wt000003NJGLIA4', 'oldvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDzsbIAD', 'newvalue__c': '005Wt000003NJD9IAO', 'oldvalue__c': 'None', 'createddate': '2023-06-30T13:03:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DE02HIAT', 'newvalue__c': '005Wt000003NIddIAG', 'oldvalue__c': 'None', 'createddate': '2023-06-03T14:45:00.000+0000', 'field__c': 'Owner Assignment'}, {'caseid__c': '500Wt00000DDDfwIAH', 'newvalue__c': '005Wt000003NJ0DIAW', 'oldvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:30:02.000+0000', 'field__c': 'Owner Assignment'}]}

exec(code, env_args)
