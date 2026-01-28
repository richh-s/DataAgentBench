code = """import json

# Get cases data
cases_data = var_functions.query_db:2
if isinstance(cases_data, str) and cases_data.endswith('.json'):
    with open(cases_data, 'r') as f:
        cases = json.load(f)
else:
    cases = cases_data

print("Total cases loaded:", len(cases))

# Get order items for the product
order_items = var_functions.query_db:0
orderitem_ids = []
for item in order_items:
    oid = str(item.get('Id', ''))
    clean_oid = oid.lstrip('#').strip()
    orderitem_ids.append(clean_oid)

orderitem_set = set(orderitem_ids)
print("OrderItem IDs for product:", len(orderitem_set))

# Filter cases that match the product
product_cases = []
for case in cases:
    case_oid = str(case.get('orderitemid__c', '')).lstrip('#').strip()
    if case_oid in orderitem_set:
        product_cases.append(case)

print("Cases related to SecureAnalytics Pro:", len(product_cases))

# Count cases by month
from datetime import datetime
month_counts = {}

for case in product_cases:
    created_date = case.get('createddate')
    if created_date:
        try:
            date_str = str(created_date).replace('Z', '+00:00')
            date_obj = datetime.fromisoformat(date_str)
            month_key = date_obj.strftime('%Y-%m')
            month_name = date_obj.strftime('%B')
            
            if month_key not in month_counts:
                month_counts[month_key] = {'count': 0, 'name': month_name}
            month_counts[month_key]['count'] += 1
        except:
            pass

print("\nMonth counts:")
sorted_months = sorted(month_counts.items(), key=lambda x: x[0])
for month_key, data in sorted_months:
    print(f"{month_key}: {data['count']} cases")

result = "No significant month found"
if month_counts:
    counts = [data['count'] for data in month_counts.values()]
    if counts:
        avg_count = sum(counts) / len(counts)
        max_month = max(month_counts.items(), key=lambda x: x[1]['count'])
        
        print(f"\nAverage: {avg_count:.2f}")
        print(f"Max month: {max_month[1]['name']} with {max_month[1]['count']} cases")
        
        if max_month[1]['count'] > avg_count * 1.5:
            result = max_month[1]['name']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
