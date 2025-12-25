code = """import json
from datetime import datetime

cases_data = locals()['var_function-call-4627593676811812952']

case_dates = []
for case in cases_data:
    created_date_str = case['createddate']
    # Parse the date string, handling the timezone offset and potential microseconds
    if '.' in created_date_str:
        date_object = datetime.strptime(created_date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
    else:
        date_object = datetime.strptime(created_date_str, '%Y-%m-%dT%H:%M:%S%z')
    case_dates.append(date_object)

# Define the 10-month period ending in March 2021 (since today's date is April 10, 2021)
end_date_period = datetime(2021, 3, 31)
start_date_period = datetime(2020, 6, 1)

monthly_counts = {}
for i in range(10):
    current_month = (end_date_period.replace(day=1) - timedelta(days=1)).replace(day=1) if i > 0 else end_date_period.replace(day=1)
    if i > 0:
        for _ in range(i):
            current_month = (current_month - timedelta(days=1)).replace(day=1)
    
    month_name = current_month.strftime('%B')
    monthly_counts[month_name] = 0

for date_obj in case_dates:
    if start_date_period <= date_obj.replace(tzinfo=None) <= end_date_period:
        month_name = date_obj.strftime('%B')
        if month_name in monthly_counts:
            monthly_counts[month_name] += 1

# Identify the month with the highest count
if monthly_counts:
    max_month = max(monthly_counts, key=monthly_counts.get)
    max_count = monthly_counts[max_month]

    # Check if this count significantly exceeds others (e.g., more than double the second highest)
    sorted_counts = sorted(monthly_counts.values(), reverse=True)
    if len(sorted_counts) > 1:
        second_highest_count = sorted_counts[1]
        if max_count > 0 and max_count > 2 * second_highest_count:
            result = max_month
        else:
            result = "No particular month significantly exceeds others."
    elif len(sorted_counts) == 1 and max_count > 0:
        result = max_month
    else:
        result = "No particular month significantly exceeds others."
else:
    result = "No cases found in the past 10 months."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13291623538806716327': [{'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-12346428839927143793': [{'Id': '802Wt00000797awIAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-3258717655134617731': "802Wt00000797awIAA', '802Wt00000798VPIAY', '802Wt00000799o1IAA', '802Wt0000079A2bIAE', '802Wt0000079ACGIA2', '802Wt0000079B6gIAE", 'var_function-call-4627593676811812952': [{'createddate': '2021-01-25T09:30:00.000+0000', 'id': '#500Wt00000DDxnbIAD'}]}

exec(code, env_args)
