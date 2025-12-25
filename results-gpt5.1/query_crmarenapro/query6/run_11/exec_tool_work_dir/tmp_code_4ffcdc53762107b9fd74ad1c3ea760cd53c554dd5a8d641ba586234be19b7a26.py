code = """import json, pandas as pd
qli = pd.DataFrame(var_call_SLvPaLfNDOGNXwHTU93iXlrk)
# Load full knowledge articles
import os
with open(var_call_wmD142Us6wNelTtJjvaSmRnH, 'r') as f:
    kav = pd.DataFrame(json.load(f))
# Search for pricing / discount policy related articles
text_cols = ['title','summary','faq_answer__c']
for c in text_cols:
    kav[c] = kav[c].fillna('')
joined = (kav.assign(all_text=lambda df: df['title']+' '+df['summary']+' '+df['faq_answer__c'])
           )
# Simple heuristic keywords
keywords = ['discount','maximum quantity','min quantity','bulk','bundle','pricing policy','quote','quotation','approval','needs review','configuration','product mix','upsell','cross-sell','promotion','promo','limit','regulation']
mask = joined['all_text'].str.lower().apply(lambda t: any(k in t for k in keywords))
relevant = joined[mask]
result_ids = relevant['id'].tolist()
# If none found, return empty list
out = result_ids
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_SLvPaLfNDOGNXwHTU93iXlrk': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_wmD142Us6wNelTtJjvaSmRnH': 'file_storage/call_wmD142Us6wNelTtJjvaSmRnH.json', 'var_call_eTimaGxU5KSic9bBu4AMbvMw': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}]}

exec(code, env_args)
