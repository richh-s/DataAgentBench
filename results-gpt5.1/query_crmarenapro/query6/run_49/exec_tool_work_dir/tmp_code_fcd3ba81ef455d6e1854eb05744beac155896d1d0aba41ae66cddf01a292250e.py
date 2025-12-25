code = """import json, pandas as pd, os
path = var_call_ihjHSDAhecK2oI5fjOa2bGVv
with open(path) as f:
    data = json.load(f)
# simple heuristic: look for pricing / discount / quantity policy articles
candidates = []
for row in data:
    text = (row.get('title','') + ' ' + row.get('summary','') + ' ' + row.get('faq_answer__c','')).lower()
    if any(k in text for k in ['discount','quantity','pricing','price book','pricebook','quote','quotation','bundle','upsell','cross-sell']):
        candidates.append(row)
# rank by presence of multiple relevant words
scored = []
for row in candidates:
    text = (row.get('title','') + ' ' + row.get('summary','') + ' ' + row.get('faq_answer__c','')).lower()
    score = sum(text.count(k) for k in ['discount','quantity','pricing','quote','quotation'])
    scored.append((score, row['id']))
scored.sort(reverse=True)
result = scored[0][1] if scored else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_OCkUXXPTzAGKk0YXShUnpUB2': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_aG1VoPkfKoMBqpW9XG57LpxL': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_ihjHSDAhecK2oI5fjOa2bGVv': 'file_storage/call_ihjHSDAhecK2oI5fjOa2bGVv.json'}

exec(code, env_args)
