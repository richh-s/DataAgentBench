code = """import json, pandas as pd
from pathlib import Path

qli = pd.DataFrame(var_call_7JhGVjEN37WsjrwRJqyYVRIY)

file_path = Path(var_call_4OpHWw8ufBrCgNotEWhQTrZc)
articles = pd.read_json(file_path)

result = None
for _, row in qli.iterrows():
    qty = float(row['Quantity'])
    price = float(row['UnitPrice'])
    discount = float(row['Discount'])
    if qty > 30 and discount >= 10:
        mask = articles['faq_answer__c'].str.contains('bulk order discount', case=False, na=False)
        if mask.any():
            result = articles[mask].iloc[0]['id']
            break

if result is None:
    result = ''

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_7JhGVjEN37WsjrwRJqyYVRIY': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_4B8g8nhO4FmQhOAmZsSVgdag': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_4OpHWw8ufBrCgNotEWhQTrZc': 'file_storage/call_4OpHWw8ufBrCgNotEWhQTrZc.json'}

exec(code, env_args)
