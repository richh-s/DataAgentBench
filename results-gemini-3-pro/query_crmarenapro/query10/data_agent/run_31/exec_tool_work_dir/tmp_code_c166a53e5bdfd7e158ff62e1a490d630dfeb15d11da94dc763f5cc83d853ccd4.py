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

# Define date range
end_date = pd.Timestamp('2023-09-02 23:59:59', tz='UTC')
start_date = pd.Timestamp('2023-05-02 00:00:00', tz='UTC')

# Filter cases by closed date
eligible_cases = df_cases[
    (df_cases['closeddate'].notna()) & 
    (df_cases['closeddate'] >= start_date) & 
    (df_cases['closeddate'] <= end_date)
].copy()

print(f"DEBUG: Eligible cases count: {len(eligible_cases)}")

# Process History
owner_history = df_history[df_history['caseid__c'].isin(eligible_cases['id'])].copy()
print(f"DEBUG: History rows for eligible cases: {len(owner_history)}")

case_owners = owner_history.groupby('caseid__c')['newvalue__c'].apply(list).to_dict()
print(f"DEBUG: Cases with history: {len(case_owners)}")

agent_case_counts = {}
agent_handle_times = {}

for _, row in eligible_cases.iterrows():
    case_id = row['id']
    owners = case_owners.get(case_id, [])
    
    if len(owners) == 0:
        continue # These get ignored
        
    unique_owners = set(owners)
    for agent in unique_owners:
        agent_case_counts[agent] = agent_case_counts.get(agent, 0) + 1
        
    if len(owners) == 1:
        agent = owners[0]
        ht = row['handle_time']
        if agent not in agent_handle_times:
            agent_handle_times[agent] = []
        agent_handle_times[agent].append(ht)

print(f"DEBUG: Agent case counts: {json.dumps(agent_case_counts)}")
print(f"DEBUG: Agent handle times keys: {list(agent_handle_times.keys())}")

results = []
for agent, count in agent_case_counts.items():
    if count > 1:
        if agent in agent_handle_times and len(agent_handle_times[agent]) > 0:
            avg_ht = sum(agent_handle_times[agent]) / len(agent_handle_times[agent])
            results.append({'agent': agent, 'avg_ht': avg_ht})

print(f"DEBUG: Results: {results}")

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-24126343359264322': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15645432498232903285': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-12166463853152357831': [{'count': '393'}], 'var_function-call-15618322671991513207': [{'count': '153'}], 'var_function-call-3444313059583856716': 'file_storage/function-call-3444313059583856716.json', 'var_function-call-18360485685688367650': 'file_storage/function-call-18360485685688367650.json', 'var_function-call-11583872083387282585': 'None'}

exec(code, env_args)
