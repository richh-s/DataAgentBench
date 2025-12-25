code = """import json
import os

data_source = locals()['var_function-call-18286661986496937185']

if isinstance(data_source, str) and os.path.exists(data_source):
    with open(data_source, 'r') as f:
        history = json.load(f)
else:
    history = data_source

def clean_id(i):
    if not i or i == 'None':
        return None
    i = str(i).strip()
    if i.startswith('#'):
        i = i[1:]
    return i

agents_handled = set()
transfer_counts = {}

for record in history:
    old_val = clean_id(record.get('oldvalue__c'))
    new_val = clean_id(record.get('newvalue__c'))
    
    # Check if they are users (005 prefix standard for Users in Salesforce)
    old_is_user = old_val and old_val.startswith('005')
    new_is_user = new_val and new_val.startswith('005')
    
    if old_is_user:
        agents_handled.add(old_val)
        transfer_counts[old_val] = transfer_counts.get(old_val, 0) + 1
        
    if new_is_user:
        agents_handled.add(new_val)
        if new_val not in transfer_counts:
            transfer_counts[new_val] = 0

if not transfer_counts:
    result = {"error": "No agents found"}
else:
    min_transfers = min(transfer_counts.values())
    candidates = [a for a, c in transfer_counts.items() if c == min_transfers]
    candidates.sort()
    result = {"min_transfers": min_transfers, "candidates": candidates}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8062965063719433765': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5092297911757294437': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-18286661986496937185': [{'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-05-15T14:00:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDqFIAW', 'createddate': '2022-05-12T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEzqIAG', 'createddate': '2022-08-05T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NEGhIAO', 'createddate': '2022-05-10T11:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ6gIAG', 'createddate': '2022-09-05T11:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIVZIA4', 'createddate': '2022-04-16T09:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBcAIAW', 'createddate': '2023-03-17T11:20:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2022-09-22T19:28:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFr4IAG', 'createddate': '2023-01-17T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-03-15T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2022-09-05T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHpeIAG', 'createddate': '2023-02-24T01:11:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NI2XIAW', 'createddate': '2023-03-16T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJTFIA4', 'createddate': '2022-10-01T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJoDIAW', 'createddate': '2023-01-18T14:45:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIc2IAG', 'createddate': '2023-03-01T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NBykIAG', 'createddate': '2023-01-18T10:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2022-04-18T10:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJrRIAW', 'createddate': '2022-04-17T14:20:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDsUIAW', 'createddate': '2022-09-16T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIliIAG', 'createddate': '2022-08-10T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIwzIAG', 'createddate': '2022-08-01T10:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-26T12:38:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJhlIAG', 'createddate': '2023-01-03T10:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-08T06:49:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIaQIAW', 'createddate': '2023-02-15T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-05T09:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-01-04T08:47:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NHsrIAG', 'createddate': '2023-02-01T14:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NDJ1IAO', 'createddate': '2023-01-23T08:02:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIvNIAW', 'createddate': '2022-12-01T10:00:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2022-07-23T07:37:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NISLIA4', 'createddate': '2023-03-20T14:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJEjIAO', 'createddate': '2022-10-15T11:00:00.000+0000'}, {'oldvalue__c': '005Wt000003NIliIAG', 'newvalue__c': '005Wt000003NGjuIAG', 'createddate': '2022-05-15T14:12:42.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ8HIAW', 'createddate': '2023-04-05T17:51:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NFKoIAO', 'createddate': '2023-03-22T14:30:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-03-23T09:15:00.000+0000'}, {'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NInLIAW', 'createddate': '2022-09-03T15:30:00.000+0000'}]}

exec(code, env_args)
