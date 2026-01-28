code = """import json, re
# Load data from storage variables
quote = var_call_Khova90dcaPd1mpUsZLdCGQu[0] if isinstance(var_call_Khova90dcaPd1mpUsZLdCGQu, list) and var_call_Khova90dcaPd1mpUsZLdCGQu else None
qlis = var_call_Uk5oFfVyTyVjIxxUKDYfd7A2
pbes = var_call_axhlztujn1MN1COyUTteACsP
# Load knowledge articles from file path
kb_path = var_call_4yTPlE6M8yN29KIJ5i2pLL14
with open(kb_path, 'r', encoding='utf-8') as f:
    kbs = json.load(f)

# Extract discounts from quote line items
discounts = []
for q in qlis:
    try:
        d = float(q.get('Discount') or 0)
    except:
        # Some discounts might be strings with trailing spaces
        try:
            d = float(str(q.get('Discount','0')).strip())
        except:
            d = 0.0
    discounts.append(d)

max_discount = max(discounts) if discounts else 0.0

# Helper to find numeric percent patterns and context
percent_pattern = re.compile(r"([0-9]+(?:\.[0-9]+)?)\s*%")

violation_id = None

for art in kbs:
    art_id = art.get('id')
    text_parts = [str(art.get('title') or ''), str(art.get('summary') or ''), str(art.get('faq_answer__c') or '')]
    text = ' '.join(text_parts).lower()
    # Quick keyword filter
    if not any(k in text for k in ['discount', 'pricing', 'price', 'approval', 'setup', 'setup fee', 'installation fee', 'authorization', 'authorize', 'approval required']):
        continue
    # Find percent numbers
    for m in percent_pattern.finditer(text):
        pct = float(m.group(1))
        start = max(0, m.start()-80)
        end = min(len(text), m.end()+80)
        context = text[start:end]
        # Look for keywords indicating a rule about discounts
        if any(w in context for w in ['require', 'approval', 'approv', 'authorize', 'authorization', 'must', 'not exceed', 'no more than', 'maximum', 'max', 'limit', 'restricted', 'cannot exceed', 'exceeding', 'exceed']):
            # Determine comparator from nearby words
            # If context contains 'over' or 'above' or 'exceed' before/after number -> threshold means discounts above pct require approval -> violation if max_discount > pct
            if re.search(r"(over|above|exceed|exceeding|more than|greater than)", context):
                if max_discount > pct + 1e-9:
                    violation_id = art_id
                    break
            # If context contains 'not exceed' or 'no more than' or 'cannot exceed' -> pct is cap; violation if max_discount > pct
            if re.search(r"(not exceed|no more than|cannot exceed|cannot be more than|no greater than|not be greater than|should not exceed|min|max|limit)", context):
                if max_discount > pct + 1e-9:
                    violation_id = art_id
                    break
            # If context contains 'up to X% without approval' or 'approval required for discounts above X%'
            if re.search(r"(without approval|without.*approval|approval required|requires approval)", context):
                # If phrase suggests approvals needed above pct
                if max_discount > pct + 1e-9:
                    violation_id = art_id
                    break
    if violation_id:
        break

# Additionally, check for explicit rules about setup fees being disallowed or requiring approval
if not violation_id:
    # Look for setup-related rules
    for art in kbs:
        art_id = art.get('id')
        text = ' '.join([str(art.get('title') or ''), str(art.get('summary') or ''), str(art.get('faq_answer__c') or '')]).lower()
        if 'setup' in text or 'setup fee' in text or 'installation fee' in text:
            # If text states 'setup fees are not allowed' or 'setup fees require approval' and quote seems to include a setup product name
            if 'not allowed' in text or 'prohibited' in text:
                # Does any product name or description indicate setup? Check product names/descriptions
                # Load product info from storage if available
                p_list = []
                try:
                    p_list = var_call_FplrY4JKcU9ED4VpPqffWs15
                except NameError:
                    p_list = []
                # Check if any product description/title contains 'setup' or 'installation' or 'implementation'
                has_setup_product = False
                for p in p_list:
                    if any(w in (str(p.get('ProductName') or '') + ' ' + str(p.get('Description') or '')).lower() for w in ['setup', 'implementation', 'installation', 'onboarding', 'services']):
                        has_setup_product = True
                        break
                if has_setup_product:
                    violation_id = art_id
                    break

# Prepare result: ID string or None
result = violation_id if violation_id is not None else None

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Khova90dcaPd1mpUsZLdCGQu': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_YFuCbawQCo0VvJOBgxNpapl1': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_Uk5oFfVyTyVjIxxUKDYfd7A2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_FplrY4JKcU9ED4VpPqffWs15': [{'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'Pricebook2Id': 'None', 'PricebookName': 'None', 'PricebookEntryId': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}], 'var_call_axhlztujn1MN1COyUTteACsP': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_4WaAghbakIXTPJ6TN6ii0Wkd': [], 'var_call_4yTPlE6M8yN29KIJ5i2pLL14': 'file_storage/call_4yTPlE6M8yN29KIJ5i2pLL14.json'}

exec(code, env_args)
