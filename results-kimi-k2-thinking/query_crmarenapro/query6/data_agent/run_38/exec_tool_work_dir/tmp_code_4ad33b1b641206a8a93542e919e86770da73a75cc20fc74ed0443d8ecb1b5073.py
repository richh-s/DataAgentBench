code = """import json

# Read the knowledge articles file
with open('/mnt/data/tmpw8z1b4s5.json', 'r') as f:
    knowledge_articles = json.load(f)

print(f"Total knowledge articles found: {len(knowledge_articles)}")

# Look for articles specifically about discounts or quantity limits
relevant_articles = []
for article in knowledge_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    
    # Check for discount and quantity related keywords
    keywords = ['discount', 'quantity limit', 'maximum', 'limit', 'volume discount', 'approval', 'pricing rule', 'pricing policy']
    content = title + ' ' + summary + ' ' + faq
    
    if any(keyword in content for keyword in keywords):
        relevant_articles.append(article)
        print(f"\nRelevant Article Found:")
        print(f"ID: {article['id']}")
        print(f"Title: {article['title']}")
        if 'discount' in content:
            print("- Contains discount information")
        if 'limit' in content:
            print("- Contains limit information")

print(f"\n\nTotal relevant articles: {len(relevant_articles)}")
print("__RESULT__:")
print(json.dumps([{'id': a['id'], 'title': a['title']} for a in relevant_articles]))"""

env_args = {'var_functions.query_db:0': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
