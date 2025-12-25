code = """import json, re, pandas as pd

# Load knowledge articles from file
path = var_call_nVPCzACYKVqcPHlxlOv1qxcE
with open(path, 'r') as f:
    articles = json.load(f)

# Company policy likely encoded in specific knowledge articles about quote approvals
# We'll search for terms related to quotes, pricing, discount, approval, TCO, implementation cost, setup fees
policy_keywords = ['quote', 'pricing', 'discount', 'approval', 'setup fee', 'implementation', 'deployment', 'tco', 'total cost of ownership']

relevant = []
for art in articles:
    text = ' '.join([
        str(art.get('title','')),
        str(art.get('summary','')),
        str(art.get('faq_answer__c',''))
    ]).lower()
    if any(k in text for k in policy_keywords):
        relevant.append(art)

result = json.dumps([{'id': a['id'], 'title': a['title']} for a in relevant])
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Tae911WzjaIFUHaNADq1XrNb': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_nVPCzACYKVqcPHlxlOv1qxcE': 'file_storage/call_nVPCzACYKVqcPHlxlOv1qxcE.json', 'var_call_FWvTQfiIxVQHII3ah1hTPVNh': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript']}

exec(code, env_args)
