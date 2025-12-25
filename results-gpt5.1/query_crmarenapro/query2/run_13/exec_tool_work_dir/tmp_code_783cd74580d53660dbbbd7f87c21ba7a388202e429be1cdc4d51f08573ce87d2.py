code = """import json, pandas as pd
from pathlib import Path

# Load full knowledge articles
path = Path(var_call_1uNfqN6twmCxTFUehpQd5YgK)
records = json.loads(path.read_text())

# Put into DataFrame for simple text search
df = pd.DataFrame(records)

# Focus on policy-related articles
mask = df['title'].str.contains('Policy', case=False, na=False) | df['summary'].str.contains('policy', case=False, na=False)
policy_articles = df[mask]

# For this task we only need to know if any cost/setup policy is clearly defined.
# Heuristically look for pricing/discount/quote/approval keywords.
keywords = ['discount', 'pricing', 'price', 'quote', 'approval', 'install', 'implementation', 'setup', 'services', 'professional services']
relevant = []
for _, row in policy_articles.iterrows():
    text = (str(row.get('title','')) + ' ' + str(row.get('summary',''))).lower()
    if any(k in text for k in keywords):
        relevant.append(row['id'])

# Without explicit policy context, we cannot assert a violation reliably.
result = None

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_CgcbjHPopB0AKPfwnhkOjl6C': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_7kmN4Dtdu76qubbvj6hf0cel': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_1uNfqN6twmCxTFUehpQd5YgK': 'file_storage/call_1uNfqN6twmCxTFUehpQd5YgK.json'}

exec(code, env_args)
