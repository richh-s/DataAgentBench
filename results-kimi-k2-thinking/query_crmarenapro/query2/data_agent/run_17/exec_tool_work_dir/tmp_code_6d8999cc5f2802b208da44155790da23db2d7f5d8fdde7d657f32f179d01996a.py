code = """import json

# Get the knowledge articles from storage
file_path = locals()['var_functions.query_db:4']

# Read the knowledge articles from the file
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Let's examine the article about Mandatory Bundles more closely
mandatory_bundle_article = None
discount_article = None

for article in knowledge_articles:
    if 'Mandatory Bundles' in article.get('title', ''):
        mandatory_bundle_article = article
    elif 'Volume-Based Discounts' in article.get('title', ''):
        discount_article = article

# Get quote line items from storage
quote_line_items = locals()['var_functions.query_db:2']

# Extract product IDs from quote line items
product_ids_in_quote = []
for item in quote_line_items:
    product_id = item['Product2Id']
    # Clean the ID (remove leading # if present)
    if product_id.startswith('#'):
        product_id = product_id[1:]
    product_ids_in_quote.append(product_id)

print('__RESULT__:')
print(json.dumps({
    'mandatory_bundle_article': mandatory_bundle_article,
    'discount_article': discount_article,
    'products_in_quote': product_ids_in_quote,
    'quote_line_items': quote_line_items
}, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
