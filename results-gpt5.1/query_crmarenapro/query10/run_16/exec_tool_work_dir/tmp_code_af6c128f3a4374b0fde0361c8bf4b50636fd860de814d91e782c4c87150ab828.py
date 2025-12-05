code = """import json
from datetime import datetime

cases = var_call_hBDW4T5esrUYSq5b9NHlObIG

fmt = '%Y-%m-%dT%H:%M:%S.000+0000'

handle_times = {}
case_counts = {}

for row in cases:
    aid = row['agent_id']
    created = datetime.strptime(row['createddate'], fmt)
    closed = datetime.strptime(row['closeddate'], fmt)
    diff_hours = (closed - created).total_seconds() / 3600.0
    handle_times.setdefault(aid, 0.0)
    case_counts.setdefault(aid, 0)
    handle_times[aid] += diff_hours
    case_counts[aid] += 1

avg_times = {}
for aid, total in handle_times.items():
    if case_counts[aid] > 1:
        avg_times[aid] = total / case_counts[aid]

if avg_times:
    best_agent = min(avg_times, key=avg_times.get)
else:
    best_agent = None

result = json.dumps(best_agent)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_hBDW4T5esrUYSq5b9NHlObIG': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_1zcoYKouIccRVmhoLYJzqoWH': []}

exec(code, env_args)
