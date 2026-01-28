code = """import json

# Load variables from storage
kb_var = var_call_KAYoOJ59ObdGKhvhEGwccHpS
quote = var_call_ewsueAqUkuu31qf7Xg9Vrvu9
qli = var_call_dbvG8lpOJvJMrhJDwlgUUK6L

# kb_var may be a filepath (string) or already loaded list
if isinstance(kb_var, str):
    with open(kb_var, 'r', encoding='utf-8') as f:
        kb = json.load(f)
else:
    kb = kb_var

# Normalize knowledge articles
for a in kb:
    # ensure keys exist
    a['title'] = a.get('title','')
    a['summary'] = a.get('summary','')
    a['faq'] = a.get('faq_answer__c','')
    a['text'] = (a['title'] + ' ' + a['summary'] + ' ' + a['faq']).lower()

# Evaluate quote discounts
violates_discount = False
max_discount = 0.0
for item in qli:
    try:
        d = float(item.get('Discount') or 0)
    except:
        d = 0.0
    if d > max_discount:
        max_discount = d
    if d > 10.0:
        violates_discount = True

# Search KB for relevant policy articles
candidates = []
for a in kb:
    text = a['text']
    if 'discount' in text and ('approval' in text or 'requires' in text or 'require' in text or 'authorization' in text or 'manager' in text):
        candidates.append(a)

# If no direct discount/approval article found, search for pricing/quote approval
if not candidates:
    for a in kb:
        text = a['text']
        if ('quote' in text or 'pricing' in text or 'approval' in text or 'discount' in text) and ('policy' in text or 'approve' in text or 'approval' in text):
            candidates.append(a)

selected_id = None
if violates_discount and candidates:
    # Prefer candidate that mentions explicit discount and approval phrases
    best = None
    best_score = -1
    for a in candidates:
        s = 0
        t = a['text']
        if 'maximum discount' in t: s += 20
        if 'discount greater' in t or 'greater than' in t and 'discount' in t: s += 15
        if 'discount' in t: s += 10
        if 'approval' in t: s += 10
        if 'requires approval' in t or 'require approval' in t or 'must be approved' in t: s += 30
        if 'manager' in t or 'director' in t: s += 5
        if s > best_score:
            best_score = s
            best = a
    if best:
        selected_id = best.get('id')

# If we didn't find discount violation or no candidates, try to find setup/installation policy violations
if selected_id is None:
    # Check if quote description or product names mention 'setup' or 'installation' fees not allowed
    quote_desc = quote[0].get('Description','').lower()
    has_setup_term = 'setup' in quote_desc or 'installation' in quote_desc or 'implementation' in quote_desc
    if has_setup_term:
        for a in kb:
            t = a['text']
            if ('setup' in t or 'installation' in t or 'implementation' in t) and ('fee' in t or 'cost' in t or 'charge' in t or 'not allowed' in t or 'prohibited' in t):
                selected_id = a.get('id')
                break

# Final result: either selected_id or None
result = selected_id if selected_id is not None else None

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ewsueAqUkuu31qf7Xg9Vrvu9': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_dbvG8lpOJvJMrhJDwlgUUK6L': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_iKYFzSdhdXQzrEdqZlFbYjSo': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99'}], 'var_call_KAYoOJ59ObdGKhvhEGwccHpS': 'file_storage/call_KAYoOJ59ObdGKhvhEGwccHpS.json'}

exec(code, env_args)
