code = """import json
import re

# Load the quote and line items data using locals()
quote_data = locals()['var_functions.query_db:0']
quote_line_items = locals()['var_functions.query_db:2']

print("Quote Data:")
print(json.dumps(quote_data, indent=2))
print("\nQuote Line Items:")
print(json.dumps(quote_line_items, indent=2))

# Load full knowledge articles
knowledge_file_path = locals()['var_functions.query_db:4']
if isinstance(knowledge_file_path, str) and knowledge_file_path.endswith('.json'):
    with open(knowledge_file_path, 'r') as f:
        knowledge_articles = json.load(f)
else:
    knowledge_articles = knowledge_file_path

print(f"\nTotal knowledge articles: {len(knowledge_articles)}")

# Search for policy-related articles
policy_keywords = ['quote', 'approval', 'discount', 'pricing', 'policy', 'compliance', 'limit', 'setup']
policy_articles = []

for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq_answer = article.get('faq_answer__c', '').lower()
    
    # Check if article contains policy keywords
    has_policy_keyword = any(keyword in title or keyword in summary or keyword in faq_answer 
                            for keyword in policy_keywords)
    
    if has_policy_keyword:
        policy_articles.append({
            'id': article.get('id'),
            'title': article.get('title'),
            'summary': article.get('summary'),
            'faq_answer': article.get('faq_answer__c')
        })

print(f"\nFound {len(policy_articles)} potentially relevant policy articles:")
for article in policy_articles:
    print(f"ID: {article['id']}, Title: {article['title']}")

# Analyze the quote details
total_quote_amount = 0
for line_item in quote_line_items:
    total_quote_amount += float(line_item.get('TotalPrice', 0))

print(f"\nTotal Quote Amount: ${total_quote_amount:.2f}")

# Look at discount amounts
discounts = []
for line_item in quote_line_items:
    discounts.append({
        'product': line_item.get('Product2Id'),
        'discount': float(line_item.get('Discount', 0)),
        'quantity': float(line_item.get('Quantity', 0))
    })

print("\nDiscounts per line item:")
for d in discounts:
    print(f"Product: {d['product']}, Discount: {d['discount']}%, Quantity: {d['quantity']}")

result = {
    'total_quote_amount': total_quote_amount,
    'discounts': discounts,
    'policy_articles_found': len(policy_articles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
