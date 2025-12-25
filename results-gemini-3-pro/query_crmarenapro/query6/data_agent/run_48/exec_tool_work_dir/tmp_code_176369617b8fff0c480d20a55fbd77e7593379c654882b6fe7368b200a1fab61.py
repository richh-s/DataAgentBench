code = """import json

with open(locals()['var_function-call-13985513228594472999'], 'r') as f:
    relevant_articles = json.load(f)

keywords = ['policy', 'regulation', 'limit', 'requires', 'bundle', 'discount', 'quantity', 'price', 'must', 'sold with', 'minimum', 'maximum', 'exceed']

filtered_articles = []
for article in relevant_articles:
    text = (article.get('title', '') + ' ' + article.get('faq_answer__c', '')).lower()
    
    # specific check for product names again just to be sure
    products_in_text = []
    for p in ['ecopcb', 'cirku-tech', 'devvision', 'collabdesign']:
        if p in text:
            products_in_text.append(p)
            
    if not products_in_text:
        continue
        
    # check for constraint keywords
    found_kw = []
    for kw in keywords:
        if kw in text:
            found_kw.append(kw)
            
    if found_kw:
        filtered_articles.append({
            'id': article['id'],
            'title': article['title'],
            'text': text[:500] + '...', # snippet
            'found_keywords': found_kw,
            'full_text': text # keep for further analysis if needed
        })

print("__RESULT__:")
print(json.dumps(filtered_articles))"""

env_args = {'var_function-call-5966384792397248609': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-6390951173537209928': 'file_storage/function-call-6390951173537209928.json', 'var_function-call-7766566947645911139': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-5471434017419684553': 'file_storage/function-call-5471434017419684553.json', 'var_function-call-13985513228594472999': 'file_storage/function-call-13985513228594472999.json'}

exec(code, env_args)
