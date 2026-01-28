code = """import json
from datetime import datetime

# Get the cases from storage
cases = var_functions["query_db:18"]

# Count cases by month-month_year
month_counts = {}
for case in cases:
    created_date = case['createddate']
    # Extract month from date string
    date_obj = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
    month_key = date_obj.strftime('%Y-%m')
    
    if month_key in month_counts:
        month_counts[month_key] += 1
    else:
        month_counts[month_key] = 1

# Convert month counts to a list for easier analysis
month_list = []
for month, count in month_counts.items():
    month_list.append({
        'month_year': month,
        'count': count,
        'year': month.split('-')[0],
        'month_num': month.split('-')[1]
    })

# Sort by month
month_list.sort(key=lambda x: x['month_year'])

print('__RESULT__:')
print(json.dumps({
    'month_counts': month_counts,
    'month_list': month_list,
    'total_cases': len(cases)
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:4': [{'id': '500Wt00000DDDtTIAX', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ'}, {'id': '500Wt00000DDPM6IAP', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ'}, {'id': '500Wt00000DDRB2IAP', 'subject': 'AI Cirku-Tech Workflow Lag', 'description': "I'm experiencing latency issues with AI Cirku-Tech when integrating it into our current workflow systems.", 'status': 'Waiting on Customer  ', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA', 'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'id': '500Wt00000DDRVzIAP', 'subject': 'Training Portal Login Problem', 'description': 'The login process for the training modules included with the SecureFlow Suite is causing disruption due to technical glitches, affecting our learning path.', 'status': 'Closed', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ'}, {'id': '500Wt00000DDYpGIAX', 'subject': 'Workflow Integration Lag  ', 'description': 'I am experiencing latency issues when deploying TechPulse solutions within complex existing workflows, causing delays in operations.', 'status': 'Waiting on Customer', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI', 'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'id': '#500Wt00000DDZmsIAH', 'subject': 'Lack of Feature Updates', 'description': 'We are not consistently notified about new feature updates in the DesignWave Automation tool, causing us to miss out on utilizing its full capabilities.', 'status': 'Closed', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI', 'issueid__c': 'a03Wt00000JqzSfIAJ'}, {'id': '500Wt00000DDeoCIAT', 'subject': 'Integration Lag Issue', 'description': 'I have been experiencing latency issues when deploying the AI Cirku-Tech platform within our complex workflows, and it is hindering our productivity.', 'status': 'Waiting on Customer', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ', 'issueid__c': 'a03Wt00000JqzR3IAJ'}, {'id': '#500Wt00000DDfvXIAT', 'subject': 'Data Integration Error', 'description': 'I am experiencing challenges when integrating TechPulse solutions with specific third-party software, leading to workflow disruptions.', 'status': 'Waiting on Customer', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ', 'issueid__c': 'a03Wt00000JqzKcIAJ'}, {'id': '#500Wt00000DDg8QIAT', 'subject': 'Feature Updates Not Communicated', 'description': "I'm finding it difficult to keep up with the latest improvements in SecureFlow Suite as update alerts are not always received.", 'status': 'Closed ', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ'}, {'id': '500Wt00000DDsG4IAL', 'subject': 'Cannot Access Training Resources', 'description': 'I am facing occasional difficulties accessing the training resources necessary for gaining proficiency with PulseSim Pro.', 'status': 'Working', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU', 'issueid__c': 'a03Wt00000JqvNUIAZ'}], 'var_functions.list_db:6': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.list_db:8': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:10': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}], 'var_functions.query_db:12': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_functions.query_db:18': [{'id': '500Wt00000DDy8bIAD', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them.", 'status': 'Closed', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards.", 'status': 'Waiting on Customer', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.', 'status': 'Closed', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.', 'status': 'Closed', 'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
