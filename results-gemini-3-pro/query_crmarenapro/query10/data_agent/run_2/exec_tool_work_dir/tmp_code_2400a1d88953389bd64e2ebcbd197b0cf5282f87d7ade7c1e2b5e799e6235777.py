code = """import json
from datetime import datetime

cases_key = 'var_function-call-7634771961496327246'
cases_raw = locals()[cases_key]
if isinstance(cases_raw, str):
    with open(cases_raw, 'r') as f:
        cases_list = json.load(f)
else:
    cases_list = cases_raw

history_key = 'var_function-call-10689379072275162428'
history_path = locals()[history_key]
with open(history_path, 'r') as f:
    history_list = json.load(f)

def clean_id(i):
    if i and isinstance(i, str):
        if i.startswith('#'):
            return i[1:]
    return i

case_assignments = {}
case_agents = {}

for h in history_list:
    if h.get('field__c') == 'Owner Assignment':
        cid = clean_id(h.get('caseid__c'))
        case_assignments[cid] = case_assignments.get(cid, 0) + 1
        
        old_val = clean_id(h.get('oldvalue__c'))
        new_val = clean_id(h.get('newvalue__c'))
        if cid not in case_agents:
            case_agents[cid] = set()
        if old_val and old_val != 'None':
            case_agents[cid].add(old_val)
        if new_val and new_val != 'None':
            case_agents[cid].add(new_val)

debug_info = []

valid_case_ids = set()
for c in cases_list:
    cid = clean_id(c['id'])
    valid_case_ids.add(cid)
    
    num = case_assignments.get(cid, 0)
    owner = clean_id(c['ownerid'])
    agents = list(case_agents.get(cid, set()))
    
    debug_info.append({
        'case_id': cid,
        'num_assigns': num,
        'owner': owner,
        'history_agents': agents
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-9342110329570298783': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-7634771961496327246': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-4838252256481333369': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-16296263846446172672': ['500Wt00000DDepmIAD', '500Wt00000DDyzpIAD', '500Wt00000DDzUPIA1', '500Wt00000DDzsbIAD', '500Wt00000DDzscIAD', '500Wt00000DDzuEIAT', '500Wt00000DE02HIAT'], 'var_function-call-10689379072275162428': 'file_storage/function-call-10689379072275162428.json', 'var_function-call-4960120652764271519': []}

exec(code, env_args)
