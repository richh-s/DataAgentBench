code = """import json
import pandas as pd
# Load previous tool results from storage variables
cases = var_call_7znFSGi8VcAnECEJCDFXk848
# var_call_QHxrD2NgBgeYTHDHGeVWSEBX is a file path to the large JSON
with open(var_call_QHxrD2NgBgeYTHDHGeVWSEBX, 'r') as f:
    casehist = json.load(f)

# Create DataFrames
df_cases = pd.DataFrame(cases)
df_hist = pd.DataFrame(casehist)

# Normalize IDs: remove leading # and strip whitespace for case ids and owner ids
def norm_id(x):
    if pd.isna(x):
        return x
    if isinstance(x, str):
        return x.strip().lstrip('#')
    return x

for col in ['id','caseid__c','oldvalue__c','newvalue__c']:
    if col in df_hist.columns:
        df_hist[col] = df_hist[col].apply(norm_id)
for col in ['id','ownerid','createddate','closeddate']:
    if col in df_cases.columns:
        df_cases[col] = df_cases[col].apply(norm_id) if col in ['id','ownerid'] else df_cases[col]

# Count owner assignment entries per case
# The query to casehistory already filtered to Owner Assignment entries, but ensure field__c contains Owner
if 'field__c' in df_hist.columns:
    df_hist = df_hist[df_hist['field__c'].str.contains('Owner', case=False, na=False)]

counts = df_hist.groupby('caseid__c').size().reset_index(name='assign_count')

# Normalize case ids in df_cases
df_cases['id'] = df_cases['id'].apply(norm_id)

# Merge counts into cases
df = pd.merge(df_cases, counts, left_on='id', right_on='caseid__c', how='left')
# If no history rows found, assign_count NaN -> 0
df['assign_count'] = df['assign_count'].fillna(0).astype(int)

# We only compute handle time for cases that have NOT been transferred: assign_count == 1
# Also consider createddate and closeddate parse
df['createddate_parsed'] = pd.to_datetime(df['createddate'], errors='coerce')
df['closeddate_parsed'] = pd.to_datetime(df['closeddate'], errors='coerce')
# Compute handle time in seconds
df['handle_seconds'] = (df['closeddate_parsed'] - df['createddate_parsed']).dt.total_seconds()

# Filter to assign_count == 1 and positive handle_seconds
df_valid = df[(df['assign_count'] == 1) & (df['handle_seconds'].notna())]

# Normalize ownerid
df_valid['ownerid'] = df_valid['ownerid'].apply(norm_id)

# Group by ownerid, compute count and average
grp = df_valid.groupby('ownerid').agg(case_count=('id','count'), avg_handle_seconds=('handle_seconds','mean')).reset_index()

# Filter agents processing more than one case (case_count > 1)
grpf = grp[grp['case_count'] > 1]

result_id = None
if not grpf.empty:
    # Find owner with lowest avg_handle_seconds
    min_row = grpf.loc[grpf['avg_handle_seconds'].idxmin()]
    result_id = min_row['ownerid']
else:
    # No agent with >1 non-transferred cases in period; we'll return empty string
    result_id = ""

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_call_lCqHCLG3aXnND4ZSSpauSnGG': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_QHxrD2NgBgeYTHDHGeVWSEBX': 'file_storage/call_QHxrD2NgBgeYTHDHGeVWSEBX.json', 'var_call_7znFSGi8VcAnECEJCDFXk848': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
