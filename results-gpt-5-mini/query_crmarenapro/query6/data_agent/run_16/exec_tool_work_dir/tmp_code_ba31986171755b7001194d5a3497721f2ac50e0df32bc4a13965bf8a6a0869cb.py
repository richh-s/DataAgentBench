code = """import json
# load previous tool results
quotes = var_call_BWYn3PyHvRVHdsQFqKcIkck7
qlineitems = var_call_utIpwpmV335OvLyHZgRgO6U7
# load knowledge articles from file path
with open(var_call_uaNYThWtfR1XK49RQRkSVil7, 'r') as f:
    knowledge = json.load(f)
# Prepare a simple list of id and title for inspection
out = [{ 'id': k.get('id'), 'title': k.get('title'), 'summary': (k.get('summary') or '')[:200] } for k in knowledge]
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_SBwyCPxIxPmVRKe5sx1vDfNp': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_Lo39St9Wsy9Hf3w2dyBBhJZa': [], 'var_call_BWYn3PyHvRVHdsQFqKcIkck7': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'AccountId': '001Wt00000PHVsDIAX', 'OpportunityId': '006Wt000007BGgXIAW', 'Status': 'Needs Review'}], 'var_call_utIpwpmV335OvLyHZgRgO6U7': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_uaNYThWtfR1XK49RQRkSVil7': 'file_storage/call_uaNYThWtfR1XK49RQRkSVil7.json'}

exec(code, env_args)
