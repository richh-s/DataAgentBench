code = """import json

# Load Knowledge Articles
with open(locals()['var_function-call-711494007316219769'], 'r') as f:
    knowledge_articles = json.load(f)

# Find "Quote Approval Guide" or similar
# And read Volume-Based Discounts
target_articles = []
for art in knowledge_articles:
    title = art.get('title', '').lower()
    if 'quote approval' in title or 'approval guide' in title or 'volume-based discounts' in title:
        target_articles.append(art)

print("__RESULT__:")
print(json.dumps(target_articles))"""

env_args = {'var_function-call-711494007316221003': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-711494007316218338': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-711494007316219769': 'file_storage/function-call-711494007316219769.json', 'var_function-call-11684513859335262418': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}], 'var_function-call-11684513859335265651': 'file_storage/function-call-11684513859335265651.json', 'var_function-call-5875496314434973886': 'file_storage/function-call-5875496314434973886.json', 'var_function-call-6238258111911298071': [{'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}]}

exec(code, env_args)
