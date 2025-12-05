code = """import json
import pandas as pd

kavs_path = var_call_vD2qOKdlRODCIArvMHhadt7g
with open(kavs_path, 'r') as f:
    kavs = json.load(f)

# Look for articles mentioning discount, quantity limits, bundling, or pricing rules
keywords = ['discount', 'quantity', 'minimum', 'maximum', 'bundle', 'bundling', 'volume pricing', 'price rule', 'quote', 'configuration', 'product mix']

matches = []
for row in kavs:
    text = ' '.join(str(row.get(col, '')) for col in ['title', 'faq_answer__c', 'summary']).lower()
    if any(k in text for k in keywords):
        matches.append(row)

# also inspect product-related or quote-related titles if not captured
if not matches:
    for row in kavs:
        title = str(row.get('title','')).lower()
        if any(w in title for w in ['pricing', 'discount', 'quote', 'configuration', 'product', 'bundle']):
            matches.append(row)

# For this task, assume there is a single relevant article defining invalid config; pick the one that talks about quote configuration or discount/quantity rules
chosen_id = None
for row in matches:
    t = str(row.get('title','')).lower()
    body = str(row.get('faq_answer__c','')).lower()
    if 'quote' in t or 'configuration' in t or 'config' in t or 'discount' in t or 'quantity' in body:
        chosen_id = row['id']
        break

if chosen_id is None and matches:
    chosen_id = matches[0]['id']

result = json.dumps(chosen_id if chosen_id is not None else '')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_bp4mSetw26MxbxIG01yurjDk': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_O3H0yRX6v4xShDXbqBOg2AD4': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_5oolbWibG6XXMSettLu0AqU8': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_uOteHHWCNMHDxtdwzZZ6mcJ7': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}], 'var_call_vD2qOKdlRODCIArvMHhadt7g': 'file_storage/call_vD2qOKdlRODCIArvMHhadt7g.json'}

exec(code, env_args)
