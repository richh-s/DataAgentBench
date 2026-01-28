code = """import json
# Load previous tool results
quote_lines = var_call_c6RRAuPAvFGxeDuFXh95bq40
# knowledge file path
knowledge_path = var_call_4VcG3YrGOXDHlmkHiT7k0KEA

# Read the knowledge articles file
with open(knowledge_path, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Normalize quote line discounts
discounts = []
for li in quote_lines:
    try:
        discounts.append(float(li.get('Discount') or li.get('discount') or 0.0))
    except:
        try:
            discounts.append(float(str(li.get('Discount')).strip()))
        except:
            discounts.append(0.0)
max_discount = max(discounts) if discounts else 0.0

# Search knowledge articles for discount/approval rules
candidates = []
for art in knowledge:
    art_text = ' '.join([str(art.get('title','') or ''), str(art.get('summary','') or ''), str(art.get('faq_answer__c','') or '')]).lower()
    if 'discount' in art_text or 'approval' in art_text or 'price' in art_text or 'pricing' in art_text or 'approve' in art_text or '%' in art_text:
        # look for explicit percentage rules
        pct_rules = []
        import re
        for m in re.finditer(r'(?:no more than|maximum|max(?:imum)?|must not exceed|cannot exceed|limit(?:ed)? to|up to|at least|at most|require(?:s)? approval for|requires approval for|requires manager approval for|approval required for)?\s*(\d{1,3})%\s*(?:discount|off)?', art_text):
            try:
                pct = int(m.group(1))
                pct_rules.append(pct)
            except:
                pass
        # Also detect phrases like 'discounts above 10% require approval'
        approval_flag = False
        if 'require' in art_text or 'approval' in art_text or 'manager' in art_text or 'approve' in art_text:
            approval_flag = True
        candidates.append({'id': art.get('id'), 'title': art.get('title'), 'text': art_text, 'pct_rules': pct_rules, 'approval_flag': approval_flag})

# Determine violation: if any candidate has a pct_rule less than max_discount, or mentions discounts requiring approval and max_discount > 10 (common threshold)
violating_id = None
# First prefer explicit numeric rules
for c in candidates:
    if c['pct_rules']:
        # if any rule value is less than max_discount -> violation
        for rule in c['pct_rules']:
            if max_discount > rule:
                violating_id = c['id']
                break
    if violating_id:
        break
# If no explicit numeric rule found, check for approval_flag with language indicating approvals for discounts and assume threshold 10%
if not violating_id:
    for c in candidates:
        if c['approval_flag'] and 'discount' in c['text']:
            # assume policy that discounts require approval beyond 10%
            if max_discount > 10.0:
                violating_id = c['id']
                break

# If nothing found, set result to None
result = violating_id if violating_id is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XJPmtOMq3vKsYbD1Yuf34LpJ': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_c6RRAuPAvFGxeDuFXh95bq40': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_zRQ5ObqViKG7t184bsAMh6QW': [], 'var_call_4VcG3YrGOXDHlmkHiT7k0KEA': 'file_storage/call_4VcG3YrGOXDHlmkHiT7k0KEA.json'}

exec(code, env_args)
