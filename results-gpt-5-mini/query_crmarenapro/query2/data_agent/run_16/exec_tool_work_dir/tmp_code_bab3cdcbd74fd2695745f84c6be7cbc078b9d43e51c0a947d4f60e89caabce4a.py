code = """import json, re

# Load data from storage variables
kb_path = var_call_EJsq60vhGWHqFw5CXtxkiCYx
with open(kb_path, 'r', encoding='utf-8') as f:
    kb = json.load(f)

quote = var_call_BIrHCzMM2apIpXK477mn3kv7[0] if isinstance(var_call_BIrHCzMM2apIpXK477mn3kv7, list) and len(var_call_BIrHCzMM2apIpXK477mn3kv7)>0 else None
qlis = var_call_99zQi9M6WgJ9EQnIRgavPUSz
pbes = var_call_ya3PdpbQn96mzYZimt4haaRN

# Get max discount in the quote
discounts = []
for li in qlis:
    try:
        discounts.append(float(li.get('Discount') or 0))
    except:
        try:
            discounts.append(float(str(li.get('Discount')).replace('%','').strip()))
        except:
            discounts.append(0.0)
max_discount = max(discounts) if discounts else 0.0

# Helper to find percentage numbers in text
def find_percentages(text):
    nums = [int(m.group(1)) for m in re.finditer(r"(\d{1,3})\s*%", text)]
    return nums

violation_id = None

# Scan knowledge articles for discount/approval policies
for art in kb:
    text_parts = []
    for k in ('title','summary','faq_answer__c','urlname'):
        if k in art and art[k]:
            text_parts.append(str(art[k]))
    full = " ".join(text_parts).lower()
    if 'discount' in full or 'approval' in full or 'approval required' in full or 'maximum discount' in full or 'max discount' in full or 'no discount' in full:
        # Check for explicit 'no discounts'
        if 'no discount' in full or 'discounts not allowed' in full:
            allowed = 0.0
            if max_discount > allowed:
                violation_id = art.get('id')
                break
        # Look for patterns like 'discounts above X% require approval' or 'discounts > X% require approval'
        m = re.search(r'discounts? (?:above|greater than|over|>)\s*(\d{1,3})\s*%', full)
        if m:
            thresh = float(m.group(1))
            # If discounts above thresh require approval, then allowed without approval = thresh
            if max_discount > thresh:
                violation_id = art.get('id')
                break
        m2 = re.search(r'require approval for discounts? (?:above|over|greater than|>)?\s*(\d{1,3})\s*%', full)
        if m2:
            thresh = float(m2.group(1))
            if max_discount > thresh:
                violation_id = art.get('id')
                break
        # Look for 'maximum discount' or 'max discount X%'
        m3 = re.search(r'(?:maximum|max) discount(?: is|:)?\s*(\d{1,3})\s*%', full)
        if m3:
            allowed = float(m3.group(1))
            if max_discount > allowed:
                violation_id = art.get('id')
                break
        # Look for 'discount up to X%'
        m4 = re.search(r'discounts? up to\s*(\d{1,3})\s*%', full)
        if m4:
            allowed = float(m4.group(1))
            if max_discount > allowed:
                violation_id = art.get('id')
                break
        # Look for generic percentages near the word discount
        for match in re.finditer(r'(discount[^\.\n]{0,60}?(\d{1,3})\s*%)', full):
            pct = int(match.group(2))
            # ambiguous: assume this is allowed maximum
            if max_discount > pct:
                violation_id = art.get('id')
                break
        if violation_id:
            break

# If no explicit discount policy found, also check for 'approval' rules mentioning percentage without 'discount'
if not violation_id:
    for art in kb:
        full = " ".join([str(art.get(k,'')).lower() for k in ('title','summary','faq_answer__c')])
        m = re.search(r'approval required for.*(\d{1,3})\s*%|authorize.*(\d{1,3})\s*%|approval.*(\d{1,3})\s*%', full)
        if m:
            groups = [g for g in m.groups() if g]
            if groups:
                thresh = float(groups[0])
                if max_discount > thresh:
                    violation_id = art.get('id')
                    break

# Prepare result: return first violating article id or None
import json as _json
res = violation_id if violation_id is not None else None
print("__RESULT__:")
print(_json.dumps(res))"""

env_args = {'var_call_EJsq60vhGWHqFw5CXtxkiCYx': 'file_storage/call_EJsq60vhGWHqFw5CXtxkiCYx.json', 'var_call_99zQi9M6WgJ9EQnIRgavPUSz': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_BIrHCzMM2apIpXK477mn3kv7': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_iCRR9CVS1yQWDvjkPid5p9PW': [], 'var_call_ya3PdpbQn96mzYZimt4haaRN': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_jNvMeUixr0AFqsXYKbq9d4tJ': []}

exec(code, env_args)
