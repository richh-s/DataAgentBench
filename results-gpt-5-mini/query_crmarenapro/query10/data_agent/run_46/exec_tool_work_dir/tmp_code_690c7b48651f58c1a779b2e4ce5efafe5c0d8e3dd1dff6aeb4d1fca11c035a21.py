code = """import json
import pandas as pd

# Load casehistory data
ch_file = var_call_5Ouzu45Z010s9qKph4RYPs3l
with open(ch_file, 'r') as f:
    ch = json.load(f)

cases = var_call_PixTdIQwyZMdRaIsejUczpIw

def norm(s):
    if s is None:
        return None
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s.strip()

df_ch = pd.DataFrame(ch)
df_ch_oa = df_ch[df_ch.get('field__c') == 'Owner Assignment'].copy()
df_ch_oa['caseid_norm'] = df_ch_oa['caseid__c'].apply(norm)
assign_counts = df_ch_oa.groupby('caseid_norm').size().reset_index(name='owner_assignment_count')

df_cases = pd.DataFrame(cases)
df_cases['caseid_norm'] = df_cases['id'].apply(norm)
df_cases['ownerid_norm'] = df_cases['ownerid'].apply(norm)
df_cases['created_dt'] = pd.to_datetime(df_cases['createddate'])
df_cases['closed_dt'] = pd.to_datetime(df_cases['closeddate'])
df_cases['handle_seconds'] = (df_cases['closed_dt'] - df_cases['created_dt']).dt.total_seconds()

df = df_cases.merge(assign_counts, left_on='caseid_norm', right_on='caseid_norm', how='left')
df['owner_assignment_count'] = df['owner_assignment_count'].fillna(0).astype(int)

df_non_transferred = df[df['owner_assignment_count'] == 1].copy()

grp = df_non_transferred.groupby('ownerid_norm').agg(case_count=('id','count'), avg_handle_seconds=('handle_seconds','mean')).reset_index()

grp_multi = grp[grp['case_count'] > 1].copy()

# prepare serializable output
out = {
    'total_cases_in_window': len(df_cases),
    'non_transferred_cases': len(df_non_transferred),
    'agents_summary': grp.to_dict(orient='records'),
    'agents_with_more_than_one_case': grp_multi.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_53qHU9cY2ypfetZWaJjKJHlw': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_5Ouzu45Z010s9qKph4RYPs3l': 'file_storage/call_5Ouzu45Z010s9qKph4RYPs3l.json', 'var_call_PixTdIQwyZMdRaIsejUczpIw': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_m1dhvjpICWgGWA66a73j8l7Y': None}

exec(code, env_args)
