code = """import json
# load previous tool results
kp = None
with open(var_call_Gmj0QHlPbamSIVssx1Mi4om8, 'r') as f:
    kp = json.load(f)
quotes = var_call_vUqHbXFe9SExJW9lkFnwM6jZ
qli = var_call_8kjzqI1e1g6RlAYIRf00V654
pbe = var_call_BiUleHBww18JWFlep3S9l0Iq

# search knowledge articles for keywords
keywords = ['discount', 'pricing', 'price', 'approval', 'setup', 'setup fee', 'fees', 'cost', 'authorization', 'discounts']
matches = []
for art in kp:
    text = ' '.join([str(art.get('title','')), str(art.get('faq_answer__c','')), str(art.get('summary',''))]).lower()
    if any(k in text for k in keywords):
        matches.append({'id': art.get('id'), 'title': art.get('title'), 'summary': art.get('summary')})

result = {'quote': quotes, 'quote_line_items': qli, 'pricebook_entries': pbe, 'matching_knowledge_articles': matches}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vUqHbXFe9SExJW9lkFnwM6jZ': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_8kjzqI1e1g6RlAYIRf00V654': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_BiUleHBww18JWFlep3S9l0Iq': [{'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'ProductName': 'CircuitSync Pro'}], 'var_call_Gmj0QHlPbamSIVssx1Mi4om8': 'file_storage/call_Gmj0QHlPbamSIVssx1Mi4om8.json', 'var_call_yktKsxZRLKl1ZrB1qvXCH4yR': []}

exec(code, env_args)
