code = """import json
from datetime import datetime
import re

# Case data from different queries - combining and deduplicating
cases = [
    {"createddate": "2020-09-29T01:59:00.000+0000", "id": "500Wt00000DE00gIAD", "subject": "SecureAnalytics Compliance Concern", "description": "I need clarification on SecureAnalytics Pro's adherence to security compliance standards."},
    {"createddate": "2020-11-05T08:19:00.000+0000", "id": "500Wt00000DDy8bIAD", "subject": "Update Alerts Absent", "description": "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them."},
    {"createddate": "2020-11-09T19:02:00.000+0000", "id": "500Wt00000DE0NFIA1", "subject": "Missing Feature Notifications", "description": "I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform."},
    {"createddate": "2021-01-25T09:30:00.000+0000", "id": "#500Wt00000DDxnbIAD", "subject": "ROI Metrics Clarification  ", "description": "I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies."},
    {"createddate": "2021-03-07T11:25:00.000+0000", "id": "500Wt00000DE0AMIA1", "subject": "No Feature Update Notices", "description": "I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements."}
]

# Calculate month counts for the past 10 months from 2021-04-10
today = datetime.strptime('2021-04-10', '%Y-%m-%d')
# Past 10 months means from June 2020 to April 2021 (approximate)
start_date = datetime(2020, 6, 10)
end_date = today

print(f"Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")

month_counts = {}
cases_in_range = []

for case in cases:
    case_date_str = case['createddate'][:10]
    case_date = datetime.strptime(case_date_str, '%Y-%m-%d')
    
    # Check if within date range
    if start_date <= case_date <= end_date:
        month_name = case_date.strftime('%B %Y')
        month_counts[month_name] = month_counts.get(month_name, 0) + 1
        cases_in_range.append({
            'date': case_date_str,
            'month': month_name,
            'subject': case['subject'],
            'id': case['id']
        })

# Sort by month and count
sorted_months = sorted(month_counts.items(), key=lambda x: datetime.strptime(x[0], '%B %Y'))
sorted_by_count = sorted(month_counts.items(), key=lambda x: x[1], reverse=True)

print("\nCases in range:")
for case in cases_in_range:
    print(f"  {case['date']} - {case['month']} - {case['subject']}")

print(f"\nMonth counts (chronological):")
for month, count in sorted_months:
    print(f"  {month}: {count}")

print(f"\nMonth counts (by count):")
for month, count in sorted_by_count:
    print(f"  {month}: {count}")

# Find month with highest count
if sorted_by_count:
    top_month = sorted_by_count[0][0]
    top_count = sorted_by_count[0][1]
    
    # Check if it's significantly higher (at least 2x the second highest)
    second_highest = sorted_by_count[1][1] if len(sorted_by_count) > 1 else 0
    
    print(f"\nTop month: {top_month} with {top_count} cases")
    print(f"Second highest: {second_highest} cases")
    
    if top_count >= 2 * second_highest:
        significance = f"Significantly higher ({top_count} vs {second_highest})"
    else:
        significance = f"Not significantly higher ({top_count} vs {second_highest})"
    print(f"Significance: {significance}")
else:
    top_month = None
    top_count = 0

result = {
    "top_month": top_month,
    "top_month_count": top_count,
    "all_months": sorted_months
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.'}], 'var_functions.query_db:6': [{'createddate': '2020-09-29T01:59:00.000+0000', 'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards."}, {'createddate': '2020-11-05T08:19:00.000+0000', 'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them."}, {'createddate': '2020-11-09T19:02:00.000+0000', 'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.'}, {'createddate': '2021-01-25T09:30:00.000+0000', 'id': '#500Wt00000DDxnbIAD', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.'}, {'createddate': '2021-03-07T11:25:00.000+0000', 'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.'}], 'var_functions.execute_python:8': {'month_counts': {'September 2020': 1, 'November 2020': 2, 'January 2021': 1, 'March 2021': 1}, 'sorted_months': [['November 2020', 2], ['September 2020', 1], ['January 2021', 1], ['March 2021', 1]], 'top_month': 'November 2020', 'top_month_count': 2}, 'var_functions.query_db:10': [{'id': '#500Wt00000DDDfwIAH', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ'}, {'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ'}, {'id': '500Wt00000DDNYoIAP', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ'}, {'id': '500Wt00000DDPIsIAP', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ'}, {'id': '500Wt00000DDPSZIA5', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ'}, {'id': '500Wt00000DDPZ0IAP', 'orderitemid__c': '802Wt0000078xAFIAY', 'issueid__c': 'a03Wt00000JqxtvIAB'}, {'id': '500Wt00000DDPsOIAX', 'orderitemid__c': '802Wt0000079ATyIAM', 'issueid__c': 'a03Wt00000JqzKcIAJ'}, {'id': '500Wt00000DDPsPIAX', 'orderitemid__c': '802Wt00000794bXIAQ', 'issueid__c': 'a03Wt00000JqmX6IAJ'}, {'id': '500Wt00000DDQRsIAP', 'orderitemid__c': '802Wt00000796yFIAQ', 'issueid__c': 'a03Wt00000JqxtvIAB'}], 'var_functions.query_db:12': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000797awIAA', 'OrderId': '801Wt00000PGdVGIA1', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0', 'UnitPrice': '584.991'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '#802Wt00000798VPIAY', 'OrderId': '#801Wt00000PGdjoIAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0', 'UnitPrice': '584.991'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '#802Wt00000799o1IAA', 'OrderId': '#801Wt00000PGoc0IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '19.0', 'UnitPrice': '584.991'}, {'Id': '802Wt0000079A2bIAE', 'OrderId': '801Wt00000PGe00IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '12.0', 'UnitPrice': '584.991'}, {'Id': '802Wt0000079ACGIA2', 'OrderId': '#801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079B6gIAE', 'OrderId': '#801Wt00000PHQz1IAH', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '4.0', 'UnitPrice': '649.99'}], 'var_functions.query_db:14': [{'createddate': '2020-11-05T08:19:00.000+0000', 'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2023-06-30T13:03:00.000+0000', 'id': '500Wt00000DDzsbIAD', 'subject': 'Scalability Problem', 'description': 'I am encountering difficulties in scaling TechPulse solutions to meet the increasing demands of our enterprise which is impacting our expansion efforts.', 'orderitemid__c': '802Wt00000798YdIAI'}, {'createddate': '2020-09-29T01:59:00.000+0000', 'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'orderitemid__c': '802Wt00000796bfIAA'}, {'createddate': '2021-03-07T11:25:00.000+0000', 'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'createddate': '2020-11-09T19:02:00.000+0000', 'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
