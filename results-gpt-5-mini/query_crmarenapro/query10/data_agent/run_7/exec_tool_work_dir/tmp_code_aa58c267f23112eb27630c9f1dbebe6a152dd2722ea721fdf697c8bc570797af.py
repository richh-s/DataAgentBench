code = """import json
from collections import defaultdict

cases = var_call_69JElMd8xY9awTdZ9bCy5wc4
casehistory_path = var_call_HfcrefbZsfmGeLaNAK0n3Cx7
with open(casehistory_path, 'r', encoding='utf-8') as f:
    casehistory = json.load(f)

def norm(val):
    if val is None:
        return None
    s = str(val).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

owner_map = defaultdict(list)
for rec in casehistory:
    if rec.get('field__c') != 'Owner Assignment':
        continue
    caseid = norm(rec.get('caseid__c'))
    newval = norm(rec.get('newvalue__c'))
    if caseid is None or newval is None:
        continue
    owner_map[caseid].append(newval)

processed_counts = defaultdict(int)
handle_times = defaultdict(list)
case_ids = [norm(c.get('case_id')) for c in cases]
case_by_id = {norm(c.get('case_id')): c for c in cases}

for cid in case_ids:
    if cid is None:
        continue
    owners_for_case = owner_map.get(cid, [])
    unique_agents = set(owners_for_case)
    for ag in unique_agents:
        processed_counts[ag] += 1
    if not owners_for_case:
        ownerid = norm(case_by_id[cid]['owner_id'])
        if ownerid:
            processed_counts[ownerid] += 1
            owners_for_case = [ownerid]
    if len(owners_for_case) <= 1:
        owner_for_handle = norm(case_by_id[cid]['owner_id'])
        if owner_for_handle:
            try:
                hs = float(case_by_id[cid]['handle_seconds'])
                handle_times[owner_for_handle].append(hs)
            except Exception:
                pass

avgs = {}
for ag, times in handle_times.items():
    if times:
        avgs[ag] = sum(times)/len(times)

candidates = {ag: avgs[ag] for ag in avgs.keys() if processed_counts.get(ag, 0) > 1}

out = {
    'processed_counts': dict(processed_counts),
    'handle_times': {k: v for k, v in handle_times.items()},
    'avgs': avgs,
    'candidates': candidates
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_r2LIKtM63KptKkz5yGdsEjxX': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_VL7krWab6rBG3eCZbBSqa8e9': [{'field__c': 'Case Creation'}, {'field__c': 'Case Closed'}, {'field__c': 'Owner Assignment'}], 'var_call_HfcrefbZsfmGeLaNAK0n3Cx7': 'file_storage/call_HfcrefbZsfmGeLaNAK0n3Cx7.json', 'var_call_69JElMd8xY9awTdZ9bCy5wc4': [{'case_id': '500Wt00000DDepmIAD', 'owner_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'handle_seconds': '33068.0'}, {'case_id': '500Wt00000DDyzpIAD', 'owner_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'handle_seconds': '1442.0'}, {'case_id': '500Wt00000DDzUPIA1', 'owner_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'handle_seconds': '882.0'}, {'case_id': '500Wt00000DDzsbIAD', 'owner_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'handle_seconds': '21608.0'}, {'case_id': '#500Wt00000DDzscIAD', 'owner_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'handle_seconds': '1007.0'}, {'case_id': '500Wt00000DDzuEIAT', 'owner_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'handle_seconds': '14712.0'}, {'case_id': '#500Wt00000DE02HIAT', 'owner_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'handle_seconds': '2194.0'}], 'var_call_eEdgAykPnxtQGuO1td03mc8Y': None}

exec(code, env_args)
