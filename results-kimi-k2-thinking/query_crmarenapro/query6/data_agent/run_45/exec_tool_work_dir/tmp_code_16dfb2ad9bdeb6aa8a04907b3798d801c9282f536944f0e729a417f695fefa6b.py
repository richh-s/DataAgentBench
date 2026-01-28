code = """import json

# Read the knowledge articles file since it's too large
full_result_file = var_functions.query_db:10
with open(full_result_file, 'r') as f:
    knowledge_articles = json.load(f)

# Filter for relevant articles about configuration, setup, and regulations
relevant_articles = []
for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    # Look for articles about pricing rules, configuration policies, quantity limits, etc.
    if any(keyword in title + summary + faq for keyword in 
           ['config', 'setup', 'regulation', 'policy', 'quantity limit', 'maximum quantity', 
            'invalid config', 'pricing rule', 'bundle rule', 'product setup', 
            'combination', 'restrict', 'require', 'minimum', 'maximum']):
        relevant_articles.append(article)

print(f'Found {len(relevant_articles)} relevant articles:')
for article in relevant_articles:
    print(f"ID: {article['id']}, Title: {article['title']}")
    print(f"Summary: {article['summary'][:200]}...")
    print('---')"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
