code = """import json
import pandas as pd
from datetime import datetime

# Load the SecureAnalytics cases data
secureanalytics_cases = [
    {"id": "#500Wt00000DDxnbIAD", "subject": "ROI Metrics Clarification  ", "description": "I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.", "createddate": "2021-01-25T09:30:00.000+0000"},
    {"id": "500Wt00000DDy8bIAD", "subject": "Update Alerts Absent", "description": "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", "createddate": "2020-11-05T08:19:00.000+0000"},
    {"id": "500Wt00000DE00gIAD", "subject": "SecureAnalytics Compliance Concern", "description": "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", "createddate": "2020-09-29T01:59:00.000+0000"},
    {"id": "500Wt00000DE0AMIA1", "subject": "No Feature Update Notices", "description": "I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.", "createddate": "2021-03-07T11:25:00.000+0000"},
    {"id": "500Wt00000DE0NFIA1", "subject": "Missing Feature Notifications", "description": "I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.", "createddate": "2020-11-09T19:02:00.000+0000"}
]

# Convert to DataFrame
df = pd.DataFrame(secureanalytics_cases)

# Parse dates
df['createddate'] = pd.to_datetime(df['createddate'])

# Filter for past 10 months from today's date (2021-04-10)
end_date = datetime(2021, 4, 10)
start_date = datetime(2020, 6, 10)  # 10 months before

df_filtered = df[(df['createddate'] >= start_date) & (df['createddate'] <= end_date)]

# Group by month and count
df_filtered['month'] = df_filtered['createddate'].dt.to_period('M')
monthly_counts = df_filtered.groupby('month').size().sort_index()

print("__RESULT__:")
print(json.dumps({
    "monthly_counts": monthly_counts.to_dict(),
    "total_cases": len(df_filtered),
    "months_in_range": len(monthly_counts)
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge', 'Description': 'Edge-ready simulation tool for real-time data analytics and verification.'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': '#500Wt00000DDxnbIAD', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.', 'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
