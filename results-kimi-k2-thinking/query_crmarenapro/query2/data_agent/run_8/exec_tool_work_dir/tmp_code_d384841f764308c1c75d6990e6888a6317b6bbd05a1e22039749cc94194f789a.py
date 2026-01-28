code = """import json

# Access storage variables using direct keys
quote_result = var_functions.query_db_0
quote_line_items_result = var_functions.query_db_5
knowledge_file_path = var_functions.query_db_12

# Calculate total quote amount
total_amount = 0.0
for item in quote_line_items_result:
    total_amount += float(item['TotalPrice'])

print('Total quote amount: $' + str(round(total_amount, 2)))

# Total meets highest tier ($20) for 15% discount
tier_20_applies = total_amount >= 20.0
print('Meets $20+ tier for 15% discount: ' + str(tier_20_applies))

# Check actual discounts vs policy
policy_violations = []
for item in quote_line_items_result:
    discount = float(item['Discount'])
    if tier_20_applies and discount < 15.0:
        policy_violations.append({
            'product': item['Product2Id'],
            'actual_discount': discount,
            'expected_min_discount': 15.0
        })

print('Policy violations found: ' + str(len(policy_violations)))

# Find knowledge article ID for volume discounts
volume_article_id = None
with open(knowledge_file_path, 'r') as f:
    knowledge_articles = json.load(f)

for article in knowledge_articles:
    if 'Volume-Based Discounts' in article['title']:
        volume_article_id = article['id']
        break

print('Volume discount article ID: ' + str(volume_article_id))
print('Has violations: ' + str(len(policy_violations) > 0))

result = {
    'has_violations': len(policy_violations) > 0,
    'volume_article_id': volume_article_id,
    'violations': policy_violations
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes'}]}

exec(code, env_args)
