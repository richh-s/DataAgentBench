code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_03sZl2gsnhefQjmhBBgwsNYN)
articles_preview = json.loads(open(var_call_N4SBYoEQHQ8N5qEMMyivvonr, 'r').read())
articles = pd.DataFrame(articles_preview)

text = ' '.join([f"Quote status: Needs Review. Line discounts: {', '.join(qli['Discount'].astype(str).tolist())}." ]).lower()

matches = []
for _, row in articles.iterrows():
    haystack = (str(row.get('title','')) + ' ' + str(row.get('summary',''))).lower()
    if 'discount' in haystack or 'pricing' in haystack or 'quote' in haystack:
        matches.append(row['id'])

result = None
if matches:
    # assume pricing/discount policy article is the violation for a "Needs Review" quote with discounts
    # prefer articles whose title mentions discount/price
    scored = []
    for mid in matches:
        row = articles[articles['id']==mid].iloc[0]
        title = str(row.get('title','')).lower()
        score = 0
        if 'discount' in title: score += 2
        if 'pricing' in title or 'price' in title: score += 2
        if 'quote' in title: score += 1
        scored.append((score, mid))
    scored.sort(reverse=True)
    result = scored[0][1]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tZEuSKnlPmkiQdUwc2VaZWUr': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_03sZl2gsnhefQjmhBBgwsNYN': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_N4SBYoEQHQ8N5qEMMyivvonr': 'file_storage/call_N4SBYoEQHQ8N5qEMMyivvonr.json'}

exec(code, env_args)
