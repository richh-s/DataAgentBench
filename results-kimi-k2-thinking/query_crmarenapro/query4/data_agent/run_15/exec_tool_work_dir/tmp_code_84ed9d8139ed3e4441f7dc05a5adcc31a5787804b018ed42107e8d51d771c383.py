code = """import json
from datetime import datetime

# Get the cases data
cases_data = [
    {"id": "500Wt00000DDy8bIAD", "createddate": "2020-11-05T08:19:00.000+0000", "orderitemid__c": "802Wt00000796qFIAQ"},
    {"id": "500Wt00000DDzsbIAD", "createddate": "2023-06-30T13:03:00.000+0000", "orderitemid__c": "802Wt00000798YdIAI"},
    {"id": "500Wt00000DE00gIAD", "createddate": "2020-09-29T01:59:00.000+0000", "orderitemid__c": "802Wt00000796bfIAA"},
    {"id": "500Wt00000DE0AMIA1", "createddate": "2021-03-07T11:25:00.000+0000", "orderitemid__c": "802Wt00000796qFIAQ"},
    {"id": "500Wt00000DE0NFIA1", "createddate": "2020-11-09T19:02:00.000+0000", "orderitemid__c": "802Wt00000796qFIAQ"}
]

today = datetime(2021, 4, 10)
# Calculate 10 months ago
ten_months_ago = datetime(2020, 6, 10)

# Filter cases within the past 10 months
filtered_cases = []
for case in cases_data:
    created_date = datetime.strptime(case['createddate'].split('T')[0], '%Y-%m-%d')
    if ten_months_ago <= created_date <= today:
        filtered_cases.append(case)

# Group by month and count
case_counts = {}
for case in filtered_cases:
    created_date = datetime.strptime(case['createddate'].split('T')[0], '%Y-%m-%d')
    month = created_date.strftime('%Y-%m')
    month_name = created_date.strftime('%B')
    if month in case_counts:
        case_counts[month]['count'] += 1
    else:
        case_counts[month] = {'count': 1, 'month_name': month_name}

# Sort by count descending
sorted_counts = sorted(case_counts.items(), key=lambda x: x[1]['count'], reverse=True)

result = {
    'filtered_cases': filtered_cases,
    'case_counts_by_month': sorted_counts,
    'total_months': len(sorted_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}], 'var_functions.query_db:5': [{'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDzsbIAD', 'createddate': '2023-06-30T13:03:00.000+0000', 'orderitemid__c': '802Wt00000798YdIAI'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
