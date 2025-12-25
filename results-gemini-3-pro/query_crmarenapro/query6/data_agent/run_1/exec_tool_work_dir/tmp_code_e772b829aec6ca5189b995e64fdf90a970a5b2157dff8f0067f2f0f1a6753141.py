code = """import json

# Load the knowledge articles
with open(locals()['var_function-call-13537633994279520430'], 'r') as f:
    articles = json.load(f)

# Quote items for reference
quote_items = [
    {"product": "EcoPCB Creator", "qty": 3, "price": 349.99, "discount": 0},
    {"product": "AI Cirku-Tech", "qty": 2, "price": 529.99, "discount": 0},
    {"product": "DevVision IDE", "qty": 4, "price": 299.99, "discount": 0},
    {"product": "CollabDesign Studio", "qty": 35, "price": 399.99, "discount": 15}
]

keywords = ["EcoPCB", "Cirku-Tech", "DevVision", "CollabDesign", "policy", "regulation", "limit", "maximum", "minimum", "discount"]

relevant_articles = []

for art in articles:
    text = (art.get('title', '') + ' ' + art.get('faq_answer__c', '') + ' ' + art.get('summary', '')).lower()
    
    # Check for specific product mentions combined with rule keywords
    for item in quote_items:
        prod_name_lower = item['product'].split()[0].lower() # e.g., "ecopcb", "collabdesign"
        if prod_name_lower in text:
             relevant_articles.append(art)
             break # Prevent adding same article multiple times for same product
    
    # Check for general keywords if not already added
    if art not in relevant_articles:
        for kw in ["policy", "regulation", "compliance", "invalid config"]:
            if kw in text:
                relevant_articles.append(art)
                break

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-200643612261626635': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-200643612261629920': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-13537633994279521977': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-13537633994279520430': 'file_storage/function-call-13537633994279520430.json'}

exec(code, env_args)
