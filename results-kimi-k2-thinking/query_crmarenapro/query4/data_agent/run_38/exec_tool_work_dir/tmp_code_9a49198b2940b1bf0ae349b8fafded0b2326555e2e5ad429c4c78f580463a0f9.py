code = """import json
from datetime import datetime

# Get the case data
cases = locals()['var_functions.query_db:10']

print("Total cases found:", len(cases))
print("\nCase details:")
for case in cases:
    print(f"ID: {case['id']}")
    print(f"Subject: {case['subject']}")
    print(f"Created: {case['createddate']}")
    print(f"OrderItem: {case['orderitemid__c']}")
    print("---")

# Group by month
monthly_counts = {}
for case in cases:
    created_str = case['createddate']
    if created_str and created_str != 'None':
        # Parse date
        created_str = created_str.split('+')[0]
        created_date = datetime.strptime(created_str, '%Y-%m-%dT%H:%M:%S.%f')
        
        month_key = created_date.strftime('%Y-%m')
        month_name = created_date.strftime('%B %Y')
        
        if month_key not in monthly_counts:
            monthly_counts[month_key] = {'name': month_name, 'count': 0}
        
        monthly_counts[month_key]['count'] += 1

# Sort and display
sorted_months = sorted(monthly_counts.items())
print("\nMonthly breakdown:")
for month_key, data in sorted_months:
    print(f"{data['name']}: {data['count']} cases")

# Find month with most cases
max_month = None
max_count = 0
if sorted_months:
    max_month = sorted_months[0][1]['name']
    max_count = sorted_months[0][1]['count']
    
    for month_key, data in sorted_months:
        if data['count'] > max_count:
            max_count = data['count']
            max_month = data['name']

print(f"\nMonth with most cases: {max_month} ({max_count} cases)")

# Extract just month name
result = max_month.split()[0] if max_month else "No data"
print(f"\nFinal answer: {result}")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_functions.query_db:2': [{'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'status': 'Closed', 'createddate': '2020-11-05T08:19:00.000+0000', 'closeddate': '2020-11-05T08:50:10.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDzsbIAD', 'subject': 'Scalability Problem', 'status': 'Closed', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'status': 'Waiting on Customer', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'status': 'Closed', 'createddate': '2021-03-07T11:25:00.000+0000', 'closeddate': '2021-03-07T17:46:52.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'status': 'Closed', 'createddate': '2020-11-09T19:02:00.000+0000', 'closeddate': '2020-11-10T09:47:54.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}], 'var_functions.execute_python:8': "TRIM(REPLACE(orderitemid__c, '#', '')) IN ('802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797awIAA', '802Wt00000797z7IAA', '802Wt00000798VPIAY', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt00000799o1IAA', '802Wt0000079A2bIAE', '802Wt0000079ACGIA2', '802Wt0000079B0EIAU', '802Wt0000079B6gIAE')", 'var_functions.query_db:10': [{'id': '#500Wt00000DDxnbIAD', 'subject': 'ROI Metrics Clarification  ', 'status': 'Closed', 'createddate': '2021-01-25T09:30:00.000+0000', 'closeddate': '2021-01-25T15:27:34.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'status': 'Closed', 'createddate': '2020-11-05T08:19:00.000+0000', 'closeddate': '2020-11-05T08:50:10.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'status': 'Waiting on Customer', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'status': 'Closed', 'createddate': '2021-03-07T11:25:00.000+0000', 'closeddate': '2021-03-07T17:46:52.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'status': 'Closed', 'createddate': '2020-11-09T19:02:00.000+0000', 'closeddate': '2020-11-10T09:47:54.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
