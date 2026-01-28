code = """import json

# Read the full knowledge article results
with open(var_functions.query_db:2, 'r') as f:
    knowledge_articles = json.load(f)

# Read quote and quote line items
quote_data = var_functions.query_db:0
quote_line_items = var_functions.query_db:4

# Calculate total quote value and analyze discounts
total_quote_value = sum(float(item['TotalPrice']) for item in quote_line_items)

discounts = [float(item['Discount']) for item in quote_line_items]
quantities = [float(item['Quantity']) for item in quote_line_items]

print("=== QUOTE ANALYSIS ===")
print(f"Quote ID: {quote_data[0]['Id']}")
print(f"Status: {quote_data[0]['Status']}")
print(f"Total Value: ${total_quote_value:.2f}")
print(f"Line Items: {len(quote_line_items)}")
print(f"Discounts: {discounts}")
print(f"Quantities: {quantities}")
print(f"Max Discount: {max(discounts)}%")
print(f"Total Quantity: {sum(quantities)}")

# Look for relevant policy articles
policy_keywords = ['discount', 'approval', 'quote', 'pricing', 'competing', 'policy']
relevant_articles = []

for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower() if article.get('faq_answer__c') else ''
    
    # Check if article contains policy-related keywords
    if any(keyword in title or keyword in summary or keyword in faq for keyword in policy_keywords):
        relevant_articles.append(article)

print(f"\n=== FOUND {len(relevant_articles)} RELEVANT POLICY ARTICLES ===")

# Extract key policy information
for article in relevant_articles:
    print(f"\n--- ARTICLE ID: {article['id']} ---")
    print(f"Title: {article['title']}")
    print(f"Summary: {article['summary']}")
    if article.get('faq_answer__c'):
        print(f"FAQ (first 300 chars): {article['faq_answer__c'][:300]}")

# Search for specific policies about discounts and approvals
violation_found = False
violating_article_id = None

for article in relevant_articles:
    article_text = (article.get('title', '') + ' ' + 
                   article.get('summary', '') + ' ' + 
                   (article.get('faq_answer__c', '') or '')).lower()
    
    # Check for discount policy
    if 'competing' in article_text and 'discount' in article_text:
        print(f"\n=== FOUND COMPETING OFFERS POLICY: {article['id']} ===")
        # This article likely contains discount approval rules
        if max(discounts) > 10:  # Assuming 10% might be a threshold
            print(f"VIOLATION: Max discount {max(discounts)}% exceeds policy")
            violation_found = True
            violating_article_id = article['id']
    
    # Check for general approval policies
    if 'approval' in article_text and 'quote' in article_text:
        print(f"\n=== FOUND QUOTE APPROVAL POLICY: {article['id']} ===")

# Check status - if it's "Needs Review", there might be a violation
if quote_data[0]['Status'] == 'Needs Review':
    print(f"\nQuote status is 'Needs Review' - indicating potential policy violation")
    if not violating_article_id:
        # Find the most relevant article about quotes/competing offers
        for article in relevant_articles:
            if 'competing' in article.get('title', '').lower():
                violating_article_id = article['id']
                break

print(f"\n=== FINAL DETERMINATION ===")
print(f"Violation Found: {violation_found}")
print(f"Violating Article ID: {violating_article_id}")

result = {
    "violating_article_id": violating_article_id,
    "status": quote_data[0]['Status']
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}]}

exec(code, env_args)
