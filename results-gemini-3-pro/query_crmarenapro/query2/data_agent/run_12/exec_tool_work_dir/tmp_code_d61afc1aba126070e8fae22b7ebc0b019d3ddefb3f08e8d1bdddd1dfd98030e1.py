code = """import json

# Load Quote Items
quote_items = [
    {"Product": "DesignWave Automation", "Quantity": 5.0, "UnitPrice": 479.99, "Discount": 5.0},
    {"Product": "EcoPCB Creator", "Quantity": 8.0, "UnitPrice": 349.99, "Discount": 15.0},
    {"Product": "PulseSim Pro", "Quantity": 10.0, "UnitPrice": 499.99, "Discount": 10.0},
    {"Product": "CircuitSync Pro", "Quantity": 7.0, "UnitPrice": 339.99, "Discount": 5.0}
]

total_amount = 0
max_discount = 0
for item in quote_items:
    disc_decimal = item['Discount'] / 100.0
    line_total = item['Quantity'] * item['UnitPrice'] * (1 - disc_decimal)
    total_amount += line_total
    if item['Discount'] > max_discount:
        max_discount = item['Discount']

print(f"Quote Total: {total_amount}")
print(f"Max Discount: {max_discount}%")

# Load Knowledge Articles
with open(locals()['var_function-call-4108610738548567913'], 'r') as f:
    articles = json.load(f)

relevant_articles = []
keywords = ['policy', 'quote', 'approval', 'discount', 'setup', 'cost', 'standard']

for art in articles:
    text = (art.get('title', '') + " " + art.get('faq_answer__c', '') + " " + art.get('summary', '')).lower()
    if any(k in text for k in keywords):
        relevant_articles.append({
            "id": art['id'],
            "title": art['title'],
            "content": art['faq_answer__c']
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-6000944950341241942': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-6000944950341241257': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-4108610738548566120': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  ', 'Description': 'Customizable workflow automation tool enhancing process efficiency.'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.'}], 'var_function-call-4108610738548567913': 'file_storage/function-call-4108610738548567913.json'}

exec(code, env_args)
