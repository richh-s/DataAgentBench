code = """import json, re, pandas as pd

# Load previous tool results from storage variables
kb_path = var_call_Y8p2UXjr0ihoEzQaBmWiDTRX
quote = var_call_4sErjXSQvUUaA8Syd4b209Lc[0]
q_line_items = var_call_T6ilSsnS1Rhv6CYlBqsrbK9K

# Read the knowledge articles JSON file (path provided in kb_path)
with open(kb_path, 'r') as f:
    kb = json.load(f)

# Convert to DataFrame for easier searching
df_kb = pd.DataFrame(kb)

# Prepare text fields to search
df_kb['text'] = (df_kb.get('title','').fillna('') + ' ' + df_kb.get('faq_answer__c','').fillna('') + ' ' + df_kb.get('summary','').fillna(''))

# Compute max discount in quote
discounts = []
for li in q_line_items:
    try:
        discounts.append(float(str(li.get('Discount','0')).strip()))
    except:
        pass
max_discount = max(discounts) if discounts else 0.0

# Search KB for discount-related policies
candidates = []
for idx, row in df_kb.iterrows():
    text = row['text'].lower()
    if 'discount' in text or 'setup' in text or 'setup fee' in text or 'approval' in text or 'approve' in text:
        # try to find percentage numbers near 'discount'
        # find patterns like '10%', '10 %', 'ten percent', or 'must not exceed 10%'
        pct_matches = re.findall(r"(\d{1,3}(?:\.\d+)?)[ ]?%", row['text'])
        # also find patterns like 'percent' with number before
        pct_matches += re.findall(r"(\d{1,3}(?:\.\d+)?)\s+percent", row['text'].lower())
        # also look for phrases implying maximums e.g., 'no more than 10%','must not exceed 10%', 'requires approval for discounts over 10%'
        max_hit = None
        if pct_matches:
            # take smallest percentage mentioned as a conservative policy threshold
            nums = [float(x) for x in pct_matches]
            max_hit = min(nums)
        else:
            # look for phrases with numbers spelled out? skip for now
            pass

        candidates.append({'id': row.get('id'), 'title': row.get('title'), 'summary': row.get('summary'), 'text': row.get('faq_answer__c'), 'pct_threshold': max_hit})

# Now determine which candidate is violated: pct_threshold exists and max_discount > pct_threshold
violations = []
for c in candidates:
    if c['pct_threshold'] is not None:
        try:
            if max_discount > float(c['pct_threshold']):
                violations.append(c)
        except:
            pass

# If we found violations, pick the first one (or any). Otherwise, check for setup fee policies (not applicable here) or 'requires approval' phrases that indicate conflict if Status is 'Needs Review' and discount > 0
result_id = None
if violations:
    result_id = violations[0]['id']
else:
    # look for approval-related articles that require approval for any discount or for quotes 'Needs Review'
    for c in candidates:
        txt = (c['title'] or '') + ' ' + (c['summary'] or '') + ' ' + (c['text'] or '')
        txt = txt.lower()
        if 'requires approval' in txt or 'require approval' in txt or 'must be approved' in txt or 'needs approval' in txt:
            # if quote status is 'Needs Review' and has non-zero discount, consider it a conflict
            if quote.get('Status','').lower() == 'needs review' and max_discount > 0:
                result_id = c['id']
                break

# If still none, return None
out = result_id if result_id is not None else None

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_4sErjXSQvUUaA8Syd4b209Lc': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_T6ilSsnS1Rhv6CYlBqsrbK9K': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_Cywnsu5aVSAfrU0wP6ZhD7c2': [{'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'PricebookEntryId': '01uWt0000027P3lIAE', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_gcyMzSzSZwZyimZpGnmkKrPG': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_TEHmo2WEZOisDnIdh2dgtOzJ': [], 'var_call_Y8p2UXjr0ihoEzQaBmWiDTRX': 'file_storage/call_Y8p2UXjr0ihoEzQaBmWiDTRX.json'}

exec(code, env_args)
