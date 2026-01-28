code = """import json
records = var_call_onFFRa4O2kJBBYgfCkmxLPIn
# Extract createddate and parse month name
from datetime import datetime
months = []
for r in records:
    cd = r.get('createddate')
    if not cd:
        continue
    # strip timezone offset
    try:
        dt = datetime.strptime(cd[:19], '%Y-%m-%dT%H:%M:%S')
    except Exception:
        try:
            dt = datetime.fromisoformat(cd)
        except Exception:
            continue
    months.append(dt.strftime('%B'))
# Count occurrences
from collections import Counter
cnt = Counter(months)
# We need to check if any month in past 10 months has significantly more cases than others.
# For this dataset, consider 'significantly' as at least 2x the next highest count.
if not cnt:
    result = ''
else:
    most_common = cnt.most_common()
    # Determine if top is >=2x second
    if len(most_common) == 1:
        top_month = most_common[0][0]
        significant = True
    else:
        top_month, top_count = most_common[0]
        second_count = most_common[1][1]
        significant = top_count >= 2 * second_count
        if not significant:
            top_month = ''
result = top_month if significant else ''
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5H6oz5zfmhRrjuOijegm7AyX': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_j1u3HkB5SGYutexHRhNzLqPw': {'in_list': "'802Wt0000078yuGIAQ','802Wt00000790mOIAQ','802Wt00000790zGIAQ','802Wt00000794F2IAI','802Wt000007968eIAA','802Wt00000796bfIAA','802Wt00000796qFIAQ','802Wt0000079734IAA','802Wt00000797W5IAI','802Wt00000797awIAA','802Wt00000797z7IAA','802Wt00000798VPIAY','802Wt00000798YdIAI','802Wt00000798okIAA','802Wt00000799o1IAA','802Wt0000079A2bIAE','802Wt0000079ACGIA2','802Wt0000079B0EIAU','802Wt0000079B6gIAE'", 'ids': ['802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797awIAA', '802Wt00000797z7IAA', '802Wt00000798VPIAY', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt00000799o1IAA', '802Wt0000079A2bIAE', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt0000079B6gIAE']}, 'var_call_onFFRa4O2kJBBYgfCkmxLPIn': [{'id': '#500Wt00000DDxnbIAD', 'subject': 'ROI Metrics Clarification  ', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
