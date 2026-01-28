code = """import json

# Read the full knowledge article results from the file path
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Read quote and quote line items
quote_data = var_functions.query_db:0
quote_line_items = var_functions.query_db:4

# Check the quote status
quote_status = quote_data[0]['Status']
print(f"Quote Status: {quote_status}")

# Calculate the maximum discount
max_discount = max(float(item['Discount']) for item in quote_line_items)
print(f"Maximum Discount: {max_discount}%")

# Find the competing offers policy article
competing_offers_article = None
for article in knowledge_articles:
    title = article.get('title', '').lower()
    if 'competing' in title:
        competing_offers_article = article
        break

if competing_offers_article:
    print(f"Found Competing Offers Article: {competing_offers_article['id']}")
    print(f"Article Title: {competing_offers_article['title']}")
else:
    print("No competing offers article found")

# Determine if there's a violation
violating_article_id = None
if quote_status == 'Needs Review' and competing_offers_article:
    # The quote needs review, likely due to policy violation
    # The competing offers policy likely governs discount approvals
    violating_article_id = competing_offers_article['id']

result = json.dumps({"violating_article_id": violating_article_id})
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}]}

exec(code, env_args)
