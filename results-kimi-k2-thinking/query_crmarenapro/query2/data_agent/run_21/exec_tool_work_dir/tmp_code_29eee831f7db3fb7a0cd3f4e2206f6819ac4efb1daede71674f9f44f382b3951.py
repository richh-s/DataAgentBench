code = """import json

# Read knowledge articles
with open('var_functions.query_db:10', 'r') as f:
    kb_articles = json.load(f)

# Read quote line items
with open('var_functions.query_db:2', 'r') as f:
    quote_lines = json.load(f)

# Calculate total
quote_total = sum(float(line['TotalPrice']) for line in quote_lines)

# Find relevant policies and check violations
violation_kb_id = None

# Check Volume-Based Discounts
vb_article = None
for article in kb_articles:
    if article['title'] == 'Volume-Based Discounts':
        vb_article = article
        break

if vb_article:
    max_discount_pct = 15.0  # According to the article
    
    for line in quote_lines:
        discount = float(line['Discount'])
        if discount > max_discount_pct:
            violation_kb_id = vb_article['id']
            break

# Print results
print(f'Quote total: {quote_total}')
print(f'Violation found: {violation_kb_id}')

# Format for output
result = {
    'violation_kb_id': violation_kb_id,
    'quote_total': quote_total,
    'kb_article_count': len(kb_articles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
