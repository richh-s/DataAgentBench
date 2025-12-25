code = """import json
import pandas as pd

# Load full knowledge articles from file
path = var_call_zSjJOgES0LsV2hsoyc1WK3th
with open(path, 'r') as f:
    knowledge = json.load(f)

kdf = pd.DataFrame(knowledge)

# Inspect for any articles that mention quotes, pricing, discount, quantity, or configuration rules
mask = kdf['faq_answer__c'].str.contains('quote', case=False, na=False) | \
       kdf['faq_answer__c'].str.contains('pricing', case=False, na=False) | \
       kdf['faq_answer__c'].str.contains('discount', case=False, na=False) | \
       kdf['faq_answer__c'].str.contains('quantity', case=False, na=False) | \
       kdf['faq_answer__c'].str.contains('configuration', case=False, na=False) | \
       kdf['title'].str.contains('discount', case=False, na=False) | \
       kdf['title'].str.contains('bundle', case=False, na=False) | \
       kdf['title'].str.contains('configuration', case=False, na=False)

candidates = kdf[mask]

result = candidates[['id','title']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MYwXHvKJBdEbAE0Ai0kIAevZ': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_c3MWv17M3TuV4dAKwLKvS9sq': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_BJ0GwEDhAAKS4vT5Lds5fdc5': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_zSjJOgES0LsV2hsoyc1WK3th': 'file_storage/call_zSjJOgES0LsV2hsoyc1WK3th.json'}

exec(code, env_args)
