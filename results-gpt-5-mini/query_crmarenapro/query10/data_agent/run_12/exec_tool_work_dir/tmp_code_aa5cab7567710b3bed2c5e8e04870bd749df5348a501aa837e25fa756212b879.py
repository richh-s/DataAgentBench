code = """import json
import pandas as pd
from datetime import datetime

# Load previous tool results from storage variables
# var_call_W5j0Zc0qCY34J8SueX695ZnJ may be a filepath string to a JSON file or a list
hist_source = var_call_W5j0Zc0qCY34J8SueX695ZnJ
if isinstance(hist_source, str):
    with open(hist_source, 'r') as f:
        hist_records = json.load(f)
else:
    hist_records = hist_source

cases_records = var_call_9PlNZpdtpWSZhfAY9KJlL7K6

# Create DataFrames
hist_df = pd.DataFrame(hist_records)
cases_df = pd.DataFrame(cases_records)

# Normalize ID-like fields: strip leading '#' and whitespace
def clean_id(x):
    if pd.isna(x):
        return x
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

hist_df['caseid_clean'] = hist_df['caseid__c'].apply(clean_id)
# Also normalize field__c and newvalue__c
hist_df['field_clean'] = hist_df['field__c'].astype(str).str.strip()
hist_df['newvalue_clean'] = hist_df['newvalue__c'].apply(clean_id)

cases_df['id_clean'] = cases_df['id'].apply(clean_id)
# normalize ownerid
cases_df['ownerid_clean'] = cases_df['ownerid'].apply(clean_id)
# parse dates
cases_df['created_dt'] = pd.to_datetime(cases_df['createddate'])
cases_df['closed_dt'] = pd.to_datetime(cases_df['closeddate'])

# Consider only Owner Assignment entries
owner_assignments = hist_df[hist_df['field_clean'].str.lower() == 'owner assignment']

# Count owner assignment events per case
oa_counts = owner_assignments.groupby('caseid_clean').size().rename('owner_assignment_count').reset_index()

# Merge counts into cases
cases_merged = cases_df.merge(oa_counts, left_on='id_clean', right_on='caseid_clean', how='left')
# If no owner assignment entries found, assume 0
cases_merged['owner_assignment_count'] = cases_merged['owner_assignment_count'].fillna(0).astype(int)

# According to policy, for cases that have been transferred to other agents, there will be MORE THAN ONE 'Owner Assignment'.
# For handle time computation, exclude cases with owner_assignment_count > 1
cases_merged['handle_seconds'] = (cases_merged['closed_dt'] - cases_merged['created_dt']).dt.total_seconds()

valid_cases = cases_merged[cases_merged['owner_assignment_count'] <= 1].copy()

# Compute per-agent stats
agent_stats = valid_cases.groupby('ownerid_clean').agg(
    case_count=('id', 'count'),
    avg_handle_seconds=('handle_seconds', 'mean')
).reset_index()

# Filter agents who processed more than one case (case_count > 1)
eligible_agents = agent_stats[agent_stats['case_count'] > 1].copy()

# If no eligible agents, result should be empty
if eligible_agents.empty:
    result = None
else:
    # Find agent with lowest average handle time
    best = eligible_agents.loc[eligible_agents['avg_handle_seconds'].idxmin()]
    result = best['ownerid_clean']

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_W5j0Zc0qCY34J8SueX695ZnJ': 'file_storage/call_W5j0Zc0qCY34J8SueX695ZnJ.json', 'var_call_9PlNZpdtpWSZhfAY9KJlL7K6': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
