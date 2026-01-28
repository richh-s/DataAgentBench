code = """import json

# Access storage variables
quote_line_items_result = var_functions.query_db_5
quote_result = var_functions.query_db_0

# Calculate total quote amount
total_amount = 0.0
for item in quote_line_items_result:
    total_amount += float(item['TotalPrice'])

print(f"Total quote amount: ${total_amount:.2f}")

# Get discount-related knowledge
knowledge_file_path = var_functions.query_db_12
with open(knowledge_file_path, 'r') as f:
    knowledge_articles = json.load(f)

volume_discount_article = None
for article in knowledge_articles:
    if 'Volume-Based Discounts' in article['title']:
        volume_discount_article = article
        break

print(f"\nVolume discount article found: {volume_discount_article is not None}")
if volume_discount_article:
    print(f"Article ID: {volume_discount_article['id']}")
    print(f"Total price check: Compare discounts vs. actual discounts")

# Check actual discounts in the quote
for item in quote_line_items_result:
    discount = float(item['Discount'])
    total_price = float(item['TotalPrice'])
    quantity = float(item['Quantity'])
    unit_price = float(item['UnitPrice'])
    expected_price = quantity * unit_price
    expected_discounted = expected_price * (1 - discount/100)
    print(f"Item: {item['Product2Id']}, Discount: {discount}%, Expected: ${expected_discounted:.2f}, Actual: ${total_price:.2f}")

print('__RESULT__:')
print(json.dumps({'total_amount': total_amount, 'has_volume_article': volume_discount_article is not None}, default=str))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes'}]}

exec(code, env_args)
