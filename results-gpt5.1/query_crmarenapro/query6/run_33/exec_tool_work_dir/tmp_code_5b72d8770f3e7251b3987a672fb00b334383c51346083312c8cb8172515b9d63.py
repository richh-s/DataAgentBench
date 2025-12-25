code = """import json, pandas as pd
qli = pd.DataFrame(var_call_qzcum3rfKtW2ynTMz9v5UgaX)
# load full knowledge articles
with open(var_call_2pAQ7CbZMApwTsSusB8o7q5z, 'r') as f:
    knowledge = pd.DataFrame(json.load(f))
# simple heuristic: look for pricing/discount/quantity policy articles
candidates = knowledge[knowledge['title'].str.contains('Discount|Volume|Installation Timeline|Policy|Pricing', case=False, na=False)].copy()
result = candidates[['id']].to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qzcum3rfKtW2ynTMz9v5UgaX': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_8RJOfjPINNjvEFrvEATZS7YH': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_2pAQ7CbZMApwTsSusB8o7q5z': 'file_storage/call_2pAQ7CbZMApwTsSusB8o7q5z.json'}

exec(code, env_args)
