code = """import json
from collections import defaultdict
from datetime import datetime

# Get the cases data
cases_data = var_functions.query_db:4

# Extract month from createddate and count cases per month
cases_by_month = defaultdict(int)
month_names = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

for case in cases_data:
    created_date_str = case['createddate']
    # Parse the date string
    created_date = datetime.fromisoformat(created_date_str.replace('Z', '+00:00'))
    month_key = created_date.strftime('%Y-%m')  # e.g., '2020-11'
    month_name = month_names[created_date.month]
    cases_by_month[month_key] += 1

# Sort by month
cases_by_month = dict(sorted(cases_by_month.items()))

# Print the result
result = json.dumps(cases_by_month)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_functions.query_db:4': [{'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
