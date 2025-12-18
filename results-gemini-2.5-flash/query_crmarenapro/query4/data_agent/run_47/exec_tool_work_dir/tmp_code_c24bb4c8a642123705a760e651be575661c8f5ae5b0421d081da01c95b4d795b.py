code = """import json
from datetime import datetime, timedelta

cases_data = locals()['var_function-call-4627593676811812952']

case_dates = []
for case in cases_data:
    created_date_str = case['createddate']
    if '.' in created_date_str:
        date_object = datetime.strptime(created_date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
    else:
        date_object = datetime.strptime(created_date_str, '%Y-%m-%dT%H:%M:%S%z')
    case_dates.append(date_object)

# Today's date is 2021-04-10. So the past 10 months are from June 2020 to March 2021.
start_date_period = datetime(2020, 6, 1)
end_date_period = datetime(2021, 3, 31, 23, 59, 59)

monthly_counts = {}
current_month_iter = start_date_period
while current_month_iter <= end_date_period:
    month_name = current_month_iter.strftime('%B')
    monthly_counts[month_name] = 0
    # Move to the next month
    if current_month_iter.month == 12:
        current_month_iter = current_month_iter.replace(year=current_month_iter.year + 1, month=1, day=1)
    else:
        current_month_iter = current_month_iter.replace(month=current_month_iter.month + 1, day=1)


for date_obj in case_dates:
    # Remove timezone info for comparison with naive datetime objects
    naive_date_obj = date_obj.replace(tzinfo=None)
    if start_date_period <= naive_date_obj <= end_date_period:
        month_name = naive_date_obj.strftime('%B')
        if month_name in monthly_counts:
            monthly_counts[month_name] += 1

if monthly_counts:
    max_month = max(monthly_counts, key=monthly_counts.get)
    max_count = monthly_counts[max_month]

    sorted_counts = sorted(monthly_counts.values(), reverse=True)
    
    if len(sorted_counts) > 1 and max_count > 0:
        second_highest_count = sorted_counts[1]
        if max_count > 2 * second_highest_count:
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
