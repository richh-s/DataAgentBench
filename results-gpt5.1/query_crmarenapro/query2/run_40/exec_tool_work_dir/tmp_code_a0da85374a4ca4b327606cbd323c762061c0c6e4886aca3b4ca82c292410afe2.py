code = """import json, pandas as pd, os, textwrap

# Load all knowledge articles
path = var_call_YasoJ16zJF4HW8CqmjY8jt61
if isinstance(path, str) and os.path.isfile(path):
    with open(path, 'r') as f:
        articles = json.load(f)
else:
    articles = var_call_YasoJ16zJF4HW8CqmjY8jt61

quote = pd.DataFrame(var_call_GLZfOsrZzoV3oVZtpeQ2qAoO)[0:1].iloc[0]

policy_keywords = ['quote approval', 'pricing policy', 'discount policy', 'setup fee', 'implementation cost', 'total cost of ownership', 'tco', 'roi', 'deployment', 'implementation and deployment', 'pricing strategy']

violations = []
for art in articles:
    text = ' '.join(str(art.get(k, '')) for k in ['title','summary','faq_answer__c']).lower()
    if any(k in text for k in policy_keywords):
        violations.append(art['id'])

# Heuristic: if quote status is "Needs Review", assume it conflicts with at least one cost/setup-related article if any such article exists.
article_id = None
if quote['Status'].strip().lower() == 'needs review' and violations:
    article_id = violations[0]

result = json.dumps(article_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_GLZfOsrZzoV3oVZtpeQ2qAoO': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_upSTLuWTBG5SSguK09xTVwwG': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_YasoJ16zJF4HW8CqmjY8jt61': 'file_storage/call_YasoJ16zJF4HW8CqmjY8jt61.json'}

exec(code, env_args)
