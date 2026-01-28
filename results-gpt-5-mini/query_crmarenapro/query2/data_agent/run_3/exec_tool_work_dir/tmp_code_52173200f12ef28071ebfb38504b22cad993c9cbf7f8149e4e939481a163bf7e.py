code = """import json
# Load knowledge articles JSON from the file path stored in var_call_UOOkXxmFLodOFSKYgf5WPgNt
path = var_call_UOOkXxmFLodOFSKYgf5WPgNt
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Load quote and quote line items from storage variables
quote = var_call_jxHrAfYUPcv18wfFj7ev9IKw[0]
qli = var_call_woFkDWeGVisxchiy23tJohui

# Compute numeric totals
for item in qli:
    # convert strings to floats safely
    item['Quantity'] = float(item['Quantity'])
    item['UnitPrice'] = float(item['UnitPrice'])
    item['Discount'] = float(item['Discount'])
    item['TotalPrice'] = float(item['TotalPrice'])

quote_total = sum(item['TotalPrice'] for item in qli)
# compute effective discount per item
violations = []
for item in qli:
    if item['Discount'] > 10.0:
        violations.append({'type':'high_discount','item':item})

# Search articles for relevant keywords
keywords = ['discount','approval','price','pricing','quote','setup','setup fee','setup\s+fee','cost','authorization']
matched = []
for art in articles:
    text = ' '.join([str(art.get(k,'') or '') for k in ('title','faq_answer__c','summary')]).lower()
    for kw in keywords:
        if kw in text:
            matched.append({'id': art.get('id'), 'title': art.get('title'), 'keyword': kw, 'snippet': text[:300]})
            break

result = {
    'quote_id': quote['Id'],
    'quote_total': quote_total,
    'high_discount_line_items_count': len(violations),
    'violating_line_items': violations,
    'matched_articles': matched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jxHrAfYUPcv18wfFj7ev9IKw': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_woFkDWeGVisxchiy23tJohui': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_n3e4pKGRQ6rJL79lgxiieVc5': [{'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_GS3GX1SZjE15iFQlVfGhner3': [], 'var_call_UOOkXxmFLodOFSKYgf5WPgNt': 'file_storage/call_UOOkXxmFLodOFSKYgf5WPgNt.json'}

exec(code, env_args)
