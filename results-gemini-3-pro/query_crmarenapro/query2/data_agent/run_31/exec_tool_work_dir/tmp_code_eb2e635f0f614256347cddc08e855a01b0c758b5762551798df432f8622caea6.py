code = """import json

with open(locals()['var_function-call-14756650280646482975'], 'r') as f:
    articles = json.load(f)

filtered_articles = []
for art in articles:
    title = art.get('title', '').lower()
    summary = art.get('summary', '').lower()
    faq = art.get('faq_answer__c', '').lower()
    full_text = title + " " + summary + " " + faq
    
    # Exclude competitors
    if "competitor" in title:
        continue
        
    # Look for policy related keywords
    if "policy" in full_text and ("quote" in full_text or "approval" in full_text or "discount" in full_text):
        filtered_articles.append({
            "id": art.get("id"),
            "title": art.get("title"),
            "summary": art.get("summary"),
            "faq_answer__c": art.get("faq_answer__c")
        })

print("__RESULT__:")
print(json.dumps(filtered_articles))"""

env_args = {'var_function-call-17879767230944425435': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-17879767230944424718': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-17879767230944424001': 'file_storage/function-call-17879767230944424001.json', 'var_function-call-14756650280646482975': 'file_storage/function-call-14756650280646482975.json'}

exec(code, env_args)
