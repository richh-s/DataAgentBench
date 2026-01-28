code = """import json

# Access the storage variables directly
quote_result = var_functions.query_db_0
knowledge_file_path = var_functions.query_db_2
quote_line_items_result = var_functions.query_db_5

print(f"Quote: {quote_result}")
print(f"Quote Line Items: {quote_line_items_result}")

# Read knowledge articles from file
with open(knowledge_file_path, 'r') as f:
    knowledge_articles = json.load(f)

print(f"Total knowledge articles: {len(knowledge_articles)}")

# Search for articles related to quote approval policies
policy_keywords = ['quote', 'approval', 'policy', 'discount', 'cost', 'setup', 'pricing', 'limit', 'threshold', 'configuration', 'setup', 'minimum', 'maximum']
policy_articles = []

for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    text = title + summary + faq
    if any(keyword in text for keyword in policy_keywords):
        policy_articles.append({
            'id': article.get('id'),
            'title': article.get('title'),
            'summary': article.get('summary', '')[:200] + '...' if len(article.get('summary', '')) > 200 else article.get('summary', '')
        })

print(f"Found {len(policy_articles)} policy-related articles")
for pa in policy_articles:
    print(f"- {pa['id']}: {pa['title']}")

print('__RESULT__:')
print(json.dumps(policy_articles, default=str))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}]}

exec(code, env_args)
