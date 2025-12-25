code = """import json, re
import pandas as pd

# Load full knowledge articles
path = var_call_2SegnWrhhA32bfjMUrunVYvA
with open(path, 'r') as f:
    knowledge = json.load(f)

# Simple heuristic: look for article titles indicating pricing/discount/setup policy
candidates = []
for art in knowledge:
    text = ' '.join(str(art.get(k,'') or '') for k in ['title','summary','faq_answer__c']).lower()
    if any(w in text for w in ['discount policy','pricing policy','quote approval','deal desk','commercial policy','implementation costs','setup fee policy','professional services policy']):
        candidates.append(art)

# Default: no violation
result = None

# If we had explicit policy, we would parse and check against quote; absent that, we assume no clear violation

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_hGocMNO0IvPPkay28RwEzCx2': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_J5YvA0UsCbf5A3d2PIOIfwN0': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_yUFgeLLKCrzpDjYB5EUHcML4': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_2SegnWrhhA32bfjMUrunVYvA': 'file_storage/call_2SegnWrhhA32bfjMUrunVYvA.json'}

exec(code, env_args)
