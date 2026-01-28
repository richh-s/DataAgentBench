code = """import json
import re
from datetime import datetime

# Get the case data from storage
cases = locals()['var_functions.query_db:2']

# Define date range - past 10 months from 2021-04-10
end_date = datetime(2021, 4, 10)
start_date = datetime(2020, 6, 1)  # 10 months back

print("Analyzing cases from", start_date, "to", end_date)
print("Total cases found:", len(cases))

# Group cases by month
monthly_counts = {}

for case in cases:
    # Parse created date
    created_str = case['createddate']
    if created_str and created_str != 'None':
        # Remove timezone info for parsing
        created_str = created_str.split('+')[0]
        created_date = datetime.strptime(created_str, '%Y-%m-%dT%H:%M:%S.%f')
        
        # Check if within date range
        if start_date <= created_date <= end_date:
            month_key = created_date.strftime('%Y-%m')  # e.g., '2020-11'
            month_name = created_date.strftime('%B %Y')  # e.g., 'November 2020'
            
            if month_key not in monthly_counts:
                monthly_counts[month_key] = {'name': month_name, 'count': 0, 'cases': []}
            
            monthly_counts[month_key]['count'] += 1
            monthly_counts[month_key]['cases'].append({
                'id': case['id'],
                'subject': case['subject'],
                'date': created_date.strftime('%Y-%m-%d')
            })

# Sort by month
sorted_months = sorted(monthly_counts.items())

print("\nMonthly case counts:")
for month_key, data in sorted_months:
    print(f"{data['name']}: {data['count']} cases")

# Find month with most cases
max_month = None
max_count = 0

for month_key, data in sorted_months:
    if data['count'] > max_count:
        max_count = data['count']
        max_month = data['name']

print(f"\nMonth with most cases: {max_month} ({max_count} cases)")

# Just get the month name without year
if max_month:
    month_name_only = max_month.split()[0]
    print(f"Month name: {month_name_only}")
    
    result = month_name_only
else:
    result = "No cases found in date range"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_functions.query_db:2': [{'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'status': 'Closed', 'createddate': '2020-11-05T08:19:00.000+0000', 'closeddate': '2020-11-05T08:50:10.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDzsbIAD', 'subject': 'Scalability Problem', 'status': 'Closed', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'status': 'Waiting on Customer', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'status': 'Closed', 'createddate': '2021-03-07T11:25:00.000+0000', 'closeddate': '2021-03-07T17:46:52.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'status': 'Closed', 'createddate': '2020-11-09T19:02:00.000+0000', 'closeddate': '2020-11-10T09:47:54.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
