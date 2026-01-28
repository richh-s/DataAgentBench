code = """import json
import os

# Load the quote line items from the database
quote_line_items = [
    {"Id": "0QLWt0000022j3GOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HUwhIAG", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": "3.0", "UnitPrice": "349.99", "Discount": "0.0", "TotalPrice": "1049.97"},
    {"Id": "0QLWt0000022j81OAA", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HHRkIAO", "Product2Id": "01tWt000006hV8LIAU", "PricebookEntryId": "01uWt0000027P8cIAE", "Quantity": "2.0", "UnitPrice": "529.99", "Discount": "0.0", "TotalPrice": "1059.98"},
    {"Id": "0QLWt0000022n8TOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJYIA4", "Product2Id": "#01tWt000006hPffIAE", "PricebookEntryId": "01uWt0000027PADIA2", "Quantity": "4.0", "UnitPrice": "299.99", "Discount": "0.0", "TotalPrice": "1199.96"},
    {"Id": "#0QLWt0000022oAvOAI", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJZIA4", "Product2Id": "01tWt000006hVczIAE", "PricebookEntryId": "01uWt0000027Pi5IAE", "Quantity": "35.0", "UnitPrice": "399.99", "Discount": "15.0", "TotalPrice": "11899.7025"}
]

# Check for corrupted IDs (leading #)
corrupted_fields = []
violated_articles = []

for item in quote_line_items:
    # Check Product2Id for corruption
    if item['Product2Id'].startswith('#'):
        corrupted_fields.append(f"Product2Id: {item['Product2Id']}")
    
    # Check QuoteLineItem Id for corruption
    if item['Id'].startswith('#'):
        corrupted_fields.append(f"QuoteLineItemId: {item['Id']}")

print("__RESULT__:")
print(json.dumps({
    "corrupted_fields": corrupted_fields,
    "number_of_corruptions": len(corrupted_fields)
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
