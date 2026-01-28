code = """import json
# var_call_moQKSYWtL2Ow94xUUfZGTgrd contains the filepath to the full JSON result
path = var_call_moQKSYWtL2Ow94xUUfZGTgrd
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)
# search for relevant keywords
keywords = ['discount', 'discounts', 'quantity', 'price', 'pricing', 'pricebook', 'unit price', 'approval', 'bulk', 'limit', 'maximum']
matches = []
for a in articles:
    text = ' '.join([str(a.get('title','') or ''), str(a.get('faq_answer__c','') or ''), str(a.get('summary','') or '')]).lower()
    for k in keywords:
        if k in text:
            matches.append({'id': a.get('id'), 'title': a.get('title'), 'summary': a.get('summary')})
            break
# Deduplicate
seen = set(); uniq = []
for m in matches:
    if m['id'] not in seen:
        seen.add(m['id']); uniq.append(m)

result = {'matches': uniq, 'count': len(uniq)}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_W4Un3dnKY44yTBweUPoCaifK': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_moQKSYWtL2Ow94xUUfZGTgrd': 'file_storage/call_moQKSYWtL2Ow94xUUfZGTgrd.json', 'var_call_4HZHCRx6d7lDbRRvXnJlEhPM': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_WwP2dNeI5cBA7fhZC3cPDPhA': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}]}

exec(code, env_args)
