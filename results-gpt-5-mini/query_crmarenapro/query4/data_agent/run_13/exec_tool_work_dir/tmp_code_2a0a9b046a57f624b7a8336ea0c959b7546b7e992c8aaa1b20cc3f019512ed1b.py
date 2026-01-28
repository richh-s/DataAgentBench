code = """import pandas as pd
import json
# read records from previous query
records = var_call_VMLp9gH9T63sNxto6gCJTXOP

df = pd.DataFrame(records)
if df.empty:
    result = None
else:
    df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')
    df = df.dropna(subset=['createddate'])
    df['month'] = df['createddate'].dt.strftime('%B')
    counts = df['month'].value_counts()
    if counts.empty:
        result = None
    else:
        top_count = counts.iloc[0]
        second_count = counts.iloc[1] if len(counts) > 1 else 0
        top_month = counts.index[0]
        # consider it significant if top_count > second_count
        if top_count > second_count:
            result = top_month
        else:
            result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_B18NjMlS8EGvejhwlsPedD55': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_call_VMLp9gH9T63sNxto6gCJTXOP': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
