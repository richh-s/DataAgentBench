code = """import json
import pandas as pd

ch_var = var_call_XOVX3CNKGzLYu53I7Rb0E9y3
if isinstance(ch_var, str):
    with open(ch_var, 'r', encoding='utf-8') as f:
        ch_data = json.load(f)
else:
    ch_data = ch_var

cases_data = var_call_gMJb6CQU78Slfuo4ErmYrzN6

# helpers
def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    return s[1:] if s.startswith('#') else s

# DataFrames
ch_df = pd.DataFrame(ch_data)
cases_df = pd.DataFrame(cases_data)

# Ensure columns
for col in ['caseid__c','newvalue__c','field__c']:
    if col not in ch_df.columns:
        ch_df[col] = None
for col in ['id','createddate','closeddate','ownerid']:
    if col not in cases_df.columns:
        cases_df[col] = None

ch_df['caseid_clean'] = ch_df['caseid__c'].apply(clean_id)
ch_df['newvalue_clean'] = ch_df['newvalue__c'].apply(clean_id)
ch_df['field_clean'] = ch_df['field__c'].astype(str).str.strip().str.lower()

cases_df['caseid_clean'] = cases_df['id'].apply(clean_id)
cases_df['ownerid_clean'] = cases_df['ownerid'].apply(clean_id)

# Filter casehistory to owner assignments
ch_owner = ch_df[ch_df['field_clean'].str.contains('owner')]

# Only consider casehistory entries for cases in our closed cases set
closed_case_ids = set(cases_df['caseid_clean'].dropna().unique())
ch_owner = ch_owner[ch_owner['caseid_clean'].isin(closed_case_ids)].copy()

# Compute owner assignment count per case
owner_counts = ch_owner.groupby('caseid_clean').size().reset_index(name='owner_assignment_count')

# For agent assignment counts: count distinct cases assigned to each agent (newvalue_clean)
agent_assignment_counts = ch_owner.groupby('newvalue_clean')['caseid_clean'].nunique().reset_index(name='assigned_case_count')
agent_assignment_counts = agent_assignment_counts.rename(columns={'newvalue_clean':'agentid'})

# Compute handle time per case for non-transferred cases (owner_assignment_count == 1)
cases_merged = cases_df.merge(owner_counts, on='caseid_clean', how='left')
cases_merged['owner_assignment_count'] = cases_merged['owner_assignment_count'].fillna(0).astype(int)

# select only non-transferred cases (==1)
non_transferred = cases_merged[cases_merged['owner_assignment_count'] == 1].copy()
non_transferred['created_dt'] = pd.to_datetime(non_transferred['createddate'])
non_transferred['closed_dt'] = pd.to_datetime(non_transferred['closeddate'])
non_transferred['handle_seconds'] = (non_transferred['closed_dt'] - non_transferred['created_dt']).dt.total_seconds()

# group by ownerid_clean to compute avg handle
agent_handle = non_transferred.groupby('ownerid_clean').agg(avg_handle_seconds=('handle_seconds','mean'), handled_case_count=('caseid_clean','count')).reset_index().rename(columns={'ownerid_clean':'agentid'})

# Merge assignment counts and handle stats
agents = agent_assignment_counts.merge(agent_handle, on='agentid', how='left')

# Filter agents who processed more than one case (assigned_case_count > 1)
candidates = agents[agents['assigned_case_count'] > 1].copy()

# Also require that avg_handle_seconds is not null (they must have at least one non-transferred case to compute handle time)
candidates = candidates[candidates['avg_handle_seconds'].notna()]

# Find agent with lowest average handle time
if not candidates.empty:
    best_row = candidates.sort_values(['avg_handle_seconds','agentid']).iloc[0]
    best_agent = best_row['agentid']
else:
    best_agent = None

print('__RESULT__:')
print(json.dumps(best_agent))"""

env_args = {'var_call_7utMviyenT2oVIqaTVgIgDIn': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_XOVX3CNKGzLYu53I7Rb0E9y3': 'file_storage/call_XOVX3CNKGzLYu53I7Rb0E9y3.json', 'var_call_gMJb6CQU78Slfuo4ErmYrzN6': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_XNLG8QZAbKJXZLrp3RMMjQMe': None}

exec(code, env_args)
