code = """import json
import pandas as pd

cases_list = locals()['var_function-call-5909842420318969754']
with open(locals()['var_function-call-11308014558138915622'], 'r') as f:
    history_list = json.load(f)

def clean_id(x):
    if not isinstance(x, str): return x
    x = x.strip()
    if x.startswith('#'): return x[1:]
    return x

debug_info = {}
debug_info["Total Cases"] = len(cases_list)
debug_info["Total History Entries"] = len(history_list)

case_owners = {}
for h in history_list:
    cid = clean_id(h.get('caseid__c'))
    oid = clean_id(h.get('newvalue__c'))
    if cid and oid:
        if cid not in case_owners: case_owners[cid] = []
        case_owners[cid].append(oid)

debug_info["Cases with History"] = len(case_owners)

matched_count = 0
single_owner_count = 0
multi_owner_count = 0
no_history_count = 0

sample_case_ids = []

for c in cases_list:
    cid = clean_id(c.get('id'))
    if len(sample_case_ids) < 5: sample_case_ids.append(cid)
    owners = case_owners.get(cid, [])
    if len(owners) > 0:
        matched_count += 1
        if len(owners) == 1:
            single_owner_count += 1
        else:
            multi_owner_count += 1
    else:
        no_history_count += 1

debug_info["Matched Cases"] = matched_count
debug_info["Single Owner Cases"] = single_owner_count
debug_info["Multi Owner Cases"] = multi_owner_count
debug_info["No History Cases"] = no_history_count
debug_info["Sample Case IDs"] = sample_case_ids
debug_info["Sample History IDs"] = list(case_owners.keys())[:5]

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-9305866664193886812': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-5909842420318969754': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-10922903359105958166': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-11308014558138915622': 'file_storage/function-call-11308014558138915622.json', 'var_function-call-16183834308635989304': []}

exec(code, env_args)
