code = """import json

# Read knowledge articles about policies
with open('var_functions.query_db:10', 'r') as f:
    kb_articles = json.load(f)

print('Found', len(kb_articles), 'policy-related articles')

# Read quote line items  
with open('var_functions.query_db:2', 'r') as f:
    quote_lines = json.load(f)

total_quote_value = sum(float(line['TotalPrice']) for line in quote_lines)
line_count = len(quote_lines)

print(f'Quote has {line_count} line items, total value: ${total_quote_value:.2f}')

# Check for violation - looking at volume discounts policy
volume_discounts_article = None
mandatory_bundles_article = None

for article in kb_articles:
    if 'Volume-Based Discounts' in article['title']:
        volume_discounts_article = article
    if 'Mandatory Bundles' in article['title']:
        mandatory_bundles_article = article

if volume_discounts_article:
    print('\nVolume Discounts Article Found:', volume_discounts_article['id'])
    print('Content mentions discounts up to 15% for purchases over $20')
    print('Our quote total is: $', total_quote_value)
    
    # Check discounts applied in our quote
    for line in quote_lines:
        print(f"Product {line['Product2Id']}: Discount {line['Discount']}%")
        
    if total_quote_value >= 20:
        max_allowed_discount = 15.0
        for line in quote_lines:
            if float(line['Discount']) > max_allowed_discount:
                print(f"VIOLATION: Discount {line['Discount']}% exceeds max {max_allowed_discount}% for purchases over $20")
                violation_id = volume_discounts_article['id']
                break
        else:
            violation_id = None
            print('No volume discount violations found')
    else:
        violation_id = None
        print('Quote value under $20, different discount rules apply')

----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps({
    'kb_articles_count': len(kb_articles),
    'quote_total': total_quote_value,
    'volume_discounts_article_id': volume_discounts_article['id'] if volume_discounts_article else None,
    'mandatory_bundles_article_id': mandatory_bundles_article['id'] if mandatory_bundles_article else None,
    'violation_found': violation_id is not None,
    'violation_id': violation_id
}, default=str))
----END PRINT FORMAT----"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
