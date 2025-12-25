code = """import json

# Load knowledge articles
with open(locals()['var_function-call-6390951173537209928'], 'r') as f:
    articles = json.load(f)

# Product names
products = {
    '01tWt000006hV6jIAE': 'EcoPCB Creator',
    '01tWt000006hV8LIAU': 'AI Cirku-Tech',
    '01tWt000006hPffIAE': 'DevVision IDE',
    '01tWt000006hVczIAE': 'CollabDesign Studio'
}

# Quote items
items = [
    {"Product": "EcoPCB Creator", "Quantity": 3.0, "UnitPrice": 349.99, "Discount": 0.0},
    {"Product": "AI Cirku-Tech", "Quantity": 2.0, "UnitPrice": 529.99, "Discount": 0.0},
    {"Product": "DevVision IDE", "Quantity": 4.0, "UnitPrice": 299.99, "Discount": 0.0},
    {"Product": "CollabDesign Studio", "Quantity": 35.0, "UnitPrice": 399.99, "Discount": 15.0}
]

# Search keywords
keywords = ['EcoPCB', 'Cirku-Tech', 'DevVision', 'CollabDesign', 'Quantity', 'Price', 'Discount', 'Regulation', 'Policy', 'Limit', 'Bundling', 'Setup']

relevant_articles = []

for article in articles:
    text = (article.get('title', '') + ' ' + article.get('faq_answer__c', '') + ' ' + article.get('summary', '')).lower()
    
    score = 0
    matched_keywords = []
    for kw in keywords:
        if kw.lower() in text:
            score += 1
            matched_keywords.append(kw)
    
    if score > 0:
        relevant_articles.append({
            'id': article['id'],
            'title': article['title'],
            'text': text,
            'matched': matched_keywords
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-5966384792397248609': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-6390951173537209928': 'file_storage/function-call-6390951173537209928.json', 'var_function-call-7766566947645911139': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
