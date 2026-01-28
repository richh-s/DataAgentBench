code = """import json
# load the full knowledge articles from the storage key var_call_kPphv9sNOmrMP08s5rlugVoD
path = var_call_kPphv9sNOmrMP08s5rlugVoD
with open(path, 'r') as f:
    kav = json.load(f)
# We'll also load other query results available in storage for analysis
ql = var_call_JpXi51gFI2ddiHuC4C7bTEF3
quote = var_call_ya7w8HViauIGA2eB85vXiP6w
quote_line_items = ql
products = var_call_6LPEnywQLpCW1iAaCkNoV47E
pricebook = var_call_0jL4rRK2s1GogMvGZlRPdblS
opportunity = var_call_MmYQFhLqBJtHx7zDpuFxTJ6c
account = var_call_8BNrvRxDbXDDrR4svx9a3wDz
contact = var_call_tta6sYREOL5KML2JO1Bkrii4
pcp = var_call_yNKk3WtLtvttiksGT6CAEC1k

# Basic checks: calculate total quote price sum of TotalPrice from QuoteLineItem
# Convert strings to floats
try:
    total = sum([float(x['TotalPrice']) for x in quote_line_items])
except Exception:
    total = None

# Find if any knowledge article mentions pricing, discounts, competitor pricing, or cost objections
violating_article_id = None
for a in kav:
    txt = (a.get('faq_answer__c') or '') + ' ' + (a.get('summary') or '') + ' ' + (a.get('title') or '')
    ltxt = txt.lower()
    # simple heuristics: look for policy-like keywords
    if 'pricing' in ltxt or 'cost' in ltxt or 'discount' in ltxt or 'total cost of ownership' in ltxt or 'pricing strategy' in ltxt or 'transparency' in ltxt:
        violating_article_id = a.get('id')
        break

# If no candidate found, set None
if violating_article_id is None:
    violating_article_id = None

result = {
    'quote_id': quote[0]['Id'],
    'quote_total': total,
    'violating_article_id': violating_article_id
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ya7w8HViauIGA2eB85vXiP6w': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_JpXi51gFI2ddiHuC4C7bTEF3': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_6LPEnywQLpCW1iAaCkNoV47E': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_call_0jL4rRK2s1GogMvGZlRPdblS': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_yNKk3WtLtvttiksGT6CAEC1k': [{'Id': '#0ZRWt0000005SbZOAU', 'ProductCategoryId': '0ZGWt0000005XeTOAU', 'ProductId': '01tWt000006hV57IAE'}, {'Id': '0ZRWt0000005SdBOAU', 'ProductCategoryId': '#0ZGWt0000005XcrOAE', 'ProductId': '01tWt000006hV57IAE'}], 'var_call_MmYQFhLqBJtHx7zDpuFxTJ6c': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_8BNrvRxDbXDDrR4svx9a3wDz': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'Phone': '222-111-2222', 'Industry': 'Tech Consulting', 'Description': 'InnovateX Solutions provides cutting-edge consulting services, assisting businesses in integrating the latest technologies into their operations. Using tools like CloudLink Designer and CircuitAI Innovator, they enhance collaborative efforts and circuit design precision. Their focus on seamless tech integration empowers clients to achieve significant efficiency gains.', 'NumberOfEmployees': '850.0', 'ShippingState': 'WA'}], 'var_call_tta6sYREOL5KML2JO1Bkrii4': [{'Id': '003Wt00000JqkgYIAR', 'FirstName': 'Nina', 'LastName': 'Tran', 'Email': 'nina.tran@innovatexsolutions.com', 'AccountId': '001Wt00000PGXrKIAX'}], 'var_call_kPphv9sNOmrMP08s5rlugVoD': 'file_storage/call_kPphv9sNOmrMP08s5rlugVoD.json'}

exec(code, env_args)
