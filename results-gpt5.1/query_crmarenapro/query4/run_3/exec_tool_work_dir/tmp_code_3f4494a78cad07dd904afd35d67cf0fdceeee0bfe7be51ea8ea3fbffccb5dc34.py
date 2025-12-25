code = """import json
import calendar

rows = var_call_BA4uwfw9q36EVDDzqK1OiC82

max_count = 0
max_month = None
for r in rows:
    c = int(r['case_count'])
    if c > max_count:
        max_count = c
        max_month = r['month']

if max_month is None:
    result = None
else:
    year, month_num = max_month.split('-')
    month_name = calendar.month_name[int(month_num)]
    result = month_name

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4DeDclrNB35boOs4fc3FVaFn': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_BA4uwfw9q36EVDDzqK1OiC82': [{'month': '2020-09', 'case_count': '1'}, {'month': '2020-11', 'case_count': '2'}, {'month': '2021-01', 'case_count': '1'}, {'month': '2021-03', 'case_count': '1'}]}

exec(code, env_args)
