code = """import json
import calendar

records = var_call_MIYDIryTSyAH0UXmdcDt8Rnc
counts = {}
for r in records:
    cd = r.get('createddate')
    if not cd:
        continue
    # Extract date part before 'T'
    date_part = cd.split('T')[0]
    parts = date_part.split('-')
    if len(parts) < 2:
        continue
    try:
        month = int(parts[1])
    except:
        continue
    counts[month] = counts.get(month, 0) + 1

if not counts:
    result = ""
else:
    max_count = max(counts.values())
    months_with_max = [calendar.month_name[m] for m,c in counts.items() if c == max_count]
    # If unique max, return that month name, else empty string
    result = months_with_max[0] if len(months_with_max) == 1 else ""

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EaWC0T4VAkgCDTpEy3JRtjYU': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_MIYDIryTSyAH0UXmdcDt8Rnc': [{'createddate': '2021-01-25T09:30:00.000+0000'}, {'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
