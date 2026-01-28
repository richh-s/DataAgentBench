code = """import json

# Load the knowledge articles JSON result from storage
path = var_call_ZKPrJMFL2kXWEGYBC1Q6hYOX
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find articles related to discounts, volume, installation, pricing, setup
keywords = ['discount', 'volume', 'installation', 'setup', 'price', 'pricing', 'install']
matches = []
for rec in data:
    title = (rec.get('title') or '').lower()
    summary = (rec.get('summary') or '').lower()
    if any(k in title or k in summary for k in keywords):
        matches.append({'id': rec.get('id'), 'title': rec.get('title'), 'summary': rec.get('summary')})

import json
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_call_wvSWocroqxXzZPEsD8AcumCq': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_YhuEQFSjhJviKUmXB6Vmoif0': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_1Ab1N51zjZMHOb9RU865i4DV': [{'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_ZnXv9FZgUQh05wahwR9A6W1X': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ'}], 'var_call_iAweqGB6AbEEKrZr570JYP95': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'Phone': '222-111-2222', 'Industry': 'Tech Consulting', 'Description': 'InnovateX Solutions provides cutting-edge consulting services, assisting businesses in integrating the latest technologies into their operations. Using tools like CloudLink Designer and CircuitAI Innovator, they enhance collaborative efforts and circuit design precision. Their focus on seamless tech integration empowers clients to achieve significant efficiency gains.', 'NumberOfEmployees': '850.0', 'ShippingState': 'WA'}], 'var_call_IkMNuZteIaWUp78yho7YAJRG': [{'Id': '003Wt00000JqkgYIAR', 'FirstName': 'Nina', 'LastName': 'Tran', 'Email': 'nina.tran@innovatexsolutions.com', 'AccountId': '001Wt00000PGXrKIAX'}], 'var_call_lKpArYVIoxMof4y0t6v3uK6H': [], 'var_call_Eb7bluxzNBaJTy9sHCEC5yRj': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_ZKPrJMFL2kXWEGYBC1Q6hYOX': 'file_storage/call_ZKPrJMFL2kXWEGYBC1Q6hYOX.json'}

exec(code, env_args)
