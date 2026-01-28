code = """import json
# load previous tool results from storage variables
with open(var_call_qzIzbtaTJjqpXaAugEbG0nfT, 'r') as f:
    knowledge = json.load(f)
quote_line_items = var_call_4cuxRdfY1rLrF4AeUHMu27Uq
pricebook_entries = var_call_vL3fNSQRCTUT6xiBVHPhO9qf
# normalize text to search for relevant policy keywords
keywords = ['discount','pricing','price','quantity','pricebook','approval','unauthor','limit','maximum','minim','configuration']
matches = []
for k in knowledge:
    text = ' '.join([str(k.get('title','')), str(k.get('summary','')), str(k.get('faq_answer__c',''))]).lower()
    if any(kw in text for kw in keywords):
        matches.append({'id': k.get('id'), 'title': k.get('title'), 'summary': k.get('summary')})
# Also identify anomalies in quote line items
anomalies = []
# check for missing pricebookentry
pb_ids = {p['Id'] for p in pricebook_entries}
for q in quote_line_items:
    if q.get('PricebookEntryId') not in pb_ids:
        anomalies.append({'Id': q['Id'], 'issue': 'Missing PricebookEntry', 'PricebookEntryId': q.get('PricebookEntryId')})
    # check unit price mismatch with pricebook
    for p in pricebook_entries:
        if p['Id'] == q.get('PricebookEntryId'):
            if float(q.get('UnitPrice',0)) != float(p.get('UnitPrice',0)):
                anomalies.append({'Id': q['Id'], 'issue': 'UnitPrice mismatch', 'QuoteUnitPrice': q.get('UnitPrice'), 'PricebookUnitPrice': p.get('UnitPrice')})
    # check high discount
    try:
        if float(q.get('Discount',0)) > 10.0:
            anomalies.append({'Id': q['Id'], 'issue': 'High discount', 'Discount': q.get('Discount')})
    except:
        pass
    # check unusually high quantity
    try:
        if float(q.get('Quantity',0)) > 20:
            anomalies.append({'Id': q['Id'], 'issue': 'High quantity', 'Quantity': q.get('Quantity')})
    except:
        pass

result = {'matches': matches, 'anomalies': anomalies}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4cuxRdfY1rLrF4AeUHMu27Uq': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_qzIzbtaTJjqpXaAugEbG0nfT': 'file_storage/call_qzIzbtaTJjqpXaAugEbG0nfT.json', 'var_call_vL3fNSQRCTUT6xiBVHPhO9qf': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_WntCrUYS5f0YcSyn6y04wFcH': []}

exec(code, env_args)
