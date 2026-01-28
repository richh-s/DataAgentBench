code = """# Load knowledge articles from the file
import json, os

# Read the knowledge articles file
knowledge_file = locals()['var_functions.query_db:2']
if isinstance(knowledge_file, str) and knowledge_file.endswith('.json'):
    with open(knowledge_file, 'r') as f:
        knowledge_articles = json.load(f)
else:
    knowledge_articles = knowledge_file

print(f'Number of knowledge articles: {len(knowledge_articles)}')

# Look for pricing/discount/approval related articles
relevant_articles = []
techpulse_articles = []

for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = (article.get('faq_answer__c') or '').lower()
    
    # Look for quote/pricing/discount related articles
    keywords = ['quote', 'discount', 'approval', 'pricing', 'cost', 'setup', 'contract', 'policy']
    if any(word in title for word in keywords) or any(word in summary for word in keywords) or any(word in faq for word in keywords):
        relevant_articles.append(article)
    
    # Look for TechPulse/EDA related articles
    if 'techpulse' in title or 'techpulse' in summary or 'techpulse' in faq or 'eda' in title or 'eda' in summary or 'eda' in faq:
        techpulse_articles.append(article)

print(f'Quote/pricing related articles: {len(relevant_articles)}')
print(f'TechPulse/EDA related articles: {len(techpulse_articles)}')

# Check quote details from var_functions.query_db:4
quote_items = locals()['var_functions.query_db:4']
print(f'\nQuote items: {len(quote_items)}')
print('Quote line items:')
for item in quote_items:
    print(f"  - Product: {item['Product2Id']}, Quantity: {item['Quantity']}, Unit Price: ${item['UnitPrice']}, Discount: {item['Discount']}%, Total: ${item['TotalPrice']}")

print('\nFirst 5 TechPulse articles:')
for article in techpulse_articles[:5]:
    print(f"  ID: {article.get('id')}, Title: {article.get('title')}")"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}]}

exec(code, env_args)
