code = """import json
import pandas as pd

cases = locals()['var_function-call-15813525106352124259']
history_path = locals()['var_function-call-1992848873889521844']
with open(history_path, 'r') as f:
    history = json.load(f)

def clean_id(x):
    if not isinstance(x, str):
        return x
    x = x.strip()
    if x.startswith('#'):
        x = x[1:]
    return x

debug_info = {}

cleaned_cases = []
for c in cases:
    c['id'] = clean_id(c['id'])
    c['ownerid'] = clean_id(c['ownerid'])
    cleaned_cases.append(c)

owner_counts = {}
for h in history:
    cid = clean_id(h['caseid__c'])
    owner_counts[cid] = owner_counts.get(cid, 0) + 1

agent_counts = {}
for c in cleaned_cases:
    aid = c['ownerid']
    agent_counts[aid] = agent_counts.get(aid, 0) + 1

debug_info['agent_counts'] = agent_counts
debug_info['owner_counts_sample'] = {k: owner_counts[k] for k in list(owner_counts)[:5]}

agent_details = []
for agent, count in agent_counts.items():
    if count <= 1:
        continue
    
    agent_case_list = [c for c in cleaned_cases if c['ownerid'] == agent]
    valid_count = 0
    
    for c in agent_case_list:
        cid = c['id']
        oc = owner_counts.get(cid, 0)
        if oc <= 1:
            valid_count += 1
    
    agent_details.append({'agent': agent, 'total': count, 'valid': valid_count})

debug_info['agent_details'] = agent_details

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-14838987602196373344': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-8892615390852284541': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_function-call-14093882633430532867': [{'count': '165'}], 'var_function-call-15813525106352124259': [{'id': '500Wt00000DDepmIAD', 'ownerid': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'id': '500Wt00000DDyzpIAD', 'ownerid': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'id': '500Wt00000DDzUPIA1', 'ownerid': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'id': '500Wt00000DDzsbIAD', 'ownerid': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'id': '#500Wt00000DDzscIAD', 'ownerid': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'id': '500Wt00000DDzuEIAT', 'ownerid': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'id': '#500Wt00000DE02HIAT', 'ownerid': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_function-call-1992848873889521844': 'file_storage/function-call-1992848873889521844.json', 'var_function-call-6551131518112016470': 'No qualifying agents', 'var_function-call-3479205796434553846': 'Done'}

exec(code, env_args)
