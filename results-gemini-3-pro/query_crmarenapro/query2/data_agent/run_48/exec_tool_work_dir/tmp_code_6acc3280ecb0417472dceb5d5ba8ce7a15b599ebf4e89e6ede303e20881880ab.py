code = """import json

# Load knowledge articles
with open(locals()['var_function-call-1725784444598671306'], 'r') as f:
    articles = json.load(f)

# Search for approval policies
approval_articles = []
for art in articles:
    text = (art.get('title', '') + ' ' + art.get('summary', '') + ' ' + art.get('faq_answer__c', '')).lower()
    if 'approval' in text or 'authority' in text or 'limit' in text or 'margin' in text:
        approval_articles.append(art)

print(f"Found {len(approval_articles)} approval articles.")
for art in approval_articles:
    print(f"ID: {art['id']}, Title: {art['title']}")
    print(f"Summary: {art['summary']}")
    print(f"Body snippet: {art['faq_answer__c'][:200]}")
    print("-" * 20)

print("__RESULT__:")
print(json.dumps(approval_articles))"""

env_args = {'var_function-call-1725784444598673348': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-1725784444598670279': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-1725784444598671306': 'file_storage/function-call-1725784444598671306.json', 'var_function-call-4995927499890345620': 'file_storage/function-call-4995927499890345620.json', 'var_function-call-5752983261684237683': 'file_storage/function-call-5752983261684237683.json'}

exec(code, env_args)
