code = """import json, pandas as pd, os, textwrap

# Load articles
path = var_call_8b5sAI0waYhRnn6zSuVJiIIB
with open(path, 'r') as f:
    articles = json.load(f)

# Simple heuristic: find policies related to pricing/discounts/quotes/approval
keywords = ['discount', 'pricing', 'price', 'quote', 'approval', 'install', 'implementation', 'timeline']

candidates = []
for art in articles:
    text = ((art.get('title') or '') + ' ' + (art.get('summary') or '')).lower()
    if any(k in text for k in keywords):
        candidates.append(art)

# For this task, we just look for something clearly policy-like on quotes/discounts
chosen_id = None
for art in candidates:
    title = (art.get('title') or '').lower()
    if 'discount' in title or 'pricing' in title or 'quote' in title:
        chosen_id = art['id'].replace('#','')
        break

# Without detailed policy text and quote line items, we cannot reliably assert a violation.
result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IDkB5QJ2BJLpMgmvqCLFtC2n': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_TWO0qoux0spmWsNtECuheZUN': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_8b5sAI0waYhRnn6zSuVJiIIB': 'file_storage/call_8b5sAI0waYhRnn6zSuVJiIIB.json'}

exec(code, env_args)
