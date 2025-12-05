code = """import json
from datetime import datetime

rows = var_call_bfFMRhAII7rcU7z8qxIqcVXK

fmt = '%Y-%m-%dT%H:%M:%S.000+0000'

handle_times = []
for r in rows:
    created = datetime.strptime(r['createddate'], fmt)
    closed = datetime.strptime(r['closeddate'], fmt)
    minutes = (closed - created).total_seconds() / 60.0
    handle_times.append({'agent_id': r['agent_id'], 'minutes': minutes})

# aggregate per agent
agg = {}
case_counts = {}
for ht in handle_times:
    aid = ht['agent_id']
    agg[aid] = agg.get(aid, 0) + ht['minutes']
    case_counts[aid] = case_counts.get(aid, 0) + 1

avg_times = []
for aid, total in agg.items():
    cnt = case_counts[aid]
    if cnt > 1:
        avg_times.append({'agent_id': aid, 'avg_minutes': total / cnt, 'count': cnt})

if avg_times:
    best = min(avg_times, key=lambda x: x['avg_minutes'])
    result = best['agent_id']
else:
    result = None

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_bfFMRhAII7rcU7z8qxIqcVXK': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_Xuubg71NWHmAnPQ9WeIx0INV': []}

exec(code, env_args)
