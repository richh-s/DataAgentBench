code = """import json, pandas as pd, os
path = var_call_Mbr4T4giYthWg4BqW95rfF84
with open(path, 'r') as f:
    articles = json.load(f)
# simple heuristic: look for policy-related articles mentioning quotes, discount, pricing, approval, TCO, ROI, implementation, deployment, setup
keywords = ['quote', 'pricing', 'discount', 'approval', 'tco', 'roi', 'implementation', 'deployment', 'setup', 'total cost of ownership']
policy_candidates = []
for art in articles:
    text = ((art.get('title') or '') + ' ' + (art.get('summary') or '') + ' ' + (art.get('faq_answer__c') or '')).lower()
    if any(k in text for k in keywords):
        policy_candidates.append(art)
# further narrow to those that sound like internal policy vs competitor analysis by excluding 'competitor' in title
policy_candidates = [a for a in policy_candidates if 'competitor' not in (a.get('title') or '').lower()]
# For this synthetic dataset, assume there is at most one relevant approval/quote policy article; return its id if any, else None
result = policy_candidates[0]['id'] if policy_candidates else None
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YgKkvTQgZFtpmUgD0DbVIw7u': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_4taJC64zsE5LZFbZGnf7b54F': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_sagyz0B5ZpOiuScjO7Adwwgm': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'Phone': '222-111-2222', 'Industry': 'Tech Consulting', 'Description': 'InnovateX Solutions provides cutting-edge consulting services, assisting businesses in integrating the latest technologies into their operations. Using tools like CloudLink Designer and CircuitAI Innovator, they enhance collaborative efforts and circuit design precision. Their focus on seamless tech integration empowers clients to achieve significant efficiency gains.', 'NumberOfEmployees': '850.0', 'ShippingState': 'WA'}], 'var_call_S4TkixVyTyeZIVCV7jxdgWgj': [{'Id': '003Wt00000JqkgYIAR', 'FirstName': 'Nina', 'LastName': 'Tran', 'Email': 'nina.tran@innovatexsolutions.com', 'AccountId': '001Wt00000PGXrKIAX'}], 'var_call_syoOp56hnsyHsyQ55gIfW7Zj': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_Mbr4T4giYthWg4BqW95rfF84': 'file_storage/call_Mbr4T4giYthWg4BqW95rfF84.json'}

exec(code, env_args)
