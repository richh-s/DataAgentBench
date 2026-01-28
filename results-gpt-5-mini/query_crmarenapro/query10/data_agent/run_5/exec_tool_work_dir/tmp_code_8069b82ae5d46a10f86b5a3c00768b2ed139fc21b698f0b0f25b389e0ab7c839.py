code = """import json
import pandas as pd

ch_var = var_call_XOVX3CNKGzLYu53I7Rb0E9y3
if isinstance(ch_var, str):
    with open(ch_var, 'r', encoding='utf-8') as f:
        ch_data = json.load(f)
else:
    ch_data = ch_var
cases_data = var_call_gMJb6CQU78Slfuo4ErmYrzN6

def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    return s[1:] if s.startswith('#') else s

ch_df = pd.DataFrame(ch_data)
ch_df['caseid_clean'] = ch_df.get('caseid__c', pd.Series()).apply(clean_id)
ch_df['newvalue_clean'] = ch_df.get('newvalue__c', pd.Series()).apply(clean_id)
ch_df['field_clean'] = ch_df.get('field__c', pd.Series()).astype(str).str.strip().str.lower()

cases_df = pd.DataFrame(cases_data)
cases_df['caseid_clean'] = cases_df['id'].apply(clean_id)
cases_df['ownerid_clean'] = cases_df['ownerid'].apply(clean_id)

closed_case_ids = set(cases_df['caseid_clean'].dropna().unique())
ch_owner_all = ch_df[ch_df['field_clean'].str.contains('owner', na=False)].copy()
ch_owner_closed = ch_owner_all[ch_owner_all['caseid_clean'].isin(closed_case_ids)].copy()

owner_counts = ch_owner_closed.groupby('caseid_clean').size().reset_index(name='owner_assignment_count')
agent_assignment_counts = ch_owner_closed.groupby('newvalue_clean')['caseid_clean'].nunique().reset_index(name='assigned_case_count').rename(columns={'newvalue_clean':'agentid'})

# handle times for non-transferred cases (owner_assignment_count == 1)
cases_merged = cases_df.merge(owner_counts, on='caseid_clean', how='left')
cases_merged['owner_assignment_count'] = cases_merged['owner_assignment_count'].fillna(0).astype(int)
non_transferred = cases_merged[cases_merged['owner_assignment_count'] == 1].copy()
non_transferred['created_dt'] = pd.to_datetime(non_transferred['createddate'])
non_transferred['closed_dt'] = pd.to_datetime(non_transferred['closeddate'])
non_transferred['handle_seconds'] = (non_transferred['closed_dt'] - non_transferred['created_dt']).dt.total_seconds()
agent_handle = non_transferred.groupby('ownerid_clean').agg(avg_handle_seconds=('handle_seconds','mean'), handled_case_count=('caseid_clean','count')).reset_index().rename(columns={'ownerid_clean':'agentid'})

agents = agent_assignment_counts.merge(agent_handle, on='agentid', how='left')

# build diagnostics
diag = {
    'total_closed_cases_count': len(cases_df),
    'closed_case_ids': list(closed_case_ids),
    'total_ch_owner_all': len(ch_owner_all),
    'total_ch_owner_closed': len(ch_owner_closed),
    'owner_counts_sample': owner_counts.head(20).to_dict(orient='records'),
    'agent_assignment_counts_sample': agent_assignment_counts.head(20).to_dict(orient='records'),
    'non_transferred_cases_count': len(non_transferred),
    'agent_handle_sample': agent_handle.head(20).to_dict(orient='records'),
    'agents_merged_sample': agents.head(50).to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(diag))"""

env_args = {'var_call_7utMviyenT2oVIqaTVgIgDIn': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_XOVX3CNKGzLYu53I7Rb0E9y3': 'file_storage/call_XOVX3CNKGzLYu53I7Rb0E9y3.json', 'var_call_gMJb6CQU78Slfuo4ErmYrzN6': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_XNLG8QZAbKJXZLrp3RMMjQMe': None, 'var_call_okBgRxh1gUH93JLzEcavSEjj': None}

exec(code, env_args)
