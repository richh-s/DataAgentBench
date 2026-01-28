code = """import json

quote = var_call_hv3kEWmxTjfSEOQaq59G8pqT
qli = var_call_8O3eyAnTs64CM73ANtAZ7DRh
kb_path = var_call_whmF1Av3KiqEPrA1t2rqfLAQ

with open(kb_path, 'r', encoding='utf-8') as f:
    kbs = json.load(f)

keywords = ['discount','setup','setup fee','pricing','price','approval','authorize','authorization','quot','quote','approval threshold','max discount','maximum discount']

matches = []
for art in kbs:
    title = art.get('title','') or ''
    summary = art.get('summary','') or ''
    faq = art.get('faq_answer__c','') or ''
    text = (title + ' ' + summary + ' ' + faq).lower()
    found = [kw for kw in keywords if kw in text]
    if found:
        snippets = []
        for kw in found:
            idx = text.find(kw)
            start = idx-60 if idx-60>0 else 0
            end = idx+60 if idx+60<len(text) else len(text)
            snippets.append(text[start:end].replace(chr(10),' '))
        matches.append({'id': art.get('id'), 'title': title, 'found_keywords': found, 'snippets': snippets})

out = {'quote_id': quote[0].get('Id'), 'matches': matches}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_hv3kEWmxTjfSEOQaq59G8pqT': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_8O3eyAnTs64CM73ANtAZ7DRh': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_C7CyCFD0cCXtrxEBDUW149wV': [{'Product2Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_mmCAkQAMl9ZFHY8HTGKTp6OW': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_jlt0ueEBF7vhKzcvddWXGjpv': [], 'var_call_whmF1Av3KiqEPrA1t2rqfLAQ': 'file_storage/call_whmF1Av3KiqEPrA1t2rqfLAQ.json', 'var_call_avSeZYUGoIDh4c0KwOInHqNB': []}

exec(code, env_args)
