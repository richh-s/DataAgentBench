code = """import json

# This is the result from the previous execution
result_data = locals()['var_functions.query_db:6']

# Load knowledge articles to find any policy violations
knowledge_file = locals()['var_functions.query_db:5']
with open(knowledge_file, 'r') as f:
    knowledge_articles = json.load(f)

print("=== Knowledge Articles Available ===")
for article in knowledge_articles:
    print(f"ID: {article['id']}")
    print(f"Title: {article['title']}")
    print(f"URL: {article['urlname']}")
    print("---")

# Look for specific policy articles
policy_keywords = ['quote approval', 'approval', 'policy', 'discount limit', 'maximum discount', 'quote policy']
matching_articles = []

for article in knowledge_articles:
    title_lower = article['title'].lower()
    content_lower = article['faq_answer__c'].lower()
    
    for keyword in policy_keywords:
        if keyword in title_lower or keyword in content_lower:
            matching_articles.append(article)
            break

print(f"\n=== Found {len(matching_articles)} potentially relevant policy articles ===")
for article in matching_articles:
    print(f"- {article['id']}: {article['title']}")"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [], 'var_functions.execute_python:12': {'total_before_discount': 10179.75, 'total_after_discount': 9140.78, 'max_discount_applied': 15.0, 'min_discount_applied': 5.0, 'volume_discount_article_id': 'ka0Wt000000Eq0MIAS', 'volume_discount_article_title': 'Volume-Based Discounts'}}

exec(code, env_args)
