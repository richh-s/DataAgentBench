code = """import json

# Load the full knowledge articles search result
with open(locals()['var_function-call-15430046982164314124'], 'r') as f:
    articles = json.load(f)

keywords = ["quantity", "price", "discount", "limit", "bundle", "regulation", "policy", "CollabDesign", "EcoPCB", "Cirku-Tech", "DevVision"]

candidates = []
for art in articles:
    text = (art['Title'] + "\n" + art['Text']).lower()
    score = 0
    matched_keywords = []
    for kw in keywords:
        if kw.lower() in text:
            score += 1
            matched_keywords.append(kw)
    
    if score > 0:
        candidates.append({
            "Id": art['Id'],
            "Title": art['Title'],
            "Snippet": art['Text'][:500], # Preview
            "Matched": matched_keywords
        })

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-3871856346329201065': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3871856346329201134': 'file_storage/function-call-3871856346329201134.json', 'var_function-call-3871856346329201203': 'file_storage/function-call-3871856346329201203.json', 'var_function-call-15430046982164314124': 'file_storage/function-call-15430046982164314124.json'}

exec(code, env_args)
