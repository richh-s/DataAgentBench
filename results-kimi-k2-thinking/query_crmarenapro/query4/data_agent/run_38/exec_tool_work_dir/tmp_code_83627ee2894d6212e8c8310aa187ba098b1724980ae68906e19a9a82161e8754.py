code = """import json
import re
from datetime import datetime

# Get the OrderItem data from storage
order_items = locals()['var_functions.query_db:0']

# Extract OrderItem IDs
case_ids = []
for item in order_items:
    order_id = item['Id'].strip()
    if order_id.startswith('#'):
        order_id = order_id[1:]
    case_ids.append(order_id)

# Print the IDs to construct the query
print("OrderItem IDs:", case_ids)
print("Number of IDs:", len(case_ids))

# Build WHERE clause
where_clause = "TRIM(REPLACE(orderitemid__c, '#', '')) IN ("
for i, oid in enumerate(case_ids):
    if i > 0:
        where_clause += ", "
    where_clause += f"'{oid}'"
where_clause += ")"

print("WHERE clause:", where_clause)

result = where_clause
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_functions.query_db:2': [{'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'status': 'Closed', 'createddate': '2020-11-05T08:19:00.000+0000', 'closeddate': '2020-11-05T08:50:10.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDzsbIAD', 'subject': 'Scalability Problem', 'status': 'Closed', 'createddate': '2023-06-30T13:03:00.000+0000', 'closeddate': '2023-06-30T19:03:08.000+0000', 'orderitemid__c': '802Wt00000798YdIAI'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'status': 'Waiting on Customer', 'createddate': '2020-09-29T01:59:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'status': 'Closed', 'createddate': '2021-03-07T11:25:00.000+0000', 'closeddate': '2021-03-07T17:46:52.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'status': 'Closed', 'createddate': '2020-11-09T19:02:00.000+0000', 'closeddate': '2020-11-10T09:47:54.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
