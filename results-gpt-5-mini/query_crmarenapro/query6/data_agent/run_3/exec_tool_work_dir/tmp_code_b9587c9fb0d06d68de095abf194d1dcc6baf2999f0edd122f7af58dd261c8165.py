code = """import json
from pathlib import Path
# Load knowledge articles from storage file path
path = Path(var_call_UBSEwzhCruvwIkjx6sEEhiRR)
with open(path, 'r', encoding='utf-8') as f:
    ka = json.load(f)
# Search for relevant keywords
keywords = ['discount', 'approval', 'approve', 'quantity', 'max', 'minimum', 'price', 'pricing', 'pricebook', 'override', 'unauthorized', 'limit']
matches = []
for article in ka:
    text = ' '.join([str(article.get('title','')), str(article.get('faq_answer__c','')), str(article.get('summary',''))]).lower()
    for kw in keywords:
        if kw in text:
            matches.append({'id': article.get('id'), 'title': article.get('title'), 'summary': article.get('summary')})
            break
# Print matches as JSON string
import json
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_call_i25sxslZHda6XTnRwj17GXYS': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_UBSEwzhCruvwIkjx6sEEhiRR': 'file_storage/call_UBSEwzhCruvwIkjx6sEEhiRR.json'}

exec(code, env_args)
