code = """import pandas as pd
import json

data = var_call_HNtvz4qkSL8MMrE5DS2CV8xb
# Create DataFrame
df = pd.DataFrame(data)
# Normalize 'None' strings to actual None
for col in ['field__c','oldvalue__c','newvalue__c','hist_createddate','createddate','closeddate','ownerid']:
    if col in df.columns:
        df[col] = df[col].replace({'None': None})

# Parse dates
df['case_created'] = pd.to_datetime(df['createddate'])
# hist_createddate may be None
df['hist_createddate'] = pd.to_datetime(df['hist_createddate'])
# closeddate comes from case rows repeated; ensure we pull closeddate per case
# For each caseid, get createddate and closeddate from the row(s) (they repeat)
case_meta = df.groupby('caseid').agg({
    'createddate': lambda x: next((v for v in x if v is not None), None),
    'closeddate': lambda x: next((v for v in x if v is not None), None)
}).reset_index()
case_meta['createddate'] = case_meta['createddate'].replace({'None': None})
case_meta['closeddate'] = case_meta['closeddate'].replace({'None': None})
case_meta['created_dt'] = pd.to_datetime(case_meta['createddate'])
case_meta['closed_dt'] = pd.to_datetime(case_meta['closeddate'])

# Count Owner Assignment events per case
owner_assignments = df[df['field__c'] == 'Owner Assignment'].copy()
owner_assign_count = owner_assignments.groupby('caseid').size().reset_index(name='owner_assign_count')

# For non-transferred cases: owner_assign_count == 1
case_meta = case_meta.merge(owner_assign_count, on='caseid', how='left')
case_meta['owner_assign_count'] = case_meta['owner_assign_count'].fillna(0).astype(int)

# Determine agent assignments per case from Owner Assignment entries
# Use newvalue__c as the assigned agent id
assigns = owner_assignments[['caseid','newvalue__c']].copy()
assigns = assigns.rename(columns={'newvalue__c':'agentid'})
# Normalize agent id by stripping leading '#'
assigns['agentid'] = assigns['agentid'].astype(str).str.lstrip('#')

# Compute agent_case_count (agents processing cases) from all owner assignment events within period
agent_case_pairs = assigns.dropna(subset=['agentid']).drop_duplicates()
agent_case_count = agent_case_pairs.groupby('agentid').size().reset_index(name='case_count')

# For cases which have exactly 1 owner assignment and are closed, compute handle time and attribute to agent
# Merge case_meta with assigns to get assigned agent for non-transferred cases
case_with_agent = case_meta.merge(assigns, on='caseid', how='left')
# Normalize agentid
case_with_agent['agentid'] = case_with_agent['agentid'].astype(object)
case_with_agent['agentid'] = case_with_agent['agentid'].where(case_with_agent['agentid'].notnull(), None)
case_with_agent['agentid'] = case_with_agent['agentid'].apply(lambda x: x.lstrip('#') if isinstance(x,str) else x)

# Filter non-transferred and closed
valid_cases = case_with_agent[(case_with_agent['owner_assign_count'] == 1) & (case_with_agent['closed_dt'].notna())]

# Compute handle time in hours
valid_cases['handle_hours'] = (valid_cases['closed_dt'] - valid_cases['created_dt']).dt.total_seconds() / 3600.0

# Now compute average handle time per agent
agent_handle = valid_cases.dropna(subset=['agentid']).groupby('agentid').agg(
    avg_handle_hours = ('handle_hours','mean'),
    handled_cases = ('caseid','nunique')
).reset_index()

# Now join with agent_case_count to filter agents who processed more than one case (case_count >1)
agent_stats = agent_handle.merge(agent_case_count, on='agentid', how='left')
agent_stats['case_count'] = agent_stats['case_count'].fillna(0).astype(int)
# Filter agents with processed case_count > 1 and with at least one handle case
candidates = agent_stats[agent_stats['case_count'] > 1].copy()

# If no candidates, return None
if candidates.empty:
    result = None
else:
    # find agent with lowest avg_handle_hours
    best = candidates.loc[candidates['avg_handle_hours'].idxmin()]
    result = best['agentid']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_w3nM7U8qDhF7spCA4kFjdbhH': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_IqeAnsO6ZQeCsKRxTJWbvDjU': [{'id': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'owner_change_count': '1', 'total_history': '2'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'owner_change_count': '1', 'total_history': '3'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'owner_change_count': '0', 'total_history': '0'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'owner_change_count': '1', 'total_history': '3'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'owner_change_count': '1', 'total_history': '3'}, {'id': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'owner_change_count': '1', 'total_history': '2'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'owner_change_count': '0', 'total_history': '0'}, {'id': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'owner_change_count': '0', 'total_history': '0'}, {'id': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'owner_change_count': '1', 'total_history': '2'}, {'id': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'owner_change_count': '0', 'total_history': '0'}, {'id': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'owner_change_count': '1', 'total_history': '2'}, {'id': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'owner_change_count': '2', 'total_history': '3'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'owner_change_count': '1', 'total_history': '3'}, {'id': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'owner_change_count': '0', 'total_history': '0'}, {'id': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'owner_change_count': '1', 'total_history': '2'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'owner_change_count': '1', 'total_history': '3'}], 'var_call_HNtvz4qkSL8MMrE5DS2CV8xb': [{'caseid': '#500Wt00000DDDfwIAH', 'ownerid': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': 'None'}, {'caseid': '#500Wt00000DDsG3IAL', 'ownerid': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': 'None'}, {'caseid': '#500Wt00000DDzivIAD', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': 'None'}, {'caseid': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': 'None'}, {'caseid': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'field__c': 'None', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': 'None'}, {'caseid': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIfFIAW', 'hist_createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid': '500Wt00000DDTxbIAH', 'ownerid': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'hist_createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-07-01T19:41:08.000+0000'}, {'caseid': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NF1SIAW', 'hist_createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid': '500Wt00000DDflsIAD', 'ownerid': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'field__c': 'Owner Assignment', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'hist_createddate': '2023-06-12T10:00:06.000+0000'}, {'caseid': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-08-15T14:54:02.000+0000'}, {'caseid': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'hist_createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-05-10T14:59:42.000+0000'}, {'caseid': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'hist_createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJUrIAO', 'hist_createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid': '500Wt00000DDzXdIAL', 'ownerid': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid': '500Wt00000DDzZHIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'hist_createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid': '500Wt00000DDzkXIAT', 'ownerid': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'hist_createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid': '500Wt00000DDzr0IAD', 'ownerid': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcvIAG', 'hist_createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-06-30T19:03:08.000+0000'}, {'caseid': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'hist_createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'field__c': 'Owner Assignment', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'hist_createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'field__c': 'Case Closed', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-06-02T13:35:12.000+0000'}, {'caseid': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'field__c': 'Case Creation', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'hist_createddate': '2023-06-02T09:30:00.000+0000'}]}

exec(code, env_args)
