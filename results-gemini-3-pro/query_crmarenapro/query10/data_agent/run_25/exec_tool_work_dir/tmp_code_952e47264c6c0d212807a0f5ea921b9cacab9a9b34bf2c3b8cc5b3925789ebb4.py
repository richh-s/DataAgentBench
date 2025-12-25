code = """import pandas as pd
import json
import io

# Load data
cases_data = locals()['var_function-call-10958570626037852530'] # List of dicts
history_file = locals()['var_function-call-670256500848698491'] # Path to JSON file

with open(history_file, 'r') as f:
    history_data = json.load(f)

# Create DataFrames
df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

# Helper to clean IDs
def clean_id(x):
    if pd.isna(x) or x == 'None':
        return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Clean columns
df_cases['id'] = df_cases['id'].apply(clean_id)
df_cases['ownerid'] = df_cases['ownerid'].apply(clean_id)
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

df_history['caseid__c'] = df_history['caseid__c'].apply(clean_id)
df_history['oldvalue__c'] = df_history['oldvalue__c'].apply(clean_id)
df_history['newvalue__c'] = df_history['newvalue__c'].apply(clean_id)

# Calculate Handle Time (Duration) for each case
df_cases['handle_time'] = (df_cases['closeddate'] - df_cases['createddate']).dt.total_seconds()

# Identify Processors per Case
# Map case_id -> set of agents
case_processors = {}

# Initialize with the final owner from Case table
for _, row in df_cases.iterrows():
    cid = row['id']
    oid = row['ownerid']
    if cid not in case_processors:
        case_processors[cid] = set()
    if oid:
        case_processors[cid].add(oid)

# Add processors from history
# Filter history to only relevant cases
relevant_case_ids = set(df_cases['id'].unique())
df_history_rel = df_history[df_history['caseid__c'].isin(relevant_case_ids)]

for _, row in df_history_rel.iterrows():
    cid = row['caseid__c']
    old_v = row['oldvalue__c']
    new_v = row['newvalue__c']
    
    if cid in case_processors:
        if old_v:
            case_processors[cid].add(old_v)
        if new_v:
            case_processors[cid].add(new_v)

# Count cases processed per agent (among the relevant cases)
agent_case_counts = {}
for cid, agents in case_processors.items():
    for agent in agents:
        agent_case_counts[agent] = agent_case_counts.get(agent, 0) + 1

# Calculate Average Handle Time per Agent
# Only credit the final owner (Case.ownerid) with the time
agent_handle_times = {} # list of times

for _, row in df_cases.iterrows():
    agent = row['ownerid']
    time = row['handle_time']
    if agent:
        if agent not in agent_handle_times:
            agent_handle_times[agent] = []
        agent_handle_times[agent].append(time)

# Compute averages and filter
results = []
for agent, times in agent_handle_times.items():
    # Check processing count
    count = agent_case_counts.get(agent, 0)
    if count > 1:
        avg_time = sum(times) / len(times)
        results.append({
            'agent_id': agent,
            'avg_time': avg_time,
            'processed_count': count,
            'closed_count': len(times)
        })

# Sort by avg_time
results_df = pd.DataFrame(results).sort_values(by='avg_time')

print("__RESULT__:")
print(results_df.to_json(orient='records'))"""

env_args = {'var_function-call-9776892701324455047': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-10958570626037852530': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10769889240167148629': [{'count': '153'}], 'var_function-call-1350100862477643396': [{'min': '2020-07-05T09:51:05.000+0000', 'max': '2023-12-02T16:45:51.000+0000'}], 'var_function-call-10171662404576225263': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-670256500848698491': 'file_storage/function-call-670256500848698491.json'}

exec(code, env_args)
