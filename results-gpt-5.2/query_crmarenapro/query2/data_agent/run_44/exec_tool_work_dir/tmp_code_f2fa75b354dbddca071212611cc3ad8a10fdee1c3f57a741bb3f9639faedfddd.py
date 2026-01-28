code = """import json, pandas as pd

# Load knowledge articles (may be file path)
ka = var_call_6IDoI28tzk1imyEj6LgUgEDY
if isinstance(ka, str):
    with open(ka, 'r', encoding='utf-8') as f:
        ka = json.load(f)

# Simple heuristic: look for quote policy/approval/discount/setup keywords
keywords = [
    'quote approval', 'quote', 'discount', 'pricing', 'price', 'setup', 'implementation',
    'professional services', 'services', 'approval', 'policy'
]

def score_article(a):
    text = ' '.join([
        str(a.get('title','') or ''),
        str(a.get('summary','') or ''),
        str(a.get('faq_answer__c','') or ''),
        str(a.get('urlname','') or '')
    ]).lower()
    return sum(1 for k in keywords if k in text)

scored = sorted([(score_article(a), a.get('id'), a.get('title','')) for a in ka], reverse=True)
# take top few
top = scored[:20]
print('__RESULT__:')
print(json.dumps(top))"""

env_args = {'var_call_ocVs3LxerQrwOCPU9tCAkrOp': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_37YhCK3zW9eI8SLvDN10UcIn': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_6IDoI28tzk1imyEj6LgUgEDY': 'file_storage/call_6IDoI28tzk1imyEj6LgUgEDY.json'}

exec(code, env_args)
