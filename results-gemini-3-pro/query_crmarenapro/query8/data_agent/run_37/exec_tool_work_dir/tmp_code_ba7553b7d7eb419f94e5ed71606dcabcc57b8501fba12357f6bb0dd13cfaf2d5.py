code = """import json
from datetime import datetime

# Read the file
with open(locals()['var_function-call-7370318940516593212'], 'r') as f:
    history_data = json.load(f)

# Define window: Last 4 completed quarters (Q2 2022, Q3 2022, Q4 2022, Q1 2023)
# 2022-04-01 to 2023-03-31
start_date = datetime(2022, 4, 1).timestamp()
end_date = datetime(2023, 4, 1).timestamp() # Up to Apr 1st midnight

handled_counts = {}
transfer_counts = {}

def clean_id(id_str):
    if not id_str or id_str == 'None': return None
    return id_str.lstrip('#').strip()

# Process
for record in history_data:
    try:
        dt = datetime.strptime(record['createddate'], "%Y-%m-%dT%H:%M:%S.%f%z")
    except ValueError:
        dt = datetime.strptime(record['createddate'], "%Y-%m-%dT%H:%M:%S%z")
    
    ts = dt.timestamp()
    
    if start_date <= ts < end_date: # Using < end_date to exclude Apr 1st itself if needed, or <= for inclusive. Let's use < 2023-04-01
        old_val = clean_id(record.get('oldvalue__c'))
        new_val = clean_id(record.get('newvalue__c'))
        
        # Transfer Count (Outgoing)
        if old_val:
            transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1
        
        # Handled Count (Incoming Only)
        if new_val:
            handled_counts[new_val] = handled_counts.get(new_val, 0) + 1

# Filter: Handled > 0 (Incoming in window)
candidates = []
for agent, h_count in handled_counts.items():
    if h_count > 0:
        t_count = transfer_counts.get(agent, 0)
        candidates.append({'id': agent, 'transfers': t_count, 'handled': h_count})

# Sort by transfers ASC, then handled DESC
candidates.sort(key=lambda x: (x['transfers'], -x['handled']))

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-11319294601133468608': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-15707160685309008611': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-1723384662900447026': [{'id': 'a04Wt00000534p0IAA', 'caseid__c': '500Wt00000DDzRCIA1', 'oldvalue__c': '005Wt000003NFhOIAW', 'newvalue__c': '005Wt000003NHuUIAW', 'createddate': '2021-09-20T15:38:02.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000535UwIAI', 'caseid__c': '500Wt00000DDzW3IAL', 'oldvalue__c': '005Wt000003NJ6gIAG', 'newvalue__c': '005Wt000003NIfHIAW', 'createddate': '2021-11-02T13:31:14.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000537YNIAY', 'caseid__c': '500Wt00000DDflsIAD', 'oldvalue__c': '005Wt000003NF1SIAW', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000', 'field__c': 'Owner Assignment'}, {'id': '#a04Wt00000537riIAA', 'caseid__c': '500Wt00000DDzSnIAL', 'oldvalue__c': '005Wt000003NHuUIAW', 'newvalue__c': '005Wt000003NJ9tIAG', 'createddate': '2021-10-15T13:58:32.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt0000053831IAA', 'caseid__c': '500Wt00000DDnt7IAD', 'oldvalue__c': '005Wt000003NHGAIA4', 'newvalue__c': '005Wt000003NEdKIAW', 'createddate': '2021-09-02T15:47:56.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-4226301716621980325': [{'id': '#500Wt00000DDDfwIAH', 'createddate': '2023-07-02T11:00:00.000+0000', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDNYoIAP', 'createddate': '2023-09-30T11:30:00.000+0000', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'createddate': '2022-08-05T14:30:00.000+0000', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPSZIA5', 'createddate': '2023-10-02T14:15:00.000+0000', 'ownerid': '005Wt000003NJhlIAG'}, {'id': '500Wt00000DDPZ0IAP', 'createddate': '2022-04-18T10:30:00.000+0000', 'ownerid': '005Wt000003NJD9IAO'}], 'var_function-call-10041239716983636839': [{'id': 'a04Wt00000538O1IAI', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000539GoIAI', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-07-02T11:00:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000539QTIAY', 'caseid__c': '500Wt00000DDDfwIAH', 'oldvalue__c': '005Wt000003NH3GIAW', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-15083401529753318684': [{'count': '39'}], 'var_function-call-16065977505509795385': [{'count': '393'}], 'var_function-call-7370318940516593212': 'file_storage/function-call-7370318940516593212.json', 'var_function-call-5404701045690186135': [{'id': '005Wt000003NJhlIAG', 'transfers': 0}, {'id': '005Wt000003NISLIA4', 'transfers': 0}, {'id': '005Wt000003NJTFIA4', 'transfers': 0}, {'id': '005Wt000003NEzqIAG', 'transfers': 0}, {'id': '005Wt000003NDJ1IAO', 'transfers': 0}, {'id': '005Wt000003NGjuIAG', 'transfers': 0}, {'id': '005Wt000003NIwzIAG', 'transfers': 0}, {'id': '005Wt000003NJ6gIAG', 'transfers': 0}, {'id': '005Wt000003NDsUIAW', 'transfers': 0}, {'id': '005Wt000003NJ8HIAW', 'transfers': 0}, {'id': '005Wt000003NINVIA4', 'transfers': 0}, {'id': '005Wt000003NHpeIAG', 'transfers': 0}, {'id': '005Wt000003NJoDIAW', 'transfers': 0}, {'id': '005Wt000003NI2XIAW', 'transfers': 0}, {'id': '005Wt000003NIVZIA4', 'transfers': 0}, {'id': '005Wt000003NFr4IAG', 'transfers': 0}, {'id': '005Wt000003NInLIAW', 'transfers': 0}, {'id': '005Wt000003NIc2IAG', 'transfers': 0}, {'id': '005Wt000003NBcAIAW', 'transfers': 0}, {'id': '005Wt000003NBykIAG', 'transfers': 0}, {'id': '005Wt000003NEGhIAO', 'transfers': 0}, {'id': '005Wt000003NJ0DIAW', 'transfers': 0}, {'id': '005Wt000003NHsrIAG', 'transfers': 0}, {'id': '005Wt000003NJrRIAW', 'transfers': 0}, {'id': '005Wt000003NIaQIAW', 'transfers': 0}, {'id': '005Wt000003NFKoIAO', 'transfers': 0}, {'id': '005Wt000003NJD9IAO', 'transfers': 0}, {'id': '005Wt000003NDqFIAW', 'transfers': 0}, {'id': '005Wt000003NIvNIAW', 'transfers': 0}, {'id': '005Wt000003NJEjIAO', 'transfers': 0}, {'id': '005Wt000003NIliIAG', 'transfers': 1}], 'var_function-call-6973009691941201383': [{'id': '005Wt000003NJ8HIAW', 'transfers': 0, 'handled': 3}, {'id': '005Wt000003NFKoIAO', 'transfers': 0, 'handled': 3}, {'id': '005Wt000003NHsrIAG', 'transfers': 0, 'handled': 2}, {'id': '005Wt000003NINVIA4', 'transfers': 0, 'handled': 2}, {'id': '005Wt000003NJhlIAG', 'transfers': 0, 'handled': 2}, {'id': '005Wt000003NDqFIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NEzqIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NEGhIAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJ6gIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIVZIA4', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NBcAIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NFr4IAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NHpeIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NI2XIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJTFIA4', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJoDIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIc2IAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NBykIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJD9IAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJrRIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NDsUIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIwzIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIaQIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NDJ1IAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIvNIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NISLIA4', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJEjIAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NGjuIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJ0DIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NInLIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIliIAG', 'transfers': 1, 'handled': 3}], 'var_function-call-12564117282649602265': [{'id': '005Wt000003NJ8HIAW', 'transfers': 0, 'handled': 3}, {'id': '005Wt000003NFKoIAO', 'transfers': 0, 'handled': 3}, {'id': '005Wt000003NHsrIAG', 'transfers': 0, 'handled': 2}, {'id': '005Wt000003NINVIA4', 'transfers': 0, 'handled': 2}, {'id': '005Wt000003NJhlIAG', 'transfers': 0, 'handled': 2}, {'id': '005Wt000003NDqFIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NEzqIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NEGhIAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJ6gIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIVZIA4', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NBcAIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NFr4IAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NHpeIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NI2XIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJTFIA4', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJoDIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIc2IAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NBykIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJD9IAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJrRIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NDsUIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIwzIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIaQIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NDJ1IAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIvNIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NISLIA4', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJEjIAO', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NGjuIAG', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NJ0DIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NInLIAW', 'transfers': 0, 'handled': 1}, {'id': '005Wt000003NIliIAG', 'transfers': 1, 'handled': 2}], 'var_function-call-16949603287843763299': [{'Id': '005Wt000003NFKoIAO', 'FirstName': 'Akari', 'LastName': 'Fujiwara', 'Alias': 'fujiwara'}, {'Id': '005Wt000003NJ8HIAW', 'FirstName': 'Sun', 'LastName': 'Park', 'Alias': 'sun.park'}]}

exec(code, env_args)
