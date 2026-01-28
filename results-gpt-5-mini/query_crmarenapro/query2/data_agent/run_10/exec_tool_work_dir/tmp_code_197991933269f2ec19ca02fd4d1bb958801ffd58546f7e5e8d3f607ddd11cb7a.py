code = """import json
# load the two large query results from storage
path1 = var_call_MKEtyWwmVTI5et9VwpDLii3v
path2 = var_call_ZmzjYtgO6917QjPOegRiNiYm

# read the json files
with open(path1, 'r') as f:
    ka_all = json.load(f)
with open(path2, 'r') as f:
    ka_filtered = json.load(f)

# We need to determine if the quote violates any knowledge article based on cost and setup.
# Load quote and quote line items and product info from storage variables available
quote = var_call_5RJxRDrPmeIjpBbdWWVJY32H[0]
items = var_call_uly0PBZ2ZF0D1SaC8tdJEhvL
products = var_call_lsGMFgOUqZgBZ7NhJRz6vXaE

# Compute totals from quote line items
total_quote = 0.0
for it in items:
    # fields are strings
    tp = float(it['TotalPrice'])
    total_quote += tp

# Also compute expected totals from unit price, quantity, discount
for it in items:
    q = float(it['Quantity'])
    up = float(it['UnitPrice'])
    disc = float(it['Discount'])

# Simple check: see if any knowledge article mentions volume-based discounts or installation timeline
violations = []
# Check for Volume-Based Discounts article id
for ka in ka_all:
    title = ka.get('title','').lower()
    faq = ka.get('faq_answer__c','').lower()
    if 'volume' in title or 'volume' in faq or 'discount' in title or 'discount' in faq:
        violations.append(ka['id'])
    if 'installation' in title or 'installation' in faq or 'install' in title or 'install' in faq or 'setup' in title or 'timeline' in faq:
        violations.append(ka['id'])

# dedupe
violations = list(dict.fromkeys(violations))

# Determine logic to pick which KA is violated: The Quote includes discounts (15%,10%,5%) and quantities (8,10,7)
# The 'Volume-Based Discounts' KA describes discounts tiers for purchases over $5/$10/$20 with absurd small numbers, but our quote totals are in thousands.
# The 'TechPulse Solution Volume-Based Installation Timeline Policy' covers setup timelines depending on volume units (1,5,15,25). The quote has quantities totaling 25 units (8+10+7=25)
# So if quote total quantity == 25, then installation timeline for large batch applies. Check that.

total_qty = sum(float(it['Quantity']) for it in items)
matched_violation = None
if total_qty == 25:
    # find the KA about Volume-Based Installation Timeline Policy
    for ka in ka_all:
        faq = ka.get('faq_answer__c','')
        if 'Volume-Based Installation Timeline Policy' in ka.get('title','') or 'Volume-Based Installation Timeline Policy' in faq:
            matched_violation = ka['id']
            break

# If not matched, maybe violates Volume-Based Discounts if discounts applied don't match policy tiers.
if not matched_violation:
    # find Volume-Based Discounts article
    for ka in ka_all:
        if 'Volume-Based Discounts' in ka.get('title',''):
            # The quote applies discounts 15%,10%,5% per line. Check if overall logic matches article which sets 5% for >$5, 10% for >$10, 15% for >$20 (absurd but we'll apply)
            # Compute per-line discount percentages and see if any exceed allowed
            mismatch = False
            for it in items:
                disc_pct = float(it['Discount'])
                # find line total before discount
                up = float(it['UnitPrice'])
                q = float(it['Quantity'])
                pre = up*q
                # Article tiers are based on purchase amount thresholds (in dollars). Using pre as purchase amount
                allowed_pct = 0
                if pre > 20:
                    allowed_pct = 15
                elif pre > 10:
                    allowed_pct = 10
                elif pre > 5:
                    allowed_pct = 5
                else:
                    allowed_pct = 0
                if disc_pct > allowed_pct:
                    mismatch = True
                    break
            if mismatch:
                matched_violation = ka['id']
                break

# Prepare output
out = None
if matched_violation:
    out = matched_violation
else:
    out = None

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5RJxRDrPmeIjpBbdWWVJY32H': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_uly0PBZ2ZF0D1SaC8tdJEhvL': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_lsGMFgOUqZgBZ7NhJRz6vXaE': [{'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_ua8Da2wKmMkD1tEtmDWJL0h0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_MKEtyWwmVTI5et9VwpDLii3v': 'file_storage/call_MKEtyWwmVTI5et9VwpDLii3v.json', 'var_call_ZmzjYtgO6917QjPOegRiNiYm': 'file_storage/call_ZmzjYtgO6917QjPOegRiNiYm.json'}

exec(code, env_args)
