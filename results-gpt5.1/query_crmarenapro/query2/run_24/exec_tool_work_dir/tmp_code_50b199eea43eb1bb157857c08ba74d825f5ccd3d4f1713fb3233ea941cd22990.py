code = """import json, pandas as pd, os
path = var_call_7cMkg95OlWSRKoeEqOnol5uD
with open(path, 'r') as f:
    articles = json.load(f)
# Filter for policy-like articles about quote approval, pricing, cost, discount, or setup
keywords = ['quote approval','discount','pricing','price','total cost of ownership','tco','roi','implementation','deployment','setup','services','ps policy','professional services','configuration','scope']
policy_articles = []
for a in articles:
    text = ((a.get('title') or '') + ' ' + (a.get('summary') or '') + ' ' + (a.get('faq_answer__c') or '')).lower()
    if any(k in text for k in keywords):
        policy_articles.append(a)
result = json.dumps(policy_articles)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_t80Wdm92TMhOUxuq4Lh3dtWF': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ptAvdVCVYq5MdT2TXgIsPbBZ': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_7cMkg95OlWSRKoeEqOnol5uD': 'file_storage/call_7cMkg95OlWSRKoeEqOnol5uD.json'}

exec(code, env_args)
