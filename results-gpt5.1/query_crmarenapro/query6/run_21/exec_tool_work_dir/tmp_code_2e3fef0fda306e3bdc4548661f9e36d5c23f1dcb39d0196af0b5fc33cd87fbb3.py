code = """import json, pandas as pd
from pathlib import Path

path = var_call_oCpUDs6oBtn36DrBc0xF6hgc
with open(path, 'r') as f:
    all_kb = json.load(f)

df = pd.DataFrame(all_kb)

mask = df['title'].str.contains('discount', case=False, na=False) | df['summary'].str.contains('discount', case=False, na=False) | df['title'].str.contains('pricing', case=False, na=False) | df['summary'].str.contains('pricing', case=False, na=False) | df['title'].str.contains('configuration', case=False, na=False) | df['summary'].str.contains('configuration', case=False, na=False)

candidates = df[mask][['id','title','summary']]

result = candidates.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ElqgsaSBtrC0ZJ7wGZ1zjorR': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_8Zv4d6qcl8VS5whvVmso1VXa': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_oCpUDs6oBtn36DrBc0xF6hgc': 'file_storage/call_oCpUDs6oBtn36DrBc0xF6hgc.json'}

exec(code, env_args)
