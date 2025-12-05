code = """import json, pandas as pd, os
from datetime import datetime

quote = pd.DataFrame(var_call_ypFD5zYUWFWL6dY7GBPIFGVc)[0:1]

path = var_call_CEjQoBoKn2j9SeddF2AnlhME
with open(path, 'r') as f:
    articles = json.load(f)
ka = pd.DataFrame(articles)

violating_id = None

status = str(quote.loc[0, 'Status']).strip()
exp = pd.to_datetime(quote.loc[0,'ExpirationDate']).tz_localize('UTC')
created = pd.to_datetime(quote.loc[0,'CreatedDate']).tz_convert('UTC')
valid_days = (exp - created).days

policies = ka[ka['title'].str.contains('Discount', case=False, na=False) | ka['title'].str.contains('Quote', case=False, na=False) | ka['title'].str.contains('Pricing', case=False, na=False) | ka['summary'].str.contains('discount', case=False, na=False)]

if valid_days > 30:
    cand = policies[policies['summary'].str.contains('Expiration', case=False, na=False) | policies['title'].str.contains('Expiration', case=False, na=False)]
    if not cand.empty:
        violating_id = cand.iloc[0]['id']

if violating_id is None and status.lower() == 'needs review':
    cand = policies.head(1)
    if not cand.empty:
        violating_id = cand.iloc[0]['id']

result = violating_id if violating_id is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ypFD5zYUWFWL6dY7GBPIFGVc': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_KiuIjP0G4hHXrYwL5CsvBXNF': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_CEjQoBoKn2j9SeddF2AnlhME': 'file_storage/call_CEjQoBoKn2j9SeddF2AnlhME.json'}

exec(code, env_args)
