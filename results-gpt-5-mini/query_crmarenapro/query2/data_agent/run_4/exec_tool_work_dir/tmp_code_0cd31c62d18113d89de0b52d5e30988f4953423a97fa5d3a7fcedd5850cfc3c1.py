code = """import json, re

with open(var_call_Zfg5bx9JK6QSf3ncatbFyTWK, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

qline = var_call_xBEvKZfQykUO7up9DOQ1Vxir

max_discount = 0.0
for li in qline:
    val = li.get('Discount') or '0'
    try:
        d = float(val)
    except Exception:
        m = re.search(r"(\d+(?:\.\d+)?)", str(val))
        d = float(m.group(1)) if m else 0.0
    if d > max_discount:
        max_discount = d

violation_id = None
patterns = [
    r"max(?:imum)?\s+(?:discount|discounts)[^\d]{0,40}(\d+(?:\.\d+)?)\s*%?",
    r"discounts?[^\d]{0,40}max(?:imum)?[^\d]{0,40}(\d+(?:\.\d+)?)\s*%?",
    r"discounts?[^\d]{0,40}cannot\s+exceed[^\d]{0,40}(\d+(?:\.\d+)?)\s*%?",
    r"discounts?[^\d]{0,40}not\s+exceed[^\d]{0,40}(\d+(?:\.\d+)?)\s*%?"
]

for k in knowledge:
    text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
    text = text.replace('\n', ' ')
    found = False
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            try:
                num = float(m.group(1))
            except Exception:
                continue
            if max_discount > num + 1e-9:
                violation_id = k.get('id')
                found = True
                break
    if found:
        break

if not violation_id:
    for k in knowledge:
        text = ' '.join([str(k.get('title') or ''), str(k.get('faq_answer__c') or ''), str(k.get('summary') or '')]).lower()
        if 'discount' in text and 'approval' in text:
            if max_discount > 0:
                violation_id = k.get('id')
                break

print("__RESULT__:")
print(json.dumps(violation_id))"""

env_args = {'var_call_Zfg5bx9JK6QSf3ncatbFyTWK': 'file_storage/call_Zfg5bx9JK6QSf3ncatbFyTWK.json', 'var_call_CPqm0eONObe8A3HvRz3xSkmw': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_xBEvKZfQykUO7up9DOQ1Vxir': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_hPelouuwbk8zQV5wIZXpmLg0': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_RF1Z5kRgUSfjD5dmKiAS8DcH': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_MrN7AMhle3ORsDjT4nnS2GEP': []}

exec(code, env_args)
