code = """import json
import pandas as pd
from datetime import datetime

# Load data
with open(locals()['var_function-call-3444313059583856716'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-18360485685688367650'], 'r') as f:
    history_data = json.load(f)

# Create DataFrames
df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

# Convert dates
# Case dates: 2023-09-30T11:30:00.000+0000
# Pandas to_datetime handles this format usually
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'])
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'])

# Define date range
end_date = pd.Timestamp('2023-09-02 23:59:59', tz='UTC')
start_date = pd.Timestamp('2023-05-02 00:00:00', tz='UTC')

# Filter cases by closed date
# Ensure closeddate is timezone aware or handle comparison
# The data seems to have +0000, so it is UTC.
eligible_cases = df_cases[
    (df_cases['closeddate'].notna()) & 
    (df_cases['closeddate'] >= start_date) & 
    (df_cases['closeddate'] <= end_date)
].copy()

# Calculate Handle Time (seconds)
eligible_cases['handle_time'] = (eligible_cases['closeddate'] - eligible_cases['createddate']).dt.total_seconds()

# Process History to get Owners per case
# Filter history for 'Owner Assignment'
owner_history = df_history[df_history['caseid__c'].isin(eligible_cases['id'])].copy()
# Note: The SQL query already filtered for 'Owner Assignment', but let's be safe if I used a broader query or variable reuse
# The SQL query was: SELECT ... WHERE field__c = 'Owner Assignment'
# So owner_history contains only assignments.

# Group by Case ID to get list of owners
# map case_id -> list of newvalue__c
# We preserve order if possible, though mostly we just need the set and the count.
case_owners = owner_history.groupby('caseid__c')['newvalue__c'].apply(list).to_dict()

# Aggregation variables
agent_case_counts = {} # Total cases processed (transferred or not)
agent_handle_times = {} # List of handle times for non-transferred cases

for _, row in eligible_cases.iterrows():
    case_id = row['id']
    
    # Get owners from history
    owners = case_owners.get(case_id, [])
    
    # "For cases that have NOT been transferred... only ONE 'Owner Assignment'"
    # If owners list is empty, it might be data issue or logic mismatch.
    # If empty, let's look at row['ownerid'].
    # The prompt implies history tracks it.
    # Let's count owners.
    
    # If no history, assume 1 owner (current ownerid)??
    # Or strict: count = 0.
    # Let's track how many have 0.
    if len(owners) == 0:
        # If I strictly follow the prompt "there will be only ONE", 0 means data issue or ignored.
        # However, checking the preview, some cases might not be in the history snippet if they are old or just missing.
        # But for "Lowest Average Handle Time" calculation, I need valid data.
        # Let's assume valid cases have history.
        continue
        
    # Increment processing counts
    # A case counts for ALL agents involved.
    unique_owners = set(owners)
    for agent in unique_owners:
        agent_case_counts[agent] = agent_case_counts.get(agent, 0) + 1
        
    # Handle Time eligibility
    # "do not compute handle time for cases that have been transferred"
    # Transferred means > 1 Owner Assignment.
    if len(owners) == 1:
        # Not transferred.
        agent = owners[0]
        ht = row['handle_time']
        if agent not in agent_handle_times:
            agent_handle_times[agent] = []
        agent_handle_times[agent].append(ht)

# Filter agents and find winner
results = []
for agent, count in agent_case_counts.items():
    if count > 1:
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_ht = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            results.append({'agent': agent, 'avg_ht': avg_ht, 'count': count})

# Find min
if results:
    best_agent = min(results, key=lambda x: x['avg_ht'])
    print(f"__RESULT__:\n{json.dumps(best_agent['agent'])}")
else:
    print("__RESULT__:\n\"No eligible agent found\"")"""

env_args = {'var_function-call-24126343359264322': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15645432498232903285': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-12166463853152357831': [{'count': '393'}], 'var_function-call-15618322671991513207': [{'count': '153'}], 'var_function-call-3444313059583856716': 'file_storage/function-call-3444313059583856716.json', 'var_function-call-18360485685688367650': 'file_storage/function-call-18360485685688367650.json'}

exec(code, env_args)
