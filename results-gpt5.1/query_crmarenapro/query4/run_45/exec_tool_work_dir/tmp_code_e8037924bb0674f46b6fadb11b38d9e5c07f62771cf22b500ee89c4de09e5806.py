code = """import json
import calendar

rows = var_call_IRzbnygLk2JujdDbnOCrlN8Q

# Convert to numeric counts
months = []
for r in rows:
    months.append((r['month'], int(r['case_count'])))

# Find max and check if significantly exceeds others: define as > mean + 2*std, or simply strictly greater than second highest and by at least 50%
if not months:
    result = None
else:
    months_sorted = sorted(months, key=lambda x: x[1], reverse=True)
    top_month, top_count = months_sorted[0]
    if len(months_sorted) == 1:
        significant = True
    else:
        second = months_sorted[1][1]
        significant = top_count >= second * 1.5 and top_count != second
    if significant:
        year, month_num = top_month.split('-')
        month_name = calendar.month_name[int(month_num)]
        result = month_name
    else:
        result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_nU2IavzdBFLgt27u4LOzdaew': [{'clean_id': '802Wt0000078yuGIAQ'}, {'clean_id': '802Wt00000790mOIAQ'}, {'clean_id': '802Wt00000790zGIAQ'}, {'clean_id': '802Wt00000794F2IAI'}, {'clean_id': '802Wt000007968eIAA'}, {'clean_id': '802Wt00000796bfIAA'}, {'clean_id': '802Wt00000796qFIAQ'}, {'clean_id': '802Wt0000079734IAA'}, {'clean_id': '802Wt00000797W5IAI'}, {'clean_id': '802Wt00000797awIAA'}, {'clean_id': '802Wt00000797z7IAA'}, {'clean_id': '802Wt00000798VPIAY'}, {'clean_id': '802Wt00000798YdIAI'}, {'clean_id': '802Wt00000798okIAA'}, {'clean_id': '802Wt00000799o1IAA'}, {'clean_id': '802Wt0000079A2bIAE'}, {'clean_id': '802Wt0000079ACGIA2'}, {'clean_id': '802Wt0000079B0EIAU'}, {'clean_id': '802Wt0000079B6gIAE'}], 'var_call_IRzbnygLk2JujdDbnOCrlN8Q': [{'month': '2020-09', 'case_count': '1'}, {'month': '2020-11', 'case_count': '2'}, {'month': '2021-01', 'case_count': '1'}, {'month': '2021-03', 'case_count': '1'}]}

exec(code, env_args)
