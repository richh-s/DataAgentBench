code = """import json
import pandas as pd

# Load previous tool results from storage variables
# var_call_XOVX3CNKGzLYu53I7Rb0E9y3 is expected to be a filepath containing JSON list (casehistory records)
# var_call_gMJb6CQU78Slfuo4ErmYrzN6 is the direct list of Case records

# Read casehistory data
ch_var = var_call_XOVX3CNKGzLYu53I7Rb0E9y3
if isinstance(ch_var, str):
    # treat as filepath
    with open(ch_var, 'r', encoding='utf-8') as f:
        ch_data = json.load(f)
else:
    ch_data = ch_var

cases_data = var_call_gMJb6CQU78Slfuo4ErmYrzN6

# Helper to clean IDs (strip whitespace and leading '#')
def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Build DataFrames
ch_df = pd.DataFrame(ch_data)
if ch_df.empty:
    ch_df = pd.DataFrame(columns=['id','caseid__c','oldvalue__c','newvalue__c','createddate','field__c'])

cases_df = pd.DataFrame(cases_data)
if cases_df.empty:
    cases_df = pd.DataFrame(columns=['id','createddate','closeddate','ownerid'])

# Clean IDs
ch_df['caseid_clean'] = ch_df['caseid__c'].apply(clean_id)
ch_df['field_clean'] = ch_df['field__c'].astype(str).str.strip().str.lower()

cases_df['caseid_clean'] = cases_df['id'].apply(clean_id)
cases_df['ownerid_clean'] = cases_df['ownerid'].apply(clean_id)

# Filter casehistory to Owner Assignment entries
ch_owner = ch_df[ch_df['field_clean'].str.contains('owner') | ch_df['field_clean'].str.contains('owner assignment')]

# Count owner assignment records per case
owner_counts = ch_owner.groupby('caseid_clean').size().reset_index(name='owner_assignment_count')

# Merge with cases that were closed in past 4 months (our cases_df already filtered by query)
merged = cases_df.merge(owner_counts, on='caseid_clean', how='left')
# owner_assignment_count NaN means no owner assignment recorded; treat as 0
merged['owner_assignment_count'] = merged['owner_assignment_count'].fillna(0).astype(int)

# According to policy, cases that have NOT been transferred will have only ONE 'Owner Assignment'
# So we only include cases with owner_assignment_count == 1
selected = merged[merged['owner_assignment_count'] == 1].copy()

# Compute handle time in seconds
selected['created_dt'] = pd.to_datetime(selected['createddate'])
selected['closed_dt'] = pd.to_datetime(selected['closeddate'])
selected['handle_seconds'] = (selected['closed_dt'] - selected['created_dt']).dt.total_seconds()

# Group by owner and compute average handle time and count
grouped = selected.groupby('ownerid_clean').agg(count_cases=('caseid_clean','count'), avg_handle_seconds=('handle_seconds','mean')).reset_index()

# Filter agents that processed more than one case
candidates = grouped[grouped['count_cases'] > 1].copy()

# Find agent with lowest average handle time
if not candidates.empty:
    best_row = candidates.sort_values(['avg_handle_seconds','ownerid_clean']).iloc[0]
    best_agent = best_row['ownerid_clean']
else:
    best_agent = None

# Output result as JSON-serializable string
print("__RESULT__:")
print(json.dumps(best_agent))"""

env_args = {'var_call_7utMviyenT2oVIqaTVgIgDIn': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_XOVX3CNKGzLYu53I7Rb0E9y3': 'file_storage/call_XOVX3CNKGzLYu53I7Rb0E9y3.json', 'var_call_gMJb6CQU78Slfuo4ErmYrzN6': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
