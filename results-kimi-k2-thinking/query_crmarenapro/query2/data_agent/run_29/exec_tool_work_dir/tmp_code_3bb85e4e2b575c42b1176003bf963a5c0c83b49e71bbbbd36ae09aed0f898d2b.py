code = """import json

# Load the quote data
quote_data = [{"Id": "0Q0Wt000001WSDVKA4", "OpportunityId": "#006Wt000007BHHfIAO", "AccountId": "#001Wt00000PGXrKIAX", "ContactId": "003Wt00000JqkgYIAR", "Name": "TechPulse-InnovateX Integration Quote", "Description": "Initial quote for AI-powered EDA solutions integration", "Status": "Needs Review", "CreatedDate": "2021-06-01T10:00:00.000+0000", "ExpirationDate": "2021-07-01"}]

# Load the quote line items
quote_line_items = [
    {"Id": "0QLWt0000022yNAOAY", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HavbIAC", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": "8.0", "UnitPrice": "349.99", "Discount": "15.0", "TotalPrice": "2379.932"},
    {"Id": "0QLWt0000022z7tOAA", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HXg4IAG", "Product2Id": "01tWt000006hV57IAE", "PricebookEntryId": "01uWt0000027P3lIAE", "Quantity": "10.0", "UnitPrice": "499.99", "Discount": "10.0", "TotalPrice": "4499.91"},
    {"Id": "0QLWt0000022z9VOAQ", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HL76IAG", "Product2Id": "#01tWt000006hVQ5IAM", "PricebookEntryId": "01uWt0000027PVBIA2", "Quantity": "7.0", "UnitPrice": "339.99", "Discount": "5.0", "TotalPrice": "2260.9335"}
]

# Calculate totals
subtotal = sum(float(item['TotalPrice']) for item in quote_line_items)
total_discounts = []
for item in quote_line_items:
    quantity = float(item['Quantity'])
    unit_price = float(item['UnitPrice'])
    discount_percent = float(item['Discount'])
    line_subtotal = quantity * unit_price
    line_discount = line_subtotal * (discount_percent / 100)
    total_discounts.append(line_discount)
    
total_discount = sum(total_discounts)

print("__RESULT__:")
print(json.dumps({
    "quote_id": quote_data[0]['Id'],
    "status": quote_data[0]['Status'],
    "total_amount": round(subtotal, 2),
    "total_discount": round(total_discount, 2),
    "line_items": [
        {
            "product_id": item['Product2Id'],
            "quantity": float(item['Quantity']),
            "unit_price": float(item['UnitPrice']),
            "discount_percent": float(item['Discount']),
            "total_price": float(item['TotalPrice'])
        } for item in quote_line_items
    ]
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
