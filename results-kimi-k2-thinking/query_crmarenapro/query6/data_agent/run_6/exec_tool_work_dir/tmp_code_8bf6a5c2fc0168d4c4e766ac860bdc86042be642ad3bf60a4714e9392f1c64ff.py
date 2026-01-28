code = """import json

# Analyze the quote line items to identify violations
quote_line_items = [
    {"Id": "0QLWt0000022j3GOAQ", "Quantity": 3.0, "UnitPrice": 349.99, "Discount": 0.0, "TotalPrice": 1049.97},
    {"Id": "0QLWt0000022j81OAA", "Quantity": 2.0, "UnitPrice": 529.99, "Discount": 0.0, "TotalPrice": 1059.98},
    {"Id": "0QLWt0000022n8TOAQ", "Quantity": 4.0, "UnitPrice": 299.99, "Discount": 0.0, "TotalPrice": 1199.96},
    {"Id": "#0QLWt0000022oAvOAI", "Quantity": 35.0, "UnitPrice": 399.99, "Discount": 15.0, "TotalPrice": 11899.7025}
]

# Check for violations based on volume discount policy
violations = []
for item in quote_line_items:
    total_price = item['TotalPrice']
    discount = item['Discount']
    
    # According to policy: 15% discount for purchases over $20
    if total_price >= 20 and discount < 15:
        violations.append({
            'item_id': item['Id'],
            'total_price': total_price,
            'current_discount': discount,
            'required_discount': 15,
            'violation': f'Item {item["Id"]} with total price ${total_price} should have 15% discount but has {discount}%'
        })

print('__RESULT__:')
print(json.dumps(violations, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
