code = """import json
import pandas as pd
from datetime import datetime

# Load casehistory__c large result from file path variable
casehistory_file = var_call_KJ21cZQQkK5a2FUHKBQa4GWX
with open(casehistory_file, 'r') as f:
    casehistory = json.load(f)

# Load Case query result
cases = var_call_c0Y7BagHhQLRqI2yfQvCBX94

# Helper clean function
def clean_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

ch = pd.DataFrame(casehistory)
# Keep only Owner Assignment
ch = ch[ch['field__c'] == 'Owner Assignment'].copy()
# Clean caseid and newvalue
ch['caseid_clean'] = ch['caseid__c'].apply(clean_id)
ch['newvalue_clean'] = ch['newvalue__c'].apply(clean_id)
ch['createddate_parsed'] = pd.to_datetime(ch['createddate'], errors='coerce')

# Compute owner_counts per case
owner_counts = ch.groupby('caseid_clean').agg(
    owner_count=('id','count'),
    owner_id=('newvalue_clean', lambda x: x.iloc[0] if len(x)>0 else None)
).reset_index().rename(columns={'caseid_clean':'caseid'})

# Prepare cases DataFrame
cases_df = pd.DataFrame(cases)
if not cases_df.empty:
    cases_df['caseid'] = cases_df['id'].apply(clean_id)
    cases_df['ownerid_clean'] = cases_df['ownerid'].apply(clean_id)
    # parse without tz to avoid tz-aware vs naive problems
    cases_df['createddate_parsed'] = pd.to_datetime(cases_df['createddate'], errors='coerce').dt.tz_convert(None)
    cases_df['closeddate_parsed'] = pd.to_datetime(cases_df['closeddate'], errors='coerce').dt.tz_convert(None)
else:
    cases_df['caseid'] = []

# Filter cases within date range
start = pd.to_datetime('2023-05-02')
end = pd.to_datetime('2023-09-02')
# Ensure closeddate_parsed is naive datetimes
cases_df = cases_df[ (cases_df['closeddate_parsed'].notna()) & (cases_df['createddate_parsed'].notna()) & (cases_df['closeddate_parsed'] >= start) & (cases_df['closeddate_parsed'] <= end) ].copy()

# Merge with owner_counts
merged = pd.merge(cases_df, owner_counts, left_on='caseid', right_on='caseid', how='left')
# Only include cases with owner_count == 1 (not transferred)
merged = merged[ merged['owner_count'] == 1 ].copy()

# Compute handle seconds
merged['handle_seconds'] = (merged['closeddate_parsed'] - merged['createddate_parsed']).dt.total_seconds()

# Determine agent owner id to use: owner_id from owner_counts (newvalue) or ownerid from Case? Policy: owner assignment used. Use owner_id if present, else ownerid.
merged['agent_id'] = merged['owner_id'].where(merged['owner_id'].notna(), merged['ownerid_clean'])

# Group by agent
agent_stats = merged.groupby('agent_id').agg(
    num_cases=('caseid','nunique'),
    avg_handle_seconds=('handle_seconds','mean')
).reset_index()

# Filter agents with more than one case
agent_stats = agent_stats[ agent_stats['num_cases'] > 1 ]

# Sort by avg_handle_seconds ascending
agent_stats = agent_stats.sort_values('avg_handle_seconds')

if agent_stats.empty:
    result = None
else:
    result = agent_stats.iloc[0]['agent_id']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_RiIuDfDZO9IICiU6rGXfCp8V': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_HJC1avm8NECYX8eeMHWSoo6Q': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_KJ21cZQQkK5a2FUHKBQa4GWX': 'file_storage/call_KJ21cZQQkK5a2FUHKBQa4GWX.json', 'var_call_hpV53q7jsK7sfNQnIkBxCGCM': [], 'var_call_c0Y7BagHhQLRqI2yfQvCBX94': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
