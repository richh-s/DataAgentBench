code = """import json

# Load knowledge articles
knowledge_file = locals()['var_functions.query_db:5']
with open(knowledge_file, 'r') as f:
    knowledge_articles = json.load(f)

# Find Volume-Based Discounts article
volume_discount_article = None
for article in knowledge_articles:
    if 'Volume-Based Discounts' in article['title']:
        volume_discount_article = article
        break

# Check if there are any quote approval policies
quote_policy_article = None
for article in knowledge_articles:
    if 'quote' in article['title'].lower() and ('policy' in article['title'].lower() or 'approval' in article['title'].lower()):
        quote_policy_article = article
        break

print('Volume-Based Discounts Article:')
if volume_discount_article:
    print('ID: ' + volume_discount_article['id'])
    print('Title: ' + volume_discount_article['title'])
else:
    print('Not found')

print('\nQuote Policy Article:')
if quote_policy_article:
    print('ID: ' + quote_policy_article['id'])
    print('Title: ' + quote_policy_article['title'])
else:
    print('Not found')

# Check for Competing Offers policy (might have discount rules)
competing_offers_article = None
for article in knowledge_articles:
    if 'Competing Offers' in article['title']:
        competing_offers_article = article
        break

print('\nCompeting Offers Article:')
if competing_offers_article:
    print('ID: ' + competing_offers_article['id'])
    print('Title: ' + competing_offers_article['title'])
else:
    print('Not found')

result = {
    'volume_discount_id': volume_discount_article['id'] if volume_discount_article else None,
    'quote_policy_id': quote_policy_article['id'] if quote_policy_article else None,
    'competing_offers_id': competing_offers_article['id'] if competing_offers_article else None
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.execute_python:12': {'total_before_discount': 10179.75, 'total_after_discount': 9140.78, 'max_discount_applied': 15.0, 'min_discount_applied': 5.0, 'volume_discount_article_id': 'ka0Wt000000Eq0MIAS', 'volume_discount_article_title': 'Volume-Based Discounts'}}

exec(code, env_args)
