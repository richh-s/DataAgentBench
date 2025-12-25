code = """import json
from datetime import datetime

rows = var_call_9fQxKt8ofEZVbc9M1Un2IG7a

max_row = max(rows, key=lambda r: int(r['case_count'])) if rows else None

if not rows:
    result = None
else:
    # check if max is significantly higher: here interpret as strictly greater than all others
    max_count = int(max_row['case_count'])
    other_counts = [int(r['case_count']) for r in rows if r is not max_row]
    if other_counts and max_count <= max(other_counts):
        result = None
    else:
        # convert YYYY-MM to month name
        dt = datetime.strptime(max_row['month'], '%Y-%m')
        result = dt.strftime('%B')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JXzOFn0mSVlAnrkxoBlVIqIp': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_call_9fQxKt8ofEZVbc9M1Un2IG7a': [{'month': '2020-09', 'case_count': '1'}, {'month': '2020-11', 'case_count': '2'}, {'month': '2021-03', 'case_count': '1'}]}

exec(code, env_args)
