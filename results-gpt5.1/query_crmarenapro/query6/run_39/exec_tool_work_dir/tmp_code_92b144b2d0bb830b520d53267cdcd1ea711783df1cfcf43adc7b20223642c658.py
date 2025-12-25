code = """import json, pandas as pd
from pathlib import Path

# Load knowledge articles
path = Path(var_call_Pmy3okeMsXeZAiaYyXxozIii)
with path.open() as f:
    articles = json.load(f)

kdf = pd.DataFrame(articles)

# Simple heuristic: look for articles mentioning "quantity", "discount", "unit price", "quote" or "configuration" which might correspond to pricing/config rules
mask = (
    kdf['title'].str.contains('quantity|discount|pricing|price|quote|configuration|bundle', case=False, na=False) |
    kdf['summary'].str.contains('quantity|discount|pricing|price|quote|configuration|bundle', case=False, na=False) |
    kdf['faq_answer__c'].str.contains('quantity|discount|pricing|price|quote|configuration|bundle', case=False, na=False)
)

candidates = kdf[mask]

# If multiple, just return all ids (the question asks for Id of the knowledge article that the invalid config violates, but we don't have explicit mapping, so best-effort)
result_ids = candidates['id'].tolist()

out = json.dumps(result_ids)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9Q4BuI4J4J1xu3Qn7FoIjSU1': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_zMgPcTiukCb3qqYjEksF15uM': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_Pmy3okeMsXeZAiaYyXxozIii': 'file_storage/call_Pmy3okeMsXeZAiaYyXxozIii.json'}

exec(code, env_args)
