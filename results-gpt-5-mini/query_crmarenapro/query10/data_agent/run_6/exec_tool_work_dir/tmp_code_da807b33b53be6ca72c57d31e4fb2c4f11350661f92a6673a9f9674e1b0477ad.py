code = """import json
import pandas as pd
# Load previous results from storage variables
cases = pd.DataFrame(var_call_WOTalACzRvjfd3MX0hzb0BmW)
assigns = pd.DataFrame(var_call_tA9UBjDZ4hzursHuqLDqw8O4)
owners = pd.DataFrame(var_call_qPPXHFiJDqJQfZTw6mK9FRIz)
# join to get owner for each case, prefer owner in Case table
cases['id_clean'] = cases['id'].str.strip()
assigns['caseid_clean'] = assigns['caseid__c'].str.strip()
owners['id_clean'] = owners['id'].str.strip()
# Merge assign owner info
df = cases.merge(assigns[['caseid_clean','newvalue__c']], left_on='id_clean', right_on='caseid_clean', how='left')
# If newvalue__c present use that as assigned owner, else use Case.ownerid
df['assigned_owner'] = df['newvalue__c'].fillna(df['id_clean'].map(owners.set_index('id_clean')['ownerid'] if 'ownerid' in owners.columns else {}))
# Compute handle time in seconds
from datetime import datetime

def parse_dt(s):
    if pd.isna(s):
        return None
    try:
        return pd.to_datetime(s)
    except:
        return None

df['createddate_dt'] = df['createddate'].apply(parse_dt)
df['closeddate_dt'] = df['closeddate'].apply(parse_dt)

df['handle_seconds'] = (df['closeddate_dt'] - df['createddate_dt']).dt.total_seconds()
# Keep only cases without transfers: assign_count == 1
assign_counts = pd.DataFrame(var_call_4zkTiyMw0xjWaZkl4QhDAYdR)
assign_counts['caseid_clean'] = assign_counts['caseid__c'].str.strip()
assign_counts['assign_count'] = pd.to_numeric(assign_counts['assign_count'], errors='coerce')
df = df.merge(assign_counts[['caseid_clean','assign_count']], left_on='id_clean', right_on='caseid_clean', how='left')
df.loc[df['assign_count'].isna(),'assign_count'] = 0
# Only cases with exactly 1 Owner Assignment => not transferred
df_not_transferred = df[df['assign_count']==1].copy()
# Now compute average handle time per agent for agents handling >1 case
# We'll treat assigned_owner as the agent id (strip)
df_not_transferred['agent_id'] = df_not_transferred['assigned_owner'].fillna('').astype(str).str.strip()
agent_stats = df_not_transferred.groupby('agent_id').agg(count=('id','count'), avg_handle_seconds=('handle_seconds','mean')).reset_index()
# filter agents >1 case
agent_stats = agent_stats[agent_stats['count']>1]
# find agent with lowest avg_handle_seconds
if agent_stats.empty:
    result = []
else:
    min_row = agent_stats.loc[agent_stats['avg_handle_seconds'].idxmin()]
    result = [min_row['agent_id']]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jQaoPsgZxZ7BnksUv2BbOMEg': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_PVxI37tOmvrGERsba5Ix9zVv': 'file_storage/call_PVxI37tOmvrGERsba5Ix9zVv.json', 'var_call_WOTalACzRvjfd3MX0hzb0BmW': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_EOjyKu72TkeeTmkAAyywQpAs': [{'id': 'a04Wt00000532s4IAA', 'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'id': 'a04Wt00000536Z5IAI', 'caseid__c': '500Wt00000DDzZHIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'id': '#a04Wt00000537LUIAY', 'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'id': 'a04Wt00000537ZzIAI', 'caseid__c': '500Wt00000DDzr0IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'id': 'a04Wt00000537baIAA', 'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'id': '#a04Wt00000537zlIAA', 'caseid__c': '500Wt00000DDzXdIAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'id': 'a04Wt00000538FtIAI', 'caseid__c': '500Wt00000DDsG3IAL', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'id': 'a04Wt00000538O1IAI', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'id': 'a04Wt00000538O3IAI', 'caseid__c': '500Wt00000DDTxbIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': 'a04Wt00000538hKIAQ', 'caseid__c': '500Wt00000DDzkXIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'id': 'a04Wt00000538hMIAQ', 'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'id': 'a04Wt00000538mAIAQ', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'id': 'a04Wt00000538pNIAQ', 'caseid__c': '500Wt00000DDzivIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'id': '#a04Wt00000538r0IAA', 'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'id': 'a04Wt00000538scIAA', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'id': 'a04Wt00000539BxIAI', 'caseid__c': '500Wt00000DE02HIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000'}], 'var_call_tA9UBjDZ4hzursHuqLDqw8O4': [{'caseid__c': '500Wt00000DDepmIAD', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}], 'var_call_qPPXHFiJDqJQfZTw6mK9FRIz': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_4zkTiyMw0xjWaZkl4QhDAYdR': [{'caseid__c': '500Wt00000DDepmIAD', 'assign_count': '1'}, {'caseid__c': '500Wt00000DDyzpIAD', 'assign_count': '1'}, {'caseid__c': '500Wt00000DDzUPIA1', 'assign_count': '1'}, {'caseid__c': '500Wt00000DDzsbIAD', 'assign_count': '1'}, {'caseid__c': '500Wt00000DDzuEIAT', 'assign_count': '1'}]}

exec(code, env_args)
