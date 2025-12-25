code = """import json

# Load knowledge articles
with open(locals()['var_function-call-7262139185607178503'], 'r') as f:
    articles = json.load(f)

ids_to_fetch = ['ka0Wt000000Eq0MIAS', '#ka0Wt000000EpSUIA0']
relevant_articles = []

for art in articles:
    # Check specific IDs
    if art['id'] in ids_to_fetch:
        relevant_articles.append(art)
        continue
    
    # Check keywords in title/summary
    text = (str(art.get('title', '')) + " " + str(art.get('summary', ''))).lower()
    if 'policy' in text or 'installation' in text or 'timeline' in text or 'setup' in text or 'discount' in text:
         if art not in relevant_articles:
             relevant_articles.append(art)

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-2034190256547772921': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-2034190256547770416': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-7262139185607177728': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  ', 'Description': 'Customizable workflow automation tool enhancing process efficiency.', 'IsActive': '1', 'External_ID__c': 'Customizable Workflow Automation,Cloud-Based Design Collaboration_10'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Cloud-Based Design Collaboration_21'}], 'var_function-call-7262139185607178503': 'file_storage/function-call-7262139185607178503.json', 'var_function-call-14268975021654453383': 'file_storage/function-call-14268975021654453383.json'}

exec(code, env_args)
