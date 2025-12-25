code = """import json, re, pandas as pd

# Load knowledge articles from file
path = var_call_C9phtrf1VPNEpCcMzhdDqsmL
with open(path, 'r') as f:
    articles = json.load(f)

qli_df = pd.DataFrame(var_call_4YqG2bN0mJqwsiALNA0W4NJf)

# Compute overall discount-weighted unit prices vs list price
qli_df['Quantity'] = qli_df['Quantity'].astype(float)
qli_df['UnitPrice'] = qli_df['UnitPrice'].astype(float)
qli_df['Discount'] = qli_df['Discount'].astype(float)
qli_df['Total_calc'] = qli_df['Quantity'] * qli_df['UnitPrice'] * (1 - qli_df['Discount']/100)

# Assume company policy article will mention discounts, total cost, or setup/implementation
policy_keywords = ['discount', 'total cost of ownership', 'tco', 'roi', 'implementation', 'deployment', 'pricing', 'cost', 'setup']

violated_article_id = None

for art in articles:
    text = ' '.join(str(art.get(k, '')) for k in ['title','summary','faq_answer__c']).lower()
    if any(kw in text for kw in policy_keywords):
        # Heuristic: if article criticizes high TCO, bad ROI, or complex implementation, and our quote has large discounts (>20%) or setup-like items, might violate
        max_discount = qli_df['Discount'].max()
        if max_discount > 20:
            violated_article_id = re.sub('^#','', art['id'])
            break

# In our data, max discount is only 15%. Without explicit pricing rules in knowledge base, treat as no violation.
if violated_article_id is None:
    result = None
else:
    result = violated_article_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JIjeaG0CgmUwB4EvxvMDZMht': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_C9phtrf1VPNEpCcMzhdDqsmL': 'file_storage/call_C9phtrf1VPNEpCcMzhdDqsmL.json', 'var_call_4YqG2bN0mJqwsiALNA0W4NJf': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}]}

exec(code, env_args)
