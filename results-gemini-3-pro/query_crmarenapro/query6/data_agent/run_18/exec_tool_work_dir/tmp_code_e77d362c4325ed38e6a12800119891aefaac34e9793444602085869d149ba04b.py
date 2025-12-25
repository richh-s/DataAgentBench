code = """import json

# Get the file path from the previous variable (the filtered one is also large, so it's in a file)
file_path = locals()['var_function-call-13242775580007871930']

# Load the articles
with open(file_path, 'r') as f:
    articles = json.load(f)

# Refined keywords
keywords = ["policy", "guideline", "rule", "regulation", "limit", "bundle", "discount", "quantity", "setup", "configuration"]
products = ["EcoPCB", "Cirku-Tech", "DevVision", "CollabDesign"]

filtered_articles = []

for article in articles:
    title = article.get('title', '')
    if title.startswith("Competitor"):
        continue
    
    text = (title + " " + article.get('summary', '') + " " + article.get('faq_answer__c', '')).lower()
    
    # Check if any product name is mentioned OR if it looks like a general policy
    is_relevant = False
    if any(p.lower() in text for p in products):
        is_relevant = True
    elif any(k.lower() in text for k in keywords):
        is_relevant = True
        
    if is_relevant:
        filtered_articles.append({
            "id": article['id'],
            "title": article['title'],
            "summary": article['summary'],
            "faq_answer__c": article.get('faq_answer__c', '')
        })

print("__RESULT__:")
print(json.dumps(filtered_articles))"""

env_args = {'var_function-call-1951269998321845638': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-1951269998321846351': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-13546283390162504950': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1'}], 'var_function-call-13546283390162501759': 'file_storage/function-call-13546283390162501759.json', 'var_function-call-13242775580007871930': 'file_storage/function-call-13242775580007871930.json'}

exec(code, env_args)
