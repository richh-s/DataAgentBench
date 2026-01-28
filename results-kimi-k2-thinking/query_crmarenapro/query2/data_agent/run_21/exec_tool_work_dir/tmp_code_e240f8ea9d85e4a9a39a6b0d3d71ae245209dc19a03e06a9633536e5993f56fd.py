code = """import json

# Get quote line items from storage
quote_lines = var_functions.query_db:2

# The knowledge articles result might be a path or direct data
# Let's check if it's a path (string) or direct data
kb_result = var_functions.query_db:10

if isinstance(kb_result, str) and (kb_result.startswith('[') or kb_result.startswith('{')):
    # It's a JSON string
    kb_articles = json.loads(kb_result)
elif isinstance(kb_result, str):
    # It's a file path
    with open(kb_result, 'r') as f:
        kb_articles = json.load(f)
else:
    # It's already parsed data
    kb_articles = kb_result

# Calculate quote total
total_quote = sum(float(line['TotalPrice']) for line in quote_lines)

# Check Volume-Based Discounts article
violation_kb_id = None
vol_discounts_article = None

for article in kb_articles:
    if 'Volume-Based Discounts' in article['title']:
        vol_discounts_article = article
        break

# Apply policy checks
if vol_discounts_article and total_quote >= 20:
    max_allowed = 15.0  # per article
    for line in quote_lines:
        if float(line['Discount']) > max_allowed:
            violation_kb_id = vol_discounts_article['id']
            break

# Output results
result_data = {
    'quote_total': total_quote,
    'violation_kb_id': violation_kb_id,
    'kb_article_count': len(kb_articles)
}

print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
