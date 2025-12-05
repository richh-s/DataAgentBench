code = """import json, pandas as pd, os
path = var_call_TzW0IFFTReGtQcB3GEDo4F9z
with open(path, 'r') as f:
    arts = json.load(f)
# Simple heuristic: look for pricing/discount/quantity rules
keywords = ['discount', 'quantity', 'minimum quantity', 'max quantity', 'bundle', 'pricing rule', 'pricebook', 'quote line']
matched = []
for a in arts:
    text = (a.get('title','') + ' ' + a.get('faq_answer__c','') + ' ' + a.get('summary','')).lower()
    if any(k in text for k in keywords):
        matched.append(a)
# If multiple, just return their ids
ids = [m['id'] for m in matched]
result = json.dumps(ids)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_V5gYGwj9oBVJRMoQpGvDgwVU': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_kjMjbqprYuZW5WAZZl8fEczX': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_gKYDjypvamtBFL9dG8ECFpUY': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_TzW0IFFTReGtQcB3GEDo4F9z': 'file_storage/call_TzW0IFFTReGtQcB3GEDo4F9z.json'}

exec(code, env_args)
