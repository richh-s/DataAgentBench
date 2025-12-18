code = """from datetime import datetime
import pandas as pd
import pytz

case_dates_raw = [
    {"createddate": "2020-11-05T08:19:00.000+0000"},
    {"createddate": "2023-06-30T13:03:00.000+0000"},
    {"createddate": "2020-09-29T01:59:00.000+0000"},
    {"createddate": "2021-03-07T11:25:00.000+0000"},
    {"createddate": "2020-11-09T19:02:00.000+0000"}
]

# Convert to pandas DataFrame
df = pd.DataFrame(case_dates_raw)

# Convert 'createddate' to datetime objects, ensuring UTC timezone
df['createddate'] = pd.to_datetime(df['createddate']).dt.tz_convert(pytz.utc)

# Define today's date and the start of the 10-month window as timezone-aware UTC datetimes
utc = pytz.UTC
today = utc.localize(datetime(2021, 4, 10))
ten_months_ago = utc.localize(datetime(2020, 6, 10)) # 2021-04-10 minus 10 months is 2020-06-10

# Filter cases within the last 10 months
df_filtered = df[(df['createddate'] >= ten_months_ago) & (df['createddate'] <= today)]

# Extract month names
df_filtered['month_name'] = df_filtered['createddate'].dt.strftime('%B')

# Count cases per month
month_counts = df_filtered['month_name'].value_counts()

if not month_counts.empty:
    # Find the month with the maximum count
    most_frequent_month = month_counts.idxmax()
    # Check if this month's count is significantly higher (e.g., at least twice the next highest, if there are others)
    # This is a simple heuristic for "significantly exceeds"
    if len(month_counts) > 1:
        sorted_counts = month_counts.sort_values(ascending=False)
        highest_count = sorted_counts.iloc[0]
        second_highest_count = sorted_counts.iloc[1]
        if highest_count >= 2 * second_highest_count:
            result = most_frequent_month
        else:
            result = "No single month significantly exceeds others."
    else:
        result = most_frequent_month # Only one month found, so it's the "highest"
else:
    result = "No cases found in the last 10 months."

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-4712482174536942146': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-7894785523581058224': [{'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2023-06-30T13:03:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
