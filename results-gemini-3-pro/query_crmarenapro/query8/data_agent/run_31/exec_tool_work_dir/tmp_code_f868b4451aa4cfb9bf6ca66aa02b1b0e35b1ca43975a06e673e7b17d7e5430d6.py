code = """import json
import pandas as pd

# Load User IDs
users_list = locals()['var_function-call-11198565857358294365']
# Clean User IDs
user_ids = set()
for u in users_list:
    uid = u['Id']
    if uid.startswith('#'):
        uid = uid[1:]
    user_ids.add(uid)

# Load Case History
# The result is in a file because it was large, or in the variable if it fits. 
# The previous message showed a list directly in the result field, but also mentioned "The result is stored under key...".
# The system prompt says: "If a tool result is large, the next message will include a preview ... and the storage entry will be the .json file path".
# However, the previous output looked like a JSON list. Let's check the type.
history_data = locals()['var_function-call-16087441587863589561']
if isinstance(history_data, str) and history_data.endswith('.json'):
    with open(history_data, 'r') as f:
        history = json.load(f)
else:
    history = history_data

# Process History
transfers = []
handled_agents = set()

# Date limit
end_date = "2023-04-10T23:59:59"

for entry in history:
    cdate = entry['createddate']
    if cdate > end_date:
        continue
        
    old_val = entry['oldvalue__c']
    new_val = entry['newvalue__c']
    
    # Clean IDs
    if old_val and old_val.startswith('#'):
        old_val = old_val[1:]
    if new_val and new_val.startswith('#'):
        new_val = new_val[1:]
        
    # Check if valid agents
    # Handled set: agents who received a case (initially or via transfer)
    if new_val in user_ids:
        handled_agents.add(new_val)
        
    # Transfer logic: Agent A -> Agent B
    # Count for A
    if old_val in user_ids and new_val in user_ids:
        transfers.append(old_val)

# Calculate counts
# Initialize 0 for all handled agents
agent_counts = {agent: 0 for agent in handled_agents}

for agent in transfers:
    if agent in agent_counts:
        agent_counts[agent] += 1

# Find min
if not agent_counts:
    result = "No agents found"
else:
    min_count = min(agent_counts.values())
    min_agents = [k for k, v in agent_counts.items() if v == min_count]
    result = {"min_count": min_count, "agents": min_agents}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12934210150349246611': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8984254948452609998': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-11198565857358294365': [{'Id': '#005Wt000003MH26IAG'}, {'Id': '#005Wt000003MH27IAG'}, {'Id': '#005Wt000003MH29IAG'}, {'Id': '#005Wt000003MH2GIAW'}, {'Id': '#005Wt000003MH2JIAW'}, {'Id': '005Wt000003MH2OIAW'}, {'Id': '005Wt000003MH2WIAW'}, {'Id': '005Wt000003MNyjIAG'}, {'Id': '005Wt000003MOgHIAW'}, {'Id': '005Wt000003MOgIIAW'}, {'Id': '#005Wt000003MOgJIAW'}, {'Id': '005Wt000003NBcAIAW'}, {'Id': '005Wt000003NBcBIAW'}, {'Id': '005Wt000003NBp4IAG'}, {'Id': '005Wt000003NBp5IAG'}, {'Id': '005Wt000003NBsIIAW'}, {'Id': '005Wt000003NBykIAG'}, {'Id': '005Wt000003NBylIAG'}, {'Id': '005Wt000003NCRmIAO'}, {'Id': '#005Wt000003NCZqIAO'}, {'Id': '005Wt000003NCd5IAG'}, {'Id': '#005Wt000003NCegIAG'}, {'Id': '005Wt000003ND9KIAW'}, {'Id': '005Wt000003NDEBIA4'}, {'Id': '005Wt000003NDJ0IAO'}, {'Id': '005Wt000003NDJ1IAO'}, {'Id': '005Wt000003NDXZIA4'}, {'Id': '#005Wt000003NDXaIAO'}, {'Id': '005Wt000003NDqDIAW'}, {'Id': '005Wt000003NDqEIAW'}, {'Id': '#005Wt000003NDqFIAW'}, {'Id': '005Wt000003NDsUIAW'}, {'Id': '#005Wt000003NDu7IAG'}, {'Id': '005Wt000003NDu8IAG'}, {'Id': '#005Wt000003NEGhIAO'}, {'Id': '005Wt000003NEGiIAO'}, {'Id': '005Wt000003NEGjIAO'}, {'Id': '005Wt000003NETaIAO'}, {'Id': '#005Wt000003NETbIAO'}, {'Id': '#005Wt000003NEa3IAG'}, {'Id': '005Wt000003NEdJIAW'}, {'Id': '005Wt000003NEdKIAW'}, {'Id': '#005Wt000003NEoYIAW'}, {'Id': '#005Wt000003NErnIAG'}, {'Id': '005Wt000003NEtOIAW'}, {'Id': '005Wt000003NEtPIAW'}, {'Id': '005Wt000003NEzqIAG'}, {'Id': '005Wt000003NEzrIAG'}, {'Id': '#005Wt000003NF1SIAW'}, {'Id': '005Wt000003NF9WIAW'}, {'Id': '005Wt000003NF9XIAW'}, {'Id': '005Wt000003NF9YIAW'}, {'Id': '#005Wt000003NFB8IAO'}, {'Id': '005Wt000003NFKoIAO'}, {'Id': '#005Wt000003NFKpIAO'}, {'Id': '005Wt000003NFRKIA4'}, {'Id': '005Wt000003NFW6IAO'}, {'Id': '005Wt000003NFhOIAW'}, {'Id': '005Wt000003NFhPIAW'}, {'Id': '005Wt000003NFr4IAG'}, {'Id': '#005Wt000003NG2MIAW'}, {'Id': '005Wt000003NG2NIAW'}, {'Id': '#005Wt000003NGFGIA4'}, {'Id': '#005Wt000003NGFHIA4'}, {'Id': '#005Wt000003NGOxIAO'}, {'Id': '005Wt000003NGdSIAW'}, {'Id': '005Wt000003NGjuIAG'}, {'Id': '005Wt000003NGjvIAG'}, {'Id': '005Wt000003NGjwIAG'}, {'Id': '005Wt000003NGtbIAG'}, {'Id': '#005Wt000003NGtcIAG'}, {'Id': '005Wt000003NGwoIAG'}, {'Id': '005Wt000003NGwpIAG'}, {'Id': '005Wt000003NH3GIAW'}, {'Id': '005Wt000003NH86IAG'}, {'Id': '#005Wt000003NHGAIA4'}, {'Id': '#005Wt000003NHfFIAW'}, {'Id': '#005Wt000003NHfyIAG'}, {'Id': '005Wt000003NHfzIAG'}, {'Id': '#005Wt000003NHg0IAG'}, {'Id': '#005Wt000003NHpdIAG'}, {'Id': '#005Wt000003NHpeIAG'}, {'Id': '005Wt000003NHrFIAW'}, {'Id': '005Wt000003NHsrIAG'}, {'Id': '005Wt000003NHuTIAW'}, {'Id': '005Wt000003NHuUIAW'}, {'Id': '#005Wt000003NHw5IAG'}, {'Id': '#005Wt000003NHxhIAG'}, {'Id': '005Wt000003NHzJIAW'}, {'Id': '005Wt000003NI2XIAW'}, {'Id': '005Wt000003NI49IAG'}, {'Id': '005Wt000003NI4AIAW'}, {'Id': '#005Wt000003NI5lIAG'}, {'Id': '005Wt000003NI5mIAG'}, {'Id': '005Wt000003NI7NIAW'}, {'Id': '005Wt000003NI7OIAW'}, {'Id': '005Wt000003NI7PIAW'}, {'Id': '005Wt000003NI7QIAW'}, {'Id': '005Wt000003NI90IAG'}, {'Id': '005Wt000003NIAbIAO'}, {'Id': '005Wt000003NIAcIAO'}, {'Id': '005Wt000003NIAdIAO'}, {'Id': '#005Wt000003NICDIA4'}, {'Id': '#005Wt000003NIDpIAO'}, {'Id': '005Wt000003NIDqIAO'}, {'Id': '005Wt000003NIH3IAO'}, {'Id': '005Wt000003NIIfIAO'}, {'Id': '#005Wt000003NIKHIA4'}, {'Id': '005Wt000003NILtIAO'}, {'Id': '005Wt000003NINVIA4'}, {'Id': '005Wt000003NINWIA4'}, {'Id': '005Wt000003NIP7IAO'}, {'Id': '005Wt000003NIQjIAO'}, {'Id': '#005Wt000003NISLIA4'}, {'Id': '005Wt000003NISMIA4'}, {'Id': '005Wt000003NISNIA4'}, {'Id': '005Wt000003NITxIAO'}, {'Id': '005Wt000003NIVZIA4'}, {'Id': '005Wt000003NIXBIA4'}, {'Id': '005Wt000003NIXCIA4'}, {'Id': '005Wt000003NIXDIA4'}, {'Id': '005Wt000003NIYnIAO'}, {'Id': '005Wt000003NIYoIAO'}, {'Id': '005Wt000003NIaPIAW'}, {'Id': '005Wt000003NIaQIAW'}, {'Id': '005Wt000003NIaRIAW'}, {'Id': '005Wt000003NIc1IAG'}, {'Id': '005Wt000003NIc2IAG'}, {'Id': '#005Wt000003NIc3IAG'}, {'Id': '#005Wt000003NIddIAG'}, {'Id': '005Wt000003NIdeIAG'}, {'Id': '005Wt000003NIfFIAW'}, {'Id': '005Wt000003NIfGIAW'}, {'Id': '005Wt000003NIfHIAW'}, {'Id': '005Wt000003NIgrIAG'}, {'Id': '#005Wt000003NIiTIAW'}, {'Id': '005Wt000003NIiUIAW'}, {'Id': '005Wt000003NIiVIAW'}, {'Id': '005Wt000003NIk5IAG'}, {'Id': '005Wt000003NIk6IAG'}, {'Id': '005Wt000003NIk7IAG'}, {'Id': '005Wt000003NIlhIAG'}, {'Id': '005Wt000003NIliIAG'}, {'Id': '005Wt000003NIljIAG'}, {'Id': '005Wt000003NInJIAW'}, {'Id': '005Wt000003NInKIAW'}, {'Id': '#005Wt000003NInLIAW'}, {'Id': '#005Wt000003NIovIAG'}, {'Id': '005Wt000003NIowIAG'}, {'Id': '005Wt000003NIqXIAW'}, {'Id': '005Wt000003NIs9IAG'}, {'Id': '005Wt000003NItlIAG'}, {'Id': '005Wt000003NItmIAG'}, {'Id': '005Wt000003NIvNIAW'}, {'Id': '005Wt000003NIwzIAG'}, {'Id': '005Wt000003NIx0IAG'}, {'Id': '005Wt000003NIx1IAG'}, {'Id': '005Wt000003NIybIAG'}, {'Id': '005Wt000003NJ0DIAW'}, {'Id': '005Wt000003NJ0EIAW'}, {'Id': '005Wt000003NJ1pIAG'}, {'Id': '005Wt000003NJ3RIAW'}, {'Id': '#005Wt000003NJ53IAG'}, {'Id': '#005Wt000003NJ6fIAG'}, {'Id': '005Wt000003NJ6gIAG'}, {'Id': '005Wt000003NJ8HIAW'}, {'Id': '#005Wt000003NJ9tIAG'}, {'Id': '005Wt000003NJ9uIAG'}, {'Id': '005Wt000003NJBVIA4'}, {'Id': '005Wt000003NJD7IAO'}, {'Id': '#005Wt000003NJD8IAO'}, {'Id': '005Wt000003NJD9IAO'}, {'Id': '005Wt000003NJEjIAO'}, {'Id': '#005Wt000003NJEkIAO'}, {'Id': '#005Wt000003NJGLIA4'}, {'Id': '#005Wt000003NJHxIAO'}, {'Id': '005Wt000003NJJZIA4'}, {'Id': '005Wt000003NJJaIAO'}, {'Id': '#005Wt000003NJLBIA4'}, {'Id': '#005Wt000003NJMnIAO'}, {'Id': '005Wt000003NJOPIA4'}, {'Id': '005Wt000003NJQ1IAO'}, {'Id': '#005Wt000003NJRdIAO'}, {'Id': '005Wt000003NJReIAO'}, {'Id': '005Wt000003NJTFIA4'}, {'Id': '005Wt000003NJTGIA4'}, {'Id': '005Wt000003NJUrIAO'}, {'Id': '#005Wt000003NJWTIA4'}, {'Id': '005Wt000003NJY5IAO'}, {'Id': '#005Wt000003NJZhIAO'}, {'Id': '#005Wt000003NJbJIAW'}, {'Id': '005Wt000003NJcvIAG'}, {'Id': '#005Wt000003NJcwIAG'}, {'Id': '005Wt000003NJeXIAW'}, {'Id': '005Wt000003NJg9IAG'}, {'Id': '005Wt000003NJgAIAW'}, {'Id': '005Wt000003NJhlIAG'}, {'Id': '005Wt000003NJjNIAW'}, {'Id': '005Wt000003NJkzIAG'}, {'Id': '#005Wt000003NJmbIAG'}, {'Id': '005Wt000003NJmcIAG'}, {'Id': '005Wt000003NJmdIAG'}, {'Id': '#005Wt000003NJoDIAW'}, {'Id': '005Wt000003NJppIAG'}, {'Id': '#005Wt000003NJrRIAW'}, {'Id': '#005Wt000003NJt3IAG'}, {'Id': '#005Wt000003NJufIAG'}, {'Id': '005Wt000003NJwHIAW'}, {'Id': '#005Wt000003NJxtIAG'}, {'Id': '005Wt000003NJzVIAW'}, {'Id': '005Wt000003NK17IAG'}, {'Id': '005Wt000003PUpBIAW'}], 'var_function-call-16087441587863589561': [{'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}]}

exec(code, env_args)
