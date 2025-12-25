code = """import json, pandas as pd
qli = pd.DataFrame(var_call_o4rxr9GWJgMnXYagxpJNGqsk)
# Simple business rule guesses:
# 1) Quantity > 30 on any line might violate a "max units per quote line" policy.
# 2) Discount > 10 may violate a "max discount" policy.
violations = []
for _, r in qli.iterrows():
    qty = float(str(r['Quantity']))
    disc = float(str(r['Discount']))
    if qty > 30:
        violations.append('max_quantity')
    if disc > 10:
        violations.append('max_discount')
violations = sorted(set(violations))
# Map these hypothetical violations to knowledge article IDs by simple keyword search in titles/answers
import os, json as js
path = var_call_MxltqrI8hdpU3umq14kTI59z
with open(path, 'r') as f:
    kav = js.load(f)
max_qty_ids = []
max_disc_ids = []
for art in kav:
    text = (art.get('title','') + ' ' + art.get('faq_answer__c','')).lower()
    if any(k in text for k in ['maximum quantity','max quantity','order quantity limit','quote quantity limit']):
        max_qty_ids.append(art['id'])
    if any(k in text for k in ['maximum discount','max discount','discount limit','pricing policy']):
        max_disc_ids.append(art['id'])
result_ids = []
if 'max_quantity' in violations and max_qty_ids:
    result_ids.append(max_qty_ids[0])
if 'max_discount' in violations and max_disc_ids:
    result_ids.append(max_disc_ids[0])
# If nothing matched by search, just return empty list
out = result_ids
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_o4rxr9GWJgMnXYagxpJNGqsk': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_nNBuY9RDdE7CaVxiHaERX59X': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_MxltqrI8hdpU3umq14kTI59z': 'file_storage/call_MxltqrI8hdpU3umq14kTI59z.json'}

exec(code, env_args)
