code = """import json

# Load the knowledge articles from the previous result
file_path = locals()['var_function-call-10080377942361059663']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Search terms
products = ["EcoPCB Creator", "AI Cirku-Tech", "DevVision IDE", "CollabDesign Studio"]
keywords = ["quantity", "limit", "price", "discount", "regulation", "policy", "setup", "config", "invalid"]

relevant_articles = []

for article in articles:
    text = (article.get('title') or "") + " " + (article.get('summary') or "") + " " + (article.get('faq_answer__c') or "")
    text_lower = text.lower()
    
    # Check if any product name is in the text
    found_product = any(p.lower().strip() in text_lower for p in products)
    
    # Check if any keyword is in the text
    found_keyword = any(k in text_lower for k in keywords)
    
    if found_product or found_keyword:
        relevant_articles.append(article)

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-10080377942361061408': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-10080377942361059663': 'file_storage/function-call-10080377942361059663.json', 'var_function-call-10452825471536214684': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-10452825471536217877': []}

exec(code, env_args)
