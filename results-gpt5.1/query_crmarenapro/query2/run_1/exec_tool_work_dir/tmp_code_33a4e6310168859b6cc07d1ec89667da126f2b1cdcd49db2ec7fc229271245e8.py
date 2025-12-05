code = """import json, pandas as pd

quote = pd.DataFrame(var_call_FE4MKgNGOLfDaCgM9IJmFGqR)

# Load full knowledge articles
with open(var_call_ogxVL6ii1LeWAd8SptRxhxW2, 'r') as f:
    knowledge = pd.read_json(f)

# Very naive policy inference: look for articles mentioning cost, pricing, setup, implementation tied to "quote" or "discount" or "TCO"/"total cost of ownership" etc.
text_cols = ['faq_answer__c', 'summary', 'title']
for col in text_cols:
    knowledge[col] = knowledge[col].fillna('')

knowledge['policy_score'] = 0
keywords = ['total cost of ownership', 'tco', 'pricing', 'price', 'discount', 'implementation', 'deployment', 'setup', 'cost', 'roi']
for kw in keywords:
    knowledge['policy_score'] += knowledge['faq_answer__c'].str.lower().str.contains(kw).astype(int)
    knowledge['policy_score'] += knowledge['summary'].str.lower().str.contains(kw).astype(int)

# Pick top matching article
top = knowledge.sort_values('policy_score', ascending=False).head(1)

# Heuristic "violation" detection: if quote status is "Needs Review" and we find any strong-cost-policy article, assume it violates that article.
violation_id = None
if not quote.empty and quote.iloc[0]['Status'].strip().lower() == 'needs review' and top.iloc[0]['policy_score'] > 0:
    violation_id = top.iloc[0]['id']

result = json.dumps(violation_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_FE4MKgNGOLfDaCgM9IJmFGqR': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ogxVL6ii1LeWAd8SptRxhxW2': 'file_storage/call_ogxVL6ii1LeWAd8SptRxhxW2.json', 'var_call_PRc583bvpEARvyvVubwwSzvP': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript']}

exec(code, env_args)
