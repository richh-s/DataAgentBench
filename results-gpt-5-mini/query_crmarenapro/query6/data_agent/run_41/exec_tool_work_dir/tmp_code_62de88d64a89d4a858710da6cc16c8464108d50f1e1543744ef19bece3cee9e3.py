code = """import json
# Load the knowledge articles JSON stored in var_call_X1FZdf2TtYXCdBZ4ncGyCe0j
path = var_call_X1FZdf2TtYXCdBZ4ncGyCe0j
with open(path, 'r') as f:
    data = json.load(f)
# find articles with keywords
keywords = ['discount', 'volume', 'price', 'pricing', 'quantity', 'approval']
matches = []
for a in data:
    text = (a.get('title','') + ' ' + a.get('summary','')).lower()
    for k in keywords:
        if k in text:
            matches.append({'id': a.get('id'), 'title': a.get('title'), 'summary': a.get('summary')})
            break
# print results
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_call_odEBb1mQIHOssKI6xxcwkm7f': [], 'var_call_Gi6ZZyYcAlu58CrF9BxH7cEf': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'AccountId': '001Wt00000PHVsDIAX', 'OpportunityId': '006Wt000007BGgXIAW', 'Status': 'Needs Review'}], 'var_call_DMLKQx9SHLjUbEysnh5eJVP8': [], 'var_call_wNoGlqHGpPYskamILCNILlUJ': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_X1FZdf2TtYXCdBZ4ncGyCe0j': 'file_storage/call_X1FZdf2TtYXCdBZ4ncGyCe0j.json'}

exec(code, env_args)
