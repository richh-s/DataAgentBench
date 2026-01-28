code = """import json

# The result is stored as a file path string
articles_file_path = var_functions.query_db:10

# Open and read the full JSON content
with open(articles_file_path, 'r') as f:
    full_articles_data = json.load(f)

# Check structure and find relevant articles
print('Total articles:', len(full_articles_data))
print('First article as example:', full_articles_data[0].get('title'))

# Filter for articles that seem related to configuration or policies
config_rules = []
for article in full_articles_data:
    title = article.get('title', '').lower()
    faq = article.get('faq_answer__c', '').lower() if article.get('faq_answer__c') else ''
    
    keywords = ['volume', 'quantity', 'policy', 'regulation', 'setup', 'installation', 'timeline', 'config', 'rule', 'limit']
    
    if any(keyword in title or keyword in faq for keyword in keywords):
        config_rules.append(article)

print('Relevant articles found:', len(config_rules))
for art in config_rules:
    print('Article ID:', art['id'])
    print('Title:', art['title'])
    print('Summary:', art.get('summary', '')[:100] + '...')
    print('---')

# Now check the quote details
import pandas as pd
quote_items = var_functions.query_db:6
df_items = pd.DataFrame(quote_items)

print('Quote line items:')
print(df_items)

# Output the final result in the required format
result = { 
    'relevant_articles_count': len(config_rules), 
    'article_ids': [art['id'] for art in config_rules]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
