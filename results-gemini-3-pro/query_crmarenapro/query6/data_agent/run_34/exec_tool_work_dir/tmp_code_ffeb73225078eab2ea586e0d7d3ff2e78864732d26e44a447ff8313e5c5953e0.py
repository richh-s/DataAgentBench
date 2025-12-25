code = """import json

with open(locals()['var_function-call-10743361973864089350'], 'r') as f:
    articles = json.load(f)

keywords = ["quantity", "price", "limit", "discount", "CollabDesign", "EcoPCB", "DevVision", "AI Cirku-Tech"]
hits = []

for article in articles:
    text = (article.get('title', '') + " " + article.get('summary', '') + " " + article.get('faq_answer__c', '')).lower()
    score = sum(1 for k in keywords if k.lower() in text)
    if score > 0:
        hits.append((score, article))

# Sort by score desc
hits.sort(key=lambda x: x[0], reverse=True)

print("__RESULT__:")
print(json.dumps([h[1] for h in hits[:5]]))"""

env_args = {'var_function-call-13445076150731664055': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-15182860569453542197': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}], 'var_function-call-10743361973864089350': 'file_storage/function-call-10743361973864089350.json', 'var_function-call-1152041396580240836': 'file_storage/function-call-1152041396580240836.json'}

exec(code, env_args)
