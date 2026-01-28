code = """import json
import pandas as pd

# Load the large casehistory JSON from file path stored in var_call_3UNtbUTk6P4kqVk9aCzbF1oN
with open(var_call_3UNtbUTk6P4kqVk9aCzbF1oN, 'r') as f:
    ch_list = json.load(f)

# Load case rows from previous query (var_call_Egww...)
cases = var_call_EgwwfqOoDBWAAJZRPIT6UmbY

# Normalize ids: remove leading # and trim whitespace
def norm(s):
    if s is None:
        return None
    s = str(s).strip()
    # remove leading # characters
    while s.startswith('#'):
        s = s[1:]
    return s

# Build DataFrames
ch_df = pd.DataFrame(ch_list)
if ch_df.empty:
    ch_df = pd.DataFrame(columns=['id','caseid__c','oldvalue__c','newvalue__c','createddate','field__c'])

# normalize columns
for col in ['id','caseid__c','oldvalue__c','newvalue__c','createddate','field__c']:
    if col in ch_df.columns:
        ch_df[col] = ch_df[col].astype(object).where(pd.notnull(ch_df[col]), None)

ch_df['caseid_norm'] = ch_df['caseid__c'].apply(norm)
ch_df['newvalue_norm'] = ch_df['newvalue__c'].apply(norm)
ch_df['field'] = ch_df['field__c'].astype(str)

cases_df = pd.DataFrame(cases)
for col in ['id','ownerid','createddate','closeddate','status']:
    if col in cases_df.columns:
        cases_df[col] = cases_df[col].astype(object).where(pd.notnull(cases_df[col]), None)

cases_df['id_norm'] = cases_df['id'].apply(norm)
cases_df['ownerid_norm'] = cases_df['ownerid'].apply(norm)

# Filter cases closed in period (already queried that way but ensure)
# period 2023-05-02 to 2023-09-02 inclusive
cases_df['closed_ts'] = pd.to_datetime(cases_df['closeddate'], utc=True)
cases_df['created_ts'] = pd.to_datetime(cases_df['createddate'], utc=True)
start = pd.Timestamp('2023-05-02', tz='UTC')
end = pd.Timestamp('2023-09-02', tz='UTC')
period_cases = cases_df[(cases_df['closed_ts']>=start) & (cases_df['closed_ts']<=end)].copy()

# For these cases, count Owner Assignment events per case
ch_period = ch_df[ch_df['caseid_norm'].isin(period_cases['id_norm'].tolist())].copy()
owner_assign = ch_period[ch_period['field'].str.strip()=='Owner Assignment'].copy()

owner_count = owner_assign.groupby('caseid_norm').size().rename('owner_assign_count').reset_index()

# Merge to period_cases
period_cases = period_cases.merge(owner_count, how='left', left_on='id_norm', right_on='caseid_norm')
period_cases['owner_assign_count'] = period_cases['owner_assign_count'].fillna(0).astype(int)

# Exclude transferred cases (owner_assign_count >1) for handle time calc
non_transferred = period_cases[period_cases['owner_assign_count']==1].copy()
if non_transferred.empty:
    result = None
else:
    non_transferred['handle_seconds'] = (non_transferred['closed_ts'] - non_transferred['created_ts']).dt.total_seconds()

    # Compute avg handle time per agent using ownerid_norm from Case
    avg_handle = non_transferred.groupby('ownerid_norm')['handle_seconds'].mean().reset_index()
    avg_handle = avg_handle.rename(columns={'ownerid_norm':'agent_id','handle_seconds':'avg_handle_seconds'})

    # Compute processed_by_agent: count Owner Assignment events (newvalue) for cases in period (including transferred ones)
    # Use owner_assign (already filtered to period cases) and count distinct cases per agent or count assignments? The policy counts cases processed, so count distinct case ids per agent.
    owner_assign['agent_id'] = owner_assign['newvalue_norm']
    processed = owner_assign.groupby('agent_id')['caseid_norm'].nunique().reset_index()
    processed = processed.rename(columns={'caseid_norm':'cases_processed'})

    # Join
    merged = avg_handle.merge(processed, on='agent_id', how='left')
    merged['cases_processed'] = merged['cases_processed'].fillna(0).astype(int)

    # Filter agents who processed more than one case
    candidates = merged[merged['cases_processed']>1].copy()
    if candidates.empty:
        result = None
    else:
        # Agent with lowest avg_handle_seconds
        candidates_sorted = candidates.sort_values('avg_handle_seconds', ascending=True)
        top = candidates_sorted.iloc[0]
        result = top['agent_id']

# Print result in required format
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MHgxVBX64tfLWyrNNFGepBRm': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_3UNtbUTk6P4kqVk9aCzbF1oN': 'file_storage/call_3UNtbUTk6P4kqVk9aCzbF1oN.json', 'var_call_z3DIBbz71GpKtaeoWmroUaV9': [{'caseid': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'closeddate': '2023-07-01T19:41:08.000+0000', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'closeddate': '2023-05-10T14:59:42.000+0000', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'closeddate': '2023-06-02T13:35:12.000+0000', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'closeddate': '2023-08-15T14:54:02.000+0000', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'closeddate': '2023-06-30T19:03:08.000+0000', 'createddate': '2023-06-30T13:03:00.000+0000'}], 'var_call_ETs1KrXTyYJqxPY2nhLu2FZz': [], 'var_call_5xgaQszYiMF2i7c1WfFAfuOe': [], 'var_call_EgwwfqOoDBWAAJZRPIT6UmbY': [{'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}]}

exec(code, env_args)
