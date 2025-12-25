code = """import json

# Load hits from previous search
with open(locals()['var_function-call-3395642170722751092'], 'r') as f:
    hits = json.load(f)

# Print full text of hits containing "approval" or "limit"
for hit in hits:
    # I need to find the full article content. I can't get it from 'hits' because I only stored preview.
    # I should have stored the full content or I need to reload the original file and find these ids.
    pass

# Reload all articles to get full text
with open(locals()['var_function-call-9956328032061737126'], 'r') as f:
    articles = json.load(f)

# Filter for approval/limit/policy/quote
relevant_articles = []
for art in articles:
    text = (art.get('title', '') + ' ' + art.get('summary', '') + ' ' + art.get('faq_answer__c', '')).lower()
    if 'approval' in text or 'limit' in text or 'policy' in text:
        relevant_articles.append(art)

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-9956328032061738604': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-9956328032061735817': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-9956328032061737126': 'file_storage/function-call-9956328032061737126.json', 'var_function-call-17745145721986775796': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}], 'var_function-call-12701998892268725047': 'file_storage/function-call-12701998892268725047.json', 'var_function-call-16807647120288591689': 'file_storage/function-call-16807647120288591689.json', 'var_function-call-3395642170722751092': 'file_storage/function-call-3395642170722751092.json'}

exec(code, env_args)
