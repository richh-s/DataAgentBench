code = """import json, pandas as pd, re
from pathlib import Path

# Load knowledge articles
path = Path(var_call_JjxZ48MOXbGkHHJBs6tcyyws)
arts = json.loads(path.read_text())

# Simple heuristic: look for policy/guide about quote approval, pricing, cost, discount, implementation, setup
df = pd.DataFrame(arts)
text = (df['title'].fillna('') + ' ' + df['faq_answer__c'].fillna('') + ' ' + df['summary'].fillna('')).str.lower()
mask = text.str.contains('quote approval|pricing policy|discount policy|total cost of ownership|tco|implementation and deployment|setup fee|one[- ]time fee|approval guide|deal desk|non-standard', regex=True)
policies = df[mask]

# Assume the relevant policy is the one that mentions both cost/tco/pricing AND implementation/setup/deployment
mask_cost = text.str.contains('price|pricing|cost|tco|total cost of ownership|discount', regex=True)
mask_setup = text.str.contains('implementation|deployment|setup', regex=True)
policy_idx = (mask_cost & mask_setup)
policy = df[policy_idx]

result_id = None
if not policy.empty:
    # take first non-null id, strip leading '#'
    pid = str(policy.iloc[0]['id']).strip()
    result_id = re.sub('^#+', '', pid) if pid not in (None, 'None') else None

out = json.dumps(result_id)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lBpdlhKNM1NnOWOXON9CK444': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_1SRKZKWj7tYrcT2fnX3HOdmt': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_JjxZ48MOXbGkHHJBs6tcyyws': 'file_storage/call_JjxZ48MOXbGkHHJBs6tcyyws.json'}

exec(code, env_args)
