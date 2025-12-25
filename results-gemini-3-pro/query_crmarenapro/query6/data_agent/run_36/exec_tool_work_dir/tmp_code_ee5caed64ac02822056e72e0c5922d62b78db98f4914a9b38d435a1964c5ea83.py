code = """import json

with open(locals()['var_function-call-5411761256038888410'], 'r') as f:
    articles = json.load(f)

keywords = ["quantity", "discount", "price", "limit", "policy", "regulation", "config", "setup", "DevVision", "EcoPCB", "AI Cirku", "CollabDesign"]
results = []

for art in articles:
    text = (art.get('title') or '') + " " + (art.get('summary') or '') + " " + (art.get('faq_answer__c') or '')
    if any(k.lower() in text.lower() for k in keywords):
        results.append({
            "id": art['id'],
            "title": art['title'],
            "summary": art['summary'],
            "faq_answer__c": art['faq_answer__c']
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5411761256038891205': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-5411761256038888410': 'file_storage/function-call-5411761256038888410.json', 'var_function-call-9950533592401585476': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-13400343155588812565': 'file_storage/function-call-13400343155588812565.json'}

exec(code, env_args)
