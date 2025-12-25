code = """import json
import pandas as pd

qlis = pd.DataFrame(var_call_Rk9R2RdMj5Or9VZskTJv6GHc)

# Business rule inference from knowledge: look for articles mentioning pricing, discount, quantity, or configuration rules
import os
with open(var_call_FS08Ay4RL9I8GWAMpInKQ2Ur, 'r') as f:
    kav = pd.read_json(f)

text = (kav['title'].fillna('') + ' ' + kav['summary'].fillna('') + ' ' + kav['faq_answer__c'].fillna('')).str.lower()

mask = text.str.contains('discount') | text.str.contains('quantity') | text.str.contains('bulk') | text.str.contains('pricing') | text.str.contains('price book') | text.str.contains('quote configuration') | text.str.contains('config')

candidates = kav[mask]

# Heuristic: pick the first matching article id as governing config/discount rules
ka_id = None
if not candidates.empty:
    ka_id = candidates.iloc[0]['id']

result = json.dumps(ka_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Rk9R2RdMj5Or9VZskTJv6GHc': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_9PLdmUs2vH1elQxaYTpJgPnN': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_ff4rFyoAQgcEn1jzTYZhuE9L': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_FS08Ay4RL9I8GWAMpInKQ2Ur': 'file_storage/call_FS08Ay4RL9I8GWAMpInKQ2Ur.json'}

exec(code, env_args)
