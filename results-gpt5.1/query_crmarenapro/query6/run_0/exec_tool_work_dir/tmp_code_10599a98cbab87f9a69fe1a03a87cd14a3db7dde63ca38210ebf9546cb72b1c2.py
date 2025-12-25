code = """import json, pandas as pd, os, textwrap

path = var_call_a9CwPKP7giMKl8UPQA2VLYh7
with open(path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

mask = df['faq_answer__c'].str.contains('quantity', case=False, na=False) | df['faq_answer__c'].str.contains('discount', case=False, na=False) | df['faq_answer__c'].str.contains('pricing', case=False, na=False) | df['title'].str.contains('pricing', case=False, na=False) | df['title'].str.contains('discount', case=False, na=False) | df['title'].str.contains('quote', case=False, na=False)

cand = df[mask]

if not cand.empty:
    ka_id = cand.iloc[0]['id']
else:
    ka_id = None

res_str = json.dumps(ka_id)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_L5Odo4ll3iesPp6cuJhGtQiH': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_PlnMvKKT6W1DwtjgrthZSZRY': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_a9CwPKP7giMKl8UPQA2VLYh7': 'file_storage/call_a9CwPKP7giMKl8UPQA2VLYh7.json', 'var_call_q0XWGGce5qzYHTzh4eHawCfm': {'has_issue': True}}

exec(code, env_args)
