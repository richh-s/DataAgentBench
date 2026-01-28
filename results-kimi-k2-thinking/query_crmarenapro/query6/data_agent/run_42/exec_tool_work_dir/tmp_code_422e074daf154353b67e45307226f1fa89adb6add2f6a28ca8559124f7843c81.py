code = """import json
import pandas as pd

# Load all quote line items for the quote in question
quote_id = "#0Q0Wt000001WRAzKAO"
quote_line_items = [
    {"Id": "0QLWt0000022j3GOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": "3.0", "UnitPrice": "349.99", "Discount": "0.0", "TotalPrice": "1049.97"},
    {"Id": "0QLWt0000022j81OAA", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "01tWt000006hV8LIAU", "PricebookEntryId": "01uWt0000027P8cIAE", "Quantity": "2.0", "UnitPrice": "529.99", "Discount": "0.0", "TotalPrice": "1059.98"},
    {"Id": "0QLWt0000022n8TOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "#01tWt000006hPffIAE", "PricebookEntryId": "01uWt0000027PADIA2", "Quantity": "4.0", "UnitPrice": "299.99", "Discount": "0.0", "TotalPrice": "1199.96"},
    {"Id": "#0QLWt0000022oAvOAI", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "01tWt000006hVczIAE", "PricebookEntryId": "01uWt0000027Pi5IAE", "Quantity": "35.0", "UnitPrice": "399.99", "Discount": "15.0", "TotalPrice": "11899.7025"}
]

# Load the knowledge articles from the file
with open('var_functions.query_db:14.json', 'r') as f:
    knowledge_articles = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "quote_line_items": quote_line_items,
    "knowledge_articles_preview": len(knowledge_articles)
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#0Q0Wt000001WRAzKAO'}], 'var_functions.query_db:5': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Id': '0QLWt0000022abqOAA', 'QuoteId': '0Q0Wt000001WKe9KAG', 'Product2Id': '#01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '6.0', 'UnitPrice': '599.99', 'Discount': '5.0', 'TotalPrice': '3419.943'}, {'Id': '0QLWt0000022cHnOAI', 'QuoteId': '#0Q0Wt000001WLwnKAG', 'Product2Id': '01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '7.0', 'UnitPrice': '349.99', 'Discount': '5.0', 'TotalPrice': '2327.4335'}, {'Id': '#0QLWt0000022cHoOAI', 'QuoteId': '0Q0Wt000001WQutKAG', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '3.0', 'UnitPrice': '599.99', 'Discount': '0.0', 'TotalPrice': '1799.97'}, {'Id': '0QLWt0000022cw9OAA', 'QuoteId': '0Q0Wt000001WSIMKA4', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '10.0', 'UnitPrice': '529.99', 'Discount': '10.0', 'TotalPrice': '4769.91'}, {'Id': '0QLWt0000022cwAOAQ', 'QuoteId': '0Q0Wt000001WSevKAG', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '20.0', 'UnitPrice': '599.99', 'Discount': '20.0', 'TotalPrice': '9599.84'}], 'var_functions.query_db:10': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:12': [{'Id': '#00kWt000002HHRkIAO', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'TotalPrice': '1059.98'}, {'Id': '00kWt000002HQJYIA4', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'TotalPrice': '1199.96'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
