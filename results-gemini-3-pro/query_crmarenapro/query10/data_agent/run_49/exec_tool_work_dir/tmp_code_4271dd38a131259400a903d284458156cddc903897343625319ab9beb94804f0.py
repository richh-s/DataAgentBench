code = """import json
import pandas as pd
from dateutil import parser

# Load cases
cases = locals()['var_function-call-12556149855108314420']
# Load history
history_path = locals()['var_function-call-4118261784160134371']

with open(history_path, 'r') as f:
    history = json.load(f)

# Convert to DataFrames
df_cases = pd.DataFrame(cases)
df_history = pd.DataFrame(history)

# Filter history for relevant cases
relevant_case_ids = set(df_cases['id'])
df_history_rel = df_history[df_history['caseid__c'].isin(relevant_case_ids)].copy()

# Initialize data structures
agent_case_counts = {} # Set of case IDs per agent
agent_handle_times = {} # List of durations per agent

# Process each case
for _, case in df_cases.iterrows():
    case_id = case['id']
    created = parser.parse(case['createddate'])
    closed = parser.parse(case['closeddate'])
    duration_seconds = (closed - created).total_seconds()
    
    current_owner = case['ownerid']
    
    # Get history for this case
    case_hist = df_history_rel[df_history_rel['caseid__c'] == case_id]
    
    # Determine all owners involved
    # Owners = current owner + any newvalue__c in history
    owners = set()
    owners.add(current_owner)
    if not case_hist.empty:
        owners.update(case_hist['newvalue__c'].dropna().unique())
        
    # Update managed counts
    for owner in owners:
        if owner not in agent_case_counts:
            agent_case_counts[owner] = set()
        agent_case_counts[owner].add(case_id)
        
    # Check if transferred
    # Rule: Not transferred -> Only ONE 'Owner Assignment' record (or 0 if not logged?)
    # "For cases that have NOT been transferred... there will be only ONE 'Owner Assignment'"
    # "For those that have been transferred, there will be MORE THAN ONE"
    # This implies we count the rows in history (which is filtered to 'Owner Assignment' by query).
    
    history_count = len(case_hist)
    
    is_transferred = history_count > 1
    
    if not is_transferred:
        # Handle time applies to the single owner
        # If history count is 1, the owner in that record is the one.
        # If history count is 0, the current owner is the one.
        # They should be the same.
        
        # Add to handle times
        # The owner to credit is the single owner.
        # If history_count == 1, use newvalue__c
        # If history_count == 0, use current_owner
        
        target_owner = current_owner
        if history_count == 1:
            target_owner = case_hist.iloc[0]['newvalue__c']
            
        if target_owner not in agent_handle_times:
            agent_handle_times[target_owner] = []
        agent_handle_times[target_owner].append(duration_seconds)

# Calculate results
results = []
for agent, cases_managed in agent_case_counts.items():
    managed_count = len(cases_managed)
    if managed_count > 1:
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_time = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            results.append({
                "agent_id": agent,
                "managed_count": managed_count,
                "avg_handle_time": avg_time
            })

# Sort by avg handle time
results_df = pd.DataFrame(results)
if not results_df.empty:
    results_df = results_df.sort_values(by='avg_handle_time')
    best_agent = results_df.iloc[0]['agent_id']
    print("__RESULT__:")
    print(json.dumps(best_agent))
else:
    print("__RESULT__:")
    print(json.dumps("No matching agent"))"""

env_args = {'var_function-call-9241346808285847141': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000531RMIAY', 'caseid__c': '500Wt00000DDZ0VIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2021-10-15T13:46:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UaIAI', 'caseid__c': '500Wt00000DDQoUIAX', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJcwIAG', 'createddate': '2021-09-15T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531UbIAI', 'caseid__c': '500Wt00000DDzm9IAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ3RIAW', 'createddate': '2022-03-03T10:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531hSIAQ', 'caseid__c': '500Wt00000DDPsPIAX', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-04-06T11:30:54.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531w0IAA', 'caseid__c': '500Wt00000DE00fIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-09-05T10:15:00.000+0000', 'field__c': 'Case Creation'}], 'var_function-call-12556149855108314420': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_function-call-4118261784160134371': 'file_storage/function-call-4118261784160134371.json'}

exec(code, env_args)
