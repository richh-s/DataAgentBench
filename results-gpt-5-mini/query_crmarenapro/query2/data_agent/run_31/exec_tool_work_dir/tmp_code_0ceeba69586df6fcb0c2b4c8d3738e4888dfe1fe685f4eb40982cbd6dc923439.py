code = """import json, re

# Load knowledge articles from the large file path
with open(var_call_p30Et5SV89xAF92HWssFCxLt, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Load quote and quote line items from storage variables
quote = var_call_64vEZ7k3FfWV8IDrJtlr99Q0[0] if isinstance(var_call_64vEZ7k3FfWV8IDrJtlr99Q0, list) and var_call_64vEZ7k3FfWV8IDrJtlr99Q0 else None
quote_lines = var_call_jIOidJOxD3iD7eqc2flaPwyC

# Compute numeric discounts on quote lines
line_discounts = []
for li in quote_lines:
    try:
        d = float(li.get('Discount') or 0)
    except:
        # try parsing if trailing spaces or percent signs
        s = str(li.get('Discount') or '0')
        s = s.strip().rstrip('%')
        try:
            d = float(s)
        except:
            d = 0.0
    line_discounts.append(d)

max_discount = max(line_discounts) if line_discounts else 0.0

# Helper to search article text
def find_thresholds(text):
    # find patterns like 'greater than 10%', 'over 10%', 'above 10%', '>= 10%','maximum discount of 10%','discounts > 10%'
    patterns = [r'greater than (\d{1,2})%','over (\d{1,2})%','above (\d{1,2})%','>(\d{1,2})%','>=\s?(\d{1,2})%','maximum discount of (\d{1,2})%','discounts of (\d{1,2})%','discounts (?:above|over|greater than) (\d{1,2})%','discounts greater than (\d{1,2})%','discounts above (\d{1,2})%','discounts in excess of (\d{1,2})%']
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            try:
                return int(m.group(1))
            except:
                continue
    return None

violating_article_id = None
violations = []

for art in knowledge:
    # combine fields to search
    combined = ' '.join([str(art.get('title') or ''), str(art.get('faq_answer__c') or ''), str(art.get('summary') or ''), str(art.get('urlname') or '')])
    # look for explicit discount thresholds
    thresh = find_thresholds(combined)
    if thresh is not None:
        # If max_discount exceeds threshold and quote status is not 'Approved', consider violation
        if max_discount > thresh:
            violations.append({'id': art.get('id'), 'threshold': thresh, 'max_discount': max_discount, 'title': art.get('title')})

# Also check for 'no setup fee' or 'setup fee not allowed' policies
for art in knowledge:
    combined = ' '.join([str(art.get('title') or ''), str(art.get('faq_answer__c') or ''), str(art.get('summary') or '')])
    if re.search(r'no setup fee|setup fee not allowed|no setup fees|setup fees are not allowed|installation fee is not allowed', combined, flags=re.IGNORECASE):
        # Determine if any product or line item appears to be a setup fee by name/description (not much to go on)
        # Search product names/descriptions in the products dataset if available
        # As fallback, check if any product name or description contains 'setup' in the quote lines (not available)
        # For now, we skip unless explicit setup line exists; so we don't mark violation here.
        pass

# Choose the most relevant violation: smallest threshold that is violated (i.e., strictest policy)
if violations:
    violations_sorted = sorted(violations, key=lambda x: x['threshold'])
    violating_article_id = violations_sorted[0]['id']

# If no violations found, result is None
result = violating_article_id if violating_article_id is not None else None

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_p30Et5SV89xAF92HWssFCxLt': 'file_storage/call_p30Et5SV89xAF92HWssFCxLt.json', 'var_call_64vEZ7k3FfWV8IDrJtlr99Q0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_jIOidJOxD3iD7eqc2flaPwyC': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_D1vkhqVzFO00h2gfGKNpNTFp': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'CategoryName': 'Simulation and Verification Software'}], 'var_call_DdOa6P2UzrBv4C14V0Hh3aPW': []}

exec(code, env_args)
