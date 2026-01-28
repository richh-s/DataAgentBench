code = """import json

# Load knowledge articles from storage
with open(var_call_Zfg5bx9JK6QSf3ncatbFyTWK, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Load quote line items
qline = var_call_xBEvKZfQykUO7up9DOQ1Vxir

# Compute max discount
max_discount = 0.0
for li in qline:
    val = li.get('Discount')
    try:
        d = float(val)
    except Exception:
        # extract digits and dot
        s = ''.join(ch for ch in str(val or '') if (ch.isdigit() or ch == '.'))
        try:
            d = float(s) if s else 0.0
        except Exception:
            d = 0.0
    if d > max_discount:
        max_discount = d

# Phrases indicating caps or limits
phrases = [
    'maximum discount', 'max discount', 'discounts cannot exceed', 'discount cannot exceed',
    'discounts not exceed', 'discount not exceed', 'cannot exceed discount', 'not exceed discount',
    'discount limit', 'discounts limit', 'cannot exceed'
]

violation_id = None
for k in knowledge:
    text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
    # normalize newlines
    text = text.replace(chr(10), ' ')
    found = False
    for ph in phrases:
        idx = text.find(ph)
        if idx != -1:
            snippet = text[idx: idx+120]
            # find first number in snippet
            num = None
            num_chars = ''
            for ch in snippet:
                if ch.isdigit() or ch == '.':
                    num_chars += ch
                elif num_chars:
                    break
            if num_chars:
                try:
                    num = float(num_chars)
                except Exception:
                    num = None
            # If numeric cap found, compare
            if num is not None:
                if max_discount > num + 1e-9:
                    violation_id = k.get('id')
                    found = True
                    break
            else:
                # No numeric but phrase indicates a limit; treat any discount >0 as violation
                if max_discount > 0:
                    violation_id = k.get('id')
                    found = True
                    break
    if found:
        break

# Fallback: if article mentions discount and approval
if not violation_id:
    for k in knowledge:
        text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
        text = text.replace(chr(10), ' ')
        if 'discount' in text and 'approval' in text:
            if max_discount > 0:
                violation_id = k.get('id')
                break

print("__RESULT__:")
print(json.dumps(violation_id))"""

env_args = {'var_call_Zfg5bx9JK6QSf3ncatbFyTWK': 'file_storage/call_Zfg5bx9JK6QSf3ncatbFyTWK.json', 'var_call_CPqm0eONObe8A3HvRz3xSkmw': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_xBEvKZfQykUO7up9DOQ1Vxir': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_hPelouuwbk8zQV5wIZXpmLg0': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_RF1Z5kRgUSfjD5dmKiAS8DcH': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_MrN7AMhle3ORsDjT4nnS2GEP': []}

exec(code, env_args)
