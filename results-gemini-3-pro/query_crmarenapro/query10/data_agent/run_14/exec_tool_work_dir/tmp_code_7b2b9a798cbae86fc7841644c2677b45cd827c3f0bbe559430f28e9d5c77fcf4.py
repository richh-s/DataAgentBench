code = """import json
import pandas as pd
import dateutil.parser

# Load cases
cases_list = locals()['var_function-call-2025312579826353346']
df_cases = pd.DataFrame(cases_list)

# Clean IDs
df_cases['id'] = df_cases['id'].astype(str).str.strip().str.lstrip('#')
df_cases['ownerid'] = df_cases['ownerid'].astype(str).str.strip() # ownerid usually doesn't have # but good to trim

# Parse dates
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Define window
end_dt = pd.Timestamp('2023-09-02 23:59:59').tz_localize('UTC')
start_dt = pd.Timestamp('2023-05-02 00:00:00').tz_localize('UTC')

# Filter cases
df_cases = df_cases[(df_cases['closeddate'] >= start_dt) & (df_cases['closeddate'] <= end_dt)]

# Target Case IDs
target_ids = set(df_cases['id'].unique())

# Load history
history_file_path = locals()['var_function-call-5130305458207948578']
with open(history_file_path, 'r') as f:
    history_list = json.load(f)

df_history = pd.DataFrame(history_list)
if not df_history.empty:
    df_history['caseid__c'] = df_history['caseid__c'].astype(str).str.strip().str.lstrip('#')
    df_history = df_history[df_history['caseid__c'].isin(target_ids)]
else:
    df_history = pd.DataFrame(columns=['caseid__c', 'oldvalue__c', 'newvalue__c'])

# Build Managed Sets
agent_managed = {} # Agent -> Set(CaseID)

# Add from history
for _, row in df_history.iterrows():
    cid = row['caseid__c']
    old = row['oldvalue__c']
    new = row['newvalue__c']
    
    if old and str(old).lower() != 'none':
        agent_managed.setdefault(str(old).strip(), set()).add(cid)
    if new and str(new).lower() != 'none':
        agent_managed.setdefault(str(new).strip(), set()).add(cid)

# Add from current owner (Cases)
# If a case is in target_ids, its current owner definitely managed it.
for _, row in df_cases.iterrows():
    cid = row['id']
    owner = row['ownerid']
    if owner and str(owner).lower() != 'none':
        agent_managed.setdefault(str(owner).strip(), set()).add(cid)

# Filter Agents > 1 managed case
candidates = [agent for agent, cases in agent_managed.items() if len(cases) > 1]

# Calculate Avg Handle Time
# Only for cases CLOSED by the agent
agent_times = []

for agent in candidates:
    # Cases closed by agent
    # Check df_cases where ownerid == agent
    closed_cases = df_cases[df_cases['ownerid'] == agent]
    
    if closed_cases.empty:
        continue
        
    # Calculate duration
    # Timedelta in seconds
    durations = (closed_cases['closeddate'] - closed_cases['createddate']).dt.total_seconds()
    avg_duration = durations.mean()
    
    agent_times.append({
        'agent': agent,
        'avg_time': avg_duration,
        'num_closed': len(closed_cases),
        'num_managed': len(agent_managed[agent])
    })

# Sort by avg_time
agent_times.sort(key=lambda x: x['avg_time'])

# Result
print("__RESULT__:")
print(json.dumps(agent_times))"""

env_args = {'var_function-call-7739635252061129344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2025312579826353346': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-16971736032208043209': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-5130305458207948578': 'file_storage/function-call-5130305458207948578.json'}

exec(code, env_args)
