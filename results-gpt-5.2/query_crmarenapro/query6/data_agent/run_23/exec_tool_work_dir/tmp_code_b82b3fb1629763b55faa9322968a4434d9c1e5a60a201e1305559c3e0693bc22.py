code = """import json, pandas as pd

# Load quote line items
qli = pd.DataFrame(var_call_ts6JwhGSu1XbjCEIYGrbFoNr)

# Normalize numeric fields
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')

# Identify potential violation: discount exceeds allowed volume discount for given qty/total.
# Find line(s) with Discount > 0.15 or not matching volume thresholds (5%,10%,15%) based on TotalPrice.
# Here discount is 15.0 (percent), which is within max 15% IF it qualifies for >=$20 threshold.
# But totals are in dollars >20, so qualifies. So likely another policy: max quantity per line? We don't know.

# Load knowledge articles results (large file)
import os
path = var_call_EFpJIClvHVqMitDM2BQdxib0
with open(path,'r',encoding='utf-8') as f:
    arts = json.load(f)

# Find specific article about volume discount policy
vol = [a for a in arts if 'volume-based discounts' in (a.get('title','').lower().strip())]
# choose first id
ans = vol[0]['id'] if vol else None

print('__RESULT__:')
print(json.dumps({'article_id': ans}))"""

env_args = {'var_call_ts6JwhGSu1XbjCEIYGrbFoNr': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_G2V4xmePRG7EZEb6T8XkdlFY': [{'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech', 'IsActive': '1', 'PricebookEntryId': '01uWt0000027P8cIAE', 'PricebookName': 'Standard Price Book', 'ListUnitPrice': '529.99'}], 'var_call_EFpJIClvHVqMitDM2BQdxib0': 'file_storage/call_EFpJIClvHVqMitDM2BQdxib0.json'}

exec(code, env_args)
