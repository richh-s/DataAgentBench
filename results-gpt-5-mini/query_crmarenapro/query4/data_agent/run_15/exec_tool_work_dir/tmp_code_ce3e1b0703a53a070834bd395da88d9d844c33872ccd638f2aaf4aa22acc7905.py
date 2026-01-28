code = """import json
from collections import Counter
from datetime import datetime

# Access the query result from support Case created dates
records = var_call_oEyLjqlUvvxng85Ts3CVrZyg

# Parse dates and count months
months = []
for r in records:
    cd = r.get('createddate')
    if not cd:
        continue
    # Some createddate strings may have timezone; parse ISO-like
    try:
        dt = datetime.fromisoformat(cd.replace('Z', '+00:00'))
    except Exception:
        try:
            dt = datetime.strptime(cd[:19], '%Y-%m-%dT%H:%M:%S')
        except Exception:
            continue
    months.append(dt.strftime('%B'))

counts = Counter(months)

# Determine if a month significantly exceeds others
result = None
if counts:
    # Get top two counts
    sorted_counts = counts.most_common()
    top_month, top_count = sorted_counts[0]
    second_count = sorted_counts[1][1] if len(sorted_counts) > 1 else 0
    # Define significance: top_count >= 2 * second_count and top_count > 1
    if second_count == 0:
        significant = top_count > 1
    else:
        significant = top_count >= 2 * second_count and top_count > 1
    if significant:
        result = top_month
    else:
        result = None
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_imSJvwXQHS1fuTPb4aFO8ibo': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_EyKdvFwq43oL0yvr1SFzui1N': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_oEyLjqlUvvxng85Ts3CVrZyg': [{'createddate': '2021-01-25T09:30:00.000+0000'}, {'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
