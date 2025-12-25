code = """import json
from datetime import datetime

cases = locals()['var_function-call-17551838553651043930']
history_path = locals()['var_function-call-11261257856447075564']
with open(history_path, 'r') as f:
    history = json.load(f)

print(f"Total Cases Loaded: {len(cases)}")
print(f"Total History Entries: {len(history)}")

case_ids = set(c['id'] for c in cases)
# Filter history for these cases
relevant_history = [h for h in history if h['caseid__c'] in case_ids or ('#' + h['caseid__c']) in case_ids]
print(f"Relevant History Entries: {len(relevant_history)}")

# Debug: Print owners for each case
case_owners = {}
for h in relevant_history:
    cid = h['caseid__c']
    if cid not in case_owners: case_owners[cid] = set()
    case_owners[cid].add(h['newvalue__c'])
    if h['oldvalue__c'] and h['oldvalue__c'] != 'None':
         case_owners[cid].add(h['oldvalue__c'])

print("__RESULT__:")
print(json.dumps({k: list(v) for k, v in case_owners.items()}))"""

env_args = {'var_function-call-16084396659173659689': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-17551838553651043930': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-17551838553651042327': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-17551838553651040724': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-11261257856447075564': 'file_storage/function-call-11261257856447075564.json', 'var_function-call-3253871082083541322': [], 'var_function-call-1002297143353410861': [{'count': '21'}], 'var_function-call-1002297143353410410': [{'closeddate': '2023-12-02T16:45:51.000+0000'}, {'closeddate': '2023-11-02T14:10:33.000+0000'}, {'closeddate': '2023-10-16T15:22:17.000+0000'}, {'closeddate': '2023-10-15T14:23:52.000+0000'}, {'closeddate': '2023-10-05T16:02:30.000+0000'}]}

exec(code, env_args)
