code = """import json

# Load QuoteLineItems
quote_line_items = [
    {"Id": "0QLWt0000022xB1OAI", "QuoteId": "#0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HHpqIAG", "Product2Id": "#01tWt000006hVEnIAM", "PricebookEntryId": "01uWt0000027PGfIAM", "Quantity": 5.0, "UnitPrice": 479.99, "Discount": 5.0, "TotalPrice": 2279.9525},
    {"Id": "0QLWt0000022yNAOAY", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HavbIAC", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": 8.0, "UnitPrice": 349.99, "Discount": 15.0, "TotalPrice": 2379.932},
    {"Id": "0QLWt0000022z7tOAA", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HXg4IAG", "Product2Id": "01tWt000006hV57IAE", "PricebookEntryId": "01uWt0000027P3lIAE", "Quantity": 10.0, "UnitPrice": 499.99, "Discount": 10.0, "TotalPrice": 4499.91},
    {"Id": "0QLWt0000022z9VOAQ", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HL76IAG", "Product2Id": "#01tWt000006hVQ5IAM", "PricebookEntryId": "01uWt0000027PVBIA2", "Quantity": 7.0, "UnitPrice": 339.99, "Discount": 5.0, "TotalPrice": 2260.9335}
]

# Calculate Total Amount
total_amount = sum(item["TotalPrice"] for item in quote_line_items)

# Load Knowledge Articles
file_path = locals()['var_function-call-3712139761311028047']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Search for relevant articles
relevant_articles = []
for art in articles:
    title = art.get('title', '').lower()
    summary = art.get('summary', '').lower()
    answer = art.get('faq_answer__c', '').lower()
    content = title + " " + summary + " " + answer
    
    if "approval" in content or "policy" in content or "quote" in content:
        relevant_articles.append(art)

print("__RESULT__:")
print(json.dumps({
    "total_amount": total_amount,
    "relevant_articles_count": len(relevant_articles),
    "relevant_articles_preview": [{k: v for k, v in a.items() if k in ['id', 'title']} for a in relevant_articles]
}))"""

env_args = {'var_function-call-3712139761311028513': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-3712139761311028280': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-3712139761311028047': 'file_storage/function-call-3712139761311028047.json', 'var_function-call-7471441343873170560': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}]}

exec(code, env_args)
