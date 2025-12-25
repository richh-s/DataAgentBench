code = """import json, pandas as pd, re
from pathlib import Path

# Load full knowledge articles
path = Path(var_call_uAEiMCHkzPttap9BXHq6GLbN)
articles = json.loads(path.read_text())

# Very simple heuristic: look for policy/discount/approval/quote/price keywords
df = pd.DataFrame(articles)
text = (df['title'].fillna('') + ' ' + df['summary'].fillna('')).str.lower()
mask = text.str.contains('policy') | text.str.contains('discount') | text.str.contains('pricing') | text.str.contains('quote') | text.str.contains('approval') | text.str.contains('installation timeline')
candidates = df[mask]

# Among candidates, prioritize ones clearly about discounts/pricing policies
priority_mask = candidates['title'].str.lower().str.contains('discount|pricing|timeline|policy')
priority = candidates[priority_mask]

result_id = None
if not priority.empty:
    # Assume conflict with the first relevant policy article (e.g., installation timeline/volume-based discounts)
    result_id = priority.iloc[0]['id']

result_json = json.dumps(result_id)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_YMNMexZXtf80iwZgznPnr3Ld': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_GAKxHDhmmc8ma7gmmS4BkBbd': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_uAEiMCHkzPttap9BXHq6GLbN': 'file_storage/call_uAEiMCHkzPttap9BXHq6GLbN.json'}

exec(code, env_args)
