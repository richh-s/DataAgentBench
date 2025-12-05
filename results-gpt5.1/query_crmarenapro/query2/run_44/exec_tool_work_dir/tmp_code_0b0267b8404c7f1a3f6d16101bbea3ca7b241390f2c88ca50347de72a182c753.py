code = """import json, pandas as pd
kavs_path = var_call_MUZlnauP05NRbfOQFmMfXWzJ
with open(kavs_path, 'r') as f:
    kavs = json.load(f)
quote = var_call_0sSQt4wm9gJ7gxCFdmyBfKRN[0]
qli = pd.DataFrame(var_call_xVqOYbxwtkgFv0RDBkVdaLFx)
qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)
qli['TotalPrice'] = qli['TotalPrice'].astype(float)
subtotal = float(qli['TotalPrice'].sum())
violations = []
for ka in kavs:
    title = ka.get('title','').strip()
    summary = ka.get('summary','').lower()
    if 'volume-based discounts' in title.lower():
        if qli['Quantity'].max() < 10 and qli['Discount'].max() > 10:
            violations.append(ka['id'])
    if 'return policy' in title.lower():
        if quote['Status'].lower() == 'needs review' and 'return' in quote['Description'].lower():
            violations.append(ka['id'])
    if 'installation timeline' in title.lower():
        if quote['ExpirationDate'] < '2021-06-15':
            violations.append(ka['id'])
result = None
if violations:
    result = violations[0]
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_0sSQt4wm9gJ7gxCFdmyBfKRN': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_RbQN4yGZaeo0qJCH04YRKlV4': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_xVqOYbxwtkgFv0RDBkVdaLFx': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_MUZlnauP05NRbfOQFmMfXWzJ': 'file_storage/call_MUZlnauP05NRbfOQFmMfXWzJ.json'}

exec(code, env_args)
