code = """import json

with open(locals()['var_function-call-13958055766219921849'], 'r') as f:
    articles = json.load(f)

# Filter by title containing policy-related terms
titles = []
for art in articles:
    title = art.get('title', '').lower()
    if any(k in title for k in ['policy', 'guideline', 'approval', 'process', 'standard', 'discount']):
        titles.append((art['id'], art['title']))

print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_function-call-6341133443987485715': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-6341133443987486840': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-13958055766219919458': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  ', 'Description': 'Customizable workflow automation tool enhancing process efficiency.', 'IsActive': '1', 'External_ID__c': 'Customizable Workflow Automation,Cloud-Based Design Collaboration_10'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Cloud-Based Design Collaboration_21'}], 'var_function-call-13958055766219921849': 'file_storage/function-call-13958055766219921849.json', 'var_function-call-12679510441079946961': 'file_storage/function-call-12679510441079946961.json'}

exec(code, env_args)
