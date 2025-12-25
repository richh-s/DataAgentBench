code = """import json
import pandas as pd

# Load knowledge articles
with open(locals()['var_function-call-16727299005270968316'], 'r') as f:
    articles = json.load(f)

# Quote Items for reference
items = [
    {"Product": "EcoPCB Creator", "Qty": 3.0, "Price": 349.99, "Discount": 0.0},
    {"Product": "AI Cirku-Tech", "Qty": 2.0, "Price": 529.99, "Discount": 0.0},
    {"Product": "DevVision IDE", "Qty": 4.0, "Price": 299.99, "Discount": 0.0},
    {"Product": "CollabDesign Studio", "Qty": 35.0, "Price": 399.99, "Discount": 15.0}
]

# Search for relevant articles
relevant_articles = []
keywords = ["discount", "quantity", "price", "limit", "approval", "regulation", "CollabDesign", "EcoPCB", "AI Cirku", "DevVision"]

for article in articles:
    text = (article.get('title', '') + " " + article.get('summary', '') + " " + article.get('faq_answer__c', '')).lower()
    score = 0
    matched_keywords = []
    for k in keywords:
        if k.lower() in text:
            score += 1
            matched_keywords.append(k)
    
    if score > 0:
        relevant_articles.append({
            "id": article['id'],
            "title": article['title'],
            "summary": article['summary'],
            "matches": matched_keywords,
            "text_snippet": article['faq_answer__c'][:200] if article['faq_answer__c'] else ""
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-7104661056634832035': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-7104661056634833984': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-16727299005270966683': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-16727299005270968316': 'file_storage/function-call-16727299005270968316.json'}

exec(code, env_args)
