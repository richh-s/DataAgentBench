code = """import json, re

# knowledge articles preview is in file path string
path = var_call_MAPUbvSFzYryGqD6kqFt0FQx
with open(path, 'r') as f:
    articles = json.load(f)

quote = var_call_grq7rjJMhopcXJgCUsKiOJvX[0]
lines = var_call_QvwBjQ8ml3ASRBByeOZPRsDY

text = (quote['Description'] or '') + ' ' + ' '.join(str(l.get('Discount','')) for l in lines)

violations = []
for art in articles:
    body = (art.get('faq_answer__c') or '') + ' ' + (art.get('summary') or '') + ' ' + (art.get('title') or '')
    if re.search(r"discount", body, re.I) and re.search(r"implementation|setup", body, re.I):
        violations.append(art['id'].lstrip('#'))

result = violations[0] if violations else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_grq7rjJMhopcXJgCUsKiOJvX': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_W10FNm8vTWqjyrXPkVs9KzUQ': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_QvwBjQ8ml3ASRBByeOZPRsDY': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_MAPUbvSFzYryGqD6kqFt0FQx': 'file_storage/call_MAPUbvSFzYryGqD6kqFt0FQx.json'}

exec(code, env_args)
