code = """import json

# Get quote data
quote_data = locals()['var_functions.query_db:0']
quote_line_items = locals()['var_functions.query_db:2']

print('Quote ID:', quote_data[0]['Id'])
print('Quote Status:', quote_data[0]['Status'])
print('Account ID:', quote_data[0]['AccountId'])
print('Expiration Date:', quote_data[0]['ExpirationDate'])

# Calculate totals
total_amount = 0
for item in quote_line_items:
    total_amount = total_amount + float(item['TotalPrice'])
    print('Line Item - Product:', item['Product2Id'], 'Discount:', item['Discount'], '%')

print('Total Quote Amount:', total_amount)

# Load knowledge articles
knowledge_file = locals()['var_functions.query_db:4']
if type(knowledge_file) == str and '.json' in knowledge_file:
    with open(knowledge_file, 'r') as f:
        all_articles = json.load(f)
else:
    all_articles = knowledge_file

print('Total articles found:', len(all_articles))

# Find policy articles
policy_articles = []
for article in all_articles:
    txt = (article.get('title','') + ' ' + article.get('summary','') + ' ' + article.get('faq_answer__c','')).lower()
    if 'quote' in txt or 'approval' in txt or 'discount' in txt:
        policy_articles.append(article)

print('Policy articles found:', len(policy_articles))

result = {'policy_count': len(policy_articles), 'total_amount': total_amount}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
