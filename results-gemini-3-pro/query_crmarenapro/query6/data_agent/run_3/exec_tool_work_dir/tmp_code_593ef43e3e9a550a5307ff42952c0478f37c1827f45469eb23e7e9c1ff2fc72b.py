code = """import json

# Load knowledge articles
with open(locals()['var_function-call-3392226514804622973'], 'r') as f:
    articles = json.load(f)

# Quote Items
items = [
    {"Name": "DevVision IDE", "Quantity": 4, "UnitPrice": 299.99},
    {"Name": "EcoPCB Creator", "Quantity": 3, "UnitPrice": 349.99},
    {"Name": "AI Cirku-Tech", "Quantity": 2, "UnitPrice": 529.99},
    {"Name": "CollabDesign Studio", "Quantity": 35, "UnitPrice": 399.99, "Discount": 15.0}
]

hits = []
for art in articles:
    text = (art['title'] + " " + art['summary'] + " " + (art['faq_answer__c'] or "")).lower()
    
    # Check for product names
    matched_products = []
    for item in items:
        # Check partial name match if unique enough
        prod_name_clean = item['Name'].strip().lower()
        if prod_name_clean in text:
            matched_products.append(item['Name'])
    
    # Check for keywords
    keywords = ["quantity", "limit", "max", "min", "policy", "regulation", "approval", "discount"]
    has_keyword = any(k in text for k in keywords)
    
    if matched_products and has_keyword:
        hits.append({
            "id": art['id'],
            "title": art['title'],
            "summary": art['summary'],
            "matched_products": matched_products
        })

print("__RESULT__:")
print(json.dumps(hits))"""

env_args = {'var_function-call-3392226514804621660': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3392226514804622973': 'file_storage/function-call-3392226514804622973.json', 'var_function-call-4947644945305673138': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
