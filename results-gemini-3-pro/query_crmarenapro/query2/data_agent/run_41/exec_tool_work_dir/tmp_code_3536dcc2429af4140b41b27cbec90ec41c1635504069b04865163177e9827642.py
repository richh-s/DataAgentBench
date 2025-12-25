code = """import json

# Get filename from storage
filename = locals()['var_function-call-6878268969408500026']

# Load knowledge articles
with open(filename, 'r') as f:
    articles = json.load(f)

# Search for broad approval keywords
approval_info = []
keywords = ["approval", "limit", "maximum", "threshold", "manager", "director", "vp"]
for art in articles:
    text = (str(art.get('title', '')) + ' ' + str(art.get('summary', '')) + ' ' + str(art.get('faq_answer__c', ''))).lower()
    if any(k in text for k in keywords):
        approval_info.append({
            'id': art.get('id'),
            'title': art.get('title')
        })

print("__RESULT__:")
print(json.dumps(approval_info))"""

env_args = {'var_function-call-6878268969408503484': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-6878268969408501755': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-6878268969408500026': 'file_storage/function-call-6878268969408500026.json', 'var_function-call-7000911585173099427': ['01tWt000006hVEnIAM', '01tWt000006hV6jIAE', '01tWt000006hV57IAE', '01tWt000006hVQ5IAM'], 'var_function-call-14438941877686079210': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}], 'var_function-call-18359153385456820592': 'file_storage/function-call-18359153385456820592.json', 'var_function-call-11084504168283018034': []}

exec(code, env_args)
