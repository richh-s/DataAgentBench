code = """import json, re
# Access stored query results
q = var_call_3j0PomkjMx3LGgU9cYlCEPPK
qlis = var_call_O9xsQ3fepwywhITHHLwsn2m7
products = var_call_HK6tH0ygEBsbIbEn3fBRsfrX

# Function to load knowledge variable which may be a filepath
def load_var(v):
    if isinstance(v, str):
        try:
            with open(v, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return []
    return v or []

k_all = load_var(var_call_06p3uiZELRaSmbXDvisOgQEh)
k_filtered = load_var(var_call_26vMlTuRnPHCycpRNrtkblQv)

# Combine unique knowledge articles by id
k_map = {}
for item in (k_all or []) + (k_filtered or []):
    if not item:
        continue
    k_map[item.get('id')] = item
knowledge = list(k_map.values())

# Helper
def to_float(x):
    try:
        return float(x)
    except Exception:
        return 0.0

# Compute subtotal (pre-discount) based on Quantity * UnitPrice per line
subtotal = 0.0
for li in qlis:
    subtotal += to_float(li.get('Quantity')) * to_float(li.get('UnitPrice'))

violating_article_id = None

# First, look for explicit "Volume-Based Discounts" article
for art in knowledge:
    title = (art.get('title') or '').lower()
    faq = (art.get('faq_answer__c') or '').lower()
    summary = (art.get('summary') or '').lower()
    content = title + '\n' + faq + '\n' + summary
    if 'volume-based discounts' in content:
        # extract percent tiers
        percents = [int(p) for p in re.findall(r"(\d+)%", (art.get('faq_answer__c') or ''))]
        max_tier = max(percents) if percents else None
        # Determine allowed overall discount based on subtotal and textual thresholds
        allowed = None
        # Look for patterns like '5% Discount for Purchases Over $5' to map thresholds
        thresholds = re.findall(r"(\d+)%[\s\S]*?over \$?(\d+)", (art.get('faq_answer__c') or ''), re.I)
        # thresholds -> list of tuples (percent, amount)
        parsed = []
        for p,a in thresholds:
            try:
                parsed.append((int(p), float(a)))
            except:
                pass
        if parsed:
            # sort by amount ascending
            parsed.sort(key=lambda x: x[1])
            allowed = 0
            for pct, amt in parsed:
                if subtotal > amt:
                    allowed = max(allowed, pct)
        elif max_tier is not None:
            # fallback: if subtotal > 20 assume max_tier applies (as in article preview)
            if subtotal > 20:
                allowed = max_tier
            elif subtotal > 10:
                allowed = min(max_tier, 10)
            elif subtotal > 5:
                allowed = min(max_tier, 5)
            else:
                allowed = 0
        # Now check line item discounts against allowed
        if allowed is not None:
            for li in qlis:
                if to_float(li.get('Discount')) > allowed:
                    violating_article_id = art.get('id')
                    break
        if violating_article_id:
            break

# If still not found, look for any article that mentions discount and approval requirements
if not violating_article_id:
    for art in knowledge:
        text = ' '.join([str(art.get('title','')), str(art.get('faq_answer__c','')), str(art.get('summary',''))]).lower()
        if 'discount' in text and ('approval' in text or 'requires approval' in text or 'approval required' in text or 'must be approved' in text or 'manager approval' in text or 'authorization' in text or 'approval matrix' in text or 'requires manager' in text):
            # find numeric threshold in context
            nums = re.findall(r"(\d+)%", text)
            if nums:
                # assume smallest percent is threshold requiring approval
                threshold = min(int(n) for n in nums)
                for li in qlis:
                    if to_float(li.get('Discount')) > threshold:
                        violating_article_id = art.get('id')
                        break
            else:
                # no numeric threshold; assume any discount needs approval
                for li in qlis:
                    if to_float(li.get('Discount')) > 0:
                        violating_article_id = art.get('id')
                        break
        if violating_article_id:
            break

# No setup fee info in quote; skip setup fee checks

result = violating_article_id if violating_article_id else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3j0PomkjMx3LGgU9cYlCEPPK': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_O9xsQ3fepwywhITHHLwsn2m7': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_HK6tH0ygEBsbIbEn3fBRsfrX': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'UnitPrice': '499.99'}], 'var_call_06p3uiZELRaSmbXDvisOgQEh': 'file_storage/call_06p3uiZELRaSmbXDvisOgQEh.json', 'var_call_26vMlTuRnPHCycpRNrtkblQv': 'file_storage/call_26vMlTuRnPHCycpRNrtkblQv.json'}

exec(code, env_args)
