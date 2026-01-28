code = """import json

# Get quote line items from the stored result
quote_items = var_functions.query_db:5

# Read knowledge articles file
with open(var_functions.query_db:2, 'r') as f:
    articles = json.load(f)

# Read products file
with open(var_functions.query_db:12, 'r') as f:
    products = json.load(f)

# Create product name lookup
product_names = {}
for p in products:
    clean_id = p['Id'].replace('#', '')
    product_names[clean_id] = p['Name'].strip()

# Get products in quote
quote_product_names = []
for item in quote_items:
    item_id_clean = item['Product2Id'].replace('#', '')
    if item_id_clean in product_names:
        quote_product_names.append(product_names[item_id_clean])

# Find bundles article
bundles_article_id = None
for a in articles:
    if 'Mandatory Bundles' in a.get('title', ''):
        bundles_article_id = a['id']
        article_text = a.get('faq_answer__c', '')
        break

# Check for PulseSim Pro violation
violation = None
if bundles_article_id:
    has_pulsesim = 'PulseSim Pro' in quote_product_names
    if has_pulsesim:
        has_circuitmaster = 'CircuitMaster Analyzer' in quote_product_names
        has_verisim = 'VeriSim Express' in quote_product_names
        
        # If missing either required product, it's a violation
        if not has_circuitmaster or not has_verisim:
            violation = bundles_article_id

print('__RESULT__:')
print(json.dumps({'violation_id': violation, 'quote_products': quote_product_names}))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
