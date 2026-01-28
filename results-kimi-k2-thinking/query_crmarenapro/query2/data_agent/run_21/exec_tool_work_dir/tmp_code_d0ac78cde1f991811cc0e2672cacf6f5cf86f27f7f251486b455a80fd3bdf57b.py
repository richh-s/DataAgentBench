code = """import json

# Reading the knowledge articles file
with open('var_functions.query_db:6', 'r') as f:
    knowledge_articles = json.load(f)

print('Total knowledge articles found:', len(knowledge_articles))

# Let's look for policy-related keywords in any field
policy_keywords = ['policy', 'approval', 'quote', 'pricing', 'discount', 'limit', 'compliance', 'setup', 'requirements']

policy_articles = []
for article in knowledge_articles:
    # Check in title, faq_answer, summary
    text_fields = []
    if article.get('title'):
        text_fields.append(article['title'].lower())
    if article.get('faq_answer__c'):
        text_fields.append(article['faq_answer__c'].lower())
    if article.get('summary'):
        text_fields.append(article['summary'].lower())
    
    found_keywords = []
    for field in text_fields:
        for keyword in policy_keywords:
            if keyword in field:
                found_keywords.append(keyword)
    
    if found_keywords:
        policy_articles.append({
            'id': article.get('id', ''),
            'title': article.get('title', ''),
            'found_keywords': list(set(found_keywords))
        })

print('Policy-related articles found:', len(policy_articles))
for article in policy_articles[:10]:  # Show first 10
    print(f"ID: {article['id']}, Title: {article['title']}")
    print(f"Keywords: {article['found_keywords']}")
    print()

# Also search for terms that might indicate company policies
additional_terms = ['terms', 'conditions', 'guideline', 'restriction', 'max', 'minimum', 'validate', 'violate']

additional_articles = []
for article in knowledge_articles:
    text_fields = []
    if article.get('title'):
        text_fields.append(article['title'].lower())
    if article.get('faq_answer__c'):
        text_fields.append(article['faq_answer__c'].lower())
    if article.get('summary'):
        text_fields.append(article['summary'].lower())
    
    found_terms = []
    for field in text_fields:
        for term in additional_terms:
            if term in field:
                found_terms.append(term)
    
    if found_terms:
        additional_articles.append({
            'id': article.get('id', ''),
            'title': article.get('title', ''),
            'found_terms': list(set(found_terms))
        })

print('Additional relevant articles:', len(additional_articles))
for article in additional_articles[:10]:
    print(f"ID: {article['id']}, Title: {article['title']}")
    print(f"Terms: {article['found_terms']}")
    print()

----BEGIN PRINT FORMAT----
print("__RESULT__:")
print(json.dumps({
    'policy_articles_count': len(policy_articles),
    'additional_articles_count': len(additional_articles),
    'sample_policy_articles': policy_articles[:5],
    'sample_additional_articles': additional_articles[:5]
}, default=str))
----END PRINT FORMAT----"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
