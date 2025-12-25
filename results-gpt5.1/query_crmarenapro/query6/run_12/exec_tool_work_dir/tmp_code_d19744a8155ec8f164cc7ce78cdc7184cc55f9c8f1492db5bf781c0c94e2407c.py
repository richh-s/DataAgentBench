code = """import json, pandas as pd
from pathlib import Path

path = var_call_rymkAGc3lHbGye7doW7S2Hdd

with open(path, 'r') as f:
    data = json.load(f)

# Very simple heuristic: look for articles mentioning quotes, pricing, discount, quantity, configuration, or pricebook
keywords = ['quote', 'pricing', 'price', 'discount', 'quantity', 'configuration', 'config', 'pricebook']

candidates = []
for row in data:
    text = (row.get('title','') or '') + ' ' + (row.get('faq_answer__c','') or '') + ' ' + (row.get('summary','') or '')
    lt = text.lower()
    if any(k in lt for k in keywords):
        candidates.append(row['id'])

result = candidates

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_961g2FT19VSQ92589QGN8lE8': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_1ZkAvuwAPZlfpyHTahWscc8I': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_DYghUtDW0C18LQ8L384HIsOH': [], 'var_call_rymkAGc3lHbGye7doW7S2Hdd': 'file_storage/call_rymkAGc3lHbGye7doW7S2Hdd.json'}

exec(code, env_args)
