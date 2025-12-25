code = """import json

# Load the knowledge articles
with open(locals()['var_function-call-11402171984943820752'], 'r') as f:
    articles = json.load(f)

# Define the products we are interested in
products = {
    "EcoPCB Creator": {"qty": 3.0, "price": 349.99, "discount": 0.0},
    "AI Cirku-Tech": {"qty": 2.0, "price": 529.99, "discount": 0.0},
    "DevVision IDE": {"qty": 4.0, "price": 299.99, "discount": 0.0},
    "CollabDesign Studio": {"qty": 35.0, "price": 399.99, "discount": 15.0}
}

relevant_articles = []

for article in articles:
    text = (article.get('title') or '') + " " + (article.get('summary') or '') + " " + (article.get('faq_answer__c') or '')
    text_lower = text.lower()
    
    # Check if any product name is mentioned in the article
    for prod_name in products.keys():
        if prod_name.lower() in text_lower or prod_name.split()[0].lower() in text_lower:
             relevant_articles.append({
                 "id": article['id'],
                 "title": article['title'],
                 "summary": article['summary'],
                 "faq_answer": article['faq_answer__c']
             })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-4382610911686573992': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-4382610911686570847': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-11402171984943818189': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}], 'var_function-call-11402171984943820752': 'file_storage/function-call-11402171984943820752.json'}

exec(code, env_args)
