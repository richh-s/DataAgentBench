code = """import json

# Get cases data
cases_data = var_functions.query_db:2
if isinstance(cases_data, str):
    with open(cases_data, 'r') as f:
        cases = json.load(f)
else:
    cases = cases_data

print("Total cases:", len(cases))

# Get order items
order_items = var_functions.query_db:0
orderitem_set = set()
for item in order_items:
    oid = str(item.get('Id', '')).lstrip('#').strip()
    orderitem_set.add(oid)

print("OrderItems for product:", len(orderitem_set))

# Filter cases for this product
product_cases = []
for case in cases:
    case_oid = str(case.get('orderitemid__c', '')).lstrip('#').strip()
    if case_oid in orderitem_set:
        product_cases.append(case)

print("Product cases:", len(product_cases))

# Count by month
from datetime import datetime
month_counts = {}

for case in product_cases:
    created = case.get('createddate')
    if created:
        try:
            date_str = str(created).replace('Z', '+00:00')
            date_obj = datetime.fromisoformat(date_str)
            month_key = date_obj.strftime('%Y-%m')
            month_name = date_obj.strftime('%B')
            
            if month_key not in month_counts:
                month_counts[month_key] = {'count': 0, 'name': month_name}
            month_counts[month_key]['count'] += 1
        except:
            pass

print("Month counts:")
for month in sorted(month_counts.keys()):
    print(month, month_counts[month]['name'], month_counts[month]['count'])

result = "No significant month found"
if month_counts:
    counts = [m['count'] for m in month_counts.values()]
    
    avg = sum(counts) / len(counts)
    max_month = max(month_counts.items(), key=lambda x: x[1]['count'])
    
    print("Average:", avg)
    print("Max:", max_month[1]['name'], max_month[1]['count'])
    
    if max_month[1]['count'] > avg * 1.5:
        result = max_month[1]['name']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
