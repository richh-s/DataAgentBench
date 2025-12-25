code = """import json
import pandas as pd

cases = locals()['var_function-call-10460115554179369151']
history_path = locals()['var_function-call-10460115554179367206']
with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(oid):
    if oid and isinstance(oid, str):
        return oid.lstrip('#')
    return oid

case_map = {}
target_case_ids = set()

for c in cases:
    cid = clean_id(c['id'])
    target_case_ids.add(cid)
    case_map[cid] = {'owners': set(), 'assignments': 0, 'current': clean_id(c['ownerid'])}

owner_assignments = [h for h in history if h['field__c'] == 'Owner Assignment']
history_map = {}
for h in owner_assignments:
    cid = clean_id(h['caseid__c'])
    if cid not in history_map:
        history_map[cid] = []
    history_map[cid].append(h)

for cid in target_case_ids:
    assignments = history_map.get(cid, [])
    case_map[cid]['assignments'] = len(assignments)
    for h in assignments:
        if h.get('newvalue__c'):
            case_map[cid]['owners'].add(clean_id(h['newvalue__c']))
    case_map[cid]['owners'].add(case_map[cid]['current'])
    case_map[cid]['owners'] = list(case_map[cid]['owners']) # Convert to list

print("__RESULT__:")
print(json.dumps(case_map))"""

env_args = {'var_function-call-13068910769840781709': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-1417980459216219882': [{'count': '7'}], 'var_function-call-1417980459216218149': [{'count': '165'}], 'var_function-call-10460115554179369151': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'status': 'Closed'}], 'var_function-call-10460115554179367206': 'file_storage/function-call-10460115554179367206.json', 'var_function-call-10832968714057640408': []}

exec(code, env_args)
