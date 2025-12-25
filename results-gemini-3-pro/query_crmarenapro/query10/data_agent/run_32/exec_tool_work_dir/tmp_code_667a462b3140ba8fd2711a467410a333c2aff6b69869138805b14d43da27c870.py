code = """import json
import pandas as pd
from datetime import datetime

# Load cases
cases_data = locals()['var_function-call-3515426018230989725']
# cases_data is a list of dicts.

# Load history
history_path = locals()['var_function-call-724238365973199859']
with open(history_path, 'r') as f:
    history_data = json.load(f)

# Convert to DataFrames for easier handling
df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

# Filter history for relevant cases only
relevant_case_ids = set(df_cases['id'].unique())
df_history = df_history[df_history['caseid__c'].isin(relevant_case_ids)].copy()

# Parse dates
def parse_date(date_str):
    # Format: 2023-07-01T10:30:00.000+0000
    # Python 3.11+ supports %z with colon, but 3.12 definitely does.
    # If not, might need to remove the colon or use dateutil.
    # Let's try direct parsing.
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        # Try without microseconds
        try:
             return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
        except:
             return None

df_cases['created_dt'] = df_cases['createddate'].apply(parse_date)
df_cases['closed_dt'] = df_cases['closeddate'].apply(parse_date)

# Calculate duration in seconds
df_cases['duration'] = (df_cases['closed_dt'] - df_cases['created_dt']).dt.total_seconds()

# Identify Managed Cases per Agent
# Managed = Was an owner at some point
agent_managed = {} # AgentID -> Set(CaseID)

# Initialize with current owners
for _, row in df_cases.iterrows():
    c_id = row['id']
    owner = row['ownerid']
    if owner not in agent_managed:
        agent_managed[owner] = set()
    agent_managed[owner].add(c_id)

# Add from history
# field__c is 'Owner Assignment'. newvalue__c is the new owner. oldvalue__c is the old owner.
for _, row in df_history.iterrows():
    c_id = row['caseid__c']
    new_owner = row['newvalue__c']
    old_owner = row['oldvalue__c']
    
    if new_owner and new_owner != 'None':
        if new_owner not in agent_managed:
            agent_managed[new_owner] = set()
        agent_managed[new_owner].add(c_id)
        
    if old_owner and old_owner != 'None':
        if old_owner not in agent_managed:
            agent_managed[old_owner] = set()
        agent_managed[old_owner].add(c_id)

# Filter agents with > 1 managed case
multi_case_agents = {k for k, v in agent_managed.items() if len(v) > 1}

# Calculate Handle Time for Agents
# Only credit if they are the FINAL owner (OwnerId in Case table)
# And assuming they didn't transfer it (which is true if they are the final owner of a closed case)
agent_handle_times = {} # AgentID -> List of durations

for _, row in df_cases.iterrows():
    owner = row['ownerid']
    duration = row['duration']
    
    if owner not in agent_handle_times:
        agent_handle_times[owner] = []
    agent_handle_times[owner].append(duration)

# Compute Average Handle Time for eligible agents
results = []
for agent in multi_case_agents:
    if agent in agent_handle_times:
        durations = agent_handle_times[agent]
        if durations:
            avg_time = sum(durations) / len(durations)
            results.append({'agent_id': agent, 'avg_time': avg_time, 'managed_count': len(agent_managed[agent])})

# Sort by avg_time ascending
results.sort(key=lambda x: x['avg_time'])

# Output
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-13710148199737365862': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-3515426018230989725': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-12924332762788559106': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-554246957191354409': [{'count': '7'}], 'var_function-call-724238365973199859': 'file_storage/function-call-724238365973199859.json'}

exec(code, env_args)
