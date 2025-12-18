code = """from datetime import datetime
import pandas as pd

case_dates = locals()['var_function-call-870091599546811177']
df = pd.DataFrame(case_dates)

# Convert createddate to datetime objects
df['createddate'] = pd.to_datetime(df['createddate'])

# Define today's date and the start of the 10-month period
today = datetime(2021, 4, 10)
start_date = today - pd.DateOffset(months=10)

# Filter for dates within the last 10 months
df_filtered = df[(df['createddate'] >= start_date) & (df['createddate'] <= today)]

# Extract month names
df_filtered['month'] = df_filtered['createddate'].dt.strftime('%B')

# Count cases per month
monthly_counts = df_filtered['month'].value_counts()

# Find the month with the maximum count
if not monthly_counts.empty:
    most_cases_month = monthly_counts.idxmax()
    # Check if this month significantly exceeds others (e.g., more than double the second highest)
    if len(monthly_counts) > 1:
        sorted_counts = monthly_counts.sort_values(ascending=False)
        if sorted_counts.iloc[0] > 2 * sorted_counts.iloc[1]:
            result = most_cases_month
        else:
            result = "No month significantly exceeds others."
    elif len(monthly_counts) == 1:
        result = most_cases_month
    else:
        result = "No cases found in the last 10 months."
else:
    result = "No cases found in the last 10 months."

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-11027385069598740399': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-870091599546811177': [{'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2023-06-30T13:03:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
