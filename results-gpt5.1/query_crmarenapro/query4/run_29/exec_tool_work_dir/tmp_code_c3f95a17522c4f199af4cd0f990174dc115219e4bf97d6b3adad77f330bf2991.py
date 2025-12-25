code = """import json

rows = var_call_JZsjB7pbJs93ZAvpIhQqt1BR
# Find max count
max_count = max(int(r['case_count']) for r in rows)
# Check if it's significantly higher: here interpret as strictly greater than all others and at least 50% higher than median
counts = sorted(int(r['case_count']) for r in rows)
mid = len(counts)//2
median = (counts[mid] if len(counts)%2==1 else (counts[mid-1]+counts[mid])/2)

candidates = [r for r in rows if int(r['case_count']) == max_count]
month_name = None
if len(candidates)==1 and max_count >= 1.5*median:
    # Convert YYYY-MM to month name
    import calendar
    y, m = candidates[0]['month'].split('-')
    month_name = calendar.month_name[int(m)]

result = month_name if month_name is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TCyIb71UV4HNFYOXaAoVTaNr': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_JZsjB7pbJs93ZAvpIhQqt1BR': [{'month': '2020-07', 'case_count': '2'}, {'month': '2020-09', 'case_count': '4'}, {'month': '2020-10', 'case_count': '2'}, {'month': '2020-11', 'case_count': '4'}, {'month': '2020-12', 'case_count': '1'}, {'month': '2021-01', 'case_count': '3'}, {'month': '2021-02', 'case_count': '2'}, {'month': '2021-03', 'case_count': '5'}]}

exec(code, env_args)
