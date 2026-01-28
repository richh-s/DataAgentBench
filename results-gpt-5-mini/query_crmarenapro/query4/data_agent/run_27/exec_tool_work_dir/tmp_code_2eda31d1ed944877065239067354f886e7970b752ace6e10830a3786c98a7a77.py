code = """import json
records = var_call_RZAk6oXAoFlP8X3Q9g280QSX
# Clean month names and convert counts to int
clean = [{ 'month': r['month_name'].strip(), 'cnt': int(r['cnt']) } for r in records]
# Find the month with max count; if tie, list all
max_cnt = max(r['cnt'] for r in clean) if clean else 0
max_months = [r['month'] for r in clean if r['cnt']==max_cnt]
# If one month, return its name; if multiple, return list
result = max_months[0] if len(max_months)==1 else max_months
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iWZZDos4DQ2ip9RW6eyfmwSY': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_VecEvBomusEf3gqTkTLDLtfi': ['802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797awIAA', '802Wt00000797z7IAA', '802Wt00000798VPIAY', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt00000799o1IAA', '802Wt0000079A2bIAE', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt0000079B6gIAE'], 'var_call_s93weVSJfX52DourhFAYs1Uf': [], 'var_call_RZAk6oXAoFlP8X3Q9g280QSX': [{'month_name': 'November ', 'cnt': '2'}, {'month_name': 'January  ', 'cnt': '1'}, {'month_name': 'March    ', 'cnt': '1'}, {'month_name': 'September', 'cnt': '1'}]}

exec(code, env_args)
