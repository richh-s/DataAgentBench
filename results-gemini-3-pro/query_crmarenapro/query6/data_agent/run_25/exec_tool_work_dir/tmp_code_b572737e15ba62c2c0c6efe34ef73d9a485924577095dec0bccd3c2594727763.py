code = """import json

# Load the knowledge articles
with open(locals()['var_function-call-3225485980591398081'], 'r') as f:
    articles = json.load(f)

# Keywords to look for
keywords = ["quantity", "price", "discount", "config", "rule", "policy", "limit", "invalid", "violation", "bundle"]
products = ["EcoPCB Creator", "AI Cirku-Tech", "DevVision IDE", "CollabDesign Studio"]

relevant_articles = []

for article in articles:
    text = (article.get('title', '') + " " + article.get('faq_answer__c', '') + " " + article.get('summary', '')).lower()
    
    # Check if any product name is in the text
    product_hit = any(p.lower() in text for p in products)
    
    # Check if any keyword is in the text
    keyword_hit = any(k in text for k in keywords)
    
    if product_hit or (keyword_hit and "regulation" in text) or (keyword_hit and "invalid" in text):
        relevant_articles.append(article)

# If too many, just print titles first
results = []
for a in relevant_articles:
    results.append({"id": a['id'], "title": a['title'], "content": a['faq_answer__c'][:500] + "..."})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3225485980591398358': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3225485980591398081': 'file_storage/function-call-3225485980591398081.json', 'var_function-call-10840537327752465246': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}]}

exec(code, env_args)
