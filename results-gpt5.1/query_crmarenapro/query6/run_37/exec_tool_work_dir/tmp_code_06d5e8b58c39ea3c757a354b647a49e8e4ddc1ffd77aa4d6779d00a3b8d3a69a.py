code = """import json
qli = var_call_tLk8KlBYIr3qxf4Zp63aAXsj
violations = []
for row in qli:
    qty = float(row['Quantity'])
    if qty > 30:
        violations.append({'QuoteLineItemId': row['Id'], 'Reason': 'Quantity exceeds allowed limit', 'Quantity': qty})

print("__RESULT__:")
print(json.dumps(violations))"""

env_args = {'var_call_tLk8KlBYIr3qxf4Zp63aAXsj': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_D16ACdjX7tf7uYkj7WKkWUdA': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_RrbVT7GuABacYYtWGLLrVlkb': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_5FKLpBrNIc7xNj2eislEqbXw': 'file_storage/call_5FKLpBrNIc7xNj2eislEqbXw.json', 'var_call_VzTHMDhdTO4oIVslw0rn0l9f': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   '}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers'}]}

exec(code, env_args)
