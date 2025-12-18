code = """import pandas as pd
import json

cases_data = locals()['var_function-call-5544670302811666366']
df = pd.DataFrame(cases_data)

# Convert 'createddate' to datetime objects and extract the month name
df['created_month'] = pd.to_datetime(df['createddate']).dt.strftime('%B')

# Count cases per month
monthly_case_counts = df['created_month'].value_counts().reset_index()
monthly_case_counts.columns = ['month', 'case_count']

# Find the month with the maximum case count
max_cases_month = monthly_case_counts.loc[monthly_case_counts['case_count'].idxmax()]

# Check if this month significantly exceeds others (e.g., at least 2x the next highest)
if len(monthly_case_counts) > 1:
    sorted_counts = monthly_case_counts.sort_values(by='case_count', ascending=False)
    if sorted_counts.iloc[0]['case_count'] >= 2 * sorted_counts.iloc[1]['case_count']:
        result = max_cases_month['month']
    else:
        result = "No particular month significantly exceeds others."
else:
    result = max_cases_month['month'] # Only one month, so it's the highest

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6751001765798742146': [{'cleaned_order_item_id': '802Wt0000078yuGIAQ'}, {'cleaned_order_item_id': '802Wt00000790mOIAQ'}, {'cleaned_order_item_id': '802Wt00000790zGIAQ'}, {'cleaned_order_item_id': '802Wt00000794F2IAI'}, {'cleaned_order_item_id': '802Wt000007968eIAA'}, {'cleaned_order_item_id': '802Wt00000796bfIAA'}, {'cleaned_order_item_id': '802Wt00000796qFIAQ'}, {'cleaned_order_item_id': '802Wt0000079734IAA'}, {'cleaned_order_item_id': '802Wt00000797W5IAI'}, {'cleaned_order_item_id': '802Wt00000797awIAA'}, {'cleaned_order_item_id': '802Wt00000797z7IAA'}, {'cleaned_order_item_id': '802Wt00000798VPIAY'}, {'cleaned_order_item_id': '802Wt00000798YdIAI'}, {'cleaned_order_item_id': '802Wt00000798okIAA'}, {'cleaned_order_item_id': '802Wt00000799o1IAA'}, {'cleaned_order_item_id': '802Wt0000079A2bIAE'}, {'cleaned_order_item_id': '802Wt0000079ACGIA2'}, {'cleaned_order_item_id': '802Wt0000079B0EIAU'}, {'cleaned_order_item_id': '802Wt0000079B6gIAE'}], 'var_function-call-9305990537926725248': ['802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797awIAA', '802Wt00000797z7IAA', '802Wt00000798VPIAY', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt00000799o1IAA', '802Wt0000079A2bIAE', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt0000079B6gIAE'], 'var_function-call-5544670302811666366': [{'createddate': '2021-01-25T09:30:00.000+0000'}, {'createddate': '2020-11-05T08:19:00.000+0000'}, {'createddate': '2020-09-29T01:59:00.000+0000'}, {'createddate': '2021-03-07T11:25:00.000+0000'}, {'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
