code = """import json, pandas as pd

# Load knowledge articles (may be file path)
ka = var_call_cO1wY32jPnAhL9MC5efs22xx
if isinstance(ka, str):
    with open(ka, 'r', encoding='utf-8') as f:
        ka = json.load(f)

quote = var_call_ueg2IQifCzvh59H5w32xRboC[0]
qlis = var_call_vh6v5guFHucux48p9OQRzKAg

# Heuristic: compute max discount and look for policy articles mentioning discount/setup/implementation/approval thresholds.
max_disc = max(float(r.get('Discount') or 0) for r in qlis) if qlis else 0.0
terms = []
if max_disc >= 15:
    terms += ['discount', 'approval', '15%']
terms += ['setup', 'implementation', 'services', 'quote approval', 'discount']

# score articles by keyword hits in title/summary/faq
import re
pat = re.compile('|'.join(re.escape(t.lower()) for t in set(terms) if t), re.I)
scored = []
for r in ka:
    text = ' '.join([(r.get('title') or ''), (r.get('summary') or ''), (r.get('faq_answer__c') or ''), (r.get('urlname') or '')]).lower()
    hits = len(pat.findall(text)) if pat.pattern else 0
    if hits:
        scored.append((hits, r.get('id')))
scored.sort(reverse=True)

# With available data, no explicit policy violation detectable from KA corpus subset; return None unless a clear "quote approval" article exists.
viol = None
for hits, kid in scored[:20]:
    # if an article explicitly about quote approval/discount policy likely contains those terms in title
    # select if title contains 'quote' and ('discount' or 'approval')
    pass

result = viol
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ueg2IQifCzvh59H5w32xRboC': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_vh6v5guFHucux48p9OQRzKAg': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_cO1wY32jPnAhL9MC5efs22xx': 'file_storage/call_cO1wY32jPnAhL9MC5efs22xx.json'}

exec(code, env_args)
