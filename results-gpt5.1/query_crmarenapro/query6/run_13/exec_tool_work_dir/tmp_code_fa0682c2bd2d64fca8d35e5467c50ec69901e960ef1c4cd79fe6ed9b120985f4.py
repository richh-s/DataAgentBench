code = """import json, pandas as pd
from pathlib import Path

file_path = var_call_lByWksFImY28mdjaUg6gXbV7
with open(file_path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

mask = (
    df['faq_answer__c'].str.contains('quantity', case=False, na=False) |
    df['faq_answer__c'].str.contains('pricing', case=False, na=False) |
    df['faq_answer__c'].str.contains('discount', case=False, na=False) |
    df['faq_answer__c'].str.contains('quote', case=False, na=False) |
    df['title'].str.contains('Discount', case=False, na=False) |
    df['title'].str.contains('Bundling', case=False, na=False) |
    df['title'].str.contains('Configuration', case=False, na=False)
)

candidates = df[mask]

result = candidates[['id','title']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vNkdPw0y05WcmuHFe7mRPEsn': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_o22Bkjrn4kkGYDD71eyaGjEp': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_lByWksFImY28mdjaUg6gXbV7': 'file_storage/call_lByWksFImY28mdjaUg6gXbV7.json'}

exec(code, env_args)
