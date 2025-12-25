code = """import json, pandas as pd

path = var_call_np5RU4XwoO40Dx0MY38raEPZ
with open(path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

policy_keywords = [
    'discount', 'pricing', 'price', 'rebate', 'margin', 'quote approval',
    'deal desk', 'non-standard', 'exception', 'volume-based', 'promotion',
    'installation timeline', 'payment terms', 'renewal', 'escalation'
]

mask = df['title'].str.lower().str.contains('|'.join([k.lower() for k in policy_keywords])) |
       df['summary'].str.lower().str.contains('|'.join([k.lower() for k in policy_keywords]))

policy_articles = df[mask][['id','title','summary']]

result = policy_articles.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hNQwKN79Y75XUBku9Fr7NOz0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_cUpO3DaTK6uJl3j4ZXYi3MGD': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_np5RU4XwoO40Dx0MY38raEPZ': 'file_storage/call_np5RU4XwoO40Dx0MY38raEPZ.json'}

exec(code, env_args)
