code = """import json
import re

# Get the quote details
quote_data = var_functions.query_db:0
print("Quote Data:", json.dumps(quote_data, indent=2))

# Get the quote line items
quote_line_items = var_functions.query_db:2
print("\nQuote Line Items:", json.dumps(quote_line_items, indent=2))

# Load the full knowledge article data
with open(var_functions.query_db:3, 'r') as f:
    knowledge_articles = json.load(f)

print("\nNumber of knowledge articles:", len(knowledge_articles))

# Find the Mandatory Bundles article
mandatory_bundles_article = None
for article in knowledge_articles:
    if "mandatory" in article["title"].lower() and "bundle" in article["title"].lower():
        mandatory_bundles_article = article
        break

if mandatory_bundles_article:
    print("\nFound Mandatory Bundles Article:")
    print("ID:", mandatory_bundles_article["id"])
    print("Title:", mandatory_bundles_article["title"])
    # Print first 500 chars of the article
    print("Content preview:", mandatory_bundles_article["faq_answer__c"][:500])
else:
    print("\nCould not find Mandatory Bundles article")

# Now let's check which products are in the quote
# I need to get the product names
print("\n=== Getting product details ===")"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
