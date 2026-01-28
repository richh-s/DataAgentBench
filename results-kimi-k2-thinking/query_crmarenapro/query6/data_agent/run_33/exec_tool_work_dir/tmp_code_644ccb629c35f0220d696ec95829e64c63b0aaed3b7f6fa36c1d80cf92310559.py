code = """import json

# Load the knowledge articles from the file
with open('/tmp/tmp_oxfrr9a.json', 'r') as f:
    knowledge_articles = json.load(f)

print('Total knowledge articles:', len(knowledge_articles))

# Search for articles related to regulations, policies, quotes, pricing
relevant_articles = []
for article in knowledge_articles:
    title = article.get('title', '')
    summary = article.get('summary', '')
    faq = article.get('faq_answer__c', '')
    content = (title + ' ' + summary + ' ' + faq).lower()
    
    keywords = ['quote', 'pricing', 'price', 'discount', 'approval', 'review', 'limit', 'regulation', 'policy', 'violation', 'invalid', 'needs review']
    if any(keyword in content for keyword in keywords):
        relevant_articles.append(article)

print('Relevant articles found:', len(relevant_articles))

# Display relevant article IDs and titles
for article in relevant_articles:
    print('Article ID:', article.get('id'))
    print('Title:', article.get('title'))
    print('---')

# Analyze the specific quote situation
print('\nQuote Analysis:')
print('Quote ID: #0Q0Wt000001WRAzKAO')
print('Status: Needs Review')
print('Opportunity ID: 006Wt000007BGgXIAW')

# Products in the quote
products = [
    {'name': 'AI Cirku-Tech', 'quantity': 2, 'unit_price': 529.99},
    {'name': 'DevVision IDE', 'quantity': 4, 'unit_price': 299.99}
]

print('\nProducts in quote:')
for p in products:
    print('-', p['name'], ':', p['quantity'], 'units @ $' + str(p['unit_price']))

# Check for articles about approval/review processes
print('\n\nArticles about approval/review:')
for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    if 'approval' in title or 'review' in title or 'needs review' in faq:
        print('ID:', article.get('id'))
        print('Title:', article.get('title'))

# Check product quantity limits article specifically
print('\n\nProduct Quantity Limits article:')
for article in knowledge_articles:
    if 'Product Quantity Limits' in article.get('title', ''):
        print('ID:', article.get('id'))
        print('Full content snippet:')
        content = article.get('faq_answer__c', '')
        # Get first 1000 chars to see the product list
        print(content[:1000])"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Id': '#00kWt000002HHRkIAO', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'TotalPrice': '1059.98'}, {'Id': '00kWt000002HQJYIA4', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'TotalPrice': '1199.96'}], 'var_functions.query_db:10': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'UnitPrice': '299.99'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'UnitPrice': '529.99'}], 'var_functions.list_db:12': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
