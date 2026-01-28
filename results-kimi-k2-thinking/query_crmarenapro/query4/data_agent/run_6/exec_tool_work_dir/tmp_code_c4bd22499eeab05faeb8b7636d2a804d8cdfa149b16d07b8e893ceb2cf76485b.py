code = """import json
from datetime import datetime
import re

# Case data from the query
cases = [
    {"createddate": "2020-09-29T01:59:00.000+0000", "id": "500Wt00000DE00gIAD", "subject": "SecureAnalytics Compliance Concern", "description": "I need clarification on SecureAnalytics Pro's adherence to security compliance standards."},
    {"createddate": "2020-11-05T08:19:00.000+0000", "id": "500Wt00000DDy8bIAD", "subject": "Update Alerts Absent", "description": "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them."},
    {"createddate": "2020-11-09T19:02:00.000+0000", "id": "500Wt00000DE0NFIA1", "subject": "Missing Feature Notifications", "description": "I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform."},
    {"createddate": "2021-01-25T09:30:00.000+0000", "id": "#500Wt00000DDxnbIAD", "subject": "ROI Metrics Clarification  ", "description": "I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies."},
    {"createddate": "2021-03-07T11:25:00.000+0000", "id": "500Wt00000DE0AMIA1", "subject": "No Feature Update Notices", "description": "I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements."}
]

# Calculate month counts for the past 10 months from 2021-04-10
today = datetime.strptime('2021-04-10', '%Y-%m-%d')
past_10_months_start = datetime(2020, 6, 10)  # Approx 10 months before April 2021

month_counts = {}
filtered_cases = []

for case in cases:
    case_date = datetime.strptime(case['createddate'][:10], '%Y-%m-%d')
    
    # Check if within past 10 months
    if case_date >= past_10_months_start and case_date <= today:
        month_key = case_date.strftime('%Y-%m')
        month_name = case_date.strftime('%B %Y')
        month_counts[month_name] = month_counts.get(month_name, 0) + 1
        filtered_cases.append(case)

# Find month with most cases
sorted_months = sorted(month_counts.items(), key=lambda x: x[1], reverse=True)

print("__RESULT__:")
print(json.dumps({
    "month_counts": month_counts,
    "sorted_months": sorted_months,
    "top_month": sorted_months[0][0] if sorted_months else None,
    "top_month_count": sorted_months[0][1] if sorted_months else 0
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.'}], 'var_functions.query_db:6': [{'createddate': '2020-09-29T01:59:00.000+0000', 'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards."}, {'createddate': '2020-11-05T08:19:00.000+0000', 'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them."}, {'createddate': '2020-11-09T19:02:00.000+0000', 'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.'}, {'createddate': '2021-01-25T09:30:00.000+0000', 'id': '#500Wt00000DDxnbIAD', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.'}, {'createddate': '2021-03-07T11:25:00.000+0000', 'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.'}]}

exec(code, env_args)
