code = """import json
# data from previous tool calls
quotes = var_call_H2cqgkxtZKTwYGbN3fsB5MOX
qlis = var_call_dxlhu94sEcG4RQQTm9T5tbj4
products = var_call_sACMVu6qMWeCLBLNVXpFlUDT
# load knowledge articles from file
file_path = var_call_fPLLH4nl9Mdxu0QNTcqoFZkN
with open(file_path, 'r', encoding='utf-8') as f:
    k_articles = json.load(f)

# normalize and compute quote totals
def to_float(x):
    try:
        return float(x)
    except:
        return None

for q in qlis:
    q['UnitPrice_f'] = to_float(q.get('UnitPrice'))
    q['Quantity_f'] = to_float(q.get('Quantity'))
    q['Discount_f'] = to_float(q.get('Discount'))
    q['TotalPrice_f'] = to_float(q.get('TotalPrice'))

quote_total = sum([q['TotalPrice_f'] for q in qlis if q['TotalPrice_f'] is not None])
# compute weighted average discount
numer = 0.0
denom = 0.0
for q in qlis:
    if q['UnitPrice_f'] is not None and q['Quantity_f'] is not None:
        numer += q['Discount_f'] * q['UnitPrice_f'] * q['Quantity_f']
        denom += q['UnitPrice_f'] * q['Quantity_f']
avg_discount = (numer/denom) if denom else 0.0

# Search knowledge articles for policy-like rules about discounts, approvals, setup fees, pricing
violations = []
keywords = ['discount', 'approval', 'approve', 'pricing', 'price', 'setup', 'setup fee', 'fee', 'margin', 'authorize', 'authorization', 'discounts']
for art in k_articles:
    text = ' '.join([str(art.get('title','')), str(art.get('faq_answer__c','')), str(art.get('summary',''))]).lower()
    if any(k in text for k in keywords):
        violations.append({'id': art.get('id'), 'title': art.get('title'), 'text': text})

# Now try to detect explicit numeric rules in candidate articles
import re
violation_id = None
for art in violations:
    t = art['text']
    # look for patterns like 'discount.*(\d+)%' or 'greater than (\d+)%' and 'require' or 'approval'
    m = re.search(r'discount[^\d\n\r\%]{0,30}(?:of)?\s*(\d{1,2})\s*%?', t)
    if not m:
        m = re.search(r'(?:(?:greater than|more than|over)\s*)(\d{1,2})\s*%?', t)
    if not m:
        m = re.search(r'(\d{1,2})%.*discount', t)
    if m:
        try:
            pct = float(m.group(1))
        except:
            pct = None
        if pct is not None:
            # find if text indicates approval required beyond this pct
            if 'approval' in t or 'approve' in t or 'authorization' in t or 'authorize' in t:
                # if avg_discount exceeds pct, flag
                if avg_discount > pct:
                    violation_id = art['id']
                    break
            else:
                # if text says "discounts over X% are not permitted" or similar
                if re.search(r'not permit|not allowed|forbidden|prohibit', t) and avg_discount > pct:
                    violation_id = art['id']
                    break
# If not found by numeric heuristics, check for explicit phrases forbidding setup waivers or free setup
if violation_id is None:
    for art in violations:
        t = art['text']
        # If quote contains setup fee line? Our quote has no explicit setup item; check if any product descriptions mention 'setup' cost
        if 'setup' in t and ('not allowed' in t or 'forbidden' in t or 'must not' in t or 'no setup' in t or 'free setup' in t):
            # but since our quote doesn't include setup, likely no violation
            pass

# As fallback, if any article explicitly states discounts require approval for discounts >=10% and our avg_discount >10
if violation_id is None:
    for art in violations:
        t = art['text']
        if 'discount' in t and ('approval' in t or 'requires approval' in t or 'must be approved' in t):
            # assume threshold 10% if unspecified
            if avg_discount > 10.0:
                violation_id = art['id']
                break

# If still none, set result to None
result = violation_id if violation_id is not None else None

# Prepare final string output (just the id or None)
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_H2cqgkxtZKTwYGbN3fsB5MOX': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_dxlhu94sEcG4RQQTm9T5tbj4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_sACMVu6qMWeCLBLNVXpFlUDT': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99'}], 'var_call_fPLLH4nl9Mdxu0QNTcqoFZkN': 'file_storage/call_fPLLH4nl9Mdxu0QNTcqoFZkN.json'}

exec(code, env_args)
