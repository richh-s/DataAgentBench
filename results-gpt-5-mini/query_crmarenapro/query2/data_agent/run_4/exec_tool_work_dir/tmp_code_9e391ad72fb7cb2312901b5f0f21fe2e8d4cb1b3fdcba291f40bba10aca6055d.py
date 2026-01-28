code = """import json, re

with open(var_call_Zfg5bx9JK6QSf3ncatbFyTWK, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

quote = var_call_CPqm0eONObe8A3HvRz3xSkmw[0] if isinstance(var_call_CPqm0eONObe8A3HvRz3xSkmw, list) and var_call_CPqm0eONObe8A3HvRz3xSkmw else None
qline = var_call_xBEvKZfQykUO7up9DOQ1Vxir

# compute max discount
discounts = []
for li in qline:
    try:
        d = float(li.get('Discount') or 0.0)
    except:
        m = re.search('(\\d+(?:\\.\\d+)?)', str(li.get('Discount') or ''))
        d = float(m.group(1)) if m else 0.0
    discounts.append(d)

max_discount = max(discounts) if discounts else 0.0

violating = None
for k in knowledge:
    text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
    m = re.search('(?:max(?:imum)?[^\.\n]{0,120}?discount[^\.\n]{0,40}?(\\d+(?:\\.\\d+)?))', text)
    if m:
        num = float(m.group(1))
        if max_discount > num + 1e-9:
            violating = k.get('id')
            break
    m2 = re.search('discount[^\.\n]{0,80}(\\d+(?:\\.\\d+)?)[ ]?%', text)
    if m2 and ('approve' in text or 'cannot exceed' in text or 'not exceed' in text or 'limit' in text):
        num = float(m2.group(1))
        if max_discount > num + 1e-9:
            violating = k.get('id')
            break

if not violating:
    for k in knowledge:
        text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
        if 'discount' in text and ('require approval' in text or 'requires approval' in text or 'approval required' in text or ('approval' in text and 'discount' in text)):
            if max_discount > 0:
                violating = k.get('id')
                break

print("__RESULT__:")
print(json.dumps(violating))"""

env_args = {'var_call_Zfg5bx9JK6QSf3ncatbFyTWK': 'file_storage/call_Zfg5bx9JK6QSf3ncatbFyTWK.json', 'var_call_CPqm0eONObe8A3HvRz3xSkmw': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_xBEvKZfQykUO7up9DOQ1Vxir': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_hPelouuwbk8zQV5wIZXpmLg0': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_RF1Z5kRgUSfjD5dmKiAS8DcH': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_MrN7AMhle3ORsDjT4nnS2GEP': []}

exec(code, env_args)
