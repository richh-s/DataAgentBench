code = """import json
import pandas as pd

# Load casehistory data from file path stored in var_call_5Ouzu45Z010s9qKph4RYPs3l
ch_file = var_call_5Ouzu45Z010s9qKph4RYPs3l
with open(ch_file, 'r') as f:
    ch = json.load(f)

cases = var_call_PixTdIQwyZMdRaIsejUczpIw

# Normalization function to remove leading '#' and surrounding whitespace
def norm(s):
    if s is None:
        return None
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s.strip()

# DataFrames
df_ch = pd.DataFrame(ch)
# Filter owner assignment entries
df_ch_oa = df_ch[df_ch.get('field__c') == 'Owner Assignment'].copy()
# normalize case ids
df_ch_oa['caseid_norm'] = df_ch_oa['caseid__c'].apply(norm)
# count owner assignment per case
assign_counts = df_ch_oa.groupby('caseid_norm').size().reset_index(name='owner_assignment_count')

df_cases = pd.DataFrame(cases)
# normalize case id and owner id
df_cases['caseid_norm'] = df_cases['id'].apply(norm)
df_cases['ownerid_norm'] = df_cases['ownerid'].apply(norm)
# parse datetimes
df_cases['created_dt'] = pd.to_datetime(df_cases['createddate'])
df_cases['closed_dt'] = pd.to_datetime(df_cases['closeddate'])
# compute handle time in seconds
df_cases['handle_seconds'] = (df_cases['closed_dt'] - df_cases['created_dt']).dt.total_seconds()

# merge with assignment counts (left join)
df = df_cases.merge(assign_counts, left_on='caseid_norm', right_on='caseid_norm', how='left')
# missing counts -> 0
df['owner_assignment_count'] = df['owner_assignment_count'].fillna(0).astype(int)

# Keep only cases that have exactly one Owner Assignment (not transferred)
df_non_transferred = df[df['owner_assignment_count'] == 1].copy()

# Group by owner and compute average handle time and case counts
grp = df_non_transferred.groupby('ownerid_norm').agg(case_count=('id','count'), avg_handle_seconds=('handle_seconds','mean')).reset_index()
# Keep only agents who processed more than one case
grp_multi = grp[grp['case_count'] > 1].copy()

# Determine agent with lowest average handle time
if not grp_multi.empty:
    min_row = grp_multi.loc[grp_multi['avg_handle_seconds'].idxmin()]
    agent_id = min_row['ownerid_norm']
else:
    agent_id = None

result = json.dumps(agent_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_53qHU9cY2ypfetZWaJjKJHlw': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_5Ouzu45Z010s9qKph4RYPs3l': 'file_storage/call_5Ouzu45Z010s9qKph4RYPs3l.json', 'var_call_PixTdIQwyZMdRaIsejUczpIw': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
