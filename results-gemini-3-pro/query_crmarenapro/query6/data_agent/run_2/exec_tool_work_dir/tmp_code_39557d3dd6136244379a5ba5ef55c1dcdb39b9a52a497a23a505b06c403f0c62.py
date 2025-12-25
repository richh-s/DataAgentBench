code = """import json
import pandas as pd

# Load data
quote_items = locals()['var_function-call-11112941990237070855']
products = locals()['var_function-call-16336193074995933946']
articles_path = locals()['var_function-call-11112941990237072932']

with open(articles_path, 'r') as f:
    articles = json.load(f)

# Create lookup for products
product_map = {p['Id']: p['Name'].strip() for p in products}

# Enhance quote items with product names
enhanced_items = []
for item in quote_items:
    pid = item['Product2Id'].replace('#', '')
    pname = product_map.get(pid, "Unknown")
    item['ProductName'] = pname
    enhanced_items.append(item)

# Search articles for relevant rules
# Keywords: product names, "quantity", "limit", "max", "min", "price", "discount", "config"
keywords = ["quantity", "limit", "maximum", "minimum", "discount", "price", "config", "regulation"]
product_names = [i['ProductName'] for i in enhanced_items]

potential_articles = []
for art in articles:
    text = (art['title'] + " " + art['faq_answer__c'] + " " + art['summary']).lower()
    
    # Check if article mentions any product in the quote
    mentioned_products = [p for p in product_names if p.lower() in text]
    
    # Check if article mentions any keyword
    mentioned_keywords = [k for k in keywords if k in text]
    
    if mentioned_products and mentioned_keywords:
        potential_articles.append({
            "id": art['id'],
            "title": art['title'],
            "summary": art['summary'],
            "body": art['faq_answer__c'],
            "mentioned_products": mentioned_products
        })

print("__RESULT__:")
print(json.dumps(potential_articles, indent=2))"""

env_args = {'var_function-call-11112941990237070855': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-11112941990237072932': 'file_storage/function-call-11112941990237072932.json', 'var_function-call-16336193074995933946': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}]}

exec(code, env_args)
