code = """import json, re
# Load variables from storage
q = var_call_3j0PomkjMx3LGgU9cYlCEPPK
qlis = var_call_O9xsQ3fepwywhITHHLwsn2m7
products = var_call_HK6tH0ygEBsbIbEn3fBRsfrX

# Load knowledge articles - may be large file path or list
def load_knowledge(var):
    if isinstance(var, str):
        # it's a filepath to a JSON file
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

k_all = load_knowledge(var_call_06p3uiZELRaSmbXDvisOgQEh)
k_filtered = load_knowledge(var_call_26vMlTuRnPHCycpRNrtkblQv)

# Combine and deduplicate by id
k_map = {}
for item in (k_all or []) + (k_filtered or []):
    if not item: continue
    k_map[item.get('id')] = item
knowledge = list(k_map.values())

# Compute quote totals
def to_float(x):
    try:
        return float(x)
    except:
        return 0.0

subtotal = 0.0
for li in qlis:
    qty = to_float(li.get('Quantity'))
    up = to_float(li.get('UnitPrice'))
    subtotal += qty * up

# Analyze knowledge articles for discount/approval rules
violating_article_id = None

# Search for specific "Volume-Based Discounts" article first
for art in knowledge:
    title = (art.get('title') or '').lower()
    faq = (art.get('faq_answer__c') or '').lower()
    summary = (art.get('summary') or '').lower()
    text = title + "\n" + faq + "\n" + summary
    if 'volume-based discounts' in title or 'volume-based discounts' in summary or 'volume-based discounts' in faq:
        # This article defines tiered discounts; check if per-transaction thresholds match applied discounts
        # Extract tiers from text using regex like '(
        # 1. **5% Discount for Purchases Over $5**' pattern
        percents = re.findall(r'(\d+)%', art.get('faq_answer__c') or '')
        # convert to ints
        try:
            tiers = [int(p) for p in percents]
        except:
            tiers = []
        # If tiers found, ensure that discounts applied do not exceed max tier
        if tiers:
            max_tier = max(tiers)
            # find any line item discount > max_tier
            for li in qlis:
                d = to_float(li.get('Discount'))
                if d > max_tier:
                    violating_article_id = art.get('id')
                    break
            # if no per-line violation but overall subtotal qualifies for higher discount than applied on lines
            # Determine allowed overall discount based on subtotal
            allowed = 0
            # find thresholds with their percents: look for patterns like '(
            # 1. **5% Discount for Purchases Over $5**'
            thresholds = re.findall(r'(\*\*|\*?)?(\d+)%[\s\S]*?over \$?(\d+)', art.get('faq_answer__c') or '', re.I)
            # thresholds is list of tuples; parse
            try:
                parsed = [(int(m[0] if m[0] else m[1]), int(m[2])) for m in thresholds]
            except:
                parsed = []
            # simpler: if subtotal > $20 and max_tier==15, then allowed 15
            if subtotal > 20 and max_tier>=15:
                allowed = max_tier
            elif subtotal > 10 and max_tier>=10:
                allowed = 10
            elif subtotal > 5 and max_tier>=5:
                allowed = 5
            # Check if any line has discount less than allowed - that's not a violation. Violation only if a line has discount > allowed
            if not violating_article_id:
                for li in qlis:
                    d = to_float(li.get('Discount'))
                    if d > allowed:
                        violating_article_id = art.get('id')
                        break
        else:
            # No percents found; skip
            pass
    if violating_article_id:
        break

# If not found, search for any article that explicitly limits discounts or requires approval
if not violating_article_id:
    for art in knowledge:
        content = ' '.join([str(art.get(k,'')) for k in ('title','faq_answer__c','summary')]).lower()
        if 'discount' in content and ('approval' in content or 'requires approval' in content or 'approval required' in content or 'must be approved' in content or 'manager approval' in content or 'authorization' in content or 'approval matrix' in content or 'requires manager' in content):
            # Try to find a percent threshold
            percents = re.findall(r'(\d+)%', content)
            percents = [int(p) for p in percents]
            if percents:
                min_threshold = min(percents)
                # if any line discount exceeds min_threshold, mark violation
                for li in qlis:
                    if to_float(li.get('Discount')) > min_threshold:
                        violating_article_id = art.get('id')
                        break
            else:
                # If article mentions approval for discounts but no threshold, any non-zero discount might require approval
                for li in qlis:
                    if to_float(li.get('Discount')) > 0:
                        violating_article_id = art.get('id')
                        break
        if violating_article_id:
            break

# As a fallback, check for 'setup' or 'setup fee' policy violations
if not violating_article_id:
    for art in knowledge:
        content = ' '.join([str(art.get(k,'')) for k in ('title','faq_answer__c','summary')]).lower()
        if 'setup' in content and ('fee' in content or 'cost' in content) and ('approval' in content or 'not allowed' in content or 'requires' in content):
            # If quote has any mention of setup fees? We don't have setup fees data; skip
            violating_article_id = art.get('id')
            break

# Prepare result: if violating_article_id else None
res = violating_article_id if violating_article_id else None

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_3j0PomkjMx3LGgU9cYlCEPPK': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_O9xsQ3fepwywhITHHLwsn2m7': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_HK6tH0ygEBsbIbEn3fBRsfrX': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'UnitPrice': '499.99'}], 'var_call_06p3uiZELRaSmbXDvisOgQEh': 'file_storage/call_06p3uiZELRaSmbXDvisOgQEh.json', 'var_call_26vMlTuRnPHCycpRNrtkblQv': 'file_storage/call_26vMlTuRnPHCycpRNrtkblQv.json'}

exec(code, env_args)
