code = """import json

# Read the full knowledge article results
with open(var_functions.query_db:2, 'r') as f:
    knowledge_articles = json.load(f)

# Read quote and quote line items
quote_data = var_functions.query_db:0
quote_line_items = var_functions.query_db:4

# Print what we have
print("=== QUOTE DATA ===")
print(json.dumps(quote_data, indent=2))
print("\n=== QUOTE LINE ITEMS ===")
print(json.dumps(quote_line_items, indent=2))
print(f"\n=== KNOWLEDGE ARTICLES COUNT: {len(knowledge_articles)} ===")

# Look for policy-related articles
policy_articles = []
for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    # Check for policy keywords
    policy_keywords = ['policy', 'approval', 'discount', 'pricing', 'competing', 'volume', 'terms']
    if any(keyword in title or keyword in summary or keyword in faq for keyword in policy_keywords):
        policy_articles.append(article)

print(f"\n=== FOUND {len(policy_articles)} POLICY-RELATED ARTICLES ===")
for article in policy_articles:
    print(f"ID: {article['id']}")
    print(f"Title: {article['title']}")
    print(f"Summary: {article['summary'][:200]}...")
    print("---")

# Calculate total quote value
total_quote_value = sum(float(item['TotalPrice']) for item in quote_line_items)
print(f"\n=== TOTAL QUOTE VALUE: ${total_quote_value:.2f} ===")

# Check discounts
for item in quote_line_items:
    print(f"Product: {item['Product2Id']}, Quantity: {item['Quantity']}, Discount: {item['Discount']}%, Total: ${item['TotalPrice']}")

# Print the full policy articles for analysis
print("\n=== FULL POLICY ARTICLES ===")
for article in policy_articles:
    print(f"\n--- ARTICLE: {article['title']} ---")
    print(f"ID: {article['id']}")
    print(f"SUMMARY: {article['summary']}")
    if 'faq_answer__c' in article and article['faq_answer__c']:
        print(f"FAQ: {article['faq_answer__c'][:500]}...")
    else:
        print("FAQ: None")
    print("---")

result = {
    "quote_id": quote_data[0]['Id'],
    "status": quote_data[0]['Status'],
    "total_value": total_quote_value,
    "line_items_count": len(quote_line_items),
    "policy_articles_found": len(policy_articles)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}]}

exec(code, env_args)
