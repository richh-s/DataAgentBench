code = """import json, pandas as pd, re

path = var_call_bS6vKSdR5WOM8hkwJovX29rp
with open(path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

policy_mask = df['title'].str.contains('Quote', case=False, na=False) | df['title'].str.contains('Discount', case=False, na=False) | df['summary'].str.contains('quote', case=False, na=False) | df['summary'].str.contains('discount', case=False, na=False) | df['summary'].str.contains('pricing', case=False, na=False)

policy_articles = df[policy_mask]

result = policy_articles[['id','title','summary']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result) )"""

env_args = {'var_call_5reE072AhUkGvrF0A0rwKZaa': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_YlpMzexMniWoAcGYR5qH0pdZ': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_bS6vKSdR5WOM8hkwJovX29rp': 'file_storage/call_bS6vKSdR5WOM8hkwJovX29rp.json'}

exec(code, env_args)
