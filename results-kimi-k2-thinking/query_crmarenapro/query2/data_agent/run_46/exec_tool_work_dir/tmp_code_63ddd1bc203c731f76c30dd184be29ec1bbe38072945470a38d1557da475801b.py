code = """import json, re, sys

# Access the stored results from locals() - handle the variable names safely
quote_data = locals().get('var_functions.query_db:0', [])
quote_line_items = locals().get('var_functions.query_db:2', [])

print("=== Quote Analysis ===")
print(f"Quote ID: {quote_data[0]['Id'] if quote_data else 'Not found'}")
print(f"Status: {quote_data[0]['Status'] if quote_data else 'Not found'}")
print(f"Account ID: {quote_data[0]['AccountId'] if quote_data else 'Not found'}")

if quote_line_items:
    total_amount = sum(float(item.get('TotalPrice', 0)) for item in quote_line_items)
    print(f"Total Quote Amount: ${total_amount:.2f}")
    print(f"Number of line items: {len(quote_line_items)}")
    
    # Check discounts
    for item in quote_line_items:
        discount = float(item.get('Discount', 0))
        quantity = float(item.get('Quantity', 0))
        product = item.get('Product2Id')
        print(f"Product: {product}, Discount: {discount}%, Quantity: {quantity}")

# Load knowledge articles
knowledge_file = locals().get('var_functions.query_db:4')
if knowledge_file and isinstance(knowledge_file, str) and '.json' in knowledge_file:
    with open(knowledge_file, 'r') as f:
        articles = json.load(f)
else:
    articles = knowledge_file if knowledge_file else []

print(f"\nTotal knowledge articles available: {len(articles)}")

# Look for policy-related articles
policy_articles = []
keywords = ['quote', 'approval', 'discount', 'pricing', 'policy', 'setup']

for article in articles:
    content = (article.get('title', '') + ' ' + 
               article.get('summary', '') + ' ' + 
               article.get('faq_answer__c', '')).lower()
    
    if any(keyword in content for keyword in keywords):
        policy_articles.append(article)

print(f"Found {len(policy_articles)} potentially relevant articles")

for article in policy_articles[:5]:
    print(f"- ID: {article.get('id')}, Title: {article.get('title')}")

result = {'policy_article_count': len(policy_articles)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
