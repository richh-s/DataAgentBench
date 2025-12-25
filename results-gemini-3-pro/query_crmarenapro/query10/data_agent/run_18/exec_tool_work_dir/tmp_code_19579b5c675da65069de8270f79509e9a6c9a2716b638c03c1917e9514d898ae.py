code = """import pandas as pd
import json
from datetime import datetime

# Load data
cases_data = locals()['var_function-call-14753310501971979415']
history_file = locals()['var_function-call-5340587037609171017']

with open(history_file, 'r') as f:
    history_data = json.load(f)

# Convert to DataFrames
cases_df = pd.DataFrame(cases_data)
history_df = pd.DataFrame(history_data)

# Helper to clean IDs
def clean_id(x):
    if pd.isna(x) or x == 'None':
        return None
    x = str(x).strip()
    if x.startswith('#'):
        x = x[1:]
    return x

# Clean Cases
if not cases_df.empty:
    cases_df['id'] = cases_df['id'].apply(clean_id)
    cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
    # Parse dates
    # Format looks like "2023-07-01T10:30:00.000+0000"
    # Using 'mixed' or specific format
    cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
    cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])

# Clean History
if not history_df.empty:
    history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
    history_df['oldvalue__c'] = history_df['oldvalue__c'].apply(clean_id)
    history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

# Filter Cases for Timeframe (Double check)
# Past 4 months: 2023-05-02 to 2023-09-02
start_date = pd.Timestamp('2023-05-02', tz='UTC')
end_date = pd.Timestamp('2023-09-02', tz='UTC')

# Ensure cases_df dates are UTC
if not cases_df.empty:
    if cases_df['closeddate'].dt.tz is None:
        cases_df['closeddate'] = cases_df['closeddate'].dt.tz_localize('UTC')
    else:
        cases_df['closeddate'] = cases_df['closeddate'].dt.tz_convert('UTC')

    if cases_df['createddate'].dt.tz is None:
        cases_df['createddate'] = cases_df['createddate'].dt.tz_localize('UTC')
    else:
        cases_df['createddate'] = cases_df['createddate'].dt.tz_convert('UTC')

    # Filter
    closed_cases = cases_df[
        (cases_df['closeddate'] >= start_date) & 
        (cases_df['closeddate'] <= end_date)
    ].copy()
else:
    closed_cases = pd.DataFrame()

# Dictionary to track cases processed by each agent
# agent_id -> set(case_id)
agent_processed_cases = {}

# Dictionary to track handle times for each agent
# agent_id -> list(seconds)
agent_handle_times = {}

# Prepare History Lookup
# CaseId -> set of owners (from history)
history_owners = {}
if not history_df.empty:
    for _, row in history_df.iterrows():
        cid = row['caseid__c']
        old = row['oldvalue__c']
        new = row['newvalue__c']
        
        if cid not in history_owners:
            history_owners[cid] = set()
        
        if old: history_owners[cid].add(old)
        if new: history_owners[cid].add(new)

# Process Closed Cases
for _, row in closed_cases.iterrows():
    cid = row['id']
    final_owner = row['ownerid']
    created = row['createddate']
    closed = row['closeddate']
    
    # Calculate duration
    duration = (closed - created).total_seconds()
    
    # Determine all processors
    processors = set()
    if final_owner:
        processors.add(final_owner)
    
    if cid in history_owners:
        processors.update(history_owners[cid])
    
    # Update Processed Counts
    for agent in processors:
        if agent not in agent_processed_cases:
            agent_processed_cases[agent] = set()
        agent_processed_cases[agent].add(cid)
    
    # Update Handle Time (Only for final owner)
    if final_owner:
        if final_owner not in agent_handle_times:
            agent_handle_times[final_owner] = []
        agent_handle_times[final_owner].append(duration)

# Calculate Stats
results = []
for agent, cases_set in agent_processed_cases.items():
    if len(cases_set) > 1:
        # Eligible agent
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_time = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            results.append({
                'AgentId': agent,
                'ProcessedCount': len(cases_set),
                'AvgHandleTime': avg_time
            })

# Find Lowest
if results:
    results_df = pd.DataFrame(results)
    best_agent = results_df.loc[results_df['AvgHandleTime'].idxmin()]
    final_answer = best_agent['AgentId']
    # Debug info
    debug_info = results_df.sort_values('AvgHandleTime').to_dict(orient='records')
else:
    final_answer = "No eligible agents found"
    debug_info = []

print("__RESULT__:")
print(json.dumps({
    "final_answer": final_answer,
    "debug_info": debug_info
}))"""

env_args = {'var_function-call-5914537462471561066': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-14753310501971979415': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10623675109369733718': [], 'var_function-call-6935807388844192585': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-5340587037609171017': 'file_storage/function-call-5340587037609171017.json'}

exec(code, env_args)
