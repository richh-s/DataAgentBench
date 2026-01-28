code = """import json
from datetime import datetime
from collections import Counter

# Load data
cases_data = locals()['var_functions.query_db:5']
order_items_result = locals()['var_functions.query_db:7']

# Extract OrderItem IDs for SecureAnalytics Pro (strip #)
secure_analytics_order_item_ids = []
for item in order_items_result:
    item_id = item['Id'].lstrip('#')
    secure_analytics_order_item_ids.append(item_id)

print('Found SecureAnalytics Pro OrderItem IDs:', len(secure_analytics_order_item_ids))
print('First few IDs:', secure_analytics_order_item_ids[:5])

# Filter cases that are for SecureAnalytics Pro
secure_analytics_cases = []
for case in cases_data:
    case_orderitem_id = case['orderitemid__c'].lstrip('#')
    if case_orderitem_id in secure_analytics_order_item_ids:
        secure_analytics_cases.append(case)

print('\nTotal cases for SecureAnalytics Pro:', len(secure_analytics_cases))

# Extract months from createddate
month_counts = Counter()
for case in secure_analytics_cases:
    created_date = case['createddate']
    # Parse the date and extract month
    date_obj = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
    month_name = date_obj.strftime('%B')
    month_counts[month_name] += 1

print('\nSecureAnalytics Pro cases by month:')
for month, count in sorted(month_counts.items(), key=lambda x: list(month_counts.keys()).index(x[0])):
    print(f'{month}: {count}')

# Find month with most cases
if month_counts:
    max_month = max(month_counts, key=month_counts.get)
    max_count = month_counts[max_month]
    print(f'\nMonth with most cases: {max_month} ({max_count} cases)')
    
    print('__RESULT__:')
    print(json.dumps({
        'secure_analytics_case_count': len(secure_analytics_cases),
        'monthly_distribution': dict(month_counts),
        'max_month': max_month,
        'max_count': max_count
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No SecureAnalytics Pro cases found'}))"""

env_args = {'var_functions.list_db:2': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:5': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_functions.query_db:7': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_functions.execute_python:10': {'order_item_ids': ['802Wt0000078yuGIAQ', '802Wt00000790mOIAQ', '802Wt00000790zGIAQ', '802Wt00000794F2IAI', '802Wt000007968eIAA', '802Wt00000796bfIAA', '802Wt00000796qFIAQ', '802Wt0000079734IAA', '802Wt00000797W5IAI', '802Wt00000797z7IAA', '802Wt00000798YdIAI', '802Wt00000798okIAA', '802Wt0000079B0EIAU'], 'count': 13}}

exec(code, env_args)
