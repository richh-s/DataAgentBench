code = """import json, pandas as pd, os
from pathlib import Path

path = var_call_zeisvZpa0fMpEGA2nJkNLaXY
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
mask = df['title'].str.contains('price', case=False, na=False) | df['title'].str.contains('discount', case=False, na=False) | df['summary'].str.contains('price', case=False, na=False) | df['summary'].str.contains('discount', case=False, na=False) | df['title'].str.contains('Volume-Based', case=False, na=False)
res = df[mask][['id','title']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_5ltyPlaBlWECXlukIbUNqa6j': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_LUvDkePWbDFhfxCRIWEdDuar': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_zeisvZpa0fMpEGA2nJkNLaXY': 'file_storage/call_zeisvZpa0fMpEGA2nJkNLaXY.json'}

exec(code, env_args)
