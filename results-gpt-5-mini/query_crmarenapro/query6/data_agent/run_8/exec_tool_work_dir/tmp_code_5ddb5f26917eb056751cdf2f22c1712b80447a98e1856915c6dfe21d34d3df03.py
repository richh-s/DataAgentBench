code = """import json
path = var_call_8qqeHhbLpUDLxp2jwMiqVZHU
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)
# search for relevant keywords
keywords = ['discount', 'approval', 'price', 'pricing', 'quantity', 'limit', 'bulk', 'unauthorized', 'discounts', 'pricing policy', 'pricebook', 'approval required']
matches = []
for a in articles:
    text = ' '.join([str(a.get('title','')),(a.get('faq_answer__c') or ''),(a.get('summary') or '')]).lower()
    for kw in keywords:
        if kw in text:
            matches.append({'id': a.get('id'), 'title': a.get('title'), 'snippet': (a.get('summary') or '')[:200]})
            break
# also include top few entries if no matches
result = {'matches': matches[:20], 'total_matches': len(matches)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cjoqsjVdWbDW1IWg76Pc81YX': [], 'var_call_8a4Y65GajdsxOj1eIZ86eFFO': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_43uacvyKzUYUiGuhdbw1ZNP1': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_zis5RSENC2FKSzlVU0Q7Q8Nc': [{'Id': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_dZDAj2Tsiijxi7vDeBQoKQ60': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6', 'IsActive': '1'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4', 'IsActive': '1'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5', 'IsActive': '1'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30', 'IsActive': '1'}], 'var_call_8qqeHhbLpUDLxp2jwMiqVZHU': 'file_storage/call_8qqeHhbLpUDLxp2jwMiqVZHU.json'}

exec(code, env_args)
