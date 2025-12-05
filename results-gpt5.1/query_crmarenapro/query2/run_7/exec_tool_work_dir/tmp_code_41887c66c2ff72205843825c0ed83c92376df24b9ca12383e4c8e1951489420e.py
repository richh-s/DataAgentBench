code = """import json
import pandas as pd

# Load knowledge articles
path = var_call_vONoJekmkYqA6Yx3kvn6sK0r
with open(path, 'r') as f:
    articles = json.load(f)

# Simple heuristic: look for pricing/discount/quote policy related articles
keywords = ['discount', 'pricing', 'quote', 'approval', 'cost', 'margin', 'deal desk']

candidates = []
for art in articles:
    text = (art.get('title','') + ' ' + art.get('summary','')).lower()
    if any(k in text for k in keywords):
        candidates.append(art)

# Return just IDs of candidates (we'll assume potential policy articles)
result = [c['id'] for c in candidates]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2QWi4tA47ejoXxrkC6AXpqLU': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_EdoRgDvxwPxP6bPz2BXaN6cN': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_vONoJekmkYqA6Yx3kvn6sK0r': 'file_storage/call_vONoJekmkYqA6Yx3kvn6sK0r.json'}

exec(code, env_args)
