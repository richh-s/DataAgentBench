code = """import json
from datetime import datetime

rows = var_call_z7d78L6ATnOf9BYNLYKixhEx

handle_times = {}
counts = {}

for r in rows:
    if r['closeddate'] == 'None' or r['closeddate'] is None:
        continue
    created = datetime.fromisoformat(r['createddate'].replace('Z', '+00:00').replace('+0000', '+00:00'))
    closed = datetime.fromisoformat(r['closeddate'].replace('Z', '+00:00').replace('+0000', '+00:00'))
    delta_hours = (closed - created).total_seconds() / 3600.0
    aid = r['agent_id']
    handle_times[aid] = handle_times.get(aid, 0.0) + delta_hours
    counts[aid] = counts.get(aid, 0) + 1

avg_times = {aid: handle_times[aid]/counts[aid] for aid in counts if counts[aid] > 1}

if not avg_times:
    result = None
else:
    best_agent = min(avg_times, key=avg_times.get)
    result = best_agent

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_z7d78L6ATnOf9BYNLYKixhEx': [{'agent_id': '005Wt000003NJ0DIAW', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'case_id': '#500Wt00000DDDfwIAH'}, {'agent_id': '#005Wt000003NIfFIAW', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': 'None', 'case_id': '500Wt00000DDTxbIAH'}, {'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000', 'case_id': '500Wt00000DDepmIAD'}, {'agent_id': '005Wt000003NJppIAG', 'createddate': '2023-06-12T09:45:00.000+0000', 'closeddate': 'None', 'case_id': '500Wt00000DDflsIAD'}, {'agent_id': '005Wt000003NI5mIAG', 'createddate': '2023-08-10T14:20:00.000+0000', 'closeddate': 'None', 'case_id': '#500Wt00000DDsG3IAL'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000', 'case_id': '500Wt00000DDyzpIAD'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000', 'case_id': '500Wt00000DDzUPIA1'}, {'agent_id': '#005Wt000003NJUrIAO', 'createddate': '2023-06-22T11:00:00.000+0000', 'closeddate': 'None', 'case_id': '500Wt00000DDzXdIAL'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-07-02T09:30:00.000+0000', 'closeddate': 'None', 'case_id': '500Wt00000DDzZHIA1'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-06-05T11:15:00.000+0000', 'closeddate': 'None', 'case_id': '#500Wt00000DDzivIAD'}, {'agent_id': '#005Wt000003NINVIA4', 'createddate': '2023-06-19T14:30:00.000+0000', 'closeddate': 'None', 'case_id': '500Wt00000DDzkXIAT'}, {'agent_id': '#005Wt000003NJcvIAG', 'createddate': '2023-08-01T10:00:00.000+0000', 'closeddate': 'None', 'case_id': '500Wt00000DDzr0IAD'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'case_id': '500Wt00000DDzsbIAD'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000', 'case_id': '#500Wt00000DDzscIAD'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000', 'case_id': '500Wt00000DDzuEIAT'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000', 'case_id': '#500Wt00000DE02HIAT'}], 'var_call_znQLxZOfeCiBARU6g5E55WXU': []}

exec(code, env_args)
