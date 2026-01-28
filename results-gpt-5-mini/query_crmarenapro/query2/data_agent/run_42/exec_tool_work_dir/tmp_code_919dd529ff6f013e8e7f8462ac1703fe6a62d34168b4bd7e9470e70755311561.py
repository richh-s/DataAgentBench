code = """import json
from pathlib import Path

# Load previous tool results from storage variables
quote = var_call_KGsNtcuQSvURYeJdTLJRlj6v[0]
qlis = var_call_0StGHVJSNLgohF5XmO9LbXPG
products = var_call_zq8T3UxoocuBTkASyg5YO4jQ
pricebookentries = var_call_yIByFo2svYlvaaHFBCf9giGf

# Load knowledge articles from file path
kav_path = Path(var_call_vZnW8o6v3UBbXm7LgJfWP23W)
with kav_path.open('r', encoding='utf-8') as f:
    kav = json.load(f)

# Compute quote totals
import decimal
D = decimal.Decimal
total = D('0')
for line in qlis:
    # TotalPrice may be string
    try:
        tp = D(str(line.get('TotalPrice') or '0'))
    except Exception:
        tp = D('0')
    total += tp

# Collect discounts
discounts = []
for line in qlis:
    try:
        discounts.append(D(str(line.get('Discount') or '0')))
    except Exception:
        discounts.append(D('0'))

max_discount = max(discounts) if discounts else D('0')

# Also check for any setup fees mentioned in quote description or product descriptions
setup_fee_found = False
setup_fee_amount = D('0')
# search quote description and products for 'setup' or 'implementation' or 'onboarding' and amounts
qd = quote.get('Description','')
if 'setup' in qd.lower() or 'implementation' in qd.lower() or 'onboarding' in qd.lower():
    setup_fee_found = True

for p in products:
    desc = p.get('Description','')
    if 'setup' in desc.lower() or 'implementation' in desc.lower() or 'onboarding' in desc.lower():
        setup_fee_found = True

# Search knowledge articles for policy rules related to discounts or setup fees
violating_article_id = None

for art in kav:
    title = art.get('title','').lower()
    faq = art.get('faq_answer__c','').lower() if art.get('faq_answer__c') else ''
    summary = art.get('summary','').lower() if art.get('summary') else ''
    combined = ' '.join([title, faq, summary])

    # Look for explicit discount policy statements
    if ('discount' in combined or 'price' in combined or 'pricing' in combined) and ('approval' in combined or 'require' in combined or 'manager' in combined or 'threshold' in combined or '%' in combined or 'percent' in combined):
        # Try to extract numeric percent in the text
        import re
        percents = [float(x) for x in re.findall(r"(\d+(?:\.\d+)?)\s*%", combined)]
        # also find 'percent' words
        perc2 = []
        for m in re.findall(r"(\d+(?:\.\d+)?)\s*(?:percent|percentage)", combined):
            try:
                perc2.append(float(m))
            except:
                pass
        percents.extend(perc2)
        # If percents found, assume it's a threshold
        if percents:
            thr = max(percents)
            # If max_discount exceeds threshold, mark violation
            try:
                if max_discount > D(str(thr)):
                    violating_article_id = art.get('id')
                    break
            except Exception:
                pass
        else:
            # If text mentions 'no discounts without approval' or similar, and quote has any discount >0
            if ('no discount' in combined or 'without approval' in combined or 'must be approved' in combined or 'approval required' in combined or 'requires approval' in combined) and max_discount> D('0'):
                violating_article_id = art.get('id')
                break

    # Look for setup fee policy
    if ('setup' in combined or 'implementation' in combined or 'onboarding' in combined) and ('fee' in combined or 'charge' in combined or 'cost' in combined):
        # if quote mentions setup or products mention, then violation depends on policies like 'setup fees not allowed' or 'setup fees require approval over X'
        if 'not allowed' in combined or 'prohibit' in combined or 'no setup fee' in combined:
            if setup_fee_found:
                violating_article_id = art.get('id')
                break
        # check for amounts
        import re
        amounts = [float(x.replace(',','')) for x in re.findall(r"\$\s*(\d{1,3}(?:[,\d{3}]*)(?:\.\d+)?)", combined)]
        if amounts:
            thr_amount = max(amounts)
            # If any setup fee amount in quote > threshold -> violation. But we don't have explicit setup fee amounts in quote lines
            # We will skip numeric check here

# If no violating article found, look for strict pricing/ROI/TCO guidance that might be violated
if not violating_article_id:
    # Find articles that mention 'total cost of ownership' or 'tco' and complain about insufficient ROI; if total > some typical thresholds maybe violate
    for art in kav:
        combined = ' '.join([art.get('title','').lower(), art.get('faq_answer__c','') or '', art.get('summary','') or '']).lower()
        if 'total cost of ownership' in combined or 'tco' in combined or 'return on investment' in combined or 'roi' in combined:
            # Heuristic: if total > 10000 and article warns about TCO, consider violation
            try:
                if total > D('10000'):
                    violating_article_id = art.get('id')
                    break
            except Exception:
                pass

# Prepare result: violating_article_id or None
result = violating_article_id if violating_article_id is not None else None
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KGsNtcuQSvURYeJdTLJRlj6v': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_0StGHVJSNLgohF5XmO9LbXPG': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_zq8T3UxoocuBTkASyg5YO4jQ': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99'}], 'var_call_yIByFo2svYlvaaHFBCf9giGf': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_vZnW8o6v3UBbXm7LgJfWP23W': 'file_storage/call_vZnW8o6v3UBbXm7LgJfWP23W.json'}

exec(code, env_args)
