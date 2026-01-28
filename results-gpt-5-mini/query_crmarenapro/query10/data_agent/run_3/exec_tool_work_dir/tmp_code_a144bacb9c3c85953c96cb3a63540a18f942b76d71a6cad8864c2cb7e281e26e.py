code = """import json
import pandas as pd
from datetime import datetime

# Load the closed cases from storage
cases = pd.DataFrame(var_call_dOrIyNTdH7xWnLxyqZ5diflB)

# Load owner assignment records from the large json file path
owner_assignments_path = var_call_C2jO3lXsGput58bPIBHbY5lf
with open(owner_assignments_path, 'r', encoding='utf-8') as f:
    owner_assignments = json.load(f)

oa = pd.DataFrame(owner_assignments)

# Normalize function for IDs
def normalize_id(x):
    if x is None:
        return None
    s = str(x).strip()
    # remove leading '#' characters
    while s.startswith('#'):
        s = s[1:]
    return s

# Normalize case ids in both datasets
cases['norm_case_id'] = cases['id'].apply(normalize_id)

oa['norm_caseid'] = oa['caseid__c'].apply(normalize_id)
# Filter only Owner Assignment records just in case
if 'field__c' in oa.columns:
    oa = oa[oa['field__c'] == 'Owner Assignment']

# Build counts of owner assignment per case (normalized)
oa_counts = oa.groupby('norm_caseid').size().to_dict()

# For each closed case in the date range, determine if it was transferred (count>1)
# Keep only cases with exactly 1 owner assignment
single_owner_cases = []
for _, row in cases.iterrows():
    cid = row['norm_case_id']
    cnt = oa_counts.get(cid, 0)
    if cnt == 1:
        # find the owner assignment record for this case
        rec = oa[oa['norm_caseid'] == cid].iloc[0]
        owner_raw = rec.get('newvalue__c')
        owner = normalize_id(owner_raw)
        # compute handle time in seconds: closeddate - createddate
        try:
            created = pd.to_datetime(row['createddate'])
            closed = pd.to_datetime(row['closeddate'])
            handle_seconds = (closed - created).total_seconds()
            # only include non-negative durations
            if handle_seconds >= 0:
                single_owner_cases.append({'case_id': cid, 'owner': owner, 'handle_seconds': handle_seconds})
        except Exception:
            # skip rows with parse issues
            continue

if not single_owner_cases:
    result = None
else:
    df = pd.DataFrame(single_owner_cases)
    # Aggregate per owner
    agg = df.groupby('owner').agg(count=('case_id', 'size'), avg_handle_seconds=('handle_seconds', 'mean')).reset_index()
    # Filter owners who processed more than one case
    agg_filtered = agg[agg['count'] > 1]
    if agg_filtered.empty:
        result = None
    else:
        # find owner with lowest average handle time
        best_row = agg_filtered.sort_values(['avg_handle_seconds', 'owner']).iloc[0]
        result = best_row['owner']

# Print according to required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YL9AwteVuMbq4yS0zfm47hw7': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_jNcaq3qHZlaGZzuAD3wk2SFo': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_C2jO3lXsGput58bPIBHbY5lf': 'file_storage/call_C2jO3lXsGput58bPIBHbY5lf.json', 'var_call_dOrIyNTdH7xWnLxyqZ5diflB': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
