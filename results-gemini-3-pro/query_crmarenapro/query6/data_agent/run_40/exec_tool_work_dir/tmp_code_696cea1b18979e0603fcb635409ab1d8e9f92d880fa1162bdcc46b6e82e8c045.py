code = """import json

# Load knowledge articles
with open(locals()['var_function-call-14104936062871303827'], 'r') as f:
    articles = json.load(f)

keywords = ['regulation', 'policy', 'guideline', 'limit', 'discount', 'approval', 'quantity', 'setup', 'config']

relevant_articles = []
for article in articles:
    text = (article['title'] + " " + article['summary']).lower()
    if any(k in text for k in keywords):
        relevant_articles.append({"id": article['id'], "title": article['title'], "summary": article['summary']})

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-15591580131531237653': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-14104936062871303827': 'file_storage/function-call-14104936062871303827.json', 'var_function-call-8581701186982105267': 'file_storage/function-call-8581701186982105267.json'}

exec(code, env_args)
