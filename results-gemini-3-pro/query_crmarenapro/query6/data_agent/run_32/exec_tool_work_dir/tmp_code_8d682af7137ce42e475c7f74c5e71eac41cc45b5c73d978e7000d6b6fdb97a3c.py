code = """import json

# Get the file path from the previous result variable
file_path = locals()['var_function-call-17450113416478609730']

# Load the knowledge articles
with open(file_path, 'r') as f:
    articles = json.load(f)

# Quote details
quote_items = [
    {"Product": "EcoPCB Creator", "Qty": 3.0, "Discount": 0.0},
    {"Product": "AI Cirku-Tech", "Qty": 2.0, "Discount": 0.0},
    {"Product": "DevVision IDE", "Qty": 4.0, "Discount": 0.0},
    {"Product": "CollabDesign Studio", "Qty": 35.0, "Discount": 15.0}
]

relevant_articles = []

for article in articles:
    text = (article.get('title') or "") + " " + (article.get('faq_answer__c') or "") + " " + (article.get('summary') or "")
    text_lower = text.lower()
    
    score = 0
    reasons = []
    
    # Check for specific products
    for item in quote_items:
        prod_name = item['Product']
        if prod_name.lower().strip() in text_lower:
            score += 10
            reasons.append(f"Mentions {prod_name}")
            
    # Check for keywords
    if "discount" in text_lower:
        score += 1
        reasons.append("Mentions discount")
    if "quantity" in text_lower or "qty" in text_lower:
        score += 1
        reasons.append("Mentions quantity")
    if "policy" in text_lower or "regulation" in text_lower:
        score += 1
        reasons.append("Mentions policy/regulation")
        
    if score > 0:
        relevant_articles.append({
            "id": article['id'],
            "title": article['title'],
            "faq_answer__c": article.get('faq_answer__c', ''),
            "reasons": reasons,
            "score": score
        })

# Sort by score
relevant_articles.sort(key=lambda x: x['score'], reverse=True)

# Print top matches
print("__RESULT__:")
print(json.dumps([{"id": r['id'], "title": r['title'], "reasons": r['reasons'], "snippet": r['faq_answer__c'][:200]} for r in relevant_articles[:5]]))"""

env_args = {'var_function-call-17450113416478611336': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-17450113416478612581': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-17450113416478609730': 'file_storage/function-call-17450113416478609730.json', 'var_function-call-1147513580314036578': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}]}

exec(code, env_args)
