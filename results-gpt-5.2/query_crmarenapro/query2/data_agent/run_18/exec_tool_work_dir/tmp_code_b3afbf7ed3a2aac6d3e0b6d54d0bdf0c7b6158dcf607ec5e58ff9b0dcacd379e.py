code = """import json, pandas as pd

# Load knowledge articles (may be in file)
ka_src = var_call_LZ17WjhIkjhJaW33dxfQZC9B
if isinstance(ka_src, str):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = json.load(f)
else:
    ka = ka_src

quote = var_call_AEJUgtBWV7Fl4zA8Geuhjjuv
qlis = var_call_xz7PvtstAwgmDasG6CKqdg7S

# Prepare text to search
text_blob = "\n".join([
    (quote[0].get('Name') or ''),
    (quote[0].get('Description') or ''),
    json.dumps(qlis)
]).lower()

# Heuristic: look for policy/quote approval articles; then see if they mention setup fees / cost / discount thresholds
candidates = []
for a in ka:
    title = (a.get('title') or '').strip()
    summary = (a.get('summary') or '').strip()
    ans = (a.get('faq_answer__c') or '').strip()
    blob = (title + "\n" + summary + "\n" + ans).lower()
    score = 0
    for kw in ["quote", "approval", "pricing", "discount", "setup", "implementation", "cost", "fee", "policy"]:
        if kw in blob:
            score += 1
    if score >= 3:
        candidates.append((score, a.get('id'), title, blob))

# Determine violation: based on quote line item discounts (5,15,10,5). Setup not explicitly present.
# We'll search for any article that sets max discount below 15 or requires approval above 10/5.
max_disc = max(float(r.get('Discount') or 0) for r in qlis) if qlis else 0.0
violation_id = None
# Among candidates, pick one that mentions discount thresholds and indicates violation
for score, aid, title, blob in sorted(candidates, key=lambda x: (-x[0], str(x[1]))):
    # detect threshold numbers in article
    # simple check: if article mentions "10%" and says requires approval above, and max_disc>10
    if ("discount" in blob) and ("%" in blob):
        if ("10%" in blob or "10 %" in blob or "ten percent" in blob) and max_disc > 10:
            violation_id = aid
            break
        if ("15%" in blob or "15 %" in blob or "fifteen percent" in blob) and max_disc > 15:
            violation_id = aid
            break
        if ("5%" in blob or "5 %" in blob or "five percent" in blob) and max_disc > 5:
            violation_id = aid
            break

# If none found, return None
out = violation_id if violation_id is not None else None
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AEJUgtBWV7Fl4zA8Geuhjjuv': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_xz7PvtstAwgmDasG6CKqdg7S': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_LZ17WjhIkjhJaW33dxfQZC9B': 'file_storage/call_LZ17WjhIkjhJaW33dxfQZC9B.json'}

exec(code, env_args)
