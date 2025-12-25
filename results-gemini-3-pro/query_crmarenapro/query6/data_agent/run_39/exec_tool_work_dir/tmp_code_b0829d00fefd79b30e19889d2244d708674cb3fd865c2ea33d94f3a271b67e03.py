code = """import json

# Load knowledge articles
with open(locals()['var_function-call-3577143583478871756'], 'r') as f:
    articles = json.load(f)

keywords = ['CollabDesign', 'DevVision', 'EcoPCB', 'Cirku-Tech', 'Discount', 'Quantity', 'Limit', 'Policy']
relevant_articles = []

for article in articles:
    text = (article.get('title', '') + ' ' + article.get('summary', '') + ' ' + article.get('faq_answer__c', '')).lower()
    score = 0
    for kw in keywords:
        if kw.lower() in text:
            score += 1
    if score > 0:
        relevant_articles.append(article)

# Sort by relevance (number of keyword matches is a heuristic, but simple enough for inspection)
# Actually, I'll just print titles and IDs of matches to narrow down.
results = []
for art in relevant_articles:
    results.append({'id': art['id'], 'title': art['title'], 'summary': art['summary']})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3577143583478871835': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3577143583478871756': 'file_storage/function-call-3577143583478871756.json', 'var_function-call-4227665644957381308': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
