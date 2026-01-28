code = """import json
from datetime import datetime

# Load case data from file
with open('/tmp/tmpq8u4i0y2.json', 'r') as f:
    cases_raw = json.load(f)

# Load Product Order Items orderitem ids
product_orderitems = [
    {"Id": "#802Wt0000078yuGIAQ", "OrderId": "801Wt00000PGdVHIA1", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "8.0", "UnitPrice": "617.4905"},
    {"Id": "802Wt00000790mOIAQ", "OrderId": "#801Wt00000PHQuGIAX", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "30.0", "UnitPrice": "552.4915"},
    {"Id": "802Wt00000790zGIAQ", "OrderId": "#801Wt00000PGc9QIAT", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "6.0", "UnitPrice": "617.4905"},
    {"Id": "802Wt00000794F2IAI", "OrderId": "801Wt00000PHLzOIAX", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "2.0", "UnitPrice": "649.99"},
    {"Id": "802Wt000007968eIAA", "OrderId": "801Wt00000PH4FLIA1", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "2.0", "UnitPrice": "649.99"},
    {"Id": "802Wt00000796bfIAA", "OrderId": "801Wt00000PGRh3IAH", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "3.0", "UnitPrice": "649.99"},
    {"Id": "802Wt00000796qFIAQ", "OrderId": "801Wt00000PHRdKIAX", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "7.0", "UnitPrice": "617.4905"},
    {"Id": "802Wt0000079734IAA", "OrderId": "#801Wt00000PGu6KIAT", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "1.0", "UnitPrice": "649.99"},
    {"Id": "802Wt00000797W5IAI", "OrderId": "801Wt00000PHWZlIAP", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "20.0", "UnitPrice": "552.4915"},
    {"Id": "802Wt00000797z7IAA", "OrderId": "801Wt00000PGos9IAD", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "1.0", "UnitPrice": "649.99"},
    {"Id": "802Wt00000798YdIAI", "OrderId": "801Wt00000PH8yvIAD", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "30.0", "UnitPrice": "552.4915"},
    {"Id": "802Wt00000798okIAA", "OrderId": "#801Wt00000PGVJJIA5", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "1.0", "UnitPrice": "649.99"},
    {"Id": "802Wt0000079B0EIAU", "OrderId": "801Wt00000PHHMIIA5", "Product2Id": "01tWt000006hVJdIAM", "Quantity": "6.0", "UnitPrice": "617.4905"}
]

# Extract unique orderitem IDs for SecureAnalytics Pro
secureAnalytics_orderitemids = set()
for item in product_orderitems:
    # Remove leading # if present 
    clean_id = item['Id']
    if clean_id.startswith('#'):
        clean_id = clean_id[1:]
    secureAnalytics_orderitemids.add(clean_id)

print("OrderItem IDs for SecureAnalytics Pro count:", len(secureAnalytics_orderitemids))

# Filter cases for past 10 months from 2021-04-10
# i.e., 2020-06-10 to 2021-04-10 (inclusive)
start_date = datetime(2020, 6, 10)
end_date = datetime(2021, 4, 10)

# Filter and count cases per month per SecureAnalytics
cases_per_month = {}
for case in cases_raw:
    # Parse created date
    created_str = case['createddate']
    try:
        created_dt = datetime.strptime(created_str[:19], '%Y-%m-%dT%H:%M:%S')
    except:
        continue
    
    # Check date range
    if not (start_date <= created_dt <= end_date):
        continue
        
    # Get orderitemid__c and clean it
    orderitemid = case.get('orderitemid__c', '')
    if not orderitemid:
        continue
        
    # Clean orderitemid__c (remove leading # if present)
    if orderitemid.startswith('#'):
        orderitemid = orderitemid[1:]
    
    # Check if this orderitemid is for SecureAnalytics Pro
    if orderitemid in secureAnalytics_orderitemids:
        month_key = created_dt.strftime('%Y-%m')
        month_name = created_dt.strftime('%B')
        cases_per_month[(month_key, month_name)] = cases_per_month.get((month_key, month_name), 0) + 1

# Prepare results
print("Cases per month for SecureAnalytics Pro:")
months_order = []
for (ym, name), count in sorted(cases_per_month.items(), key=lambda x: x[0]):
    print(f"  {name} {ym}: {count}")
    months_order.append((ym, name, count))

# Find month with highest count
if months_order:
    best_month = max(months_order, key=lambda x: x[2])
    print(f"\nMonth with highest cases for SecureAnalytics Pro: {best_month[1]}")
    result = best_month[1]
else:
    print("\nNo matching cases found!")
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}], 'var_functions.list_db:8': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
