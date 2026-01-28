code = """import json
import pandas as pd
from datetime import datetime

# Load data from tool outputs available in storage
owner_file = var_call_IYmLVjj7zdpUho4Ak7qg1cGQ  # this is a file path to full JSON
with open(owner_file, 'r') as f:
    owner_list = json.load(f)

case_list = var_call_HNDs1BGqMureWKUMSqn0WTPB

# Create DataFrames
df_owner = pd.DataFrame(owner_list)
df_cases = pd.DataFrame(case_list)

# Cleaning function for IDs (strip whitespace and leading '#')
def clean_id(x):
    if pd.isna(x):
        return x
    if not isinstance(x, str):
        x = str(x)
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Clean relevant ID fields
if 'caseid__c' in df_owner.columns:
    df_owner['caseid_clean'] = df_owner['caseid__c'].astype(str).map(clean_id)
else:
    df_owner['caseid_clean'] = df_owner['caseid__c'].astype(str).map(clean_id)

if 'newvalue__c' in df_owner.columns:
    df_owner['owner_clean'] = df_owner['newvalue__c'].astype(str).map(clean_id)
else:
    df_owner['owner_clean'] = df_owner['newvalue__c'].astype(str).map(clean_id)

# Clean case ids in cases
df_cases['caseid_clean'] = df_cases['id'].astype(str).map(clean_id)

# Count owner assignment occurrences per case
owner_counts = df_owner.groupby('caseid_clean').size().reset_index(name='assign_count')

# Merge counts with cases to get only cases in timeframe
df = pd.merge(df_cases, owner_counts, on='caseid_clean', how='left')

# Only consider cases with exactly one owner assignment
df_single = df[df['assign_count'] == 1].copy()

# For these cases, get the corresponding owner (the single owner assignment)
# Merge to bring in owner_clean from df_owner
df_single = pd.merge(df_single, df_owner[['caseid_clean', 'owner_clean']], on='caseid_clean', how='left')

# Compute handle time in seconds (closeddate - createddate)
# Parse datetimes
df_single['created_dt'] = pd.to_datetime(df_single['createddate'], utc=True)
df_single['closed_dt'] = pd.to_datetime(df_single['closeddate'], utc=True)

# Some rows may have nulls; drop if either is null
df_single = df_single.dropna(subset=['created_dt', 'closed_dt', 'owner_clean'])

# Handle time in seconds
df_single['handle_seconds'] = (df_single['closed_dt'] - df_single['created_dt']).dt.total_seconds()

# Group by owner and compute count and average handle time
grp = df_single.groupby('owner_clean').agg(case_count=('caseid_clean', 'nunique'), avg_handle_seconds=('handle_seconds', 'mean')).reset_index()

# Filter agents that processed more than one case
eligible = grp[grp['case_count'] > 1].copy()

# If no eligible agents, return empty string
if eligible.empty:
    result = None
else:
    # Find agent(s) with lowest avg_handle_seconds
    min_avg = eligible['avg_handle_seconds'].min()
    winners = eligible[eligible['avg_handle_seconds'] == min_avg].sort_values('owner_clean')
    # Choose first winner (deterministic)
    result = winners.iloc[0]['owner_clean']

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_g8PEloK5cySnokKEdXcLuEWA': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_4pK8jzDGduHiT4phJH0iGrKD': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_IYmLVjj7zdpUho4Ak7qg1cGQ': 'file_storage/call_IYmLVjj7zdpUho4Ak7qg1cGQ.json', 'var_call_HNDs1BGqMureWKUMSqn0WTPB': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
