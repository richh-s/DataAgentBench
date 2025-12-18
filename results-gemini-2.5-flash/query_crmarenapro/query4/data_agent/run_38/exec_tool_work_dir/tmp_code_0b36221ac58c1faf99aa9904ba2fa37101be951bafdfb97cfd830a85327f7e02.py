code = """import pandas as pd
import json
from datetime import datetime

case_dates_raw = [record["createddate"] for record in locals()["var_function-call-5918666521912037381"]]

# Convert to datetime objects and filter within the last 10 months from 2021-04-10
end_date = datetime(2021, 4, 10)
start_date = datetime(2020, 6, 10) # 10 months before 2021-04-10

filtered_dates = []
for date_str in case_dates_raw:
    dt_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.000+0000')
    if start_date <= dt_obj <= end_date:
        filtered_dates.append(dt_obj)

# Extract month names
month_names = [date.strftime('%B') for date in filtered_dates]

# Count cases per month
month_counts = pd.Series(month_names).value_counts()

# Check for significant exceedance
if not month_counts.empty:
    max_month = month_counts.idxmax()
    max_count = month_counts.max()

    if len(month_counts) > 1:
        other_months_counts = month_counts.drop(max_month)
        average_other_months = other_months_counts.mean()
        # Define 'significantly exceeds' as at least twice the average of other months
        if max_count >= 2 * average_other_months:
            result = max_month
        else:
            result = "No particular month significantly exceeds others."
    elif len(month_counts) == 1:
        result = month_counts.index[0] # If only one month, it automatically exceeds others in terms of being the only one.
    else:
        result = "No cases found in the last 10 months."
else:
    result = "No cases found in the last 10 months."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-18445006525449346873': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-3337621645028432999': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-6567023406007909171': ['802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797z7IAA', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt0000079B0EIAU'], 'var_function-call-5918666521912037381': [{'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2023-06-30T13:03:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
