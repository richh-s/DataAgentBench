code = """import json
import pandas as pd
from datetime import datetime
import pytz

# All SecureAnalytics Pro cases found from both queries
all_secureanalytics_cases = [
    # Direct orderitem matches
    {"id": "500Wt00000DDy8bIAD", "createddate": "2020-11-05T08:19:00.000+0000"},
    {"id": "500Wt00000DDzsbIAD", "createddate": "2023-06-30T13:03:00.000+0000"},
    {"id": "500Wt00000DE00gIAD", "createddate": "2020-09-29T01:59:00.000+0000"},
    {"id": "500Wt00000DE0AMIA1", "createddate": "2021-03-07T11:25:00.000+0000"},
    {"id": "500Wt00000DE0NFIA1", "createddate": "2020-11-09T19:02:00.000+0000"},
    # Subject/description matches
    {"id": "#500Wt00000DDxnbIAD", "createddate": "2021-01-25T09:30:00.000+0000"},
]

# Convert to DataFrame
df = pd.DataFrame(all_secureanalytics_cases)

# Parse dates
df['createddate'] = pd.to_datetime(df['createddate'], utc=True)

# Filter for past 10 months from today's date (2021-04-10)
end_date = datetime(2021, 4, 10, tzinfo=pytz.UTC)
start_date = datetime(2020, 6, 10, tzinfo=pytz.UTC)

df_filtered = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]

# Group by month and count
df_filtered['month'] = df_filtered['createddate'].dt.to_period('M')
monthly_counts = df_filtered.groupby('month').size().sort_index()

# Find the month with maximum cases
max_month = monthly_counts.idxmax()
max_count = monthly_counts.max()

print("__RESULT__:")
print(json.dumps({
    "monthly_counts": str(monthly_counts.to_dict()),
    "max_month": str(max_month),
    "max_count": int(max_count)
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge', 'Description': 'Edge-ready simulation tool for real-time data analytics and verification.'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': '#500Wt00000DDxnbIAD', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.', 'createddate': '2020-11-09T19:02:00.000+0000'}], 'var_functions.execute_python:14': {'monthly_counts': "{Period('2020-09', 'M'): 1, Period('2020-11', 'M'): 2, Period('2021-01', 'M'): 1, Period('2021-03', 'M'): 1}", 'total_cases': 5, 'months_in_range': 4}, 'var_functions.query_db:16': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'OrderId': '801Wt00000PGdVGIA1', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'OrderId': '#801Wt00000PGdjoIAD', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'OrderId': '#801Wt00000PGoc0IAD', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'OrderId': '801Wt00000PGe00IAD', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'OrderId': '#801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'OrderId': '#801Wt00000PHQz1IAH', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_functions.query_db:18': [{'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDzsbIAD', 'subject': 'Scalability Problem', 'description': 'I am encountering difficulties in scaling TechPulse solutions to meet the increasing demands of our enterprise which is impacting our expansion efforts.', 'createddate': '2023-06-30T13:03:00.000+0000', 'orderitemid__c': '802Wt00000798YdIAI'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
