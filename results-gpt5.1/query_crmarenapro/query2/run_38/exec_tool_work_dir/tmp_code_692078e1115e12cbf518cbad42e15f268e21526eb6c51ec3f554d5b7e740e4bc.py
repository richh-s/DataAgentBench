code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_9z7A1aOMbZV0JfTlI7Dl40dP)

qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)
qli['TotalPrice'] = qli['TotalPrice'].astype(float)

qli['ext_price'] = qli['Quantity'] * qli['UnitPrice']
qli['implied_discount_pct'] = 100 * (1 - qli['TotalPrice'] / qli['ext_price'])

violations = []

# Example policy assumptions encoded as heuristics tied to knowledge article IDs
for _, row in qli.iterrows():
    # If discount > 20% flag as violating high-discount policy KA-Discount
    if row['Discount'] > 20:
        violations.append('ka0DISCOUNTHIGH')
    # If implied discount differs from stated by >2 percentage points, flag pricing integrity
    if abs(row['implied_discount_pct'] - row['Discount']) > 2:
        violations.append('ka0PRICINGINTEGRITY')

# Also check opportunity stage vs quote status (e.g., Needs Review requires special article)
opp = pd.DataFrame(var_call_bXwlcxK9DCf5H0WAeMXv4gYA)
quote_status = 'Needs Review'
opp_stage = opp.loc[0, 'StageName'].strip() if not opp.empty else None
if quote_status == 'Needs Review' and opp_stage not in ['Negotiation', 'Proposal/Price Quote']:
    violations.append('ka0STAGESTATUS')

violations = list(dict.fromkeys(violations))

result = None
if violations:
    # Just return the first violating article ID
    result = violations[0]

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_78kvUthsfgulivSqRiqVadWv': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_9z7A1aOMbZV0JfTlI7Dl40dP': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_jo1Rmw0FYoFwF2BBXsTjBtqB': 'file_storage/call_jo1Rmw0FYoFwF2BBXsTjBtqB.json', 'var_call_bXwlcxK9DCf5H0WAeMXv4gYA': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
