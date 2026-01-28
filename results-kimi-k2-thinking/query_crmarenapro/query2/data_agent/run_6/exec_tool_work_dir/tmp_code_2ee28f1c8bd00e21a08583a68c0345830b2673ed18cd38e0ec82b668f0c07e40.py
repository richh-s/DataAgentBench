code = """import json

quote_items = var_functions.query_db:5

with open(var_functions.query_db:2, 'r') as f:
    articles = json.load(f)

with open(var_functions.query_db:12, 'r') as f:
    products = json.load(f)

# Build product ID to name map
prod_map = {}
for p in products:
    clean_id = p['Id'].replace('#', '')
    prod_map[clean_id] = p['Name'].strip()

# Get products in quote
quote_prods = []
for item in quote_items:
    item_id = item['Product2Id'].replace('#', '')
    if item_id in prod_map:
        quote_prods.append(prod_map[item_id])

# Find Mandatory Bundles article
bundles_id = None
for a in articles:
    if 'Mandatory Bundles' in a.get('title', ''):
        bundles_id = a['id']
        bundles_text = a.get('faq_answer__c', '')
        break

# Check violation
violation = None
if bundles_id:
    if 'PulseSim Pro' in quote_prods:
        cma = 'CircuitMaster Analyzer' in quote_prods
        vse = 'VeriSim Express' in quote_prods
        if not cma or not vse:
            violation = bundles_id

print('__RESULT__:')
print(json.dumps(violation))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
