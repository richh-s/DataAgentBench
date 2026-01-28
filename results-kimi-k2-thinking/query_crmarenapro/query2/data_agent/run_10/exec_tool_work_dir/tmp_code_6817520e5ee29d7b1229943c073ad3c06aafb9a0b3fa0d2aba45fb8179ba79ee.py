code = """import json

# Load the quote data
quote_data = locals()['var_functions.query_db:0']
quote_line_items = locals()['var_functions.query_db:2']

# Calculate total values
total_before_discount = 0
total_after_discount = 0
max_discount = 0
min_discount = 100

for item in quote_line_items:
    quantity = float(item['Quantity'])
    unit_price = float(item['UnitPrice'])
    discount_pct = float(item['Discount'])
    total_price = float(item['TotalPrice'])
    
    line_total_before = quantity * unit_price
    total_before_discount += line_total_before
    total_after_discount += total_price
    
    max_discount = max(max_discount, discount_pct)
    min_discount = min(min_discount, discount_pct)

# Read knowledge articles
knowledge_file = locals()['var_functions.query_db:5']
with open(knowledge_file, 'r') as f:
    knowledge_articles = json.load(f)

# Find Volume-Based Discounts article
volume_discount_article = None
for article in knowledge_articles:
    if 'Volume-Based Discounts' in article['title']:
        volume_discount_article = article
        break

result = {
    'total_before_discount': round(total_before_discount, 2),
    'total_after_discount': round(total_after_discount, 2),
    'max_discount_applied': max_discount,
    'min_discount_applied': min_discount,
    'volume_discount_article_id': volume_discount_article['id'] if volume_discount_article else None,
    'volume_discount_article_title': volume_discount_article['title'] if volume_discount_article else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': []}

exec(code, env_args)
