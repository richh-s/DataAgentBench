code = """import json

# Read the full result from the JSON file
full_result_path = var_functions.query_db:2
with open(full_result_path, 'r') as file:
    cases = json.load(file)

# For debugging, let's first count the total number of cases we have
print("Total cases loaded:", len(cases))

# Now let's filter cases that are related to the specific product
# Product ID: 01tWt000006hVJdIAM
product_id = "01tWt000006hVJdIAM"

# First, get all OrderItem IDs for this product
order_items_path = "var_functions.query_db:0"
with open(order_items_path.replace("var_", ""), 'r') as file:
    order_items = json.load(file)

product_orderitem_ids = [item['Id'] for item in order_items]
print("OrderItem IDs for product:", len(product_orderitem_ids))
print("Sample OrderItem IDs:", product_orderitem_ids[:5])

# Filter cases where orderitemid__c matches our product's order items
# Also handle potential data corruption (leading # and trailing whitespace)
clean_orderitem_ids = []
for oid in product_orderitem_ids:
    clean_id = oid.lstrip('#').strip()
    clean_orderitem_ids.append(clean_id)

# Filter cases
cases_with_product = []
for case in cases:
    case_orderitem_id = str(case.get('orderitemid__c', '')).lstrip('#').strip()
    if case_orderitem_id in clean_orderitem_ids:
        cases_with_product.append(case)

print("Cases related to the product:", len(cases_with_product))

# Extract months from created dates
from datetime import datetime

month_counts = {}
for case in cases_with_product:
    created_date = case.get('createddate')
    if created_date:
        try:
            # Parse the date string
            date_obj = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
            month_key = date_obj.strftime('%Y-%m')  # e.g., '2021-07'
            month_name = date_obj.strftime('%B')    # e.g., 'July'
            
            if month_key not in month_counts:
                month_counts[month_key] = {'count': 0, 'name': month_name}
            month_counts[month_key]['count'] += 1
        except Exception as e:
            print(f"Error parsing date {created_date}: {e}")

# Sort by month
sorted_months = sorted(month_counts.items(), key=lambda x: x[0])
print("\nMonth counts for SecureAnalytics Pro:")
for month_key, data in sorted_months:
    print(f"{month_key} ({data['name']}): {data['count']} cases")

# Identify significant months (e.g., more than 2x average)
if month_counts:
    counts = [data['count'] for data in month_counts.values()]
    avg_count = sum(counts) / len(counts)
    max_count = max(counts)
    
    print(f"\nAverage cases per month: {avg_count:.2f}")
    print(f"Maximum cases in a month: {max_count}")
    
    # Find months with significantly more cases (> 1.5x average)
    significant_months = []
    for month_key, data in month_counts.items():
        if data['count'] > avg_count * 1.5:
            significant_months.append((month_key, data['name'], data['count']))
    
    print(f"Significant months (>1.5x avg): {significant_months}")
    
    # Return the month with highest count if it exceeds avg by significant margin
    if max_count > avg_count * 1.5:
        max_month = max(month_counts.items(), key=lambda x: x[1]['count'])
        result = max_month[1]['name']
    else:
        result = "No significant month found"
else:
    result = "No cases found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
