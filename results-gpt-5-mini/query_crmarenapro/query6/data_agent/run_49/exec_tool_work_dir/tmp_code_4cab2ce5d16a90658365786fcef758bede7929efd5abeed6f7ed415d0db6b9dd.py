code = """import json
# load the knowledge articles result from storage
with open(var_call_RTPhiLSQEzYdAkkr9vtAozC5, 'r') as f:
    ka = json.load(f)
# Search for relevant articles by keywords
keywords = ['quote', 'pricing', 'price', 'discount', 'quantity', 'quantity', 'line item', 'lineitem', 'approval', 'pricebook', 'unitprice', 'pricebookentry', 'quote line', 'quote line item', 'quoteLineItem']
results = []
for a in ka:
    text = (a.get('title','') + ' ' + a.get('faq_answer__c','') + ' ' + a.get('summary','')).lower()
    for k in keywords:
        if k in text:
            results.append({'id': a.get('id'), 'title': a.get('title'), 'matched_keyword': k})
            break

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_RTPhiLSQEzYdAkkr9vtAozC5': 'file_storage/call_RTPhiLSQEzYdAkkr9vtAozC5.json', 'var_call_b2tyBDwtG2PbPfhHPHx1Cabj': [], 'var_call_PUiOLoOPMdFdaDIWCycxRjd4': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review'}], 'var_call_3Mtfx6iMPzBPtAUoT75JsVF9': [], 'var_call_oPo2Cg0FkZ6bayS30viTKs47': [{'Id': '#00kWt000002HHRkIAO', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'TotalPrice': '1059.98'}, {'Id': '00kWt000002HQJYIA4', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'TotalPrice': '1199.96'}], 'var_call_P23ZV3HlK3Wu599Z49t79FP9': [{'Id': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}]}

exec(code, env_args)
