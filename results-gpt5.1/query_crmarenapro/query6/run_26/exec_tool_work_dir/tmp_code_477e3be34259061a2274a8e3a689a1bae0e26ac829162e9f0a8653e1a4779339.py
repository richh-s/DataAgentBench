code = """import json, pandas as pd
qli = pd.DataFrame(var_call_ZpHtYkVpr3lZncbWsTVwRvP8)
arts_preview_path = var_call_8wVKCx5h3YYbPp4ZV1LC1hQn
with open(arts_preview_path, 'r') as f:
    arts = pd.DataFrame(json.load(f))
# search for knowledge mentioning discount, volume, quantity, pricing policies
mask = arts['title'].str.contains('Discount', case=False, na=False) | arts['summary'].str.contains('Discount', case=False, na=False) | arts['title'].str.contains('Volume', case=False, na=False) | arts['summary'].str.contains('Volume', case=False, na=False) | arts['summary'].str.contains('pricing', case=False, na=False)
relevant = arts[mask]
result = relevant[['id','title']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZpHtYkVpr3lZncbWsTVwRvP8': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_zmwjY4xaEAhwbw7Y7pfnqdc6': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_8wVKCx5h3YYbPp4ZV1LC1hQn': 'file_storage/call_8wVKCx5h3YYbPp4ZV1LC1hQn.json'}

exec(code, env_args)
