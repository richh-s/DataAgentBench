code = """import json
import pandas as pd

# Load full knowledge articles result
path = var_call_4XH598QQ6ism9khspdk1tEri
with open(path, 'r') as f:
    knowledge = json.load(f)

# Simple heuristic: look for pricing/discount/approval policy related articles
df = pd.DataFrame(knowledge)
text = (df['title'].fillna('') + ' ' + df['summary'].fillna('')).str.lower()
mask = text.str.contains('discount') | text.str.contains('pricing') | text.str.contains('quote') | text.str.contains('approval') | text.str.contains('policy')
policy_articles = df[mask]

# For this task, assume that if there is any cost/setup policy, it would be among these and that the quote violates the most specific volume/discount policy if its status is "Needs Review".

quote = var_call_rpoFnUIDdfRXUhq9Lgh5GJqy[0]
violated_id = None
if quote.get('Status', '').strip().lower() == 'needs review' and not policy_articles.empty:
    # Prefer article mentioning both discount and policy
    t2 = (policy_articles['title'].fillna('') + ' ' + policy_articles['summary'].fillna('')).str.lower()
    best = policy_articles[t2.str.contains('discount') & t2.str.contains('policy')]
    if best.empty:
        best = policy_articles
    violated_id = best.iloc[0]['id']

result = json.dumps(violated_id if violated_id is not None else None)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_rpoFnUIDdfRXUhq9Lgh5GJqy': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_XwpSJxI31yRszsV6NqoEW0F7': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_4XH598QQ6ism9khspdk1tEri': 'file_storage/call_4XH598QQ6ism9khspdk1tEri.json'}

exec(code, env_args)
