code = """import json
from pathlib import Path

# Load previous results from storage variables
quote = var_call_hv3kEWmxTjfSEOQaq59G8pqT
qli = var_call_8O3eyAnTs64CM73ANtAZ7DRh
kb_path = var_call_whmF1Av3KiqEPrA1t2rqfLAQ

# Load knowledge articles JSON from file path
with open(kb_path, 'r', encoding='utf-8') as f:
    kbs = json.load(f)

# Keywords to search for
keywords = [
    'discount', 'setup', 'setup fee', 'pricing', 'price', 'approval', 'authorize', 'authorization',
    'quot', 'quote', 'approval threshold', 'max discount', 'maximum discount'
]

matches = []
for art in kbs:
    text = ' '.join([str(art.get('title','') or ''), str(art.get('summary','') or ''), str(art.get('faq_answer__c','') or '')]).lower()
    found = [kw for kw in keywords if kw in text]
    if found:
        # create snippet where keyword appears
        snippet = ''
        for kw in found:
            idx = text.find(kw)
            start = max(0, idx-60)
            end = min(len(text), idx+60)
            snippet += text[start:end].replace('\n',' ') + ' ... '
        matches.append({'id': art.get('id'), 'title': art.get('title'), 'found_keywords': found, 'snippet': snippet})

# Prepare output
out = {'quote': quote, 'quote_line_items': qli, 'matching_articles': matches}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_hv3kEWmxTjfSEOQaq59G8pqT': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_8O3eyAnTs64CM73ANtAZ7DRh': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_C7CyCFD0cCXtrxEBDUW149wV': [{'Product2Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_mmCAkQAMl9ZFHY8HTGKTp6OW': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_jlt0ueEBF7vhKzcvddWXGjpv': [], 'var_call_whmF1Av3KiqEPrA1t2rqfLAQ': 'file_storage/call_whmF1Av3KiqEPrA1t2rqfLAQ.json', 'var_call_avSeZYUGoIDh4c0KwOInHqNB': []}

exec(code, env_args)
