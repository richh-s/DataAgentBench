code = """import json
import pandas as pd

# Load knowledge articles from file
file_path = var_call_XBrIwmWf2m98oSR6eRePj8QE
with open(file_path, 'r') as f:
    knowledge = json.load(f)

# Very naive heuristic: look for articles mentioning pricing, discount, quantity, or quote configuration
keywords = ['price', 'pricing', 'discount', 'quantity', 'quote', 'configuration', 'config', 'bundle']

matches = []
for art in knowledge:
    text = (art.get('title','') + ' ' + art.get('faq_answer__c','') + ' ' + art.get('summary','')).lower()
    if any(k in text for k in keywords):
        matches.append(art['id'])

result = list(sorted(set(matches)))

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lkUImd4Pqi61muVQanjUXV7i': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_ASZAjKYxv4FKV6mpSySnZkf8': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_XBrIwmWf2m98oSR6eRePj8QE': 'file_storage/call_XBrIwmWf2m98oSR6eRePj8QE.json'}

exec(code, env_args)
