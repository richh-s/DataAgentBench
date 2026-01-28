code = """import json
from statistics import mean, pstdev
# var_call_MD1dZQ3E0es5UCpgDFfqmB3Q is available from previous query
rows = var_call_MD1dZQ3E0es5UCpgDFfqmB3Q
# Normalize counts and extract
data = []
for r in rows:
    try:
        cnt = int(r.get('cnt'))
    except:
        cnt = 0
    month = r.get('month_name')
    data.append((month, cnt))

if not data:
    ans = None
else:
    counts = [c for m,c in data]
    max_count = max(counts)
    # handle case where all counts equal
    if len(counts) == 1:
        ans = data[0][0] if counts[0] > 0 else None
    else:
        mu = mean(counts)
        sigma = pstdev(counts)
        threshold = mu + 2*sigma
        # find months with max_count
        months_with_max = [m for m,c in data if c == max_count]
        if max_count > threshold and len(months_with_max) == 1:
            ans = months_with_max[0]
        else:
            ans = None

# Prepare output as JSON string (None -> null)
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_5mfTkTf1D8BlkwJb4bvWTaqH': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_call_MD1dZQ3E0es5UCpgDFfqmB3Q': [{'year_month': '2020-09', 'month_name': 'September', 'cnt': '1'}, {'year_month': '2020-11', 'month_name': 'November', 'cnt': '2'}, {'year_month': '2021-01', 'month_name': 'January', 'cnt': '1'}, {'year_month': '2021-03', 'month_name': 'March', 'cnt': '1'}]}

exec(code, env_args)
