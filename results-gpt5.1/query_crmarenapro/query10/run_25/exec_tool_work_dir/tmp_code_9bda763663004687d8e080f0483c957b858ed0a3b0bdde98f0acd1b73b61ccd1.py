code = """import json
from datetime import datetime
rows = var_call_OCviAFPb1EswapDi5BENq1XE
fmt = '%Y-%m-%dT%H:%M:%S.000+0000'
handle_times = []
for r in rows:
    start = datetime.strptime(r['createddate'], fmt)
    end = datetime.strptime(r['closeddate'], fmt)
    mins = (end-start).total_seconds()/60.0
    handle_times.append({'agent_id': r['agent_id'], 'minutes': mins})
from collections import defaultdict
sums = defaultdict(float)
counts = defaultdict(int)
for ht in handle_times:
    sums[ht['agent_id']] += ht['minutes']
    counts[ht['agent_id']] += 1
avgs = {aid: sums[aid]/counts[aid] for aid in sums if counts[aid] > 1}
if avgs:
    best_agent = min(avgs, key=avgs.get)
else:
    best_agent = None
result = json.dumps(best_agent)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_OCviAFPb1EswapDi5BENq1XE': [{'agent_id': '005Wt000003NJufIAG', 'createddate': '2023-07-01T10:30:00.000+0000', 'closeddate': '2023-07-01T19:41:08.000+0000'}, {'agent_id': '005Wt000003NJGLIA4', 'createddate': '2023-08-15T14:30:00.000+0000', 'closeddate': '2023-08-15T14:54:02.000+0000'}, {'agent_id': '005Wt000003NDqDIAW', 'createddate': '2023-05-10T14:45:00.000+0000', 'closeddate': '2023-05-10T14:59:42.000+0000'}, {'agent_id': '005Wt000003NJD9IAO', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000'}, {'agent_id': '005Wt000003NEtOIAW', 'createddate': '2023-05-02T23:55:00.000+0000', 'closeddate': '2023-05-03T00:11:47.000+0000'}, {'agent_id': '005Wt000003NJJaIAO', 'createddate': '2023-06-02T09:30:00.000+0000', 'closeddate': '2023-06-02T13:35:12.000+0000'}, {'agent_id': '005Wt000003NIddIAG', 'createddate': '2023-06-03T14:45:00.000+0000', 'closeddate': '2023-06-03T15:21:34.000+0000'}], 'var_call_64PzUOTQqMk87oHYL47yvpK5': []}

exec(code, env_args)
