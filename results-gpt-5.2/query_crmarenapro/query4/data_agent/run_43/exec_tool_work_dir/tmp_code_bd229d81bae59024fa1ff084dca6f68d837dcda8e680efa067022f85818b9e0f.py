code = """import json
from datetime import datetime
rows = var_call_f19QYMuC6PlSWhoVgtJYIDJr
# convert counts
for r in rows:
    r['case_count'] = int(r['case_count'])
# identify month with max count
max_row = max(rows, key=lambda x: x['case_count']) if rows else None
month_name = None
if max_row:
    dt = datetime.fromisoformat(max_row['month_start'])
    month_name = dt.strftime('%B')
print('__RESULT__:')
print(json.dumps(month_name))"""

env_args = {'var_call_f19QYMuC6PlSWhoVgtJYIDJr': [{'month_start': '2020-09-01 00:00:00', 'case_count': '1'}, {'month_start': '2020-11-01 00:00:00', 'case_count': '2'}, {'month_start': '2021-01-01 00:00:00', 'case_count': '1'}, {'month_start': '2021-03-01 00:00:00', 'case_count': '1'}]}

exec(code, env_args)
