code = """import json

# Access variables using locals()
quote = locals()['var_function-call-14777573000117993465']
line_items = locals()['var_function-call-14777573000117991666']
products = locals()['var_function-call-5460198670301064506']
knowledge_file_path = locals()['var_function-call-14777573000117989867']

with open(knowledge_file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Calculate Quote Metrics
total_amount = sum(float(item['TotalPrice']) for item in line_items)
max_discount = max(float(item['Discount']) for item in line_items) if line_items else 0
line_item_details = []

for item in line_items:
    prod_id = item['Product2Id'].replace('#', '')
    product_name = next((p['Name'] for p in products if p['Id'] == prod_id), "Unknown Product")
    line_item_details.append({
        'Product': product_name,
        'UnitPrice': float(item['UnitPrice']),
        'Quantity': float(item['Quantity']),
        'Discount': float(item['Discount']),
        'TotalPrice': float(item['TotalPrice'])
    })

debug_info = {
    "Total Amount": total_amount,
    "Max Discount": max_discount,
    "Line Items": line_item_details
}

# Filter Knowledge Articles for policies
relevant_articles = []
keywords = ['approval', 'policy', 'discount', 'setup', 'compliance', 'threshold']
for article in knowledge_articles:
    text = (article['title'] + " " + (article['faq_answer__c'] or "") + " " + (article['summary'] or "")).lower()
    if any(k in text for k in keywords):
        relevant_articles.append({
            'id': article['id'],
            'title': article['title'],
            'summary': article['summary'],
            'faq_answer__c': article['faq_answer__c']
        })

print("__RESULT__:")
print(json.dumps({"metrics": debug_info, "articles": relevant_articles}))"""

env_args = {'var_function-call-14777573000117993465': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-14777573000117991666': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-14777573000117989867': 'file_storage/function-call-14777573000117989867.json', 'var_function-call-5460198670301064506': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Cloud-Based Design Collaboration_21'}]}

exec(code, env_args)
