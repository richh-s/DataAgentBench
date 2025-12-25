code = """import json
from datetime import datetime

rows = var_call_Ji5UR3Ggpiz5pjNf6KqaFu5T

handle_times = {}
case_counts = {}

for r in rows:
    agent = r['agent_id']
    created = datetime.strptime(r['createddate'], '%Y-%m-%dT%H:%M:%S.000+0000')
    closed = datetime.strptime(r['closeddate'], '%Y-%m-%dT%H:%M:%S.000+0000')
    ht_hours = (closed - created).total_seconds() / 3600.0
    handle_times.setdefault(agent, 0.0)
    case_counts.setdefault(agent, 0)
    handle_times[agent] += ht_hours
    case_counts[agent] += 1

avg_times = {}
for agent, total_ht in handle_times.items():
    if case_counts[agent] > 1:
        avg_times[agent] = total_ht / case_counts[agent]

if avg_times:
    best_agent = min(avg_times, key=avg_times.get)
else:
    best_agent = None

result = json.dumps(best_agent)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_VmF066pSRmugxkvnjJH3KnOu': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_Ji5UR3Ggpiz5pjNf6KqaFu5T': [{'case_id': '500Wt00000DDepmIAD', 'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'case_id': '500Wt00000DDyzpIAD', 'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'case_id': '500Wt00000DDzUPIA1', 'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'case_id': '500Wt00000DDzsbIAD', 'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'case_id': '#500Wt00000DDzscIAD', 'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'case_id': '500Wt00000DDzuEIAT', 'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'case_id': '#500Wt00000DE02HIAT', 'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_8dHkvNtI17qCo5ouCfeVPQpD': []}

exec(code, env_args)
