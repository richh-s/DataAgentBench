code = """import json
from datetime import datetime

# Access the data from storage
orderitems = locals()['var_functions.query_db:8']
orders = locals()['var_functions.query_db:12']
cases = locals()['var_functions.query_db:14']

# Clean IDs (remove leading # and trailing whitespace)
def clean_id(id_str):
    if not id_str:
        return id_str
    cleaned = id_str.strip()
    if cleaned.startswith('#'):
        cleaned = cleaned[1:]
    return cleaned

# Clean OrderItem IDs
orderitem_ids = [clean_id(item['Id']) for item in orderitems]

# Filter cases within the date range (June 2020 - April 2021)
start_date = datetime(2020, 6, 1)
end_date = datetime(2021, 4, 30)

# Process cases and count by month
cases_by_month = {}

for case in cases:
    case_orderitem_id = clean_id(case['orderitemid__c'])
    
    # Check if this case's orderitem_id is in our list of orderitems for the product
    if case_orderitem_id in orderitem_ids:
        created_date = datetime.strptime(case['createddate'][:10], '%Y-%m-%d')
        month_key = created_date.strftime('%Y-%m')
        cases_by_month[month_key] = cases_by_month.get(month_key, 0) + 1

# Sort by month
sorted_months = sorted(cases_by_month.items())

# Convert to more readable format and check for anomalies
readable_months = []
for month, count in sorted_months:
    year, month_num = month.split('-')
    month_name = datetime(int(year), int(month_num), 1).strftime('%B %Y')
    readable_months.append((month_name, count))

print('__RESULT__:')
print(json.dumps({
    'cases_by_month': sorted_months,
    'readable_cases': readable_months,
    'total_cases': sum(cases_by_month.values())
}))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:4': [{'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}], 'var_functions.list_db:6': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:8': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGdVHIA1', 'Quantity': '8.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PHQuGIAX', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGc9QIAT', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHLzOIAX', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PH4FLIA1', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGRh3IAH', 'Quantity': '3.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHRdKIAX', 'Quantity': '7.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGu6KIAT', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHWZlIAP', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGos9IAD', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PH8yvIAD', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGVJJIA5', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHHMIIA5', 'Quantity': '6.0', 'UnitPrice': '617.4905'}], 'var_functions.query_db:12': [{'Id': '801Wt00000PGRh3IAH', 'EffectiveDate': '2020-07-01'}, {'Id': '#801Wt00000PGVJJIA5', 'EffectiveDate': '2024-07-25'}, {'Id': '#801Wt00000PGc9QIAT', 'EffectiveDate': '2021-09-10'}, {'Id': '801Wt00000PGdVHIA1', 'EffectiveDate': '2023-03-15'}, {'Id': '801Wt00000PGos9IAD', 'EffectiveDate': '2021-10-20'}, {'Id': '801Wt00000PH4FLIA1', 'EffectiveDate': '2023-12-05'}, {'Id': '801Wt00000PH8yvIAD', 'EffectiveDate': '2022-07-01'}, {'Id': '801Wt00000PHHMIIA5', 'EffectiveDate': '2020-12-20'}, {'Id': '801Wt00000PHLzOIAX', 'EffectiveDate': '2020-12-01'}, {'Id': '801Wt00000PHRdKIAX', 'EffectiveDate': '2020-10-01'}, {'Id': '801Wt00000PHWZlIAP', 'EffectiveDate': '2022-12-15'}], 'var_functions.query_db:14': [{'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}]}

exec(code, env_args)
