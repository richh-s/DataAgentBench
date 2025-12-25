code = """import json
import pandas as pd

# Load knowledge articles
with open(locals()['var_function-call-16417389658430992717'], 'r') as f:
    articles = json.load(f)

# Filter articles that might be relevant
keywords = ['regulation', 'policy', 'price', 'quantity', 'discount', 'quote', 'invalid', 'config', 'limit']
relevant_articles = []

for art in articles:
    text = (str(art.get('title', '')) + " " + str(art.get('summary', '')) + " " + str(art.get('faq_answer__c', ''))).lower()
    if any(k in text for k in keywords):
        relevant_articles.append(art)

print(f"__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-14382782062812109965': [], 'var_function-call-14382782062812108114': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-16417389658430992717': 'file_storage/function-call-16417389658430992717.json'}

exec(code, env_args)
