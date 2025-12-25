code = """import json
from collections import defaultdict
from datetime import datetime

cases = locals()['var_function-call-9379197308370690660']
history_path = locals()['var_function-call-6841357651747039383']
with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(id_str):
    if not id_str: return None
    if id_str.startswith('#'): return id_str[1:]
    return id_str

history_by_case = defaultdict(list)
for h in history:
    cid = clean_id(h.get('caseid__c'))
    if cid: history_by_case[cid].append(h)

debug_info = []

agent_processed_counts = defaultdict(int)
agent_durations = defaultdict(list)

for c in cases:
    cid = clean_id(c['id'])
    h_list = history_by_case.get(cid, [])
    owner_assignments = [h for h in h_list if h.get('field__c') == 'Owner Assignment']
    
    num_assignments = len(owner_assignments)
    final_owner = clean_id(c['ownerid'])
    
    agents = set()
    for oa in owner_assignments:
        old = clean_id(oa.get('oldvalue__c'))
        new = clean_id(oa.get('newvalue__c'))
        if old and old != 'None': agents.add(old)
        if new and new != 'None': agents.add(new)
    if final_owner: agents.add(final_owner)
    
    for a in agents: agent_processed_counts[a] += 1
    
    # Duration
    fmt = "%Y-%m-%dT%H:%M:%S.%f%z"
    created = datetime.strptime(c['createddate'], fmt)
    closed = datetime.strptime(c['closeddate'], fmt)
    dur = (closed - created).total_seconds()
    
    measured = False
    if num_assignments <= 1:
        if final_owner:
            agent_durations[final_owner].append(dur)
            measured = True
            
    debug_info.append({
        "case_id": cid,
        "num_assignments": num_assignments,
        "agents": list(agents),
        "measured": measured,
        "duration": dur,
        "final_owner": final_owner
    })

print("__RESULT__:")
print(json.dumps({
    "debug_cases": debug_info,
    "counts": agent_processed_counts,
    "durations_keys": list(agent_durations.keys())
}))"""

env_args = {'var_function-call-16935417607994828587': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-11268043920336260726': [{'id': 'a04Wt0000052xxEIAQ', 'caseid__c': '500Wt00000DDTEQIA5', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2022-03-02T10:15:00.000+0000', 'field__c': 'Case Creation'}, {'id': 'a04Wt00000531KtIAI', 'caseid__c': '500Wt00000DDzhJIAT', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-02-15T14:30:00.000+0000', 'field__c': 'Case Creation'}, {'id': '#a04Wt00000531KuIAI', 'caseid__c': '500Wt00000DDzpNIAT', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-09-07T16:30:00.000+0000', 'field__c': 'Owner Assignment'}, {'id': 'a04Wt00000531KvIAI', 'caseid__c': '500Wt00000DDzsbIAD', 'oldvalue__c': 'None', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000', 'field__c': 'Case Closed'}, {'id': 'a04Wt00000531RLIAY', 'caseid__c': '500Wt00000DDfHCIA1', 'oldvalue__c': 'None', 'newvalue__c': '005Wt000003NIXBIA4', 'createddate': '2021-07-23T11:00:00.000+0000', 'field__c': 'Owner Assignment'}], 'var_function-call-9379197308370690660': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-6841357651747039383': 'file_storage/function-call-6841357651747039383.json', 'var_function-call-10712201643136478981': []}

exec(code, env_args)
