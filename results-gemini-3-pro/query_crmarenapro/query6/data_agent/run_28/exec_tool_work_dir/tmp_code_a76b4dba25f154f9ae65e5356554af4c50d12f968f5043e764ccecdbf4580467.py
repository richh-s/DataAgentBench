code = """import json
import re

# Load knowledge articles
with open(locals()['var_function-call-5779811584283906500'], 'r') as f:
    articles = json.load(f)

# Quote Line Items Info
items = [
    {"Product": "EcoPCB Creator", "Quantity": 3.0, "UnitPrice": 349.99, "Discount": 0.0},
    {"Product": "AI Cirku-Tech", "Quantity": 2.0, "UnitPrice": 529.99, "Discount": 0.0},
    {"Product": "DevVision IDE", "Quantity": 4.0, "UnitPrice": 299.99, "Discount": 0.0},
    {"Product": "CollabDesign Studio", "Quantity": 35.0, "UnitPrice": 399.99, "Discount": 15.0}
]

# Keywords to search
keywords = ["EcoPCB", "AI Cirku-Tech", "DevVision", "CollabDesign", "quantity", "limit", "price", "discount", "regulation", "policy", "invalid", "config"]

relevant_articles = []

for article in articles:
    text = (article.get('title', '') + ' ' + article.get('summary', '') + ' ' + article.get('faq_answer__c', '')).lower()
    
    score = 0
    matches = []
    # Check for product names
    for item in items:
        prod_name = item["Product"].lower()
        if prod_name in text:
            score += 1
            matches.append(item["Product"])
            
    # Check for policy keywords
    if "regulation" in text or "policy" in text or "limit" in text:
        score += 1
        matches.append("policy/limit")

    if score > 0:
        relevant_articles.append({
            "id": article['id'],
            "title": article['title'],
            "matches": matches,
            "summary": article['summary']
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-5779811584283909379': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-5779811584283906500': 'file_storage/function-call-5779811584283906500.json', 'var_function-call-10824156375473959546': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
