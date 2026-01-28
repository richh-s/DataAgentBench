code = """import json
import pandas as pd
# Load data from storage
cases = var_call_7znFSGi8VcAnECEJCDFXk848
with open(var_call_QHxrD2NgBgeYTHDHGeVWSEBX, 'r') as f:
    casehist = json.load(f)

# DataFrames
df_cases = pd.DataFrame(cases)
df_hist = pd.DataFrame(casehist)

# Normalize IDs
def norm_id(x):
    if pd.isna(x):
        return x
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

# Apply normalization
for col in ['id','ownerid']:
    if col in df_cases.columns:
        df_cases[col] = df_cases[col].apply(norm_id)
for col in ['id','caseid__c','oldvalue__c','newvalue__c']:
    if col in df_hist.columns:
        df_hist[col] = df_hist[col].apply(norm_id)

# Filter cases closed in period already in df_cases (they are)
# Build set of case ids
case_ids = set(df_cases['id'].dropna().unique())

# Filter history to owner assignments only and only for these cases
if 'field__c' in df_hist.columns:
    df_hist = df_hist[df_hist['field__c'].str.contains('Owner', case=False, na=False)]

df_hist_period_cases = df_hist[df_hist['caseid__c'].isin(case_ids)].copy()

# Count distinct cases per agent (newvalue__c) for these cases
# Some newvalue__c might be None; drop
hist_counts = df_hist_period_cases.dropna(subset=['newvalue__c']).groupby('newvalue__c')['caseid__c'].nunique().reset_index()
hist_counts.columns = ['agentid','handled_case_count']

# Now compute average handle time per agent, but only for non-transferred cases (assign_count == 1)
# First compute assign_count per case using df_hist (for these cases)
assign_counts = df_hist[df_hist['caseid__c'].isin(case_ids)].groupby('caseid__c').size().reset_index(name='assign_count')

# Merge into df_cases

df_cases['id'] = df_cases['id'].apply(norm_id)
assign_counts['caseid__c'] = assign_counts['caseid__c'].apply(norm_id)

df = pd.merge(df_cases, assign_counts, left_on='id', right_on='caseid__c', how='left')
df['assign_count'] = df['assign_count'].fillna(0).astype(int)

# Compute handle_seconds

df['createddate_parsed'] = pd.to_datetime(df['createddate'], errors='coerce')
df['closeddate_parsed'] = pd.to_datetime(df['closeddate'], errors='coerce')
df['handle_seconds'] = (df['closeddate_parsed'] - df['createddate_parsed']).dt.total_seconds()

# Valid cases: assign_count == 1 and handle_seconds not null

df_valid = df[(df['assign_count'] == 1) & (df['handle_seconds'].notna())].copy()

df_valid['ownerid'] = df_valid['ownerid'].apply(norm_id)

# Compute avg handle per owner
avg_handle = df_valid.groupby('ownerid').agg(case_count_nontransferred=('id','count'), avg_handle_seconds=('handle_seconds','mean')).reset_index()
avg_handle.columns = ['agentid','case_count_nontransferred','avg_handle_seconds']

# Merge hist_counts (handled_case_count) with avg_handle
merged = pd.merge(hist_counts, avg_handle, on='agentid', how='left')
# handled_case_count may be NaN? but hist_counts present; avg_handle may be NaN if agent had no non-transferred cases

# Filter agents who handled more than one case (handled_case_count > 1)
merged['handled_case_count'] = merged['handled_case_count'].astype(int)
merged_f = merged[merged['handled_case_count'] > 1].copy()

# Among these, we need the agent with lowest avg_handle_seconds. But avg_handle_seconds may be NaN for agents who had no non-transferred cases; exclude those
merged_f = merged_f[merged_f['avg_handle_seconds'].notna()]

result_agent = ""
if not merged_f.empty:
    # pick min avg_handle_seconds
    min_row = merged_f.loc[merged_f['avg_handle_seconds'].idxmin()]
    result_agent = min_row['agentid']
else:
    result_agent = ""

print('__RESULT__:')
print(json.dumps(result_agent))"""

env_args = {'var_call_lCqHCLG3aXnND4ZSSpauSnGG': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_QHxrD2NgBgeYTHDHGeVWSEBX': 'file_storage/call_QHxrD2NgBgeYTHDHGeVWSEBX.json', 'var_call_7znFSGi8VcAnECEJCDFXk848': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_ckKWzLLDbyARtW30IQGRuS8K': '', 'var_call_b6hlpWzHkJS3AQM2Dyxhc9Qf': [{'ownerid': '005Wt000003NDqDIAW', 'case_count': 1, 'avg_handle_seconds': 882.0}, {'ownerid': '005Wt000003NEtOIAW', 'case_count': 1, 'avg_handle_seconds': 1007.0}, {'ownerid': '005Wt000003NIddIAG', 'case_count': 1, 'avg_handle_seconds': 2194.0}, {'ownerid': '005Wt000003NJD9IAO', 'case_count': 1, 'avg_handle_seconds': 21608.0}, {'ownerid': '005Wt000003NJGLIA4', 'case_count': 1, 'avg_handle_seconds': 1442.0}, {'ownerid': '005Wt000003NJJaIAO', 'case_count': 1, 'avg_handle_seconds': 14712.0}, {'ownerid': '005Wt000003NJufIAG', 'case_count': 1, 'avg_handle_seconds': 33068.0}]}

exec(code, env_args)
