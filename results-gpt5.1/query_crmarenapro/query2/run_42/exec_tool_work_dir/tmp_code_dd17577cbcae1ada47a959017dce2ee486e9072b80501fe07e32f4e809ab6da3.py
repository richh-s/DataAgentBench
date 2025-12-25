code = """import json, pandas as pd

quote = pd.DataFrame(var_call_GYZJ9zFQr3kITwp3REeZCXxN)
qlis = pd.DataFrame(var_call_5kCspnDmkyudYjQR1NtCY3Td)

# compute effective discount vs list price rule assumptions
qlis['Quantity'] = qlis['Quantity'].astype(float)
qlis['UnitPrice'] = qlis['UnitPrice'].astype(float)
qlis['Discount'] = qlis['Discount'].astype(float)
qlis['TotalPrice_calc'] = qlis['Quantity'] * qlis['UnitPrice'] * (1 - qlis['Discount']/100)

# simple rule: if any line discount > 10% and quantity < 10, violates Volume-Based Discounts (max 10% unless volume)
violate_volume = any((qlis['Discount'] > 10) & (qlis['Quantity'] < 10))

# simple rule: if fewer than 3 lines, must include mandatory bundle, but we have 4 lines so assume OK
violation_id = None
if violate_volume:
    violation_id = 'ka0Wt000000Eq0MIAS'

print("__RESULT__:")
print(json.dumps(violation_id))"""

env_args = {'var_call_GYZJ9zFQr3kITwp3REeZCXxN': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_5kCspnDmkyudYjQR1NtCY3Td': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_ZZLBRxYiTYyITCe0zCzM3A1d': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_m9fnL4MyXYsLFDDeAzBct7LA': 'file_storage/call_m9fnL4MyXYsLFDDeAzBct7LA.json', 'var_call_lcRNACasKwCmARFhjl9PRnyW': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes'}]}

exec(code, env_args)
