code = """import json, pandas as pd, textwrap, re

# Load knowledge articles from file
path = var_call_ePN6NSDLctKfwhKbsOZtO8W1
with open(path, 'r') as f:
    articles = json.load(f)

quote_items = pd.DataFrame(var_call_Jp8WmgsUbAC8rogSrQ5DDgBY)

# Very simplified heuristic: look for pricing/discount policy articles
candidates = []
for art in articles:
    text = (art.get('title','') + ' ' + art.get('summary','') + ' ' + art.get('faq_answer__c','')).lower()
    if any(k in text for k in ['discount', 'pricing', 'quote', 'approval', 'deal desk', 'margin']):
        candidates.append(art)

# Also search for any article that mentions "quote approval" explicitly
best_id = None
for art in candidates:
    text = (art.get('title','') + ' ' + art.get('summary','') + ' ' + art.get('faq_answer__c','')).lower()
    if 'quote approval' in text or 'quote-approval' in text:
        best_id = art['id']
        break

# If nothing obvious, we cannot reliably map to a specific article
result = best_id if best_id is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mo6aOhYxFUMzgWVMEkaqU6fq': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ImPreGrrlbzjyRU84Wrr7Bep': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_ePN6NSDLctKfwhKbsOZtO8W1': 'file_storage/call_ePN6NSDLctKfwhKbsOZtO8W1.json', 'var_call_Jp8WmgsUbAC8rogSrQ5DDgBY': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}]}

exec(code, env_args)
