code = """import json
import pandas as pd

# Load data
with open(locals()['var_function-call-3444313059583856716'], 'r') as f:
    cases_data = json.load(f)
with open(locals()['var_function-call-18360485685688367650'], 'r') as f:
    history_data = json.load(f)

# Create DataFrames
df_cases = pd.DataFrame(cases_data)
df_history = pd.DataFrame(history_data)

# Convert dates
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')
df_cases['closeddate'] = pd.to_datetime(df_cases['closeddate'], errors='coerce')

# Define date range for Handle Time
end_date = pd.Timestamp('2023-09-02 23:59:59', tz='UTC')
start_date = pd.Timestamp('2023-05-02 00:00:00', tz='UTC')

# --- Step 1: Calculate Lifetime Case Counts ---
# Use all cases
# Map case_id -> owners (lifetime)
# Need to process all cases to get owners
# History covers some cases.
# Group history by caseid
all_history_owners = df_history.groupby('caseid__c')['newvalue__c'].apply(list).to_dict()

agent_lifetime_counts = {}

# Iterate ALL cases to count participation
for _, row in df_cases.iterrows():
    case_id = row['id']
    owners = all_history_owners.get(case_id, [])
    
    if len(owners) == 0:
        # Fallback to current owner
        current_owner = row['ownerid']
        if pd.isna(current_owner) or str(current_owner) == 'None':
            continue
        owners = [current_owner]
    
    unique_owners = set(owners)
    for agent in unique_owners:
        agent_lifetime_counts[agent] = agent_lifetime_counts.get(agent, 0) + 1

# --- Step 2: Calculate Handle Times for 4-Month Window ---
# Filter cases
eligible_cases_4m = df_cases[
    (df_cases['closeddate'].notna()) & 
    (df_cases['closeddate'] >= start_date) & 
    (df_cases['closeddate'] <= end_date)
].copy()

eligible_cases_4m['handle_time'] = (eligible_cases_4m['closeddate'] - eligible_cases_4m['createddate']).dt.total_seconds()

agent_handle_times_4m = {}

for _, row in eligible_cases_4m.iterrows():
    case_id = row['id']
    owners = all_history_owners.get(case_id, [])
    
    if len(owners) == 0:
        current_owner = row['ownerid']
        if pd.isna(current_owner) or str(current_owner) == 'None':
            continue
        owners = [current_owner]
        
    # Check if transferred
    if len(owners) == 1:
        agent = owners[0]
        ht = row['handle_time']
        if agent not in agent_handle_times_4m:
            agent_handle_times_4m[agent] = []
        agent_handle_times_4m[agent].append(ht)

# --- Step 3: Filter and Average ---
results = []
for agent, count in agent_lifetime_counts.items():
    if count > 1:
        # Agent processed > 1 case in lifetime
        # Do they have handle time in the window?
        if agent in agent_handle_times_4m and len(agent_handle_times_4m[agent]) > 0:
            avg_ht = sum(agent_handle_times_4m[agent]) / len(agent_handle_times_4m[agent])
            results.append({'agent': agent, 'avg_ht': avg_ht})

# Find min
if results:
    best_agent_info = min(results, key=lambda x: x['avg_ht'])
    print("__RESULT__:")
    print(json.dumps(best_agent_info['agent']))
else:
    # Debug
    print("__RESULT__:")
    print(json.dumps({
        "msg": "No results with lifetime count > 1",
        "agent_lifetime_counts": agent_lifetime_counts,
        "agents_with_ht": list(agent_handle_times_4m.keys())
    }))"""

env_args = {'var_function-call-24126343359264322': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15645432498232903285': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-12166463853152357831': [{'count': '393'}], 'var_function-call-15618322671991513207': [{'count': '153'}], 'var_function-call-3444313059583856716': 'file_storage/function-call-3444313059583856716.json', 'var_function-call-18360485685688367650': 'file_storage/function-call-18360485685688367650.json', 'var_function-call-11583872083387282585': 'None', 'var_function-call-8470705502402153607': 'Done', 'var_function-call-2252905179264510670': {'eligible_cases_count': 7, 'cases_with_history': 5, 'agent_case_counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NJJaIAO': 1}, 'results_count': 0, 'results': []}, 'var_function-call-13082357159917459203': {'eligible_cases_count': 7, 'agent_case_counts': {'005Wt000003NJufIAG': 1, '005Wt000003NJGLIA4': 1, '005Wt000003NDqDIAW': 1, '005Wt000003NJD9IAO': 1, '005Wt000003NEtOIAW': 1, '005Wt000003NJJaIAO': 1, '005Wt000003NIddIAG': 1}, 'results': []}}

exec(code, env_args)
