code = """import json
import os

# The result is stored in a file path
file_path = var_functions.query_db_8

# Read the full knowledge articles result from the file
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Check the first few articles to understand the structure
print("Total knowledge articles:", len(knowledge_articles))
print("\nFirst few articles (sample):")
for i, article in enumerate(knowledge_articles[:3]):
    print(f"{i+1}. ID: {article['id']}")
    print(f"   Title: {article['title']}")
    print(f"   Summary: {article.get('summary', 'N/A')}")
    print()

# Look for policy-related articles specifically about discounts, approvals, or EDA products
key_articles = []
for article in knowledge_articles:
    title = article['title'].lower()
    if any(keyword in title for keyword in ['discount', 'policy', 'approval', 'eda', 'pricing', 'volume', 'setup']):
        key_articles.append(article)

print(f"\nFound {len(key_articles)} relevant articles:")
for article in key_articles:
    print(f"- {article['id']}: {article['title']}")"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.list_db:6': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
