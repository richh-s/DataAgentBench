code = """import json

# Read the knowledge articles file path from storage
knowledge_file_path = locals()['var_functions.query_db:6']
print(f"Knowledge file path: {knowledge_file_path}")

with open(knowledge_file_path, 'r') as f:
    knowledge_articles = json.load(f)

print(f"Number of knowledge articles: {len(knowledge_articles)}")
print("\nArticle IDs and titles:")
for article in knowledge_articles:
    print(f"ID: {article.get('id')}, Title: {article.get('title')}")

# Check for articles related to company regulations, pricing, quotes, etc.
regulation_keywords = ['policy', 'regulation', 'rule', 'guideline', 'compliance', 'price', 'pricing', 'discount', 'quantity', 'quote', 'approval', 'limit']
regulation_articles = []

for article in knowledge_articles:
    title = str(article.get('title', '')).lower()
    summary = str(article.get('summary', '')).lower()
    faq = str(article.get('faq_answer__c', '')).lower()
    
    text_content = title + ' ' + summary + ' ' + faq
    
    if any(keyword in text_content for keyword in regulation_keywords):
        regulation_articles.append(article)

print(f"\nFound {len(regulation_articles)} articles that might contain regulations:")
for article in regulation_articles:
    print(f"ID: {article.get('id')}, Title: {article.get('title')}")

# Check quote details
quote_data = locals()['var_functions.query_db:2']
print(f"\nQuote data: {quote_data}")

# Return the regulation article IDs
result = [article.get('id') for article in regulation_articles]
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Id': '#0Q0Wt000001WLjvKAG', 'OpportunityId': '#006Wt000007BA3HIAW', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000Jqs7tIAB', 'Name': 'TechPulse-NaviCorp EDA Strategic Quote  ', 'Description': 'Initial quote for strategic partnership in electronic design automation solutions focused on AI-powered innovations.', 'Status': 'Approved', 'CreatedDate': '2024-03-18T14:15:00.000+0000', 'ExpirationDate': '2024-05-17'}, {'Id': '0Q0Wt000001WRJ3KAO', 'OpportunityId': '006Wt000007BFEFIA4', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '#003Wt00000JqmtfIAB', 'Name': 'NaviCorp Tech Advanced Navigation Optimization Quote', 'Description': 'Quote for enhancing navigation system through AI-powered EDA solutions.', 'Status': 'Accepted', 'CreatedDate': '2021-07-01T10:00:00.000+0000', 'ExpirationDate': '2021-08-01'}, {'Id': '0Q0Wt000001WKEPKA4', 'OpportunityId': '#006Wt000007BFfeIAG', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000Jqs7tIAB', 'Name': 'NaviCorp Strategic EDA Solutions Quote', 'Description': "Initial quote for AI-powered EDA solutions tailored for NaviCorp's navigation systems enhancement.", 'Status': 'Approved', 'CreatedDate': '2024-03-12T10:30:00.000+0000', 'ExpirationDate': '2024-04-12'}, {'Id': '0Q0Wt000001WREDKA4', 'OpportunityId': '006Wt000007BFpKIAW', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000JqyGWIAZ', 'Name': 'NaviCorp Expansion Quote', 'Description': 'Initial quote for enhancement and expansion of navigation systems with integrated AI-powered EDA solutions.', 'Status': 'Draft', 'CreatedDate': '2023-02-10T11:00:00.000+0000', 'ExpirationDate': '2023-03-10'}, {'Id': '0Q0Wt000001WRHRKA4', 'OpportunityId': '006Wt000007BFxOIAW', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000JqogwIAB', 'Name': 'NaviCorp Strategic Partnership Quote', 'Description': "Comprehensive proposal aligning TechPulse's AI-powered EDA solutions with NaviCorp's navigation technology goals, emphasizing cost-effectiveness and seamless integration.", 'Status': 'Needs Review   ', 'CreatedDate': '2021-05-12T09:00:00.000+0000', 'ExpirationDate': '2021-06-10'}], 'var_functions.query_db:10': [{'Id': '0QLWt0000022abqOAA', 'QuoteId': '0Q0Wt000001WKe9KAG', 'OpportunityLineItemId': '00kWt000002HGIqIAO', 'Product2Id': '#01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '6.0', 'UnitPrice': '599.99', 'Discount': '5.0', 'TotalPrice': '3419.943'}, {'Id': '0QLWt0000022cHnOAI', 'QuoteId': '#0Q0Wt000001WLwnKAG', 'OpportunityLineItemId': '00kWt000002HMB3IAO', 'Product2Id': '01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '7.0', 'UnitPrice': '349.99', 'Discount': '5.0', 'TotalPrice': '2327.4335'}, {'Id': '#0QLWt0000022cHoOAI', 'QuoteId': '0Q0Wt000001WQutKAG', 'OpportunityLineItemId': '00kWt000002HY0zIAG', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '3.0', 'UnitPrice': '599.99', 'Discount': '0.0', 'TotalPrice': '1799.97'}, {'Id': '0QLWt0000022cw9OAA', 'QuoteId': '0Q0Wt000001WSIMKA4', 'OpportunityLineItemId': '00kWt000002HR9DIAW', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '10.0', 'UnitPrice': '529.99', 'Discount': '10.0', 'TotalPrice': '4769.91'}, {'Id': '0QLWt0000022cwAOAQ', 'QuoteId': '0Q0Wt000001WSevKAG', 'OpportunityLineItemId': '00kWt000002HXD5IAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '20.0', 'UnitPrice': '599.99', 'Discount': '20.0', 'TotalPrice': '9599.84'}, {'Id': '0QLWt0000022cwBOAQ', 'QuoteId': '0Q0Wt000001WMCwKAO', 'OpportunityLineItemId': '00kWt000002HXZZIA4', 'Product2Id': '01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022el1OAA', 'QuoteId': '#0Q0Wt000001WMpeKAG', 'OpportunityLineItemId': '00kWt000002HPH2IAO', 'Product2Id': '#01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '7.0', 'UnitPrice': '529.99', 'Discount': '5.0', 'TotalPrice': '3524.4335'}, {'Id': '0QLWt0000022el2OAA', 'QuoteId': '0Q0Wt000001WKFyKAO', 'OpportunityLineItemId': '00kWt000002HUyDIAW', 'Product2Id': '01tWt000006hVBZIA2', 'PricebookEntryId': '01uWt0000027PDRIA2', 'Quantity': '1.0', 'UnitPrice': '399.99', 'Discount': '0.0', 'TotalPrice': '399.99'}, {'Id': '0QLWt0000022el3OAA', 'QuoteId': '0Q0Wt000001WTfpKAG', 'OpportunityLineItemId': '00kWt000002HThJIAW', 'Product2Id': '01tWt000006hV9xIAE', 'PricebookEntryId': '01uWt0000027PBpIAM', 'Quantity': '7.0', 'UnitPrice': '449.99', 'Discount': '5.0', 'TotalPrice': '2992.4335'}, {'Id': '0QLWt0000022ezYOAQ', 'QuoteId': '0Q0Wt000001WNovKAG', 'OpportunityLineItemId': '00kWt000002HN0kIAG', 'Product2Id': '#01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '12.0', 'UnitPrice': '529.99', 'Discount': '10.0', 'TotalPrice': '5723.892'}]}

exec(code, env_args)
