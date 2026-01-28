code = """import json

# Load knowledge articles from file
articles_file = locals()['var_functions.query_db:14']
with open(articles_file, 'r') as f:
    articles = json.load(f)

# Find discount policy article
discount_article = None
for article in articles:
    title = article.get('title', '').lower()
    if 'volume-based discount' in title:
        discount_article = article
        break

print('Discount Article ID:', discount_article['id'] if discount_article else 'Not found')

# Check quote items
quote_items = locals()['var_functions.query_db:4']
print('Quote items:', len(quote_items))

# Calculate total and check compliance
total_amount = 0
violations = []
for item in quote_items:
    total_price = float(item['TotalPrice'])
    total_amount += total_price
    discount = float(item['Discount'])
    print('Item discount:', discount, 'Total:', total_price)
    # Based on volume discount policy: 15% for purchases over $20
    if discount < 15.0:
        violations.append(item['Id'])

print('Total amount: $', round(total_amount, 2))
print('Violations found:', len(violations))

if violations:
    print('COMPLIANCE_VIOLATION')
    print('POLICY_ARTICLE_ID:', discount_article['id'])
else:
    print('COMPLIANCE_OK')"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
