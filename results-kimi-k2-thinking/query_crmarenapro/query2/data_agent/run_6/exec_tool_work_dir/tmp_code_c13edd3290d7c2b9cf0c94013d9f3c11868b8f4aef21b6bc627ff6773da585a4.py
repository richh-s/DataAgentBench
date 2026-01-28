code = """import json

# Read knowledge articles from the file path
knowledge_file_path = var_functions.query_db:2
with open(knowledge_file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Find the Mandatory Bundles article
mandatory_bundles_article = None
for article in knowledge_articles:
    if "Mandatory Bundles for Quotes" in article.get("title", ""):
        mandatory_bundles_article = article
        break

# Get all products from the database file
products_file_path = var_functions.query_db:12
with open(products_file_path, 'r') as f:
    all_products = json.load(f)

# Get quote line items
quote_items = var_functions.query_db:5

# Map product IDs to names for easier checking
product_id_to_name = {}
for prod in all_products:
    prod_id = prod['Id'].replace('#', '')
    product_id_to_name[prod_id] = prod['Name'].strip()

# Check what products are in the quote and what bundles are required
products_in_quote = []
for item in quote_items:
    item_prod_id = item['Product2Id'].replace('#', '')
    if item_prod_id in product_id_to_name:
        products_in_quote.append(product_id_to_name[item_prod_id])

# Check bundle requirements
violation_id = None
if mandatory_bundles_article:
    article_text = mandatory_bundles_article.get('faq_answer__c', '')
    
    # Check if PulseSim Pro is in the quote
    if 'PulseSim Pro' in products_in_quote:
        # Check if required bundles are included
        required_bundles = ['CircuitMaster Analyzer', 'VeriSim Express']
        for required in required_bundles:
            if required not in products_in_quote:
                violation_id = mandatory_bundles_article['id']
                break

result = {
    'article_id': mandatory_bundles_article['id'] if mandatory_bundles_article else None,
    'products_in_quote': products_in_quote,
    'violation_found': violation_id is not None,
    'violation_id': violation_id
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
