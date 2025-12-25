code = """import json, pandas as pd, os

# Load knowledge articles full file
path = var_call_fRfxKeYqjLMgJGusNZdafRx8
with open(path, 'r') as f:
    knowledge = json.load(f)

# Simple heuristic: look for policy-related articles mentioning quote, pricing, discount, approval, or TCO/ROI
policy_keywords = ['policy', 'quote', 'pricing', 'discount', 'approval', 'tco', 'roi', 'implementation', 'deployment', 'cost']

candidates = []
for art in knowledge:
    text = ' '.join([str(art.get('title','')), str(art.get('summary','')), str(art.get('faq_answer__c',''))]).lower()
    if any(k in text for k in policy_keywords):
        candidates.append(art)

# Inspect the quote line items from var_call_aUvw7HqcQIcvKVhVInH9uE5z
qli = pd.DataFrame(var_call_aUvw7HqcQIcvKVhVInH9uE5z)

# Compute effective discount and total amount
qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)
qli['TotalPrice'] = qli['TotalPrice'].astype(float)

# Assume list price = UnitPrice, so discount is just the Discount field; compute weighted average discount
qli['LineListTotal'] = qli['Quantity'] * qli['UnitPrice']

weighted_avg_discount = (qli['Discount'] * qli['LineListTotal']).sum() / qli['LineListTotal'].sum()
quote_total = qli['TotalPrice'].sum()

# Hypothetical internal policy from a knowledge article: find any article that mentions a max discount percentage
violated_article_id = None

for art in candidates:
    text = ' '.join([str(art.get('title','')), str(art.get('summary','')), str(art.get('faq_answer__c',''))]).lower()
    # Look for phrases like "maximum discount" or "max discount" with a percentage
    if 'maximum discount' in text or 'max discount' in text:
        # naive parse: find a number followed by '%'
        import re
        m = re.search(r'(\d+\.?\d*)\s*%', text)
        if m:
            max_disc = float(m.group(1))
            if weighted_avg_discount > max_disc:
                violated_article_id = art['id']
                break

# If no explicit policy found or no violation detected, return None
result = violated_article_id if violated_article_id is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_UaDsbTnxJwUrAE774Wi0yvs9': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_aUvw7HqcQIcvKVhVInH9uE5z': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_fRfxKeYqjLMgJGusNZdafRx8': 'file_storage/call_fRfxKeYqjLMgJGusNZdafRx8.json'}

exec(code, env_args)
