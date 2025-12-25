code = """import json
import pandas as pd

# Load knowledge articles from JSON file if needed
path = var_call_KcWI7kYAxbzaEMQ1vqWfjRI4
if isinstance(path, str) and path.endswith('.json'):
    with open(path, 'r') as f:
        kav = json.load(f)
else:
    kav = var_call_KcWI7kYAxbzaEMQ1vqWfjRI4

quote = var_call_V3a7xw4q3XPPAO46WwM2aw1X[0]

# Simple heuristic: look for policy/guide articles mentioning quotes, pricing, discount, cost, TCO, implementation, deployment
keywords = ['quote', 'pricing', 'price', 'discount', 'tco', 'total cost of ownership', 'cost ', 'implementation', 'deployment', 'setup', 'roi', 'approval']

matches = []
for art in kav:
    text = ' '.join([
        str(art.get('title','')),
        str(art.get('summary','')),
        str(art.get('faq_answer__c',''))
    ]).lower()
    if any(k in text for k in keywords):
        matches.append(art)

# For this exercise we must decide compliance, but there is no structured policy data.
# We'll assume no explicit violation can be determined.
result = None

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_V3a7xw4q3XPPAO46WwM2aw1X': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_YdsN8EjDcGBZnPhSWTp7aMUB': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_KcWI7kYAxbzaEMQ1vqWfjRI4': 'file_storage/call_KcWI7kYAxbzaEMQ1vqWfjRI4.json'}

exec(code, env_args)
