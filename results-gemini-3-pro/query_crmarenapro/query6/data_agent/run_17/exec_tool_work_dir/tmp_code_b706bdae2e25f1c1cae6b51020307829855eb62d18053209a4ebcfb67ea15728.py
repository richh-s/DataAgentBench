code = """import json

with open(locals()['var_function-call-12312399608239827409'], 'r') as f:
    articles = json.load(f)

matches = []
for a in articles:
    txt = (a['Title'] + " " + a['Text']).lower()
    if "discount" in txt and ("limit" in txt or "maximum" in txt or "approve" in txt or "policy" in txt):
        matches.append(a)

print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-3871856346329201065': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3871856346329201134': 'file_storage/function-call-3871856346329201134.json', 'var_function-call-3871856346329201203': 'file_storage/function-call-3871856346329201203.json', 'var_function-call-15430046982164314124': 'file_storage/function-call-15430046982164314124.json', 'var_function-call-12312399608239827409': 'file_storage/function-call-12312399608239827409.json'}

exec(code, env_args)
