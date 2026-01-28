code = """import json, re

# Load knowledge articles from the stored file
kb_path = var_call_BjZb8IefGtOzjnPwrwo4ZbN7
with open(kb_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Quote and line items are available as variables
quote = var_call_oAoW7n0s9l2iIViuXEoBD1Ji[0] if isinstance(var_call_oAoW7n0s9l2iIViuXEoBD1Ji, list) and var_call_oAoW7n0s9l2iIViuXEoBD1Ji else None
line_items = var_call_RjELb5wJVTfIwrs5bjojlhC0

# Helper to find numeric percentages in text
def extract_percentages(text):
    return [int(m.group(1)) for m in re.finditer(r"(\d{1,3})\s*%", text)]

# Helper to find numeric phrases like 'over 10 percent' or 'greater than 10%'
def extract_percent_numbers(text):
    nums = []
    for m in re.finditer(r"(\d{1,3})\s*(percent|percentage|%)", text):
        nums.append(int(m.group(1)))
    for m in re.finditer(r"(over|greater than|above|more than)\s+(\d{1,3})", text):
        nums.append(int(m.group(2)))
    for m in re.finditer(r"(max(?:imum)?|no more than|not exceed)\s+(\d{1,3})\s*(percent|%)", text):
        nums.append(int(m.group(2)))
    return nums

# Normalize text
def norm(t):
    return (t or "").lower()

# Gather candidate policy articles
candidates = []
for a in articles:
    combined = ' '.join([str(a.get('title','') or ''), str(a.get('faq_answer__c','') or ''), str(a.get('summary','') or '')])
    lc = combined.lower()
    if any(k in lc for k in ['discount', 'approval', 'requires approval', 'approval required', 'setup', 'setup fee', 'installation', 'professional services', 'one-time', 'discounts over', 'maximum discount', 'price', 'pricing', 'quote approval', 'approval limit']):
        percents = extract_percentages(combined)
        nums = extract_percent_numbers(combined)
        candidates.append({'id': a.get('id'), 'title': a.get('title'), 'text': combined, 'percents': percents, 'nums': nums})

# If no candidates, return None
violating_article_id = None

# Compute discounts in quote
discounts = []
for li in line_items:
    try:
        d = float(li.get('Discount') or li.get('discount') or 0)
    except:
        d = 0.0
    discounts.append(d)

# Check candidates for explicit rules
for c in candidates:
    text = c['text'].lower()
    # If article mentions 'requires approval' or 'approval required' and mentions a percentage threshold
    if ('approval' in text or 'requires approval' in text or 'approval required' in text) and (c['percents'] or c['nums']):
        # take the maximum referenced threshold as conservative
        thresholds = c['percents'] + c['nums']
        thresholds = thresholds if thresholds else []
        if thresholds:
            max_threshold = max(thresholds)
            # if any line item discount > max_threshold -> violation
            for d in discounts:
                if d > max_threshold:
                    violating_article_id = c['id']
                    break
    # If article states 'no discounts over X' or 'maximum discount X%'
    elif re.search(r"no discounts over|maximum discount|no more than .* percent|not exceed .* percent|do not exceed .* percent", text):
        thresholds = c['percents'] + c['nums']
        if thresholds:
            max_threshold = max(thresholds)
            for d in discounts:
                if d > max_threshold:
                    violating_article_id = c['id']
                    break
    # If article forbids setup fees and quote seems to include a setup product name
    elif 'setup fee' in text or 'setup costs' in text or 'no setup fee' in text:
        # try to detect setup-like product names in line items by product ids (not reliable)
        # If any product id contains 'setup' or 'installation' assume violation
        for li in line_items:
            pid = (li.get('Product2Id') or '').lower()
            if 'setup' in pid or 'install' in pid or 'setup' in (li.get('Description') or '').lower():
                violating_article_id = c['id']
                break
    if violating_article_id:
        break

# Fallback: if no explicit candidate rules found but there exists an article titled or summarized as 'Discount Policy' or 'Quote Approval Guide'
if not violating_article_id:
    for a in articles:
        t = (a.get('title') or '').lower()
        s = (a.get('summary') or '').lower()
        if 'discount policy' in t or 'discount policy' in s or 'quote approval' in t or 'quote approval' in s or 'approval guide' in t:
            # if any discount > 10, assume policy violation if article mentions 10 in text
            if any(d > 10 for d in discounts):
                violating_article_id = a.get('id')
                break

# Prepare result as JSON serializable: either id string or None
result = violating_article_id if violating_article_id is not None else None

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BjZb8IefGtOzjnPwrwo4ZbN7': 'file_storage/call_BjZb8IefGtOzjnPwrwo4ZbN7.json', 'var_call_oAoW7n0s9l2iIViuXEoBD1Ji': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_RjELb5wJVTfIwrs5bjojlhC0': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_jZXeiS8eJiBbdbAXIG1s75ZM': []}

exec(code, env_args)
