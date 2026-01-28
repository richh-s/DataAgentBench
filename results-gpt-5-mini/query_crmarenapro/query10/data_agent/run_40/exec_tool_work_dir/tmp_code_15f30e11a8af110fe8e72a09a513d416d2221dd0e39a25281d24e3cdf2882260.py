code = """import json
import pandas as pd

# Load large history file
history_path = var_call_4r4XuVMgUzyMqA4tXZEbrpgE
with open(history_path, 'r') as f:
    history = json.load(f)

df_hist = pd.DataFrame(history)
# Data from assign counts per case
df_assign_counts = pd.DataFrame(var_call_bhNDFuB4WYgayNO7oMscBuUD)
# Cases closed in period
df_cases = pd.DataFrame(var_call_AWbqZhpj9k4nUpx8azHfSYrE)

# Normalize IDs: strip leading # and whitespace
for df in (df_hist, df_assign_counts, df_cases):
    if 'caseid__c' in df.columns:
        df['caseid_norm'] = df['caseid__c'].astype(str).str.strip().str.lstrip('#')
    if 'caseid' in df.columns:
        df['caseid_norm'] = df['caseid'].astype(str).str.strip().str.lstrip('#')
    if 'id' in df.columns:
        df['id_norm'] = df['id'].astype(str).str.strip().str.lstrip('#')

# Normalize owner columns
if 'new_owner' in df_hist.columns:
    df_hist['new_owner_norm'] = df_hist['new_owner'].astype(str).str.strip().str.lstrip('#')
if 'old_owner' in df_hist.columns:
    df_hist['old_owner_norm'] = df_hist['old_owner'].astype(str).str.strip().str.lstrip('#')

if 'ownerid' in df_cases.columns:
    df_cases['ownerid_norm'] = df_cases['ownerid'].astype(str).str.strip().str.lstrip('#')

# Normalize assign_counts
if 'assign_count' in df_assign_counts.columns and 'caseid' in df_assign_counts.columns:
    df_assign_counts['caseid_norm'] = df_assign_counts['caseid'].astype(str).str.strip().str.lstrip('#')
    df_assign_counts['assign_count'] = pd.to_numeric(df_assign_counts['assign_count'], errors='coerce').fillna(0).astype(int)

# Filter history to only entries for cases closed in the period
closed_case_ids = set(df_cases['id_norm'].tolist())
 df_hist_filtered = df_hist[df_hist['caseid_norm'].isin(closed_case_ids)].copy()

# Count distinct cases per agent where agent appears as new_owner in history (exclude 'None')
df_hist_filtered = df_hist_filtered[df_hist_filtered['new_owner'].notna()]
# Exclude entries where new_owner is 'None' string
df_hist_filtered = df_hist_filtered[df_hist_filtered['new_owner'].astype(str).str.lower() != 'none']

agent_case_counts = df_hist_filtered.groupby(df_hist_filtered['new_owner_norm']).agg({'caseid_norm': lambda x: x.nunique()}).reset_index()
agent_case_counts.columns = ['agentid', 'cases_handled_count']

# Agents who handled more than one case
agents_gt1 = set(agent_case_counts[agent_case_counts['cases_handled_count'] > 1]['agentid'].tolist())

# Prepare cases assign count merged
# Use id_norm in df_cases and caseid_norm in df_assign_counts
df_cases2 = df_cases.copy()
if 'id_norm' in df_cases2.columns:
    df_cases2 = df_cases2.rename(columns={'id_norm': 'caseid_norm'})

df_cases2 = df_cases2.merge(df_assign_counts[['caseid_norm', 'assign_count']], on='caseid_norm', how='left')
# fill missing assign_count with 1 (if no history then assume 1?) but safer to set to 1
df_cases2['assign_count'] = df_cases2['assign_count'].fillna(1).astype(int)

# Only include non-transferred cases (assign_count == 1) for handle time computation
df_non_transferred = df_cases2[df_cases2['assign_count'] == 1].copy()

# Compute handle time in seconds
# Parse datetimes
df_non_transferred['createddate_ts'] = pd.to_datetime(df_non_transferred['createddate'], errors='coerce')
df_non_transferred['closeddate_ts'] = pd.to_datetime(df_non_transferred['closeddate'], errors='coerce')

df_non_transferred['handle_seconds'] = (df_non_transferred['closeddate_ts'] - df_non_transferred['createddate_ts']).dt.total_seconds()

# Attribute case to ownerid_norm
# If ownerid_norm missing, try to get from history new_owner where case had only one assign
# Build mapping from history where caseid_norm had single assign to new_owner_norm
single_assign_cases = set(df_assign_counts[df_assign_counts['assign_count'] == 1]['caseid_norm'].tolist())
# From history, find the new_owner for those cases (first non-None)
hist_single = df_hist[df_hist['caseid_norm'].isin(single_assign_cases)].copy()
# Exclude None
hist_single = hist_single[hist_single['new_owner'].astype(str).str.lower() != 'none']
# For cases that have an entry, take the most recent new_owner by createddate if multiple
if not hist_single.empty:
    hist_single['createddate_ts'] = pd.to_datetime(hist_single['createddate'], errors='coerce')
    hist_single_sorted = hist_single.sort_values(['caseid_norm', 'createddate_ts']).groupby('caseid_norm').last().reset_index()
    case_to_owner_hist = dict(zip(hist_single_sorted['caseid_norm'], hist_single_sorted['new_owner_norm']))
else:
    case_to_owner_hist = {}

# Fill ownerid_norm in df_non_transferred if missing
if 'ownerid_norm' not in df_non_transferred.columns:
    df_non_transferred['ownerid_norm'] = None

for idx, row in df_non_transferred[df_non_transferred['ownerid_norm'].isna()].iterrows():
    cid = row['caseid_norm']
    if cid in case_to_owner_hist:
        df_non_transferred.at[idx, 'ownerid_norm'] = case_to_owner_hist[cid]

# Now group by ownerid_norm and compute average handle_seconds
df_non_transferred = df_non_transferred[df_non_transferred['ownerid_norm'].notna()]
avg_handle = df_non_transferred.groupby('ownerid_norm').agg({'handle_seconds': 'mean'}).reset_index()
avg_handle.columns = ['agentid', 'avg_handle_seconds']

# Filter to agents who handled >1 case
avg_handle_filtered = avg_handle[avg_handle['agentid'].isin(agents_gt1)].copy()

# If none, result is None
result_agent = None
if not avg_handle_filtered.empty:
    # pick agent with lowest average
    best = avg_handle_filtered.sort_values('avg_handle_seconds').iloc[0]
    result_agent = str(best['agentid'])

import json as _json
print("__RESULT__:")
print(_json.dumps(result_agent))"""

env_args = {'var_call_B9gxT1rX7eGhshUQYMUHEQx6': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_bhNDFuB4WYgayNO7oMscBuUD': [{'caseid': '500Wt00000DDDfwIAH', 'assign_count': '2'}, {'caseid': '500Wt00000DDDtTIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDNYoIAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDPIsIAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDPM6IAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDPSZIA5', 'assign_count': '1'}, {'caseid': '500Wt00000DDPZ0IAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDPsOIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDPsPIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDQRsIAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDQoUIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDRB2IAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDRVzIAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDRW0IAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDTEQIA5', 'assign_count': '1'}, {'caseid': '500Wt00000DDTERIA5', 'assign_count': '2'}, {'caseid': '500Wt00000DDTHfIAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDTxbIAH', 'assign_count': '1'}, {'caseid': '500Wt00000DDU5iIAH', 'assign_count': '1'}, {'caseid': '500Wt00000DDYUGIA5', 'assign_count': '1'}, {'caseid': '500Wt00000DDYdwIAH', 'assign_count': '1'}, {'caseid': '500Wt00000DDYipIAH', 'assign_count': '1'}, {'caseid': '500Wt00000DDYpGIAX', 'assign_count': '2'}, {'caseid': '500Wt00000DDYpHIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDZ0VIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDZ27IAH', 'assign_count': '1'}, {'caseid': '500Wt00000DDZ5LIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDZJuIAP', 'assign_count': '1'}, {'caseid': '500Wt00000DDZmsIAH', 'assign_count': '1'}, {'caseid': '500Wt00000DDZtKIAX', 'assign_count': '1'}, {'caseid': '500Wt00000DDZtLIAX', 'assign_count': '2'}, {'caseid': '500Wt00000DDeoCIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDepmIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDet1IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDfFcIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDfHCIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDfYwIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDfYxIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDflsIAD', 'assign_count': '2'}, {'caseid': '500Wt00000DDfvXIAT', 'assign_count': '2'}, {'caseid': '500Wt00000DDfx8IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDg1yIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDg1zIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDg20IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDg8QIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDg8RIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDgLKIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDgLLIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDnt6IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDnt7IAD', 'assign_count': '2'}, {'caseid': '500Wt00000DDsG2IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDsG3IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDsG4IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDsKtIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDsKuIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDt7GIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDt7HIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDxScIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDxSdIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDxVqIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDxZ4IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDxduIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDxkMIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDxnbIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDy8aIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDy8bIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDyRvIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDydCIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDymuIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDyuwIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDyznIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDyzoIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDyzpIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDz6FIAT', 'assign_count': '2'}, {'caseid': '500Wt00000DDz6GIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzB4IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzEIIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzJ8IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzKjIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzMLIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzMMIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzNxIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzPZIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzRBIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzRCIA1', 'assign_count': '2'}, {'caseid': '500Wt00000DDzSnIAL', 'assign_count': '2'}, {'caseid': '500Wt00000DDzSoIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzUPIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzUQIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzW2IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzW3IAL', 'assign_count': '2'}, {'caseid': '500Wt00000DDzXdIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzXeIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DDzZFIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzZGIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzZHIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DDzarIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzcTIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDze5IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDze6IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzfhIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzhJIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzivIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzkXIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzm9IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzmAIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzmBIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzmCIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDznlIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzpNIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzqzIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzr0IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzr2IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzsbIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzscIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzuDIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzuEIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzvpIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzvqIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DDzxRIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DDzz3IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE00fIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE00gIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE00hIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE02HIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DE03tIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE05VIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DE077IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE078IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE079IAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE07AIAT', 'assign_count': '1'}, {'caseid': '500Wt00000DE08jIAD', 'assign_count': '1'}, {'caseid': '500Wt00000DE0ALIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0AMIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0BxIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0ByIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0DZIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0FCIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0FDIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0GnIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0IPIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0K1IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0LdIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0NFIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0NGIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0QTIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0S5IAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0ThIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0VJIA1', 'assign_count': '1'}, {'caseid': '500Wt00000DE0WvIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0WwIAL', 'assign_count': '1'}, {'caseid': '500Wt00000DE0YXIA1', 'assign_count': '2'}, {'caseid': '500Wt00000DE0a9IAD', 'assign_count': '1'}], 'var_call_AWbqZhpj9k4nUpx8azHfSYrE': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_4r4XuVMgUzyMqA4tXZEbrpgE': 'file_storage/call_4r4XuVMgUzyMqA4tXZEbrpgE.json'}

exec(code, env_args)
