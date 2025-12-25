code = """import json

# Load the knowledge articles
with open(locals()['var_function-call-3729435714753241374'], 'r') as f:
    articles = json.load(f)

# Define keywords and products
keywords = ['policy', 'regulation', 'limit', 'discount', 'quantity', 'price', 'approval']
products = ['EcoPCB Creator', 'AI Cirku-Tech', 'DevVision IDE', 'CollabDesign Studio']

# Search for relevant articles
relevant_articles = []
for art in articles:
    text = (art.get('title', '') + ' ' + art.get('summary', '') + ' ' + art.get('faq_answer__c', '')).lower()
    
    # Check if any product name is in the text
    product_found = False
    for prod in products:
        if prod.lower().strip() in text:
            product_found = True
            break
            
    # Check if any keyword is in the text
    keyword_found = False
    for kw in keywords:
        if kw in text:
            keyword_found = True
            break
            
    if product_found and keyword_found:
        relevant_articles.append({
            'id': art['id'],
            'title': art['title'],
            'summary': art['summary']
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-16774832404957305632': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-15720765471646991482': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-3729435714753241374': 'file_storage/function-call-3729435714753241374.json'}

exec(code, env_args)
