code = """import pandas as pd
import json

# Load tool results from storage variables
hist_path = var_call_p7duV5QIGtAMZnU9fOk6AZba  # this is a filepath to a JSON
with open(hist_path, 'r', encoding='utf-8') as f:
    hist = json.load(f)

cases = var_call_VjVf9ypXcO8yCXKtY9ltybly  # list of dicts

# Create DataFrames
df_hist = pd.DataFrame(hist)
df_cases = pd.DataFrame(cases)

# Normalize IDs by stripping whitespace and leading '#'
def norm_id(x):
    if pd.isna(x):
        return x
    s = str(x).strip()
    if s.startswith('#'):
        return s[1:]
    return s

for col in ['caseid__c', 'oldvalue__c', 'newvalue__c', 'id']:
    if col in df_hist.columns:
        df_hist[col] = df_hist[col].apply(norm_id)

if 'id' in df_cases.columns:
    df_cases['id'] = df_cases['id'].apply(norm_id)

# Parse dates
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])
if 'createddate' in df_hist.columns:
    df_hist['createddate'] = pd.to_datetime(df_hist['createddate'], errors='coerce')

# Consider only Owner Assignment entries
df_hist_owner = df_hist[df_hist['field__c'] == 'Owner Assignment'].copy()

# Filter to cases in df_cases (closed in window)
case_ids = set(df_cases['id'].unique())
df_hist_owner = df_hist_owner[df_hist_owner['caseid__c'].isin(case_ids)]

# For each case, count owner assignment rows
case_group = df_hist_owner.groupby('caseid__c')
case_owner_counts = case_group.size().to_dict()  # caseid -> count

# Prepare per-agent handled cases and handle times (for single-owner cases only)
agent_cases = {}  # agent_id -> set(case_ids)
agent_handle_times = {}  # agent_id -> list(seconds)

for case in df_cases.itertuples(index=False):
    cid = case.id
    created = case.createddate
    closed = case.closeddate
    # owner assignments for this case
    if cid not in case_owner_counts:
        # no owner assignment records; skip
        continue
    cnt = case_owner_counts[cid]
    rows = df_hist_owner[df_hist_owner['caseid__c'] == cid]
    # For counting: all agents that appear as newvalue__c for this case
    agents_for_case = rows['newvalue__c'].dropna().unique().tolist()
    for a in agents_for_case:
        if a is None:
            continue
        agent_cases.setdefault(a, set()).add(cid)
    # For handle time: only if cnt == 1 (not transferred)
    if cnt == 1:
        # sole agent
        sole_agent = rows['newvalue__c'].iloc[0]
        if pd.isna(sole_agent):
            continue
        sole_agent = norm_id(sole_agent)
        # compute handle time in seconds
        ht_seconds = (closed - created).total_seconds()
        agent_handle_times.setdefault(sole_agent, []).append(ht_seconds)

# Compute agents who processed more than one case
agents_with_counts = {a: len(s) for a, s in agent_cases.items()}
eligible_agents = [a for a, c in agents_with_counts.items() if c > 1]

# For those eligible, compute average handle time (only from single-owner cases included in agent_handle_times)
avg_handle = {}
for a in eligible_agents:
    times = agent_handle_times.get(a, [])
    if len(times) == 0:
        # no computable handle times for this agent; skip
        continue
    avg_handle[a] = sum(times) / len(times)

# Find agent with minimum average handle time
result_agent = None
if len(avg_handle) > 0:
    # if tie, pick smallest avg then smallest id
    min_avg = min(avg_handle.values())
    candidates = [a for a, v in avg_handle.items() if v == min_avg]
    result_agent = sorted(candidates)[0]

# Print result in required format. If None, print empty string
out = result_agent if result_agent is not None else ""

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_NLswGWVtEhqTVWqJAt1y28xp': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_Qg6VIAVYZqBjmCruFdlYGCL4': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_p7duV5QIGtAMZnU9fOk6AZba': 'file_storage/call_p7duV5QIGtAMZnU9fOk6AZba.json', 'var_call_VjVf9ypXcO8yCXKtY9ltybly': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}]}

exec(code, env_args)
