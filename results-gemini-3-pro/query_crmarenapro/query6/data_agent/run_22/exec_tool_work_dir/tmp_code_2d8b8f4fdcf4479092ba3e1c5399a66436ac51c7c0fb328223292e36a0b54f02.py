code = """import json

# Load knowledge articles
with open(locals()['var_function-call-12129349867753295834'], 'r') as f:
    articles = json.load(f)

# Quote Line Items (from previous result)
items = [
    {"Id": "0QLWt0000022j3GOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "#01tWt000006hV6jIAE", "Quantity": 3.0, "UnitPrice": 349.99, "Discount": 0.0},
    {"Id": "0QLWt0000022j81OAA", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "01tWt000006hV8LIAU", "Quantity": 2.0, "UnitPrice": 529.99, "Discount": 0.0},
    {"Id": "0QLWt0000022n8TOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "#01tWt000006hPffIAE", "Quantity": 4.0, "UnitPrice": 299.99, "Discount": 0.0},
    {"Id": "#0QLWt0000022oAvOAI", "QuoteId": "0Q0Wt000001WRAzKAO", "Product2Id": "01tWt000006hVczIAE", "Quantity": 35.0, "UnitPrice": 399.99, "Discount": 15.0}
]

# Search for relevant articles
keywords = ["discount", "quantity", "limit", "approval", "policy", "regulation", "invalid", "price"]
relevant_articles = []

for art in articles:
    text = (art.get('title', '') + ' ' + art.get('summary', '') + ' ' + art.get('faq_answer__c', '')).lower()
    if any(k in text for k in keywords):
        relevant_articles.append({
            "id": art['id'], 
            "title": art['title'], 
            "summary": art['summary']
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-12129349867753292736': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-12129349867753292237': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-12129349867753295834': 'file_storage/function-call-12129349867753295834.json'}

exec(code, env_args)
