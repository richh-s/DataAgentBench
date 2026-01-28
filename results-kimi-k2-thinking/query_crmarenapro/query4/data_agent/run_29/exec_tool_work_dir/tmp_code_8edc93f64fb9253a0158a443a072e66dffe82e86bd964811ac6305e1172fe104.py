code = """import json
import os
import calendar
from datetime import datetime

# SecureAnalytics Pro OrderItem IDs from query
secure_analytics_ids = {
    "802Wt0000078yuGIAQ", "802Wt00000790mOIAQ", "802Wt00000790zGIAQ",
    "802Wt00000794F2IAI", "802Wt000007968eIAA", "802Wt00000796bfIAA",
    "802Wt00000796qFIAQ", "802Wt0000079734IAA", "802Wt00000797W5IAU",
    "802Wt00000797z7IAA", "802Wt00000798YdIAI", "802Wt00000798okIAA",
    "802Wt0000079B0EIAU"
}

# Find the cases data file for query_db:26
import glob
cases_file_path = '/tmp/tmp0d4r7z6z.json'  # Based on the file pattern

if not os.path.exists(cases_file_path):
    print("File not found, trying other locations...")
    temp_files = glob.glob('/tmp/*.json')
    for f in temp_files:
        if os.path.getsize(f) > 1000:  # Look for larger files with data
            cases_file_path = f
            break

print("Loading cases from:", cases_file_path)

with open(cases_file_path, 'r') as f:
    all_cases = json.load(f)

print("Total cases loaded:", len(all_cases))
print("First case:", all_cases[0] if all_cases else "No data")

# Date range: past 10 months from 2021-04-10 (2020-06-10 to 2021-04-10)
start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10)

# Filter and count SecureAnalytics Pro cases
monthly_counts = {}
secure_cases_count = 0

for case in all_cases:
    orderitemid = case.get('orderitemid__c', '') or ''
    clean_id = orderitemid.lstrip('#')
    
    if clean_id in secure_analytics_ids:
        created_str = case['createddate']
        try:
            created_dt = datetime.strptime(created_str[:19], '%Y-%m-%dT%H:%M:%S')
            
            if start_date <= created_dt <= end_date:
                secure_cases_count += 1
                month_key = f"{created_dt.year}-{created_dt.month:02d}"
                monthly_counts[month_key] = monthly_counts.get(month_key, 0) + 1
        except:
            continue

print(f"Found {secure_cases_count} SecureAnalytics Pro cases in range")
print("Monthly counts:", monthly_counts)

if monthly_counts:
    best_month_key = max(monthly_counts, key=monthly_counts.get)
    year, month_num = best_month_key.split('-')
    best_month_name = calendar.month_name[int(month_num)]
    print(f"Best month: {best_month_name} with {monthly_counts[best_month_key]} cases")
    result = best_month_name
else:
    result = None
    print("No cases found")

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}], 'var_functions.list_db:8': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_functions.execute_python:18': {'count': 13}, 'var_functions.query_db:20': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_functions.execute_python:22': None, 'var_functions.execute_python:24': {'status': 'ready'}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
