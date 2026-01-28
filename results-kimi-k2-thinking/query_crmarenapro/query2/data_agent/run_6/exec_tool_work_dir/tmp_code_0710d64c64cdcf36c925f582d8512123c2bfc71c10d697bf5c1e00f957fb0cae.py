code = """import json

# Get quote line items  
quote_items = var_functions.query_db:5
print('Quote items loaded:', len(quote_items))

# Load all products
products_file = var_functions.query_db:12
with open(products_file, 'r') as f:
    products = json.load(f)

# Load knowledge articles
knowledge_file = var_functions.query_db:2
with open(knowledge_file, 'r') as f:
    articles = json.load(f)

# Create product mapping
prod_map = {}
for p in products:
    clean_id = p['Id'].replace('#', '')
    prod_map[clean_id] = p['Name'].strip()

quote_products = []
for item in quote_items:
    clean_item_id = item['Product2Id'].replace('#', '')
    if clean_item_id in prod_map:
        quote_products.append(prod_map[clean_item_id])

# Find bundles article
bundles = None
for a in articles:
    if 'Mandatory Bundles' in a.get('title', ''):
        bundles = a
        break

print('Products in quote:', quote_products)
print('Bundles article:', bundles['id'] if bundles else 'Not found')

if bundles:
    text = bundles.get('faq_answer__c', '')
    print('Has PulseSim Pro:', 'PulseSim Pro' in quote_products)
    if 'PulseSim Pro' in quote_products:
        has_cma = 'CircuitMaster Analyzer' in quote_products
        has_vse = 'VeriSim Express' in quote_products
        print('Has CircuitMaster Analyzer:', has_cma)
        print('Has VeriSim Express:', has_vse)
        
        if not has_cma or not has_vse:
            result = bundles['id']
        else:
            result = None
    else:
        result = None
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
