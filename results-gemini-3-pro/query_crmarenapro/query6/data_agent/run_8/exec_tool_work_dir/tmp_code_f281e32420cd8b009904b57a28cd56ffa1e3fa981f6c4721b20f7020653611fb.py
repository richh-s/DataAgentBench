code = """import json

# Load knowledge articles
with open(locals()['var_function-call-809277968078338312'], 'r') as f:
    articles = json.load(f)

product_names = [
    "EcoPCB Creator", 
    "AI Cirku-Tech", 
    "DevVision IDE", 
    "CollabDesign Studio"
]

restriction_keywords = ["limit", "max", "min", "restrict", "policy", "regulation", "must", "cannot", "prohibited", "bundle", "discount", "quantity", "price"]

filtered_articles = []

for article in articles:
    text_content = (str(article.get('title', '')) + " " + 
                    str(article.get('summary', '')) + " " + 
                    str(article.get('faq_answer__c', ''))).lower()
    
    # Check if any product name is present
    prod_found = any(p.lower() in text_content for p in product_names)
    
    # Check if any restriction keyword is present
    keyword_found = any(k in text_content for k in restriction_keywords)
    
    # We want articles that talk about products AND restrictions, OR generic policies about these things.
    # To reduce noise, let's look for matches where product name is mentioned OR title suggests a policy.
    
    is_policy_doc = "policy" in article.get('title', '').lower() or "regulation" in article.get('title', '').lower() or "guideline" in article.get('title', '').lower()
    
    if (prod_found and keyword_found) or is_policy_doc:
        filtered_articles.append({
            "id": article['id'],
            "title": article['title'],
            "summary": article['summary'],
            "faq": article['faq_answer__c']
        })

print("__RESULT__:")
print(json.dumps(filtered_articles))"""

env_args = {'var_function-call-15843595822989592245': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-15843595822989593884': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-809277968078339137': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}], 'var_function-call-809277968078338312': 'file_storage/function-call-809277968078338312.json', 'var_function-call-7732281217241333023': 'file_storage/function-call-7732281217241333023.json'}

exec(code, env_args)
