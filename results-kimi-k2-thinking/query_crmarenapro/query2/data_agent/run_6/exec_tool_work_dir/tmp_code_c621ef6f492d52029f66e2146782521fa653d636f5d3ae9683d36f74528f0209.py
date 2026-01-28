code = """import json

# Access knowledge articles from file path
knowledge_file = var_functions.query_db:2
with open(knowledge_file, 'r') as f:
    knowledge_articles = json.load(f)

# Access products from file path  
products_file = var_functions.query_db:12
with open(products_file, 'r') as f:
    all_products = json.load(f)

# Get quote items
quote_items = var_functions.query_db:5

# Create product ID to name mapping
product_dict = {}
for prod in all_products:
    clean_id = prod['Id'].replace('#', '')
    product_dict[clean_id] = prod['Name'].strip()

# Get products in the quote
quote_products = []
for item in quote_items:
    item_id = item['Product2Id'].replace('#', '')
    if item_id in product_dict:
        quote_products.append(product_dict[item_id])

# Find Mandatory Bundles article
bundles_article = None
for article in knowledge_articles:
    if 'Mandatory Bundles' in article.get('title', ''):
        bundles_article = article
        break

# Check for violations
violation_id = None
if bundles_article:
    article_text = bundles_article.get('faq_answer__c', '')
    
    # Check PulseSim Pro bundle requirements
    if 'PulseSim Pro' in quote_products:
        req1 = 'CircuitMaster Analyzer' in article_text
        req2 = 'VeriSim Express' in article_text
        
        # Check if required products are in the quote
        if 'CircuitMaster Analyzer' not in quote_products or 'VeriSim Express' not in quote_products:
            violation_id = bundles_article['id']

result = json.dumps({
    'violation_id': violation_id,
    'products_in_quote': quote_products,
    'article_found': bundles_article is not None
})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
