code = """import json
# Load variables from storage
quote_lines = var_call_FHkpvP7ZdMcoSnN9iO9JDjff
# knowledge articles file path
kav_path = var_call_EQ8vNet5c9rqwZOJSr0qvMBI
with open(kav_path, 'r', encoding='utf-8') as f:
    kav = json.load(f)
# Search for relevant policy keywords
keywords = ['discount', 'approval', 'approve', 'setup', 'installation', 'installation fee', 'setup fee', 'pricing', 'pricebook', 'pricebookentry', 'max discount', 'maximum discount', 'threshold', 'quota', 'quote', 'policy']
matches = []
for art in kav:
    text = ' '.join([str(art.get('title','') or ''), str(art.get('faq_answer__c','') or ''), str(art.get('summary','') or '')]).lower()
    for kw in keywords:
        if kw in text:
            matches.append({'id': art.get('id'), 'title': art.get('title'), 'keyword': kw, 'snippet': text[:400]})
            break
# Prepare quote analysis
violations = []
# Convert numeric strings
for li in quote_lines:
    try:
        discount = float(li.get('Discount') or 0)
    except:
        discount = 0.0
    try:
        unit = float(li.get('UnitPrice') or 0)
    except:
        unit = 0.0
    try:
        qty = float(li.get('Quantity') or 0)
    except:
        qty = 0.0
    # Rule check examples: if discount > 10 -> requires approval
    if discount > 10.0:
        violations.append({'QuoteLineItemId': li.get('Id'), 'issue': 'Discount exceeds 10%', 'discount': discount})

# Output findings
out = {'matches_count': len(matches), 'matches': matches[:20], 'found_violations_by_rule_check': violations}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_hq5vUwklf2vXC3j7nBdtS4Yi': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_FHkpvP7ZdMcoSnN9iO9JDjff': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_o1Nsd9qbgMnyBZXO8HpF5Jwr': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_call_B2n3Om5Ompdi69XvtJbswYp3': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE'}], 'var_call_B6iNd7slQ86JpPGxt5qcapW8': [], 'var_call_IWHtV2IOOpwHLGSAkMJOe0OQ': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_HZFUa43kgY9xKj2DNU0hBL13': [], 'var_call_sCQeRb6FBaywoGeFFbOQLsOJ': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_wTEbba5yDNsGqNvmitsP2njz': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'Phone': '222-111-2222', 'Industry': 'Tech Consulting', 'Description': 'InnovateX Solutions provides cutting-edge consulting services, assisting businesses in integrating the latest technologies into their operations. Using tools like CloudLink Designer and CircuitAI Innovator, they enhance collaborative efforts and circuit design precision. Their focus on seamless tech integration empowers clients to achieve significant efficiency gains.', 'NumberOfEmployees': '850.0', 'ShippingState': 'WA'}], 'var_call_EQ8vNet5c9rqwZOJSr0qvMBI': 'file_storage/call_EQ8vNet5c9rqwZOJSr0qvMBI.json'}

exec(code, env_args)
