code = """import json

# Get knowledge articles about pricing and discounts
kb_path = 'var_functions.query_db:10'
with open(kb_path, 'r') as f:
    kb_articles = json.load(f)

# Get quote line items
quote_path = 'var_functions.query_db:2'
with open(quote_path, 'r') as f:
    quote_lines = json.load(f)

# Calculate quote details
total_quote_amount = sum(float(line['TotalPrice']) for line in quote_lines)
line_item_count = len(quote_lines)

print('Knowledge Articles Found:')
for article in kb_articles:
    print(f'ID: {article["id"]}, Title: {article["title"]}')
    
print('\nQuote Details:')
print(f'Total Amount: ${total_quote_amount}')
print(f'Line Items: {line_item_count}')
for line in quote_lines:
    print(f"  Product: {line['Product2Id']}, Discount: {line['Discount']}%")

# Look for relevant policies
print('\nChecking policies...')
violation_article_id = None

# Check Volume-Based Discounts policy
for article in kb_articles:
    if article['title'] == 'Volume-Based Discounts':
        print(f'Found Volume Discounts Policy: {article["id"]}')
        # The article states max 15% discount for purchases over $20
        # Our quote is over $20, so check if any discount exceeds 15%
        for line in quote_lines:
            if float(line['Discount']) > 15.0:
                violation_article_id = article['id']
                print('VIOLATION: Discount exceeds 15% maximum')
        break

print('violation_article_id:', violation_article_id)"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
