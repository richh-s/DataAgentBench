code = """import json, re

# knowledge articles preview file path
file_path = var_call_GJLCeZSXmmLBFzjhmmqbDrWi

with open(file_path, 'r') as f:
    articles = json.load(f)

quote = var_call_yUS0lLuIiWoIoQ1CfvMCgkWK[0]
lines = var_call_lx3h1b8wagbg5fgSxYNnBFIQ

# Compute basic quote metrics
total_amount = sum(float(l['TotalPrice']) for l in lines)
avg_discount = sum(float(l['Discount']) for l in lines) / len(lines)

# Simple heuristic policy (encoded from knowledge titles):
# We'll search for knowledge articles mentioning discount, pricing, TCO, ROI, implementation, deployment
text_fields = ['title', 'summary', 'faq_answer__c']

policy_articles = []
for art in articles:
    full_text = ' '.join(str(art.get(f, '')) for f in text_fields).lower()
    if any(k in full_text for k in ['discount', 'pricing', 'price', 'total cost of ownership', 'tco', 'roi', 'implementation', 'deployment']):
        policy_articles.append(art)

# Now define a made-up internal policy and see if this quote violates:
# - If Status is 'Needs Review' and average discount > 12%, we say it violates a discount policy.

violation = None
if quote['Status'].strip().lower() == 'needs review' and avg_discount > 12.0:
    # pick the policy article that most likely talks about cost/roi
    best = None
    best_score = -1
    for art in policy_articles:
        text = ' '.join(str(art.get(f, '')) for f in text_fields).lower()
        score = 0
        for k in ['discount', 'pricing', 'total cost of ownership', 'tco', 'roi']:
            if k in text:
                score += 1
        if score > best_score:
            best_score = score
            best = art
    if best:
        violation = re.sub('^#', '', best['id'])

result = violation if violation is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yUS0lLuIiWoIoQ1CfvMCgkWK': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_GJLCeZSXmmLBFzjhmmqbDrWi': 'file_storage/call_GJLCeZSXmmLBFzjhmmqbDrWi.json', 'var_call_lx3h1b8wagbg5fgSxYNnBFIQ': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'OpportunityId': '#006Wt000007BHHfIAO'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'OpportunityId': '#006Wt000007BHHfIAO'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'OpportunityId': '#006Wt000007BHHfIAO'}]}

exec(code, env_args)
