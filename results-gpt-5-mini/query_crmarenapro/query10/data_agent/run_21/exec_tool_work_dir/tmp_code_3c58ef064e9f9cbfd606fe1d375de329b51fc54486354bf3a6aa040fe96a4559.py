code = """import json
import pandas as pd

# Load data from previous tool calls
case_rows = var_call_YC2VMrChNhmEZ8g9GgCIkM6R
# var_call_Fxy... is a path to a JSON file with the casehistory results
with open(var_call_Fxyqlg7mVagx0HowbFU4RKbn, 'r') as f:
    ch = json.load(f)

# Create DataFrames
cases_df = pd.DataFrame(case_rows)
ch_df = pd.DataFrame(ch)

# Normalize ID-like fields by stripping whitespace and leading '#'
def normalize_id(x):
    if pd.isna(x):
        return x
    if not isinstance(x, str):
        x = str(x)
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Normalize relevant columns
if 'id' in cases_df.columns:
    cases_df['norm_id'] = cases_df['id'].apply(normalize_id)
else:
    cases_df['norm_id'] = None

if 'ownerid' in cases_df.columns:
    cases_df['norm_ownerid'] = cases_df['ownerid'].apply(lambda x: normalize_id(x) if pd.notna(x) else x)
else:
    cases_df['norm_ownerid'] = None

if 'caseid__c' in ch_df.columns:
    ch_df['norm_caseid'] = ch_df['caseid__c'].apply(normalize_id)
else:
    ch_df['norm_caseid'] = None

# Filter only Owner Assignment records (should already be but safe)
if 'field__c' in ch_df.columns:
    ch_df = ch_df[ch_df['field__c'] == 'Owner Assignment']

# Count assignments per case
assign_counts = ch_df.groupby('norm_caseid').size().reset_index(name='assign_count')

# Parse datetimes and compute handle time in seconds
cases_df['created_dt'] = pd.to_datetime(cases_df['createddate'], utc=True)
cases_df['closed_dt'] = pd.to_datetime(cases_df['closeddate'], utc=True)
cases_df['handle_seconds'] = (cases_df['closed_dt'] - cases_df['created_dt']).dt.total_seconds()

# Merge assign counts into cases
merged = cases_df.merge(assign_counts, left_on='norm_id', right_on='norm_caseid', how='left')
# If a case has no owner assignment records in history, treat as single assignment (assign_count = 1)
merged['assign_count'] = merged['assign_count'].fillna(1)

# Keep only cases that were NOT transferred (assign_count == 1)
no_transfer_cases = merged[merged['assign_count'] == 1].copy()

# Group by owner and compute average handle time and case counts
# Normalize owner id
no_transfer_cases['norm_ownerid'] = no_transfer_cases['norm_ownerid'].fillna('').astype(str)
owner_stats = no_transfer_cases.groupby('norm_ownerid').agg(
    case_count=('norm_id', 'count'),
    avg_handle_seconds=('handle_seconds', 'mean')
).reset_index()

# Filter owners that processed more than one case (case_count > 1)
eligible = owner_stats[owner_stats['case_count'] > 1].copy()

result_id = None
if not eligible.empty:
    # Choose owner with lowest average handle time; break ties by lexicographic owner id
    eligible = eligible.sort_values(by=['avg_handle_seconds', 'norm_ownerid'], ascending=[True, True])
    result_id = eligible.iloc[0]['norm_ownerid']
    # If empty string, set to None
    if result_id == '':
        result_id = None

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_call_z0N15TOFnOovVzzLZ9Sdo3d1': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_0TW1GLrQccZLd2I5xitNdUSu': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_Fxyqlg7mVagx0HowbFU4RKbn': 'file_storage/call_Fxyqlg7mVagx0HowbFU4RKbn.json', 'var_call_G1d1M8zrVBAGl4Qrtq7ALzhw': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_YC2VMrChNhmEZ8g9GgCIkM6R': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
