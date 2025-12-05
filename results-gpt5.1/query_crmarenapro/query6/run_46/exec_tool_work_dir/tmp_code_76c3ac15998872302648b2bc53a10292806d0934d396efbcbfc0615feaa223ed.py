code = """import json
import pandas as pd
from pathlib import Path

# Load full knowledge articles
path = Path(var_call_9S4eRUTa9FAZcp3lcoLZDuF4)
with path.open() as f:
    knowledge = json.load(f)

# Simple heuristic: look for articles mentioning quote/quotations, discount, pricing rules, quantity limits, or configuration rules
keywords = ['discount', 'pricing', 'price', 'quote', 'quotation', 'config', 'configuration', 'bundle', 'quantity', 'limit', 'regulation']

candidates = []
for art in knowledge:
    text = (art.get('title','') + ' ' + art.get('faq_answer__c','') + ' ' + art.get('summary','')).lower()
    if any(k in text for k in keywords):
        candidates.append(art)

# If multiple, further filter for words about "quote line items", "unit price", "min", "max", etc.
secondary_keywords = ['unit price', 'unitprice', 'quote line', 'line item', 'minimum quantity', 'maximum quantity', 'max quantity', 'min quantity', 'volume discount', 'bulk discount', 'approval']
filtered = []
for art in candidates:
    text = (art.get('title','') + ' ' + art.get('faq_answer__c','') + ' ' + art.get('summary','')).lower()
    if any(k in text for k in secondary_keywords):
        filtered.append(art)

arts = filtered or candidates or knowledge

# For determinism, sort by title and pick first
arts_sorted = sorted(arts, key=lambda x: x.get('title',''))
selected_id = arts_sorted[0]['id']

import json as _json
result = _json.dumps(selected_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_JfBkvPVpB5frlX6yyxh5xWFO': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_JteR1oEtcePHVGjf7DuzKHwl': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_9S4eRUTa9FAZcp3lcoLZDuF4': 'file_storage/call_9S4eRUTa9FAZcp3lcoLZDuF4.json'}

exec(code, env_args)
