code = """import json
import pandas as pd
from dateutil import parser
import pytz

# Load files
active_cases_file = locals()['var_function-call-3536505408032586910']
history_file = locals()['var_function-call-17573147314422126302']

with open(active_cases_file, 'r') as f:
    active_cases = json.load(f)
cases_df = pd.DataFrame(active_cases)

with open(history_file, 'r') as f:
    history_list = json.load(f)
history_df = pd.DataFrame(history_list)

# Clean IDs
def clean_id(x):
    if not isinstance(x, str):
        return str(x) if x is not None else None
    return x.strip().lstrip('#')

cases_df['clean_id'] = cases_df['id'].apply(clean_id)
cases_df['clean_owner'] = cases_df['ownerid'].apply(clean_id)
# Handle None status
cases_df['status'] = cases_df['status'].fillna('')

history_df['clean_caseid'] = history_df['caseid__c'].apply(clean_id)
history_df['clean_new'] = history_df['newvalue__c'].apply(lambda x: clean_id(x) if x != 'None' else None)
history_df['clean_old'] = history_df['oldvalue__c'].apply(lambda x: clean_id(x) if x != 'None' else None)

# Filter history
relevant_ids = set(cases_df['clean_id'])
history_df = history_df[history_df['clean_caseid'].isin(relevant_ids)]
owner_history = history_df[history_df['field__c'] == 'Owner Assignment'].copy()

# Parse Dates
def parse_dt(x):
    if pd.isna(x) or x == 'None':
        return None
    return parser.parse(x)

cases_df['created_dt'] = cases_df['createddate'].apply(parse_dt)
cases_df['closed_dt'] = cases_df['closeddate'].apply(parse_dt)
owner_history['created_dt'] = owner_history['createddate'].apply(parse_dt)

# Define Window
window_start = parser.parse("2023-05-02T00:00:00+0000")
window_end = parser.parse("2023-09-02T23:59:59+0000")

agent_case_counts = {} # Agent -> Set of Case IDs managed in window
agent_handle_times = {} # Agent -> List of handle times

# Process each case
for _, case in cases_df.iterrows():
    cid = case['clean_id']
    created = case['created_dt']
    closed = case['closed_dt']
    final_owner = case['clean_owner']
    
    # Case End Date for "Active" check: ClosedDate or Now (if Open)
    # Using Window End as proxy for Now if active
    if closed:
        case_end = closed
    else:
        case_end = parser.parse("2099-01-01T00:00:00+0000") # Future

    # Get history for this case
    case_hist = owner_history[owner_history['clean_caseid'] == cid].sort_values('created_dt')
    
    # Build intervals
    intervals = [] # (Agent, Start, End)
    
    current_start = created
    current_agent = None 
    
    # If history exists, infer initial
    if not case_hist.empty:
        first_hist = case_hist.iloc[0]
        if first_hist['clean_old']:
            current_agent = first_hist['clean_old']
        elif first_hist['clean_new']:
             # This is a "Creation" assignment or first assignment
             # Actually if old is None, new is the FIRST owner from that point?
             # If created at T0, and Assignment at T1 (old=None, new=A), who owned T0-T1?
             # Probably A? Or "System"?
             # Let's assume the assignment at T1 (createddate ~ case createddate) sets the first owner.
             pass
    else:
        # No history, single owner
        current_agent = final_owner
        intervals.append((current_agent, created, case_end))
    
    # Iterate history
    for _, h in case_hist.iterrows():
        h_date = h['created_dt']
        h_new = h['clean_new']
        h_old = h['clean_old']
        
        # Close previous interval
        if current_agent:
            intervals.append((current_agent, current_start, h_date))
        
        # Start new
        current_agent = h_new
        current_start = h_date
        
        # If there was a gap/initial logic missing:
        # If first interval and current_agent was None?
        # If row 1 is (old=None, new=A), intervals so far empty.
        # It means A starts at h_date.
        # But who owned before?
        # If h_date is close to CreatedDate, maybe no one or "System".
        # We ignore "System" or "None".
    
    # Final interval
    if current_agent: # This should match final_owner usually
        intervals.append((current_agent, current_start, case_end))
    elif not case_hist.empty:
        # Fallback for final owner
        intervals.append((final_owner, current_start, case_end))

    # Check overlaps with window
    managed_agents = set()
    for agent, start, end in intervals:
        if agent is None: continue
        # Overlap: start < window_end AND end > window_start
        if start < window_end and end > window_start:
            managed_agents.add(agent)
    
    # Update counts
    for agent in managed_agents:
        if agent not in agent_case_counts:
            agent_case_counts[agent] = set()
        agent_case_counts[agent].add(cid)
        
    # Handle Time (only if closed in window)
    if closed and closed >= window_start and closed <= window_end:
        # "For cases that have NOT been transferred to an other agent... ONE Owner Assignment"
        # "We do not compute handle time for cases that have been transferred to other agents."
        # This means: If I am the final owner, AND the case was transferred TO me (or I am the only owner), I get the time.
        # The constraint "not compute... transferred to other agents" applies to the *previous* owner.
        # So the Final Owner gets the credit.
        duration = (closed - created).total_seconds()
        if final_owner not in agent_handle_times:
            agent_handle_times[final_owner] = []
        agent_handle_times[final_owner].append(duration)

# Compute results
results = []
for agent, cases in agent_case_counts.items():
    count = len(cases)
    if count > 1:
        if agent in agent_handle_times:
            times = agent_handle_times[agent]
            avg_time = sum(times) / len(times)
            results.append({'agent': agent, 'avg_time': avg_time, 'count': count})

if results:
    min_agent = min(results, key=lambda x: x['avg_time'])
    print("__RESULT__:")
    print(json.dumps(min_agent['agent']))
else:
    print("__RESULT__:")
    print(json.dumps("No eligible agents"))"""

env_args = {'var_function-call-5368791863856089937': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}], 'var_function-call-11270569426259875892': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-9673334345705858900': [{'count': '165'}], 'var_function-call-16300619007678097437': [{'count': '7'}], 'var_function-call-805110141175851061': [{'count': '153'}], 'var_function-call-6685924510354294491': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-17573147314422126302': 'file_storage/function-call-17573147314422126302.json', 'var_function-call-3785935391697955114': 'No eligible agents', 'var_function-call-3536505408032586910': 'file_storage/function-call-3536505408032586910.json'}

exec(code, env_args)
