code = """import json

# Load knowledge articles
with open(locals()['var_function-call-13001382274841372266'], 'r') as f:
    articles = json.load(f)

# Quote Items
quote_items = locals()['var_function-call-1582344941043085337']
# Product Map (Id -> Name)
products_raw = locals()['var_function-call-13001382274841374023']
product_map = {p['Id']: p['Name'] for p in products_raw}
# Also map cleaned ID to Name if needed
product_map_clean = {}
for p in products_raw:
    clean_id = p['Id'].replace('#', '')
    product_map_clean[clean_id] = p['Name']

# Identify product names in the quote
quote_products = []
for item in quote_items:
    pid = item['Product2Id'].replace('#', '')
    pname = product_map_clean.get(pid, "Unknown")
    quote_products.append({
        'Product': pname,
        'Quantity': float(item['Quantity']),
        'UnitPrice': float(item['UnitPrice']),
        'TotalPrice': float(item['TotalPrice']),
        'Discount': float(item['Discount']) if item['Discount'] else 0.0
    })

# Search articles for relevant rules
relevant_articles = []
keywords = ["quantity", "limit", "maximum", "minimum", "policy", "regulation", "setup", "price", "discount"]
product_names = [p['Product'] for p in quote_products]

for art in articles:
    text = (art['title'] + " " + art['summary'] + " " + (art['faq_answer__c'] or "")).lower()
    
    # Check if article mentions any of the products
    mentions_product = any(p.lower() in text for p in product_names)
    
    # Check if article mentions any keywords
    mentions_keyword = any(k in text for k in keywords)
    
    if mentions_product or (mentions_keyword and "policy" in text):
         relevant_articles.append({
             'Id': art['id'],
             'Title': art['title'],
             'Summary': art['summary']
         })

print("__RESULT__:")
print(json.dumps({'QuoteSummary': quote_products, 'RelevantArticles': relevant_articles}, indent=2))"""

env_args = {'var_function-call-1582344941043085956': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-1582344941043085337': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-13001382274841374023': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}], 'var_function-call-13001382274841372266': 'file_storage/function-call-13001382274841372266.json'}

exec(code, env_args)
