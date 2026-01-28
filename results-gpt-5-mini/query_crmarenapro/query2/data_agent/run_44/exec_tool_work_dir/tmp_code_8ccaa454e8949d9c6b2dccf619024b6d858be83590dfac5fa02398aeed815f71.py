code = """import json
# We'll do a simpler deterministic check: check if any KB article explicitly caps discount at <=10% (common policy)
kbs = json.load(open(var_call_4yTPlE6M8yN29KIJ5i2pLL14, 'r', encoding='utf-8'))
qlis = var_call_Uk5oFfVyTyVjIxxUKDYfd7A2
# compute max discount
maxd = max([float(x.get('Discount') or 0) for x in qlis]) if qlis else 0
found = None
for art in kbs:
    text = ' '.join([str(art.get('title') or ''), str(art.get('summary') or ''), str(art.get('faq_answer__c') or '')]).lower()
    if 'discount' in text and '10%' in text and ('approval' in text or 'require' in text):
        # if article says approval required for discounts over 10%
        if maxd > 10:
            found = art.get('id')
            break
# print result
print('__RESULT__:')
print(json.dumps(found if found is not None else None))"""

env_args = {'var_call_Khova90dcaPd1mpUsZLdCGQu': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_YFuCbawQCo0VvJOBgxNpapl1': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_Uk5oFfVyTyVjIxxUKDYfd7A2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_FplrY4JKcU9ED4VpPqffWs15': [{'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'Pricebook2Id': 'None', 'PricebookName': 'None', 'PricebookEntryId': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}], 'var_call_axhlztujn1MN1COyUTteACsP': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_4WaAghbakIXTPJ6TN6ii0Wkd': [], 'var_call_4yTPlE6M8yN29KIJ5i2pLL14': 'file_storage/call_4yTPlE6M8yN29KIJ5i2pLL14.json', 'var_call_BXTv5hu0e3zSuWmhgn7gWdU5': None}

exec(code, env_args)
