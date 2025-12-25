code = """import json
import pandas as pd
from datetime import datetime, timezone

# Load data
cases_path = locals()['var_function-call-9360610570707735085']
history_path = locals()['var_function-call-724238365973199859']

with open(cases_path, 'r') as f:
    cases_data = json.load(f)
    
with open(history_path, 'r') as f:
    history_data = json.load(f)

df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

# Helper to clean IDs
def clean_id(x):
    if isinstance(x, str):
        return x.lstrip('#')
    return x

# Clean IDs in DataFrames
df_cases['id_clean'] = df_cases['id'].apply(clean_id)
df_cases['owner_clean'] = df_cases['ownerid'].apply(clean_id)
df_history['caseid_clean'] = df_history['caseid__c'].apply(clean_id)
df_history['new_owner_clean'] = df_history['newvalue__c'].apply(clean_id)
df_history['old_owner_clean'] = df_history['oldvalue__c'].apply(clean_id)

# Date Parsing
def parse_date(date_str):
    if not date_str or date_str == 'None':
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except:
        try:
             return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        except:
             return None

df_cases['created_dt'] = df_cases['createddate'].apply(parse_date)
df_cases['closed_dt'] = df_cases['closeddate'].apply(parse_date)

# Define Window
# 2023-05-02 to 2023-09-02
# Use timezone from data if possible, else UTC
sample_dt = df_cases['created_dt'].dropna().iloc[0] if not df_cases['created_dt'].dropna().empty else None
tz = sample_dt.tzinfo if sample_dt else timezone.utc

start_date = datetime(2023, 5, 2, tzinfo=tz)
end_date = datetime(2023, 9, 2, tzinfo=tz)

# Identify Relevant Cases (Closed in window)
relevant_cases = df_cases[
    (df_cases['closed_dt'] >= start_date) & 
    (df_cases['closed_dt'] <= end_date)
].copy()

# Calculate Handle Time (seconds)
relevant_cases['handle_time'] = (relevant_cases['closed_dt'] - relevant_cases['created_dt']).dt.total_seconds()

# Identify Candidate Agents (Closers of relevant cases)
candidate_agents = relevant_cases['owner_clean'].unique()

# Calculate Managed Count for Candidate Agents (using ALL cases and history)
agent_managed_cases = {agent: set() for agent in candidate_agents}

# 1. From All Cases (Current Owners)
for _, row in df_cases.iterrows():
    owner = row['owner_clean']
    if owner in agent_managed_cases:
        agent_managed_cases[owner].add(row['id_clean'])

# 2. From History (Past Owners)
# Filter history for relevant agents
mask = (df_history['new_owner_clean'].isin(candidate_agents)) | (df_history['old_owner_clean'].isin(candidate_agents))
relevant_history = df_history[mask]

for _, row in relevant_history.iterrows():
    c_id = row['caseid_clean']
    new_o = row['new_owner_clean']
    old_o = row['old_owner_clean']
    
    if new_o in agent_managed_cases:
        agent_managed_cases[new_o].add(c_id)
    if old_o in agent_managed_cases:
        agent_managed_cases[old_o].add(c_id)

# Filter Agents with > 1 Managed Case
eligible_agents = []
debug_counts = {}
for agent in candidate_agents:
    count = len(agent_managed_cases[agent])
    debug_counts[agent] = count
    if count > 1:
        eligible_agents.append(agent)

# Calculate Average Handle Time for Eligible Agents
results = []
for agent in eligible_agents:
    agent_cases = relevant_cases[relevant_cases['owner_clean'] == agent]
    if not agent_cases.empty:
        avg_time = agent_cases['handle_time'].mean()
        results.append({'agent_id': agent, 'avg_time': avg_time})

# Find Lowest
best_agent = None
if results:
    results.sort(key=lambda x: x['avg_time'])
    best_agent = results[0]['agent_id']

print("__RESULT__:")
print(json.dumps({"best_agent": best_agent, "debug_counts": debug_counts, "results": results}))"""

env_args = {'var_function-call-13710148199737365862': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-3515426018230989725': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-12924332762788559106': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-554246957191354409': [{'count': '7'}], 'var_function-call-724238365973199859': 'file_storage/function-call-724238365973199859.json', 'var_function-call-4325308466962925836': [], 'var_function-call-2501105650080026199': 'debug done', 'var_function-call-7989718457643891362': {'num_cases': 7, 'num_history_filtered': 5, 'case_ids': ['#500Wt00000DDzscIAD', '#500Wt00000DE02HIAT', '500Wt00000DDzsbIAD', '500Wt00000DDzuEIAT', '500Wt00000DDyzpIAD', '500Wt00000DDepmIAD', '500Wt00000DDzUPIA1'], 'agent_managed_counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}, 'agent_closers': ['005Wt000003NJufIAG', '005Wt000003NJGLIA4', '005Wt000003NDqDIAW', '005Wt000003NJD9IAO', '005Wt000003NEtOIAW', '005Wt000003NJJaIAO', '005Wt000003NIddIAG'], 'multi_managed_agents': []}, 'var_function-call-17188930995879181795': [{'count': '153'}], 'var_function-call-9360610570707735085': 'file_storage/function-call-9360610570707735085.json'}

exec(code, env_args)
