code = """import json
from datetime import datetime

rows = var_call_PIVr6arERlNpRogdhDQhvj1a

# Convert to list of (month_start, count)
parsed = []
for r in rows:
    dt = datetime.strptime(r['month_start'], '%Y-%m-%d')
    cnt = int(r['case_count'])
    parsed.append((dt, cnt))

# Find max and check if it's significantly higher: more than 1.5x the next highest
parsed.sort(key=lambda x: x[0])
counts = [c for _, c in parsed]
max_count = max(counts)
max_idx = counts.index(max_count)
sorted_counts = sorted(counts, reverse=True)
second = sorted_counts[1] if len(sorted_counts) > 1 else 0

if second == 0 or max_count >= 1.5 * second:
    peak_dt = parsed[max_idx][0]
    month_name = peak_dt.strftime('%B')
else:
    month_name = None

import json
result = json.dumps(month_name)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_5VMum4UYqdsofMp5CMlJeHZu': [{'Id': '#01tWt000006hVJdIAM'}], 'var_call_PIVr6arERlNpRogdhDQhvj1a': [{'month_start': '2020-07-01', 'case_count': '2'}, {'month_start': '2020-09-01', 'case_count': '4'}, {'month_start': '2020-10-01', 'case_count': '2'}, {'month_start': '2020-11-01', 'case_count': '4'}, {'month_start': '2020-12-01', 'case_count': '1'}, {'month_start': '2021-01-01', 'case_count': '3'}, {'month_start': '2021-02-01', 'case_count': '2'}, {'month_start': '2021-03-01', 'case_count': '5'}]}

exec(code, env_args)
