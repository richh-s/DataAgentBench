code = """import json
# Accessing stored variables from previous tool calls
quote = var_call_e6ihKgOLAPv10xvRHUzVBIHc[0] if isinstance(var_call_e6ihKgOLAPv10xvRHUzVBIHc, list) and len(var_call_e6ihKgOLAPv10xvRHUzVBIHc)>0 else None
items = var_call_vCFWOamUhWjkHFFGyJjPF3GS
knowledge = var_call_LgWkR5EsW8m803GduTjySxEu

# Compute totals
pre_total = 0.0
post_total = 0.0
for it in items:
    qty = float(it.get('Quantity') or 0)
    unit = float(it.get('UnitPrice') or 0)
    disc = float(it.get('Discount') or 0)
    line_pre = qty * unit
    line_post = line_pre * (1 - disc/100.0)
    pre_total += line_pre
    post_total += line_post

effective_discount = (pre_total - post_total) / pre_total if pre_total>0 else 0.0

# Find Volume-Based Discounts article id
vol_article_id = None
for k in knowledge:
    title = (k.get('title') or '').lower()
    summary = (k.get('summary') or '').lower()
    if 'volume' in title or 'volume' in summary or 'volume-based' in title or 'volume-based' in summary:
        vol_article_id = k.get('id')
        break

# Policy: if pre_total > 20 -> entire order should have 15% discount
violation_id = None
if pre_total > 20 and abs(effective_discount - 0.15) > 0.001:
    violation_id = vol_article_id

# Prepare output: either id or None
output = violation_id if violation_id is not None else None
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_e6ihKgOLAPv10xvRHUzVBIHc': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_vCFWOamUhWjkHFFGyJjPF3GS': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_zK1m9TByfVF7EWQtSZjMJszL': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99'}], 'var_call_FoUpP2yuw0h80Zh3nTShieCk': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_4dSsNf8o9EBBxpitMnsaXzPn': [], 'var_call_hypTAgdVkiE9kIqe9mypxH4S': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_pcP5Mkb3L0Nma0BRb7hDWVee': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'Phone': '222-111-2222', 'Industry': 'Tech Consulting', 'Description': 'InnovateX Solutions provides cutting-edge consulting services, assisting businesses in integrating the latest technologies into their operations. Using tools like CloudLink Designer and CircuitAI Innovator, they enhance collaborative efforts and circuit design precision. Their focus on seamless tech integration empowers clients to achieve significant efficiency gains.', 'NumberOfEmployees': '850.0', 'ShippingState': 'WA'}], 'var_call_pE9lR9wDa6kI6hCaBqG9yEhW': [{'Id': '003Wt00000JqkgYIAR', 'FirstName': 'Nina', 'LastName': 'Tran', 'Email': 'nina.tran@innovatexsolutions.com', 'AccountId': '001Wt00000PGXrKIAX'}], 'var_call_s8ScDmEywG4G0dzT8dQPSAE1': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_call_Y4D5XHThTPo1VBsseIHdvijj': [], 'var_call_ys8VGLVPziOFfHDDIJ9OHe87': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'Description': 'None', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_LgWkR5EsW8m803GduTjySxEu': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}], 'var_call_8AbGGsrUvazJSQVzYdU3rMvY': 'file_storage/call_8AbGGsrUvazJSQVzYdU3rMvY.json', 'var_call_ZPltINnx6q9aBfW938SyqLIK': 'file_storage/call_ZPltINnx6q9aBfW938SyqLIK.json'}

exec(code, env_args)
