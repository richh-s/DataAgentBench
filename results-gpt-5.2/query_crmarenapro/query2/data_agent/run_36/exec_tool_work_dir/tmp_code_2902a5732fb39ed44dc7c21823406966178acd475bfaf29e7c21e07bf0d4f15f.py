code = """import json, pandas as pd
from pathlib import Path

# Load knowledge articles (may be file path)
ka_src = var_call_rhfQQwaDligASIxiv2o4i0wA
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    articles = json.loads(Path(ka_src).read_text())
else:
    articles = ka_src

quote = var_call_xPl8LQWIzAMBjeKSUgj7gutl[0]
qlis = var_call_C3DAQ8e1uZdvmzmLUvOfa6aN

# Compute discounts and look for policy thresholds in articles
max_discount = max(float(r.get('Discount') or 0) for r in qlis) if qlis else 0.0

def norm(s):
    return (s or '').lower()

candidates = []
for a in articles:
    text = ' '.join([a.get('title',''), a.get('summary',''), a.get('faq_answer__c',''), a.get('urlname','')])
    t = norm(text)
    if 'quote' in t and ('discount' in t or 'setup' in t or 'implementation' in t or 'cost' in t or 'approval' in t or 'pricing' in t):
        candidates.append(a)

# If none, broaden to any article mentioning discount/setup/approval
if not candidates:
    for a in articles:
        t = norm(' '.join([a.get('title',''), a.get('summary',''), a.get('faq_answer__c','')]))
        if ('discount' in t or 'setup' in t or 'implementation fee' in t or 'setup fee' in t or 'approval' in t or 'pricing policy' in t):
            candidates.append(a)

# Determine violation heuristically: if any candidate states max discount allowed < observed max_discount
# We'll parse simple patterns like 'discounts over X%' or 'max discount X%'
import re
violations = []
for a in candidates:
    t = norm(' '.join([a.get('title',''), a.get('summary',''), a.get('faq_answer__c','')]))
    # find thresholds
    nums = []
    for m in re.finditer(r'(?:max(?:imum)?\s+discount\s*(?:is|=)?\s*|discounts?\s+over\s+|discount\s+above\s+)(\d{1,2}(?:\.\d+)?)\s*%', t):
        nums.append(float(m.group(1)))
    # other pattern: 'cannot exceed X%'
    for m in re.finditer(r'cannot\s+exceed\s+(\d{1,2}(?:\.\d+)?)\s*%', t):
        nums.append(float(m.group(1)))
    if nums:
        thresh = min(nums)
        if max_discount > thresh + 1e-9:
            violations.append((a.get('id'), thresh, max_discount))

# If still none, check for setup fee policy: if quote description indicates integration/setup but quote has no explicit setup line item.
# We don't have a setup fee field; only line items. We'll see if any product name contains 'setup' later (not available). So skip.

violated_id = violations[0][0] if violations else None

print('__RESULT__:')
print(json.dumps({'violated_knowledge_article_id': violated_id, 'max_discount': max_discount, 'violation_details': violations[:3], 'candidate_count': len(candidates)}))"""

env_args = {'var_call_xPl8LQWIzAMBjeKSUgj7gutl': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_C3DAQ8e1uZdvmzmLUvOfa6aN': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_rhfQQwaDligASIxiv2o4i0wA': 'file_storage/call_rhfQQwaDligASIxiv2o4i0wA.json'}

exec(code, env_args)
