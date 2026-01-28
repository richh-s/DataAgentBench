code = """import json
import pandas as pd

# Load previous tool results available as variables
# var_call_5RQtEVuS99zLPxpFGoaR0eBf is a file path containing the large casehistory__c result
# var_call_xicnFukmeFH6CycwiG1m8g52 is the case list for closed cases in period

with open(var_call_5RQtEVuS99zLPxpFGoaR0eBf, 'r') as f:
    casehistory = json.load(f)

cases = var_call_xicnFukmeFH6CycwiG1m8g52

# Normalize helper
def norm_id(s):
    if s is None:
        return None
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s.strip()

# Filter owner assignment entries
owner_assignments = [r for r in casehistory if r.get('field__c') == 'Owner Assignment']
# Normalize case ids in owner assignments
for r in owner_assignments:
    r['caseid_norm'] = norm_id(r.get('caseid__c'))

# Count assignments per case
df_oa = pd.DataFrame(owner_assignments)
if df_oa.empty:
    assignment_counts = {}
else:
    assignment_counts = df_oa.groupby('caseid_norm').size().to_dict()

# Determine transferred cases: more than one owner assignment
transferred_cases = {cid for cid, cnt in assignment_counts.items() if cnt > 1}

# Prepare cases dataframe
for r in cases:
    r['id_norm'] = norm_id(r.get('id'))
    r['ownerid_norm'] = norm_id(r.get('ownerid'))

df_cases = pd.DataFrame(cases)
# Exclude transferred cases
if 'id_norm' not in df_cases.columns:
    df_cases['id_norm'] = df_cases['id'].apply(norm_id)

df_cases = df_cases[~df_cases['id_norm'].isin(transferred_cases)].copy()

# If no cases remain, return null
if df_cases.empty:
    result = None
else:
    # Parse dates
    df_cases['createddate_parsed'] = pd.to_datetime(df_cases['createddate'], utc=True)
    df_cases['closeddate_parsed'] = pd.to_datetime(df_cases['closeddate'], utc=True)
    # Compute handle time in seconds
    df_cases['handle_seconds'] = (df_cases['closeddate_parsed'] - df_cases['createddate_parsed']).dt.total_seconds()
    # Group by ownerid_norm
    grouped = df_cases.groupby('ownerid_norm').agg(
        cases_handled=('id_norm', 'count'),
        avg_handle_seconds=('handle_seconds', 'mean')
    ).reset_index()
    # Filter agents who processed more than one case
    grouped = grouped[grouped['cases_handled'] > 1]
    if grouped.empty:
        result = None
    else:
        # Find agent with lowest average handle time
        best = grouped.sort_values(['avg_handle_seconds', 'ownerid_norm']).iloc[0]
        result = best['ownerid_norm']

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5RQtEVuS99zLPxpFGoaR0eBf': 'file_storage/call_5RQtEVuS99zLPxpFGoaR0eBf.json', 'var_call_xicnFukmeFH6CycwiG1m8g52': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}]}

exec(code, env_args)
