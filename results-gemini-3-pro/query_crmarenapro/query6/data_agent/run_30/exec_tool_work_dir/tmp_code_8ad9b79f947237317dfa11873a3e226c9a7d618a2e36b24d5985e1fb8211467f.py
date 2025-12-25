code = """import json

# Load knowledge articles using the correct key with hyphens
with open(locals()['var_function-call-17564922171353455982'], 'r') as f:
    articles = json.load(f)

# Define keywords and product names
# Using parts of names to be safe against whitespace issues
product_names = ["DevVision", "EcoPCB", "AI Cirku", "CollabDesign"]
keywords = ["quantity", "limit", "max", "min", "price", "discount", "config", "invalid", "regulation", "policy", "bundle"]

relevant_articles = []

for article in articles:
    # Combine fields for search
    text = (str(article.get('title', '')) + ' ' + str(article.get('faq_answer__c', '')) + ' ' + str(article.get('summary', ''))).lower()
    
    # Check for keywords
    has_keyword = any(k in text for k in keywords)
    
    # Check for product names
    has_product = any(p.lower() in text for p in product_names)
    
    if has_keyword or has_product:
        relevant_articles.append({
            "id": article['id'],
            "title": article['title'],
            "summary": article['summary']
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-17564922171353456476': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-17564922171353454181': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-17564922171353455982': 'file_storage/function-call-17564922171353455982.json', 'var_function-call-2150965838396186453': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}]}

exec(code, env_args)
