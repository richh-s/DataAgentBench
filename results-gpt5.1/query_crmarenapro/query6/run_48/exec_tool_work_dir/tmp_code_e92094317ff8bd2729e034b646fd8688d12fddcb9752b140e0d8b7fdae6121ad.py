code = """import json
import pandas as pd

kavs_path = var_call_aD1a0W9nQiXnzdazmP5sUuKw

with open(kavs_path, 'r') as f:
    kavs = json.load(f)

text = json.dumps(kavs).lower()

keywords = ['quantity', 'quantities', 'overbooking', 'over-sell', 'oversell', 'discount', 'discounts', 'unit price', 'unitprice', 'pricing', 'pricebook', 'bundle', 'bundling', 'compatibility', 'configuration', 'config', 'quote line item', 'quote', 'minimum', 'maximum', 'floor', 'ceiling']

matched = []
for row in kavs:
    blob = (row.get('title','') + ' ' + row.get('summary','') + ' ' + row.get('faq_answer__c','')).lower()
    score = sum(1 for k in keywords if k in blob)
    if score:
        matched.append({'id': row['id'], 'title': row['title'], 'score': score})

matched_sorted = sorted(matched, key=lambda x: x['score'], reverse=True)

result = [m['id'] for m in matched_sorted[:5]]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6b5Y4smSY5NYsPl9BvllrWwY': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_dGUzIEln77D5qKJjm1vPWGif': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_ZGlOXVrT04Z81QNMRnLOhRSk': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_aD1a0W9nQiXnzdazmP5sUuKw': 'file_storage/call_aD1a0W9nQiXnzdazmP5sUuKw.json'}

exec(code, env_args)
