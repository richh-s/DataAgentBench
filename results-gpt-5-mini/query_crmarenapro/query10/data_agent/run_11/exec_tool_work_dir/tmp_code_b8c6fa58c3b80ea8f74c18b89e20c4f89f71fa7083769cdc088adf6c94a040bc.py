code = """import json
import os
from dateutil import parser

# load helper
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

assigns_all = load_var(var_call_ZAF1vaH2eUh91lLK93dJ1iWc)
casehistory_range = load_var(var_call_bL9n0xH7pnS2UwNou2Mjwgex)
cases_closed = load_var(var_call_gDXhe5jHAByPkuEA9jVo8EDT)
handled_counts = load_var(var_call_LAkJF7oW63fK9Sk1e0fARPu9)

def norm(s):
    if s is None:
        return None
    return str(s).lstrip('#').strip()

# build assign_count map
assign_map = {}
for r in assigns_all:
    cid = norm(r.get('caseid__c'))
    try:
        count = int(r.get('assign_count'))
    except Exception:
        try:
            count = int(str(r.get('assign_count')).strip())
        except Exception:
            count = 0
    assign_map[cid] = count

# build dict of cases closed by id
cases_map = {}
for c in cases_closed:
    cid = norm(c.get('id'))
    cases_map[cid] = c

# find agents with handled_cases >1 in timeframe
qual_agents = []
for r in handled_counts:
    agent = norm(r.get('agent'))
    try:
        cnt = int(r.get('handled_cases'))
    except Exception:
        try:
            cnt = int(str(r.get('handled_cases')).strip())
        except:
            cnt = 0
    if cnt > 1:
        qual_agents.append(agent)

# for each qualifying agent, gather their assigned caseids in timeframe from casehistory_range
agent_caseids = {}
for rec in casehistory_range:
    if rec.get('field__c') != 'Owner Assignment':
        continue
    agent = norm(rec.get('newvalue__c'))
    cid = norm(rec.get('caseid__c'))
    if agent in qual_agents:
        agent_caseids.setdefault(agent, set()).add(cid)

# compute handle times for cases that were not transferred (assign_count==1) and closed in range
agent_handle_avgs = {}
for agent, cids in agent_caseids.items():
    times = []
    for cid in cids:
        if assign_map.get(cid, 0) != 1:
            continue
        case = cases_map.get(cid)
        if not case:
            continue
        created = case.get('createddate')
        closed = case.get('closeddate')
        if not created or not closed:
            continue
        try:
            dt_created = parser.isoparse(created)
            dt_closed = parser.isoparse(closed)
        except Exception:
            continue
        sec = (dt_closed - dt_created).total_seconds()
        if sec < 0:
            continue
        times.append(sec)
    if len(times) > 0:
        agent_handle_avgs[agent] = sum(times)/len(times)

# Among qualifying agents pick lowest avg
if not agent_handle_avgs:
    out = None
else:
    best = min(agent_handle_avgs.items(), key=lambda x: x[1])[0]
    out = best

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_o408jhosKaIJW3SiOf7AaAAE': 'file_storage/call_o408jhosKaIJW3SiOf7AaAAE.json', 'var_call_ZAF1vaH2eUh91lLK93dJ1iWc': 'file_storage/call_ZAF1vaH2eUh91lLK93dJ1iWc.json', 'var_call_gDXhe5jHAByPkuEA9jVo8EDT': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_bL9n0xH7pnS2UwNou2Mjwgex': [{'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-05-03T00:11:47.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:59:42.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:54:02.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-06-03T15:21:34.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-06-02T13:35:12.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-07-01T19:41:08.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000'}], 'var_call_QeHD3gh8un57RaJ0aTVNUEhx': None, 'var_call_AtBtlFeQtovsrS0YJek6Y4XG': [], 'var_call_LAkJF7oW63fK9Sk1e0fARPu9': [{'agent': '005Wt000003NDqDIAW', 'handled_cases': '3'}, {'agent': '005Wt000003NEtOIAW', 'handled_cases': '1'}, {'agent': '005Wt000003NF1SIAW', 'handled_cases': '1'}, {'agent': '005Wt000003NH3GIAW', 'handled_cases': '1'}, {'agent': '005Wt000003NI5mIAG', 'handled_cases': '1'}, {'agent': '005Wt000003NINVIA4', 'handled_cases': '1'}, {'agent': '005Wt000003NIddIAG', 'handled_cases': '1'}, {'agent': '005Wt000003NIfFIAW', 'handled_cases': '1'}, {'agent': '005Wt000003NJ0DIAW', 'handled_cases': '1'}, {'agent': '005Wt000003NJD9IAO', 'handled_cases': '1'}, {'agent': '005Wt000003NJGLIA4', 'handled_cases': '1'}, {'agent': '005Wt000003NJJaIAO', 'handled_cases': '1'}, {'agent': '005Wt000003NJUrIAO', 'handled_cases': '1'}, {'agent': '005Wt000003NJcvIAG', 'handled_cases': '1'}, {'agent': '005Wt000003NJppIAG', 'handled_cases': '1'}, {'agent': '005Wt000003NJufIAG', 'handled_cases': '1'}]}

exec(code, env_args)
