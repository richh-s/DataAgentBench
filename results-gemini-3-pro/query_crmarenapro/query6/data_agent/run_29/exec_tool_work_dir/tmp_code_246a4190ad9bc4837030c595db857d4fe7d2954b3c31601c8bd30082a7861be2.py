code = """import json

# Load knowledge articles
with open(locals()['var_function-call-12735342974928334249'], 'r') as f:
    articles = json.load(f)

# Quote items for context
items = [
    {"Name": "DevVision IDE", "Quantity": 4.0},
    {"Name": "EcoPCB Creator", "Quantity": 3.0},
    {"Name": "AI Cirku-Tech", "Quantity": 2.0},
    {"Name": "CollabDesign Studio", "Quantity": 35.0, "Discount": 15.0}
]

relevant_articles = []
keywords = ["quantity", "limit", "maximum", "minimum", "discount", "regulation", "policy", "bundle", "invalid", "config", "CollabDesign", "EcoPCB", "DevVision", "Cirku-Tech"]

for art in articles:
    text = (art.get('title', '') + " " + art.get('summary', '') + " " + art.get('faq_answer__c', '')).lower()
    score = 0
    for k in keywords:
        if k.lower() in text:
            score += 1
    
    if score > 0:
        relevant_articles.append({
            "Id": art['id'],
            "Title": art['title'],
            "Summary": art['summary'],
            "Score": score
        })

# Sort by score
relevant_articles.sort(key=lambda x: x['Score'], reverse=True)

print("__RESULT__:")
print(json.dumps(relevant_articles[:5]))"""

env_args = {'var_function-call-12735342974928333858': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-12735342974928334249': 'file_storage/function-call-12735342974928334249.json', 'var_function-call-2171136559389802045': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
