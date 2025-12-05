code = """import json, pandas as pd, os
path = var_call_e0Br1OwmBzdTbCx8MaAwSZ26
with open(path, 'r') as f:
    ka = json.load(f)

violations = json.loads(var_call_EnxkIMCosogkAaUq7uw65zSP)

texts = []
for art in ka:
    t = (art.get('title','') or '') + ' ' + (art.get('summary','') or '') + ' ' + (art.get('faq_answer__c','') or '')
    texts.append((art['id'], t.lower()))

match_ids = set()
for vid in violations:
    if vid == 'bulk_discount_violation':
        keywords = ['bulk discount','volume discount','discount for orders over','high quantity','large order discount']
    elif vid == 'below_min_price':
        keywords = ['minimum price','floor price','cannot sell below','price floor']
    else:
        continue
    for id_, txt in texts:
        if any(k in txt for k in keywords):
            match_ids.add(id_)

result = list(match_ids)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CUQQYGxE7mdpfimiRwK6euyr': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_gioOemyFTqEefy2aLyjuYQSc': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_e0Br1OwmBzdTbCx8MaAwSZ26': 'file_storage/call_e0Br1OwmBzdTbCx8MaAwSZ26.json', 'var_call_EnxkIMCosogkAaUq7uw65zSP': ['below_min_price', 'bulk_discount_violation']}

exec(code, env_args)
