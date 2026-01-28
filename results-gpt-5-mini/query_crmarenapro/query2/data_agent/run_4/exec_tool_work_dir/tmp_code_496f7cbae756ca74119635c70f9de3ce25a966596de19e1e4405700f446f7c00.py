code = """import json, re

# Load knowledge articles
with open(var_call_Zfg5bx9JK6QSf3ncatbFyTWK, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Load quote and line items
quote = var_call_CPqm0eONObe8A3HvRz3xSkmw[0] if isinstance(var_call_CPqm0eONObe8A3HvRz3xSkmw, list) and var_call_CPqm0eONObe8A3HvRz3xSkmw else None
qline = var_call_xBEvKZfQykUO7up9DOQ1Vxir

# Parse discounts from quote line items
discounts = []
for li in qline:
    # Discount may be string, convert to float
    try:
        d = float(li.get('Discount') or 0.0)
    except:
        # try to extract number
        m = re.search(r"(\d+(?:\.\d+)?)", str(li.get('Discount') or ''))
        d = float(m.group(1)) if m else 0.0
    discounts.append(d)

max_discount_in_quote = max(discounts) if discounts else 0.0

# Helper to extract numeric percent from text near 'discount' or 'maximum'
violating_articles = []
for k in knowledge:
    text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
    # Find patterns like 'maximum discount is 10%' or 'max discount 10 percent'
    # We look for 'max' or 'maximum' within 10 words of 'discount' and a number
    patterns = [r"(max(?:imum)?[^\.\n]{0,120}?discount[^\.\n]{0,40}?(\d+(?:\.\d+)?)[ ]?%?)",
                r"(discount[^\.\n]{0,120}?max(?:imum)?[^\.\n]{0,40}?(\d+(?:\.\d+)?)[ ]?%?)",
                r"(discount[^\.\n]{0,80}?(\d+(?:\.\d+)?)[ ]?%?)"]
    found = False
    for pat in patterns:
        for m in re.finditer(pat, text):
            # capture number
            groups = m.groups()
            # find numeric in groups
            num = None
            for g in groups[::-1]:
                if g is None: continue
                mm = re.search(r"(\d+(?:\.\d+)?)", g)
                if mm:
                    num = float(mm.group(1))
                    break
            if num is None:
                continue
            # If this article sets a maximum discount less than quote's max discount, it's a violation
            # Heuristic: if pattern contained 'max' or 'maximum' or 'cannot exceed' treat as maximum
            if 'max' in m.group(0) or 'maximum' in m.group(0) or 'cannot exceed' in m.group(0) or 'not exceed' in m.group(0):
                # num is maximum allowed percent
                if max_discount_in_quote > num + 1e-9:  # strictly greater
                    violating_articles.append({'id': k.get('id'), 'max_allowed': num, 'quote_max': max_discount_in_quote, 'snippet': m.group(0)[:300]})
                    found = True
                    break
            else:
                # If pattern is generic 'discount 10%' could be descriptive; interpret as a cap only if nearby words indicate limit
                context = m.group(0)
                if any(w in context for w in ['max', 'maximum', 'cannot', 'not exceed', 'limit', 'approval']):
                    if max_discount_in_quote > num + 1e-9:
                        violating_articles.append({'id': k.get('id'), 'max_allowed': num, 'quote_max': max_discount_in_quote, 'snippet': m.group(0)[:300]})
                        found = True
                        break
        if found:
            break

# If no explicit numeric caps found, also look for articles that explicitly say 'discounts require approval' and if quote has discount >0 then it's violation
if not violating_articles:
    for k in knowledge:
        text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
        if 'discount' in text and ('require approval' in text or 'requires approval' in text or 'approval required' in text or 'approval' in text and 'discount' in text):
            # If any discount >0, violation
            if max_discount_in_quote > 0:
                violating_articles.append({'id': k.get('id'), 'reason': 'discount requires approval', 'quote_max': max_discount_in_quote})
                break

# Choose article if any
violation_id = None
if violating_articles:
    # pick the most restrictive (smallest max_allowed) if available, otherwise first
    numeric_violations = [v for v in violating_articles if 'max_allowed' in v]
    if numeric_violations:
        numeric_violations.sort(key=lambda x: x['max_allowed'])
        violation_id = numeric_violations[0]['id']
    else:
        violation_id = violating_articles[0]['id']

# Print result as JSON-serializable string: either id or None
out = violation_id if violation_id is not None else None
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Zfg5bx9JK6QSf3ncatbFyTWK': 'file_storage/call_Zfg5bx9JK6QSf3ncatbFyTWK.json', 'var_call_CPqm0eONObe8A3HvRz3xSkmw': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_xBEvKZfQykUO7up9DOQ1Vxir': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_hPelouuwbk8zQV5wIZXpmLg0': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_RF1Z5kRgUSfjD5dmKiAS8DcH': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_MrN7AMhle3ORsDjT4nnS2GEP': []}

exec(code, env_args)
