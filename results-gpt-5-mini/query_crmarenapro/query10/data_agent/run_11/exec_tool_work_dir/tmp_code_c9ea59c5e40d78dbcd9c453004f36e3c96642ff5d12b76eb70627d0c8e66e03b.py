code = """import json
from datetime import datetime

def norm_id(s):
    if s is None:
        return None
    return s.lstrip('#').strip()

cases = var_call_gDXhe5jHAByPkuEA9jVo8EDT
assigns = var_call_ZAF1vaH2eUh91lLK93dJ1iWc

# build assign_count map from assigns
assign_map = {}
for r in assigns:
    cid = norm_id(r.get('caseid__c'))
    try:
        count = int(r.get('assign_count') or 0)
    except:
        try:
            count = int(str(r.get('assign_count')).strip())
        except:
            count = 0
    assign_map[cid] = count

# process cases closed in timeframe
from dateutil import parser

agent_times = {}  # agentid -> list of handle times in seconds
for c in cases:
    cid = norm_id(c.get('id'))
    created = c.get('createddate')
    closed = c.get('closeddate')
    owner = norm_id(c.get('ownerid'))
    # ensure dates exist
    if not created or not closed or not owner:
        continue
    # exclude transferred cases: assign_count must be 1
    if assign_map.get(cid, 0) != 1:
        continue
    try:
        dt_created = parser.isoparse(created)
        dt_closed = parser.isoparse(closed)
    except Exception:
        continue
    handle_seconds = (dt_closed - dt_created).total_seconds()
    if handle_seconds < 0:
        # skip corrupted
        continue
    agent_times.setdefault(owner, []).append(handle_seconds)

# compute averages and filter agents with >1 cases
avg_times = {}
for agent, times in agent_times.items():
    if len(times) > 1:
        avg_times[agent] = sum(times) / len(times)

if not avg_times:
    result = None
else:
    # find agent with lowest average handle time
    best_agent = min(avg_times.items(), key=lambda x: x[1])[0]
    result = best_agent

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_o408jhosKaIJW3SiOf7AaAAE': 'file_storage/call_o408jhosKaIJW3SiOf7AaAAE.json', 'var_call_ZAF1vaH2eUh91lLK93dJ1iWc': 'file_storage/call_ZAF1vaH2eUh91lLK93dJ1iWc.json', 'var_call_gDXhe5jHAByPkuEA9jVo8EDT': [{'id': '500Wt00000DDepmIAD', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'ownerid': '005Wt000003NJufIAG'}, {'id': '500Wt00000DDyzpIAD', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'ownerid': '005Wt000003NJGLIA4'}, {'id': '500Wt00000DDzUPIA1', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'ownerid': '005Wt000003NDqDIAW'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'ownerid': '005Wt000003NJD9IAO'}, {'id': '#500Wt00000DDzscIAD', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'ownerid': '005Wt000003NEtOIAW'}, {'id': '500Wt00000DDzuEIAT', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'ownerid': '005Wt000003NJJaIAO'}, {'id': '#500Wt00000DE02HIAT', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'ownerid': '005Wt000003NIddIAG'}], 'var_call_bL9n0xH7pnS2UwNou2Mjwgex': [{'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-06-30T19:03:08.000+0000'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-05-03T00:11:47.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzZHIA1', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:59:42.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJppIAG', 'createddate': '2023-06-12T10:00:06.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:54:02.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzr0IAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-01T10:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzUPIA1', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-05-10T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDzXdIAL', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-06-03T15:21:34.000+0000'}, {'caseid__c': '500Wt00000DDsG3IAL', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzscIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-05-02T23:55:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NH3GIAW', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000'}, {'caseid__c': '500Wt00000DDflsIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NF1SIAW', 'createddate': '2023-06-12T09:45:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzivIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000'}, {'caseid__c': '500Wt00000DDzkXIAT', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-06-19T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzsbIAD', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000'}, {'caseid__c': '500Wt00000DDyzpIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDTxbIAH', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-08-15T14:30:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-07-01T10:30:00.000+0000'}, {'caseid__c': '500Wt00000DDzuEIAT', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-06-02T13:35:12.000+0000'}, {'caseid__c': '500Wt00000DE02HIAT', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'field__c': 'Case Creation', 'newvalue__c': 'None', 'createddate': '2023-07-02T11:00:00.000+0000'}, {'caseid__c': '500Wt00000DDepmIAD', 'field__c': 'Case Closed', 'newvalue__c': 'None', 'createddate': '2023-07-01T19:41:08.000+0000'}, {'caseid__c': '500Wt00000DDDfwIAH', 'field__c': 'Owner Assignment', 'newvalue__c': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:30:02.000+0000'}]}

exec(code, env_args)
