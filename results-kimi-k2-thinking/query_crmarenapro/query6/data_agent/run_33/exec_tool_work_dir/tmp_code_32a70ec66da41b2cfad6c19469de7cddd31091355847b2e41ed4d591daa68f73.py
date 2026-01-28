code = """import json

# Load the knowledge articles from the file
with open('/tmp/tmp_oxfrr9a.json', 'r') as f:
    knowledge_articles = json.load(f)

print('Total knowledge articles:', len(knowledge_articles))

# Find articles related to quotes, pricing, approval, or review processes
policy_articles = []
for article in knowledge_articles:
    content = (article.get('title', '') + article.get('summary', '') + article.get('faq_answer__c', '')).lower()
    if any(keyword in content for keyword in ['quote', 'pricing', 'approval', 'review', 'limit', 'policy', 'regulation']):
        policy_articles.append(article)

print('Policy-related articles found:', len(policy_articles))
for article in policy_articles:
    print('ID:', article.get('id'), '| Title:', article.get('title'))

# Analyze the quote status
print('\nAnalyzed Quote:')
print('Quote ID: #0Q0Wt000001WRAzKAO')
print('Status: Needs Review')

# The products in this quote
ai_cirku_tech = {'quantity': 2, 'price': 529.99}
devvision_ide = {'quantity': 4, 'price': 299.99}

print('Products:')
print('- AI Cirku-Tech:', ai_cirku_tech['quantity'], 'units')
print('- DevVision IDE:', devvision_ide['quantity'], 'units')

# Look for the Product Quantity Limits article specifically
print('\nProduct Quantity Limits Article:')
quantity_limits_article = None
for article in knowledge_articles:
    if 'Product Quantity Limits' in article.get('title', ''):
        quantity_limits_article = article
        print('ID:', article.get('id'))
        break

# Check if our products are listed with quantity restrictions
if quantity_limits_article:
    content = quantity_limits_article.get('faq_answer__c', '').lower()
    print('Article contains AI Cirku-Tech?', 'ai cirku-tech' in content or 'ai' in content and 'cirku' in content)
    print('Article contains DevVision IDE?', 'devvision' in content)"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Id': '#00kWt000002HHRkIAO', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'TotalPrice': '1059.98'}, {'Id': '00kWt000002HQJYIA4', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'TotalPrice': '1199.96'}], 'var_functions.query_db:10': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'UnitPrice': '299.99'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'UnitPrice': '529.99'}], 'var_functions.list_db:12': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
