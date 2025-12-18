code = """import json

quote_line_items = locals()['var_function-call-7500095766134436126']

violations = []

for item in quote_line_items:
    # Clean and convert string values to float, handling potential non-numeric characters like '#' and trailing spaces
    quantity = float(item['Quantity'].strip() if isinstance(item['Quantity'], str) else item['Quantity'])
    unit_price = float(item['UnitPrice'].strip() if isinstance(item['UnitPrice'], str) else item['UnitPrice'])
    discount = float(item['Discount'].strip() if isinstance(item['Discount'], str) else item['Discount'])
    total_price = float(item['TotalPrice'].strip() if isinstance(item['TotalPrice'], str) else item['TotalPrice'])

    calculated_total_price = quantity * unit_price * (1 - discount / 100)

    # Comparing float values with a small tolerance
    if abs(calculated_total_price - total_price) > 0.01:
        violations.append({
            "Id": item["Id"],
            "Product2Id": item["Product2Id"],
            "ExpectedTotalPrice": calculated_total_price,
            "ActualTotalPrice": total_price
        })

print("__RESULT__:")
print(json.dumps(violations))"""

env_args = {'var_function-call-7500095766134436126': [{'Id': '0QLWt0000022j3GOAQ', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}]}

exec(code, env_args)
