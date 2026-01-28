code = """import json, re
# Load stored results
quote = var_call_Ys6o1gSM3k3IhVeExqTiKtLT[0]
ql_items = var_call_81bgoWj3L9aL5Ze2cO91vQWg
# Load knowledge articles JSON file
kp = var_call_XPefcYW9zrwvRYGcx1KENl29
with open(kp, 'r') as f:
    articles = json.load(f)

# Compute total quote price
total = 0.0
for li in ql_items:
    try:
        total += float(li.get('TotalPrice') or 0)
    except:
        # try compute from Quantity * UnitPrice * (1 - Discount/100)
        try:
            qty = float(li.get('Quantity') or 0)
            unit = float(li.get('UnitPrice') or 0)
            disc = float(li.get('Discount') or 0)
            total += qty * unit * (1 - disc/100)
        except:
            pass

# Normalize articles text and search for relevant policies
violating_article_id = None
# Patterns indicating discount approval thresholds or forbids
patterns = [r'discount(s)? (over|above|greater than) (\$?\d+|\d+%|\d+ percent)',
            r'discount(s)? (of )?\d+% require',
            r'requires approval.*discount',
            r'discount.*require(s)? approval',
            r'approval.*discount.*%']
# Also look for setup fee policy
setup_patterns = [r'setup fee', r'setup.*fee', r'implementation fee', r'one[- ]time fee']

for art in articles:
    text = ' '.join(filter(None, [art.get('title',''), art.get('faq_answer__c',''), art.get('summary','')])).lower()
    # search for discount/approval policy
    for pat in patterns:
        if re.search(pat, text):
            violating_article_id = art.get('id')
            break
    if violating_article_id:
        break
    for pat in setup_patterns:
        if re.search(pat, text):
            # mark as relevant but only if setup fees present in quote (we don't see any)
            # for now capture first setup article id for potential check
            maybe_setup_id = art.get('id')
            # continue searching for discount policies

# Determine if any discount exceeds typical threshold found in articles
# Try to extract numeric threshold from the matched article if available
threshold = None
if violating_article_id:
    # find the article and extract a percent threshold
    art = next((a for a in articles if a.get('id')==violating_article_id), None)
    if art:
        t = (art.get('faq_answer__c','') or '') + ' ' + (art.get('summary','') or '') + ' ' + (art.get('title','') or '')
        m = re.search(r'(?:over|above|greater than)\s*(\d+)%', t)
        if not m:
            m = re.search(r'>(\d+)%', t)
        if m:
            threshold = int(m.group(1))

# Check quote line item discounts
max_discount = 0.0
for li in ql_items:
    try:
        d = float(li.get('Discount') or 0)
        if d > max_discount:
            max_discount = d
    except:
        pass

# Simple decision logic: if we found an article with discount approval language and quote has discount exceeding any mentioned percentage, it's a violation.
violation = False
if violating_article_id and threshold is not None:
    if max_discount > threshold:
        violation = True
elif violating_article_id:
    # if article mentions discount approval but no explicit threshold, assume any discount over 10% requires approval
    if max_discount > 10:
        violation = True

# Also check for setup fees in quote - there are none in line items or description
has_setup_fee = False
# (No explicit setup fees in QuoteLineItems)

# Prepare output: if violation True, return the article id, else None
out = violating_article_id if violation else None

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Ys6o1gSM3k3IhVeExqTiKtLT': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_81bgoWj3L9aL5Ze2cO91vQWg': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_5zV1FMtWQx7gzTiWEyeoHw6t': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'PricebookEntryId': '01uWt0000027P3lIAE', 'UnitPrice': '499.99', 'PricebookId': 'None', 'PricebookName': 'None'}], 'var_call_v2b01xTPbYREqOFGwQTj5eki': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_o0biAM7YsGTPQndoiKNefW2i': [], 'var_call_XPefcYW9zrwvRYGcx1KENl29': 'file_storage/call_XPefcYW9zrwvRYGcx1KENl29.json'}

exec(code, env_args)
