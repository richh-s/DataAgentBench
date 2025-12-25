code = """import json

file_path = locals()['var_function-call-581561251775652489']
with open(file_path, 'r') as f:
    articles = json.load(f)

keywords = ["collabdesign", "discount", "quantity", "price", "limit", "bundle", "regulation", "invalid", "setup", "policy"]
product_ids = ["01tWt000006hV6jIAE", "01tWt000006hV8LIAU", "01tWt000006hPffIAE", "01tWt000006hVczIAE"]
product_names = ["EcoPCB Creator", "AI Cirku-Tech", "DevVision IDE", "CollabDesign Studio"]

hits = []

for article in articles:
    text = (article.get('title', '') + " " + article.get('summary', '') + " " + article.get('faq_answer__c', '')).lower()
    
    score = 0
    matched_keywords = []
    
    # Check for product names
    for p in product_names:
        if p.lower() in text:
            score += 5
            matched_keywords.append(p)
            
    # Check for keywords
    for k in keywords:
        if k in text:
            score += 1
            matched_keywords.append(k)
            
    if score > 0:
        hits.append({
            "id": article['id'],
            "title": article['title'],
            "matched": matched_keywords,
            "content_preview": article.get('faq_answer__c', '')[:500]
        })

# Sort by score (approximation of relevance)
hits.sort(key=lambda x: len(x['matched']), reverse=True)

print("__RESULT__:")
print(json.dumps(hits[:10]))"""

env_args = {'var_function-call-6508513195301717407': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-6508513195301718460': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-581561251775655316': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-581561251775652489': 'file_storage/function-call-581561251775652489.json', 'var_function-call-10427006947732253282': 'file_storage/function-call-10427006947732253282.json'}

exec(code, env_args)
