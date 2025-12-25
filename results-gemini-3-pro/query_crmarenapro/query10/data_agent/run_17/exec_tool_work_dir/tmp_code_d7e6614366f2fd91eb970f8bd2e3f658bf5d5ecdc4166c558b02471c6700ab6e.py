code = """import json
import pandas as pd
from datetime import datetime

# Load cases
cases_list = locals()['var_function-call-12169961977782919954']
# cases_list is a list of dicts.

# Load history
history_file = locals()['var_function-call-11956446384836222109']
with open(history_file, 'r') as f:
    history_list = json.load(f)

# Helper to clean IDs
def clean_id(val):
    if isinstance(val, str):
        val = val.strip()
        if val.startswith('#'):
            return val[1:]
    return val

# Process Cases
cases_df = pd.DataFrame(cases_list)
cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'])
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'])

# Filter cases by date (Redundant if SQL did it, but good for safety)
# Past 4 months from 2023-09-02: May 02 to Sep 02.
start_date = pd.Timestamp("2023-05-02", tz='UTC')
end_date = pd.Timestamp("2023-09-02", tz='UTC')
# Ensure timezone awareness matches
# The data has +0000, so it is tz-aware UTC.

cases_df = cases_df[
    (cases_df['closeddate'] >= start_date) & 
    (cases_df['closeddate'] <= end_date)
]

# Process History
history_df = pd.DataFrame(history_list)
history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
history_df['oldvalue__c'] = history_df['oldvalue__c'].apply(clean_id)
history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

# Filter history to only relevant cases
relevant_case_ids = set(cases_df['id'].unique())
history_relevant = history_df[history_df['caseid__c'].isin(relevant_case_ids)].copy()

# Analyze per case
# Map CaseId -> Set of Agents
# Map CaseId -> Is Transferred?
# Map CaseId -> Handle Time (if valid) -> Owner

agent_case_counts = {} # AgentId -> Set of CaseIds they managed
agent_handle_times = {} # AgentId -> List of durations (seconds)

for _, case in cases_df.iterrows():
    cid = case['id']
    
    # Get history for this case
    c_hist = history_relevant[history_relevant['caseid__c'] == cid]
    
    # Count owner assignments
    # Assuming 'Owner Assignment' is the only field filtered in SQL
    assignments = c_hist
    assignment_count = len(assignments)
    
    # Identify all agents involved
    agents_involved = set()
    for _, row in assignments.iterrows():
        if row['oldvalue__c'] and row['oldvalue__c'] != 'None':
            agents_involved.add(row['oldvalue__c'])
        if row['newvalue__c'] and row['newvalue__c'] != 'None':
            agents_involved.add(row['newvalue__c'])
            
    # If no history found, check Case OwnerId (should have history though)
    # If assignment_count == 0, fallback to current owner
    if assignment_count == 0:
        agents_involved.add(case['ownerid'])
    
    # Update managed counts
    for agent in agents_involved:
        if agent not in agent_case_counts:
            agent_case_counts[agent] = set()
        agent_case_counts[agent].add(cid)
        
    # Determine Handle Time Eligibility
    # "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    # So valid if assignment_count == 1
    # Note: What if count == 0? If 0, it wasn't transferred (or history missing).
    # If 0, we treat as single owner (current owner).
    
    is_transferred = (assignment_count > 1)
    
    if not is_transferred:
        # Calculate duration
        duration = (case['closeddate'] - case['createddate']).total_seconds()
        
        # Who gets the credit? The final owner.
        owner = case['ownerid']
        
        if owner not in agent_handle_times:
            agent_handle_times[owner] = []
        agent_handle_times[owner].append(duration)

# Calculate results
results = []
for agent, cases in agent_case_counts.items():
    if len(cases) > 1: # Processing more than one case
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_time = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            results.append({
                "agent_id": agent,
                "avg_time": avg_time,
                "case_count": len(cases),
                "valid_samples": len(agent_handle_times[agent])
            })

# Sort by avg_time ascending
results.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17593237228977388210': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12169961977782919954': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-10103375238797437899': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11956446384836222109': 'file_storage/function-call-11956446384836222109.json'}

exec(code, env_args)
