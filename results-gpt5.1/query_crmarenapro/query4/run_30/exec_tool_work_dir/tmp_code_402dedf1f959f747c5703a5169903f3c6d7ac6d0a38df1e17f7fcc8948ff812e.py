code = """import json
from datetime import datetime

rows = var_call_Lu7dNYUwNiVeCBbUQqwy0INg

# Filter to last 10 months relative to 2021-04-10 (inclusive start 2020-06-10)
start = datetime(2020, 6, 10)
end = datetime(2021, 4, 10)

filtered = []
for r in rows:
    ym = r['ym']
    dt = datetime.strptime(ym + '-01', '%Y-%m-%d')
    if start <= dt <= end:
        filtered.append({'ym': ym, 'cnt': int(r['cnt'])})

# Determine if any month significantly exceeds others.
# Here interpret "significantly" as strictly greater than all other months in this period.
if not filtered:
    month_name = None
else:
    max_cnt = max(r['cnt'] for r in filtered)
    top_months = [r for r in filtered if r['cnt'] == max_cnt]
    if len(top_months) == 1:
        ym = top_months[0]['ym']
        month_name = datetime.strptime(ym, '%Y-%m').strftime('%B')
    else:
        month_name = None

result = json.dumps(month_name)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Lu7dNYUwNiVeCBbUQqwy0INg': [{'ym': '2020-06', 'cnt': '2'}, {'ym': '2020-07', 'cnt': '4'}, {'ym': '2020-08', 'cnt': '1'}, {'ym': '2020-09', 'cnt': '1'}, {'ym': '2020-10', 'cnt': '3'}, {'ym': '2020-11', 'cnt': '2'}, {'ym': '2020-12', 'cnt': '1'}, {'ym': '2021-01', 'cnt': '3'}, {'ym': '2021-02', 'cnt': '1'}, {'ym': '2021-03', 'cnt': '1'}, {'ym': '2021-07', 'cnt': '1'}, {'ym': '2021-08', 'cnt': '1'}, {'ym': '2021-12', 'cnt': '1'}, {'ym': '2022-01', 'cnt': '3'}, {'ym': '2022-02', 'cnt': '1'}, {'ym': '2022-06', 'cnt': '3'}, {'ym': '2022-07', 'cnt': '4'}, {'ym': '2022-09', 'cnt': '1'}, {'ym': '2022-10', 'cnt': '1'}, {'ym': '2022-11', 'cnt': '1'}, {'ym': '2023-01', 'cnt': '3'}, {'ym': '2023-02', 'cnt': '1'}, {'ym': '2023-03', 'cnt': '2'}, {'ym': '2023-04', 'cnt': '1'}, {'ym': '2023-05', 'cnt': '1'}, {'ym': '2023-06', 'cnt': '1'}, {'ym': '2023-07', 'cnt': '2'}, {'ym': '2023-08', 'cnt': '2'}, {'ym': '2023-09', 'cnt': '1'}, {'ym': '2023-10', 'cnt': '1'}, {'ym': '2023-11', 'cnt': '2'}, {'ym': '2023-12', 'cnt': '1'}, {'ym': '2024-02', 'cnt': '1'}, {'ym': '2024-04', 'cnt': '4'}, {'ym': '2024-05', 'cnt': '2'}]}

exec(code, env_args)
