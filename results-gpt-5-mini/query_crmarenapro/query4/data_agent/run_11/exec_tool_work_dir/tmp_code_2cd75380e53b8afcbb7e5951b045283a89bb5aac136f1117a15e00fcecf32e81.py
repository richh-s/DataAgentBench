code = """import json
import datetime
records = var_call_ATQiwgHTWQpdjL139Xl3zhjl
counts = {}
for r in records:
    cd = r.get('createddate')
    if not cd:
        continue
    try:
        dt = datetime.datetime.strptime(cd, '%Y-%m-%dT%H:%M:%S.%f%z')
    except Exception:
        try:
            dt = datetime.datetime.fromisoformat(cd)
        except Exception:
            continue
    month = dt.strftime('%B')
    counts[month] = counts.get(month, 0) + 1
if not counts:
    result_month = ""
else:
    max_count = max(counts.values())
    top_months = [m for m, c in counts.items() if c == max_count]
    # If tie, pick the most recent month by parsing original records order
    if len(top_months) == 1:
        result_month = top_months[0]
    else:
        # find most recent occurrence among records
        recent = None
        for r in reversed(records):
            cd = r.get('createddate')
            if not cd:
                continue
            try:
                dt = datetime.datetime.strptime(cd, '%Y-%m-%dT%H:%M:%S.%f%z')
            except Exception:
                try:
                    dt = datetime.datetime.fromisoformat(cd)
                except Exception:
                    continue
            m = dt.strftime('%B')
            if m in top_months:
                recent = m
                break
        result_month = recent if recent else top_months[0]
print("__RESULT__:")
print(json.dumps(result_month))"""

env_args = {'var_call_JjlAy1f7KQkUKx1d0lAqCpjI': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_call_ATQiwgHTWQpdjL139Xl3zhjl': [{'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
