code = """import json
import pandas as pd
import numpy as np

# Load all cases
cases_list = locals()['var_function-call-5088613732026850278']
# Load history
history_file = locals()['var_function-call-11956446384836222109']
with open(history_file, 'r') as f:
    history_list = json.load(f)

def clean_id(val):
    if isinstance(val, str):
        val = val.strip()
        if val.startswith('#'):
            return val[1:]
    return val

cases_df = pd.DataFrame(cases_list)
cases_df['id'] = cases_df['id'].apply(clean_id)
cases_df['ownerid'] = cases_df['ownerid'].apply(clean_id)
cases_df['createddate'] = pd.to_datetime(cases_df['createddate'], utc=True)
# Handle 'None' or NaT in closeddate
cases_df['closeddate'] = pd.to_datetime(cases_df['closeddate'], errors='coerce', utc=True)

# Window
window_start = pd.Timestamp("2023-05-02", tz='UTC')
window_end = pd.Timestamp("2023-09-02", tz='UTC')

# Define Managed Cases
# Created before or on End Date
# Closed on or after Start Date OR Open
managed_mask = (cases_df['createddate'] <= window_end) & \
               ((cases_df['closeddate'] >= window_start) | (cases_df['closeddate'].isna()))

managed_cases = cases_df[managed_mask].copy()

# Prepare History
history_df = pd.DataFrame(history_list)
history_df['caseid__c'] = history_df['caseid__c'].apply(clean_id)
history_df['oldvalue__c'] = history_df['oldvalue__c'].apply(clean_id)
history_df['newvalue__c'] = history_df['newvalue__c'].apply(clean_id)

relevant_ids = set(managed_cases['id'].unique())
history_relevant = history_df[history_df['caseid__c'].isin(relevant_ids)]

# Calculate Managed Counts
agent_managed_counts = {}

for _, case in managed_cases.iterrows():
    cid = case['id']
    # Agents involved
    c_hist = history_relevant[history_relevant['caseid__c'] == cid]
    
    involved = set()
    # Check history owners
    for _, row in c_hist.iterrows():
        if row['oldvalue__c'] and row['oldvalue__c'] != 'None':
            involved.add(row['oldvalue__c'])
        if row['newvalue__c'] and row['newvalue__c'] != 'None':
            involved.add(row['newvalue__c'])
            
    # If no history, or only initial, fallback to ownerid?
    # History usually covers everything. If only 1 record (Initial), ownerid matches newvalue.
    # But for safety, add current owner if open or closed.
    if case['ownerid']:
        involved.add(case['ownerid'])
        
    for agent in involved:
        agent_managed_counts[agent] = agent_managed_counts.get(agent, 0) + 1

# Calculate Handle Times for Closed Cases in Window
# Filter managed cases that are CLOSED in window
closed_mask = (managed_cases['closeddate'] >= window_start) & (managed_cases['closeddate'] <= window_end)
closed_cases_in_window = managed_cases[closed_mask]

agent_handle_times = {}

for _, case in closed_cases_in_window.iterrows():
    cid = case['id']
    c_hist = history_relevant[history_relevant['caseid__c'] == cid]
    
    # Check assignment count.
    # Note: history_relevant is filtered by managed_cases IDs.
    # Just count rows for this case.
    # Assuming 'Owner Assignment' rows are the only ones in history_relevant (from SQL)
    # Wait, SQL query was: WHERE field__c = 'Owner Assignment'
    # Yes.
    
    count = len(c_hist)
    
    # Transferred if count > 1
    # Valid if count == 1 (Initial Assignment only)
    # Or count == 0 (Should not happen but if so, not transferred)
    
    if count <= 1:
        # Valid
        duration = (case['closeddate'] - case['createddate']).total_seconds()
        owner = case['ownerid'] # Final owner
        
        if owner not in agent_handle_times:
            agent_handle_times[owner] = []
        agent_handle_times[owner].append(duration)

# Final selection
eligible_agents = []
for agent, count in agent_managed_counts.items():
    if count > 1:
        # Check if they have handle time stats
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_time = np.mean(agent_handle_times[agent])
            eligible_agents.append({
                "id": agent,
                "avg_time": avg_time,
                "count_managed": count,
                "count_valid_ht": len(agent_handle_times[agent])
            })

eligible_agents.sort(key=lambda x: x['avg_time'])

print("__RESULT__:")
print(json.dumps(eligible_agents))"""

env_args = {'var_function-call-17593237228977388210': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-12169961977782919954': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-10103375238797437899': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11956446384836222109': 'file_storage/function-call-11956446384836222109.json', 'var_function-call-11766718509489547150': [], 'var_function-call-12369524369243272128': {'num_cases': 7, 'case_ids': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'history_counts': {'500Wt00000DDepmIAD': 1, '500Wt00000DDyzpIAD': 1, '500Wt00000DDzUPIA1': 1, '500Wt00000DDzsbIAD': 1, '500Wt00000DDzscIAD': 1, '500Wt00000DDzuEIAT': 1, '500Wt00000DE02HIAT': 1}, 'history_sample': [{'caseid__c': '500Wt00000DDzscIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}]}, 'var_function-call-16260162828416650792': [{'count': '75', 'min': '2020-07-05T09:51:05.000+0000', 'max': '2023-12-02T16:45:51.000+0000'}], 'var_function-call-5088613732026850278': 'file_storage/function-call-5088613732026850278.json'}

exec(code, env_args)
